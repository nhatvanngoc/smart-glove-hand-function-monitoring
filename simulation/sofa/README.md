# SOFA simulation workspace

Muc tieu thu muc nay:

```text
SOFA mechanical simulation
    -> pressure/contact field on Velostat patch
    -> sensor-electrical model
    -> heatmap 5 x 9
```

Cau truc:

```text
simulation/sofa/scenes/        SOFA scene Python files
simulation/sofa/controllers/   Python controllers/coupling code
simulation/sofa/calibration/   R(P), Rs(P), ADC calibration data
simulation/sofa/outputs/       pressure/contact output from SOFA
```

Buoc dau tien sau khi cai SOFA:

```bash
runSofa -l SofaImGui -g imgui -l SofaPython3
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
```

Sau khi test thanh cong, se tao scene dau tien:

```text
simulation/sofa/scenes/single_velostat_patch.py
```
