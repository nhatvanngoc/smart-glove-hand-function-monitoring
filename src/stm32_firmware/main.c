/**
 * @file main.c
 * @brief STM32F407 reference firmware — Pressure matrix ADC + Valve PWM + UART bridge
 * @project Adaptive Air Cushion + Eye-Tracking AAC (THPT Quảng Trị)
 * @date 2026-06-14
 *
 * Reference implementation — board support package is HAL-based.
 * Build: arm-none-eabi-gcc -mcpu=cortex-m4 -mfloat-abi=hard
 * Flash: st-flash write build/main.bin 0x08000000
 *
 * NOTE: This is reference code. Adjust pin map, DMA streams, and clock tree
 * to match your specific Nucleo / custom board.
 */
#include "stm32f4xx_hal.h"
#include <string.h>
#include <stdint.h>
#include <stdio.h>

/* ---------- Configuration ---------- */
#define MATRIX_ROWS         8
#define MATRIX_COLS         8
#define PIEZO_ANCHORS       8
#define ADC_BUF_LEN         (MATRIX_ROWS * MATRIX_COLS + PIEZO_ANCHORS)  // 72
#define UART_TX_BUF_LEN     256
#define VALVE_PWM_PERIOD    4095   /* 12-bit PWM */
#define WATCHDOG_PERIOD_MS  100

/* ---------- Globals ---------- */
static UART_HandleTypeDef huart1;
static DMA_HandleTypeDef  hdma_adc1;
static ADC_HandleTypeDef  hadc1;
static TIM_HandleTypeDef  htim1;     /* PWM for valves */
static IWDG_HandleTypeDef hiwdg;

static volatile uint16_t adc_buf[ADC_BUF_LEN];
static volatile uint8_t  valve_pwm[64];
static volatile uint8_t  safety_latch = 0;

/* ---------- Forward decls ---------- */
static void SystemClock_Config(void);
static void GPIO_Init(void);
static void DMA_Init(void);
static void ADC1_Init(void);
static void USART1_Init(void);
static void TIM1_PWM_Init(void);
static void IWDG_Init(void);
static void MUX_SelectRow(uint8_t row);
static void PackFrame(uint8_t* out, int* outlen);
static void SendFrameUART(uint8_t* buf, int len);

/* ---------- Main ---------- */
int main(void)
{
    HAL_Init();
    SystemClock_Config();
    GPIO_Init();
    DMA_Init();
    ADC1_Init();
    USART1_Init();
    TIM1_PWM_Init();
    IWDG_Init();

    /* Start ADC DMA (continuous) */
    HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_buf, ADC_BUF_LEN);

    uint32_t last_send_ms = 0;
    uint32_t last_wd_ms    = 0;

    while (1) {
        uint32_t now = HAL_GetTick();

        /* Send pressure frame @ 10 Hz */
        if (now - last_send_ms >= 100) {
            last_send_ms = now;
            uint8_t frame[UART_TX_BUF_LEN];
            int len = 0;
            PackFrame(frame, &len);
            SendFrameUART(frame, len);
        }

        /* Refresh watchdog */
        if (now - last_wd_ms >= WATCHDOG_PERIOD_MS) {
            last_wd_ms = now;
            HAL_IWDG_Refresh(&hiwdg);
            /* safety: if Jetson silent > 5s, deflate all */
            /* (caller logic; simplified here) */
            if (safety_latch) {
                memset((void*)valve_pwm, 0, sizeof(valve_pwm));
                for (int i = 0; i < 64; ++i) {
                    __HAL_TIM_SET_COMPARE(&htim1, TIM_CHANNEL_1 + (i % 4), 0);
                }
            }
        }
    }
}

