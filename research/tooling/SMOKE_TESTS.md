# Tooling and experiment smoke tests — 2026-08-16

These checks establish only that the local reference code executes. Experiment values are generated from synthetic inputs and do **not** establish hardware, participant, clinical, or competition performance.

## Environment

- Created ignored `.venv` with Python 3.11.
- Installed NumPy 2.4.6, Matplotlib 3.11.1 and scikit-learn 1.9.0 plus transitive dependencies from `requirements.txt`.
- `scripts/check_research_environment.py`: 10/11 required/target checks pass.
- Expected failing target: `pdflatex` is absent; `miktexsetup` is an optional warning.
- All five pinned source checkouts and all four Academic Research Skills links pass commit/origin/cleanliness checks.

Exact installed versions above describe this smoke-test environment, not a locked production environment; `requirements.txt` currently uses compatible version ranges.

## PlotNeuralNet

- Upstream `pyexamples/test_simple.py` architecture loaded successfully.
- `pycore.tikzeng.to_generate` produced a non-empty 2,492-byte TeX file containing `\\begin{tikzpicture}`.
- Generated test artifact is under ignored `research/generated/plotneuralnet/`.
- PDF rendering was **not tested** because `pdflatex` is unavailable.
- The third-party checkout remained clean after the test.

## Existing synthetic experiments

All seven scripts exited with status 0. “PASS/FAIL” below is each script's own synthetic acceptance output and must not be promoted to an empirical verdict.

| Script | Observed synthetic output | Script criterion |
|---|---|---|
| EXP-01 hybrid calibration | Velostat RMSE 3.386; hybrid RMSE 3.678 mmHg; −8.6% “reduction” | **FAIL** |
| EXP-02 PTI | lead 0.01 ± 0.01 min; reported FPR 23.8% | **FAIL** |
| EXP-03 CNN-LSTM | MAE 0.5006; AUC undefined (`nan`) because all 45 labels were one class | **FAIL** both |
| EXP-04 eye tracking | top-1 100%; mean angular error 0.99° | **PASS** both, synthetic generator only |
| EXP-05 cushion control | adaptive mean sacrum 24.09 mmHg vs passive 27.95 mmHg | **PASS** both, simulation only |
| EXP-06 AAC | BLEU-4 0.0009; P95 latency rounds to 0.00 ms because LLM is disabled/falls back to heuristic | **FAIL** quality; **PASS** fallback timing only |
| EXP-07 self-improving loop | scripted reward trend +839.6% | **PASS**, not learned-system validation |

### Red flags exposed by execution

1. EXP-02 prints “Real 4-hour monitoring on immobile patients yields ≥30 min lead” without runtime evidence for that statement. It cannot be treated as a result.
2. EXP-03 has no class variation, so ROC-AUC is not estimable; a numeric model claim would be invalid from this run.
3. EXP-04's perfect grid accuracy comes from generated gaze/target pairs and is not a camera/MediaPipe measurement.
4. EXP-05 still treats 32 mmHg as an acceptance threshold despite the evidence limitations documented elsewhere.
5. EXP-06 does not exercise Qwen/LoRA, so its near-zero fallback latency is not model latency.
6. EXP-07 injects an improving environment trend; it does not by itself show causal improvement from an adaptive algorithm.

These are method findings for later redesign, not code changes made silently during intake.
