/* Diagnostic transport firmware only — no GRF/COP/calibration claim.
   USB serial is the recommended first link to Orange Pi. */
#include <Arduino.h>

const uint8_t CHANNELS = 16;
const uint32_t BAUD = 115200;
const uint16_t FRAME_HZ = 100; // measured actual rate is the result
const uint32_t PERIOD_US = 1000000UL / FRAME_HZ;
uint32_t seqNo = 0;
uint32_t dueUs = 0;

uint16_t crc16_ccitt(const char *data) {
  uint16_t crc = 0xFFFF;
  while (*data) {
    crc ^= (uint8_t)*data++ << 8;
    for (uint8_t i = 0; i < 8; i++) crc = (crc & 0x8000) ? (crc << 1) ^ 0x1021 : crc << 1;
  }
  return crc;
}

void setup() {
  Serial.begin(BAUD);
  dueUs = micros();
  Serial.println(F("# mega_link_diagnostics v1; ADC values are uncalibrated diagnostics"));
}

void loop() {
  uint32_t now = micros();
  if ((int32_t)(now - dueUs) < 0) return;
  dueUs += PERIOD_US;
  // Do not catch up with an unbounded loop: record schedule misses through timestamps.
  uint16_t a[CHANNELS];
  for (uint8_t i = 0; i < CHANNELS; i++) a[i] = analogRead(i);
  char payload[220];
  int n = snprintf(payload, sizeof(payload), "@%lu,%lu", (unsigned long)seqNo++, (unsigned long)now);
  for (uint8_t i = 0; i < CHANNELS && n > 0 && n < (int)sizeof(payload); i++)
    n += snprintf(payload + n, sizeof(payload) - n, ",%u", a[i]);
  if (n <= 0 || n >= (int)sizeof(payload) - 16) return;
  snprintf(payload + n, sizeof(payload) - n, ",diag,%04X", crc16_ccitt(payload));
  Serial.println(payload);
}