/* ---------- ADC + DMA ---------- */
static void ADC1_Init(void)
{
    hadc1.Instance                   = ADC1;
    hadc1.Init.ClockPrescaler        = ADC_CLOCKPRESCALER_PCLK_DIV4;
    hadc1.Init.Resolution            = ADC_RESOLUTION_12B;
    hadc1.Init.ScanConvMode          = ENABLE;
    hadc1.Init.ContinuousConvMode    = ENABLE;
    hadc1.Init.DiscontinuousConvMode = DISABLE;
    hadc1.Init.NbrOfDiscConversion   = 0;
    hadc1.Init.ExternalTrigConvEdge  = ADC_EXTERNALTRIGCONVEDGE_NONE;
    hadc1.Init.DataAlign             = ADC_DATAALIGN_RIGHT;
    hadc1.Init.NbrOfConversion       = ADC_BUF_LEN;
    hadc1.Init.DMAContinuousRequests = ENABLE;
    HAL_ADC_Init(&hadc1);
}

/* ---------- UART1 @ 921600 ---------- */
static void USART1_Init(void)
{
    huart1.Instance        = USART1;
    huart1.Init.BaudRate   = 921600;
    huart1.Init.WordLength  = UART_WORDLENGTH_8B;
    huart1.Init.StopBits    = UART_STOPBITS_1;
    huart1.Init.Parity      = UART_PARITY_NONE;
    huart1.Init.Mode        = UART_MODE_TX_RX;
    huart1.Init.HwFlowCtl   = UART_HWCONTROL_NONE;
    huart1.Init.OverSampling = UART_OVERSAMPLING_16;
    HAL_UART_Init(&huart1);
}

/* ---------- TIM1 PWM (12-bit) for valves (4 channels; MUX'd) ---------- */
static void TIM1_PWM_Init(void)
{
    htim1.Instance               = TIM1;
    htim1.Init.Prescaler         = 0;
    htim1.Init.CounterMode       = TIM_COUNTERMODE_UP;
    htim1.Init.Period            = VALVE_PWM_PERIOD;
    htim1.Init.ClockDivision     = TIM_CLOCKDIVISION_DIV1;
    HAL_TIM_PWM_Init(&htim1);
    TIM_OC_InitTypeDef oc = {0};
    oc.OCMode = TIM_OCMODE_PWM1;
    oc.Pulse  = 0;
    HAL_TIM_PWM_ConfigChannel(&htim1, &oc, TIM_CHANNEL_1);
    HAL_TIM_PWM_ConfigChannel(&htim1, &oc, TIM_CHANNEL_2);
    HAL_TIM_PWM_ConfigChannel(&htim1, &oc, TIM_CHANNEL_3);
    HAL_TIM_PWM_ConfigChannel(&htim1, &oc, TIM_CHANNEL_4);
    HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);
    HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_2);
    HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_3);
    HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_4);
}

/* ---------- Independent watchdog ---------- */
static void IWDG_Init(void)
{
    hiwdg.Instance       = IWDG;
    hiwdg.Init.Prescaler = IWDG_PRESCALER_64;
    hiwdg.Init.Reload    = 4095;     /* ~4s */
    hiwdg.Init.Window    = 4095;
    HAL_IWDG_Init(&hiwdg);
}

/* ---------- MUX row select ---------- */
static void MUX_SelectRow(uint8_t row)
{
    HAL_GPIO_WritePin(GPIOC, GPIO_PIN_0 << row, GPIO_PIN_SET);
    /* De-select others */
    for (int i = 0; i < MATRIX_ROWS; ++i) {
        if (i != row) HAL_GPIO_WritePin(GPIOC, GPIO_PIN_0 << i, GPIO_PIN_RESET);
    }
}

/* ---------- Pack frame: [0xAA][seq][64×P_velostat][8×P_pz][crc16] ----------
 * Binary little-endian; CRC16-CCITT for integrity.
 */
static uint16_t crc16_ccitt(const uint8_t* buf, int len) {
    uint16_t crc = 0xFFFF;
    for (int i = 0; i < len; ++i) {
        crc ^= (uint16_t)buf[i] << 8;
        for (int b = 0; b < 8; ++b) {
            crc = (crc & 0x8000) ? (crc << 1) ^ 0x1021 : (crc << 1);
        }
    }
    return crc;
}

static volatile uint8_t seq = 0;

