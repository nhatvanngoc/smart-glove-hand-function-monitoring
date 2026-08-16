# STM32 Firmware Reference

`main.c` là reference implementation cho STM32F407VGT6 (168 MHz, 1 MB Flash).

## Chức năng
1. **ADC DMA** đọc 64 Velostat + 8 Piezocapacitive (72 kênh) ở continuous mode.
2. **SPI MUX** (74HC4051 × 8) chọn hàng ma trận cảm biến.
3. **PWM 4-channel TIM1** điều khiển van khí (MUX sang 64 van).
4. **UART1 @ 921600** gửi frame 72 byte + CRC16 về Jetson mỗi 100 ms (10 Hz).
5. **IWDG** watchdog 4s — auto-deflate khi Jetson mất kết nối.

## Frame format
```
[0xAA][seq][64×Velostat(8-bit)][8×Piezocap(8-bit)][CRC16-CCITT]
```
Tổng 73 bytes/frame.

## Build (GCC ARM)
```bash
arm-none-eabi-gcc -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 \
    -DSTM32F407xx -DUSE_HAL_DRIVER \
    -IInc -ISrc -IDrivers/STM32F4xx_HAL_Driver/Inc \
    Src/*.c -o build/main.elf
arm-none-eabi-objcopy -O binary build/main.elf build/main.bin
```

## Flash
```bash
st-flash write build/main.bin 0x08000000
```

## Test
- HIL: `python tests/test_stm32_hil.py` mô phỏng sensor → STM32 → UART loopback.
- FreeRTOS variant (optional): thay `while(1)` bằng `osKernelStart()` và dùng CMSIS-RTOS v2.

## Pin map tóm tắt
| Pin | Chức năng |
|-----|-----------|
| PC0..PC7 | SPI MUX row select |
| PA9/PA10 | USART1 TX/RX |
| PA8/PA9/PA10/PA11 | TIM1 CH1..CH4 PWM |
| PE0 | Emergency stop (input pull-up) |

## Lưu ý
- Đây là **reference code**, cần tinh chỉnh pin map, DMA stream, clock tree khi mang lên board thực.
- Đã verify compile (logic), chưa flash trên hardware.
- Nếu dùng FreeRTOS, chia thành 4 task: `Task_ADC`, `Task_Control`, `Task_Comm`, `Task_Watchdog`.
