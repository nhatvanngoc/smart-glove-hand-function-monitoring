# 04 — Orange Pi 5 Pro ↔ Arduino Mega 2560 bring-up tests (before Velostat arrives)

- **Purpose:** validate acquisition-to-edge transport, timing, electrical safety, ADC behavior and edge-host stability using known signals/synthetic frames. These tests are **not** sensor validation, GRF/COP validation, drift validation, or real-time performance proof until raw logs are retained and reviewed.
- **Scope:** Arduino Mega 2560 = acquisition/timestamping; Orange Pi 5 Pro = receipt, logging, diagnostics and later inference.

## 0. Electrical rule — do this before any code

### Current owner setup: direct GPIO serial

The owner reports that direct serial GPIO communication between the Orange Pi and Arduino has already been established. This protocol therefore treats direct UART as the current transport path, not a task still to be solved.

Before collecting research data, record the **actual** interface in the session manifest:

```text
Orange Pi UART device path and GPIO pins:
Mega UART pins/port:
baud rate:
level-shifter model/wiring or verified voltage-interface method:
common-ground arrangement:
logic levels measured at Mega TX and Orange Pi RX:
```

- Mega UART TX is commonly **5 V logic**; Orange Pi GPIO RX is commonly **3.3 V logic**. The log must establish how the owner protects the Pi RX path; do not infer safety from successful basic communication alone.
- Orange Pi TX (3.3 V) → Mega RX behavior also depends on the actual board/interface and must be retained in the wiring record.
- Never power motors, sensor excitation, or unknown external loads from Orange Pi GPIO. Keep grounds intentional and inspect voltage before reconnection.

USB serial remains an optional diagnostic fallback, not the primary planned transport.

## 1. Test order and records

For every test save: date/time, board revisions, USB/UART path, firmware Git commit/hash, Pi OS/kernel, baud rate, power source, command line, raw log path, result, and anomalies. Use the headers in `research/bench/templates/` where applicable.

| Test | What it falsifies | Pass evidence (not a claim before log review) |
|---|---|---|
| T0 USB enumeration | wrong cable/driver/port | Mega device appears reliably after five reconnects |
| T1 framed packet/CRC | framing or byte corruption | receiver recomputes CRC and reports sequence gaps/CRC failures |
| T2 sustained throughput | link too slow or receiver cannot keep up | measured delivered frames/s, loss, latency proxy and jitter across planned rates |
| T3 burst/reconnect | buffer overflow or fragile restart | recovery behavior and lost-frame interval recorded |
| T4 timestamp/sync | untraceable timing | Mega `micros()` plus Pi receipt time captured; offset/jitter characterized |
| T5 ADC known-input | ADC wiring/reference/noise defect | logs for 0 V, stable midscale divider, and stable high reference; inputs never float |
| T6 16-channel scan | scan-time/ADC settling problem | measured frame period, per-channel variance, cross-channel carryover test |
| T7 Pi host stress | logging breaks under CPU/disk load | repeat T2 while Pi is under documented load; compare results |
| T8 synthetic inference | pipeline interface/latency only | fixed synthetic windows reach and return through the intended process; no biomechanics claim |
| T9 power/thermal soak | resets/overheating/USB instability | voltage, temperature, reset/disconnect events and logs recorded over declared duration |

## 2. T0–T4: transport diagnostics

1. Flash `firmware/mega_link_diagnostics/mega_link_diagnostics.ino`.
2. Use USB first at 115200 baud, then 230400 and 460800 only if each lower rate is stable.
3. The firmware emits CSV-like framed lines containing a sequence number, Mega timestamp, 16 ADC slots, mode and CRC.
4. Capture raw serial output on the Orange Pi. Do not rely on terminal screenshots.
5. Run at nominal candidate frame rates (50, 100, 200 Hz) for at least 10 min each; the actual achieved rate, errors and gaps are the results.
6. Trigger a controlled reconnect during T3; record whether frame numbering restarts and how the Pi logger detects it.

### Packet fields

```text
@seq,mega_us,adc0,...,adc15,mode,crc16\n
```

- `seq` detects drops/restarts.
- `mega_us` is acquisition-side time, not wall clock.
- `crc16` protects the complete payload before the CRC field.
- ADC slots are diagnostic only until real sensor calibration.

## 3. T5–T6: ADC/scan tests without Velostat

Use a safe known voltage source or resistor divider. Do not leave analog pins floating.

1. **Ground test:** connect one channel to GND; collect baseline distribution.
2. **Midscale test:** use a stable, measured divider/reference (e.g., nominal half-scale) and record the actual voltage with a multimeter.
3. **High-reference test:** use a safely bounded known voltage compatible with the chosen ADC reference. Never exceed the Mega analog-input/reference limits.
4. **Cross-channel test:** alternate grounded and midscale channels. This reveals carryover/settling issues when scan order changes.
5. **16-channel scan:** connect each channel to a declared known state; measure actual scan/frame timing. Arduino Mega has 10-bit ADCs and 16 analog inputs, but the achieved usable rate/noise must be measured, not assumed.

Record ADC reference mode (`DEFAULT`, `INTERNAL`, or external) and never apply an external AREF voltage while firmware is configured incompatibly.

## 4. T7–T9: Orange Pi edge-host tests

- **T7:** repeat transport while writing raw logs and applying a reproducible CPU/disk stress workload. The load command and process state must be logged.
- **T8:** run a fixed synthetic feature/inference placeholder only to test process boundaries, queueing and timestamp propagation. It cannot demonstrate NPU throughput, INT8 accuracy or biomechanics.
- **T9:** operate for a declared soak duration with ordinary cooling/enclosure state. Log `uptime`, CPU temperature, storage free space, USB disconnects and application restarts. Do not report “real time” until latency distribution is measured with the actual model.

## 5. Decision criteria before Velostat integration

Advance to sensor integration only if:

1. electrical interface is documented and safe;
2. T1/T2/T3 logs permit counting CRC failures, sequence gaps, restarts and achieved rate;
3. T5/T6 show known-input behavior and expose any scan/settling limitation;
4. raw timestamp provenance survives Pi logging;
5. failures have a recorded cause or remain explicit blockers.

Velostat arrival starts a **new** phase: cell characterization, crosstalk, hysteresis, creep, calibration and reference-load tests. These transport tests do not replace that phase.
