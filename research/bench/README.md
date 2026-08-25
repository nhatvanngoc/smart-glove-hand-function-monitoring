# Bench metrology execution area

This directory contains **empty templates and validation tooling only**. It contains no hardware measurement and must never be cited as a result.

## Gate-2 execution preconditions

1. A traceable/characterized reference load cell or test fixture is available.
2. The sensor unit, electrode layout, conditioning circuit, ADC reference, scan order and firmware hash are recorded.
3. Raw ADC and reference timestamps can be retained together.
4. The protocol operator completes `templates/session_manifest.csv` and `templates/perturbation_log.csv` without participant identifiers.
5. Reference-load calibration and nominal repeatability are run before any perturbation is interpreted.

`templates/` contains headers only. Raw measurements, photos, private subject mappings, downloaded tools and generated analysis outputs follow repository ignore/privacy rules and must be stored outside tracked templates until an owner-approved data-management plan exists.
