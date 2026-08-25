#!/usr/bin/env python3
"""Validate structural headers for bench metrology templates; never analyzes measurements."""
from __future__ import annotations
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
 'research/bench/templates/session_manifest.csv':['bench_session_id','utc_start','sensor_unit_id','firmware_hash','layout_revision','conditioning_revision','adc_reference_v','scan_order','reference_device_id','reference_device_calibration_locator','operator_code','ambient_temperature_c','ambient_humidity_pct','notes'],
 'research/bench/templates/perturbation_log.csv':['record_id','bench_session_id','perturbation_family','perturbation_level','nominal_or_altered','reference_program_id','load_amplitude_n','load_rate_n_per_s','hold_s','cycle_count','recovery_s','placement_ap_mm','placement_ml_mm','rotation_deg','calibration_condition','evaluation_condition','raw_adc_locator','reference_locator','exclusion_reason'],
 'research/bench/templates/reference_check.csv':['record_id','bench_session_id','check_load_n','reference_value','observed_value','normalized_error','repeat_index','pre_or_post','integrity_label_pending','notes'],
}
for path, expected in EXPECTED.items():
    with (ROOT/path).open(newline='',encoding='utf-8') as f:
        actual=next(csv.reader(f),[])
    if actual != expected:
        raise SystemExit(f'FAIL {path}: header mismatch')
    print(f'PASS {path}')
print('Templates only: no measurement evidence was checked or created.')