static void PackFrame(uint8_t* out, int* outlen)
{
    int p = 0;
    out[p++] = 0xAA;            /* header */
    out[p++] = seq++;           /* sequence */

    /* 64 Velostat cells = ADC channels 0..63 */
    for (int i = 0; i < 64; ++i) {
        out[p++] = (uint8_t)(adc_buf[i] >> 4);  /* 12-bit → 8-bit (top byte) */
    }
    /* 8 Piezocapacitive anchors = ADC channels 64..71 */
    for (int i = 0; i < 8; ++i) {
        out[p++] = (uint8_t)(adc_buf[64 + i] >> 4);
    }
    /* CRC16 */
    uint16_t crc = crc16_ccitt(out, p);
    out[p++] = (uint8_t)(crc & 0xFF);
    out[p++] = (uint8_t)(crc >> 8);
    *outlen = p;
}

static void SendFrameUART(uint8_t* buf, int len)
{
    HAL_UART_Transmit(&huart1, buf, len, 10);
}

/* ---------- Clock (168 MHz) ---------- */
static void SystemClock_Config(void)
{
    RCC_OscInitTypeDef osc = {0};
    RCC_ClkInitTypeDef clk = {0};

    __HAL_RCC_PWR_CLK_ENABLE();
    __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

    osc.OscillatorType = RCC_OSCILLATORTYPE_HSE;
    osc.HSEState       = RCC_HSE_ON;
    osc.PLL.PLLState   = RCC_PLL_ON;
    osc.PLL.PLLSource  = RCC_PLLSOURCE_HSE;
    osc.PLL.PLLM = 8; osc.PLL.PLLN = 336;
    osc.PLL.PLLP = RCC_PLLP_DIV2; osc.PLL.PLLQ = 7;
    HAL_RCC_OscConfig(&osc);

    clk.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK
                  | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
    clk.SYSCLKSource   = RCC_SYSCLKSOURCE_PLLCLK;
    clk.AHBCLKDivider  = RCC_SYSCLK_DIV1;
    clk.APB1CLKDivider = RCC_HCLK_DIV4;
    clk.APB2CLKDivider = RCC_HCLK_DIV2;
    HAL_RCC_ClockConfig(&clk, FLASH_LATENCY_5);
}

/* ---------- GPIO ---------- */
static void GPIO_Init(void)
{
    __HAL_RCC_GPIOA_CLK_ENABLE();
    __HAL_RCC_GPIOB_CLK_ENABLE();
    __HAL_RCC_GPIOC_CLK_ENABLE();
    __HAL_RCC_GPIOD_CLK_ENABLE();
    __HAL_RCC_GPIOE_CLK_ENABLE();

    GPIO_InitTypeDef io = {0};

    /* MUX rows PC0..PC7 */
    io.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2|GPIO_PIN_3
            |GPIO_PIN_4|GPIO_PIN_5|GPIO_PIN_6|GPIO_PIN_7;
    io.Mode = GPIO_MODE_OUTPUT_PP;
    io.Pull = GPIO_NOPULL;
    io.Speed = GPIO_SPEED_FREQ_LOW;
    HAL_GPIO_Init(GPIOC, &io);

    /* USART1 PA9/PA10 */
    io.Pin = GPIO_PIN_9|GPIO_PIN_10;
    io.Mode = GPIO_MODE_AF_PP;
    io.Pull = GPIO_PULLUP;
    io.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    io.Alternate = GPIO_AF7_USART1;
    HAL_GPIO_Init(GPIOA, &io);

    /* TIM1 PWM PA8/PA9/PA10/PA11 */
    io.Pin = GPIO_PIN_8|GPIO_PIN_9|GPIO_PIN_10|GPIO_PIN_11;
    io.Mode = GPIO_MODE_AF_PP;
    io.Pull = GPIO_NOPULL;
    io.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    io.Alternate = GPIO_AF1_TIM1;
    HAL_GPIO_Init(GPIOA, &io);

    /* Emergency stop PE0 (input pull-up) */
    io.Pin = GPIO_PIN_0;
    io.Mode = GPIO_MODE_INPUT;
    io.Pull = GPIO_PULLUP;
    HAL_GPIO_Init(GPIOE, &io);
}
