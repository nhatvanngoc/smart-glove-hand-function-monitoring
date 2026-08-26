# Kill-test 3 hướng owner đề xuất (PI-SSL / Velostat+Audio / Hysteresis-biomarker) — 2026-08-26

## Direction A — Physics-Informed Self-Supervised Learning cho lực (không cần force plate)
Tuyên bố: "SSL + physical constraints cho piezoresistive là rất mới."
**BỊ GIẾT:**
- **UniForce** (arXiv 2602.01153): học latent force từ tactile **KHÔNG cần force label**, dùng **quasi-static force equilibrium** (đúng "Constraint 1" của owner) làm nhãn miễn phí.
- **PhyDNN** (arXiv 2512.03512): physics-driven learning cho tactile, đưa forward-model/PDE constraint vào loss.
- Tactile→CoP/GRF bằng supervised DL "thay force plate" đã có (Sensors 26(1):286, 2026).
- ⚠️ Kỹ thuật: 3 constraint (equilibrium/continuity/hysteresis-closure) **không đủ** để suy ra lực tuyệt đối; equilibrium chỉ cho TỔNG lực. Đây là đề tài **phương pháp ML**, impact người **gián tiếp** → lệch "human urgent" + ViSEF.

## Direction B — Velostat + micro rẻ (contact event classification)
Tuyên bố: "chưa ai dùng Velostat + cheap mic cho contact classification."
**BỊ GIẾT:**
- **MicCheck** (arXiv 2511.18299): dùng **micro pin off-the-shelf rẻ** phân loại **tap/knock/slow-press/drag** (đúng 4 interaction owner nêu) trên 10 vật liệu, 92.9%.
- Audio–tactile fusion là lĩnh vực **trưởng thành**: optical+piezo fusion 99.88%; internal-audio+vision fabric recognition; dataset tactile+audio+visual; acoustic touch classification.
- Đổi cảm biến (Velostat) **không phải novelty**. Lại là đề tài **HCI**, ít cấp thiết.

## Direction C — Hysteresis/độ cứng mô làm biomarker loét chân tiểu đường
Tuyên bố: "hoàn toàn mới, chưa ai dùng hysteresis làm biomarker tissue health."
**SỐNG — nhưng "hoàn toàn mới" là QUÁ LỜI:**
- **Biology đã thiết lập vững:** độ cứng mô gan chân **là biomarker nguy cơ loét tiểu đường** (Sci Rep 2025 phantom; J Biomech 2020; nhiều nghiên cứu elastography). → Không mới.
- **Đã có công cụ đo độ cứng:** SWE, MyotonPRO, IndentoPRO, **Tissue Compliance Meter**, **Shore Durometer** (rẻ) — đều validated trên phantom (Sci Rep 2025).
- **Cận kề ý tưởng:** "Flexible Sensors for Pressure Therapy: effect of **substrate curvature & stiffness** on sensor performance" (PMC5676615) — output cảm biến áp điện trở **phụ thuộc độ cứng nền** → đúng cơ sở vật lý của C.
- ⚠️ **Rủi ro kỹ thuật lớn:** hysteresis/drift **của chính Velostat** (lớn, trôi) có thể **lấn át** tín hiệu độ cứng mô (confound). Phải tách được.

### Reframe C cho đúng (giảm overclaim, tăng khả thi)
> **"Máy sàng lọc độ cứng mô gan chân GIÁ RẺ, dạng mảng, dùng tại nhà, dựa trên cảm biến áp điện trở (Velostat), để theo dõi nguy cơ loét chân tiểu đường."**
- **Đứng trên biology đã có** (stiffness→DFU risk): không phải chứng minh biomarker mới.
- **Novelty thật = phương pháp sensing rẻ**: thay elastography/MyotonPRO (đắt, cồng kềnh, 1 điểm) bằng **mảng Velostat rẻ, đo nhiều điểm, theo dõi tại nhà theo thời gian**.
- **Bench được:** phantom silicone độ cứng biết trước (ground truth) — **không cần bệnh nhân/IRB**.
- **Gate-2 phải trả lời:** Velostat có **phân giải được** khác biệt độ cứng mô **trên nền drift/hysteresis của chính nó** không? (Dùng indenter cứng + loading curve; đối chiếu durometer/phantom.)

## Xếp hạng
1. **Direction C (đã reframe)** — ƯU TIÊN: human-urgent thật (loét chân tiểu đường → đoạn chi), bench được, novelty nằm ở "sensing rẻ thay elastography", story mạnh. Rủi ro: confound sensor + phải vượt durometer rẻ.
2. Direction A — phương pháp ML, đã chiếm (UniForce/PhyDNN), impact gián tiếp.
3. Direction B — HCI, đã chiếm (MicCheck), ít cấp thiết.
