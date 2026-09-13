# Găng tay thông minh — Đánh giá & theo dõi chức năng vận động bàn tay sau đột quỵ

**Đề tài (tên chính thức):**

> **Nghiên cứu và phát triển găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ**

**Tiếng Anh:**

> A low-cost smart glove with directional piezoresistive sensing for quantitative hand motor-function assessment and longitudinal monitoring in post-stroke rehabilitation.

**Pitch 1 câu ("viên đạn"):**

> **Theo dõi định lượng chức năng bàn tay tại nhà, liên tục giữa các lần tái khám lâm sàng.**

---

## ⚠️ Trạng thái bằng chứng — đọc trước khi trích dẫn

- Giai đoạn hiện tại: **định hướng đề tài + thiết kế + prior art**. **Chưa có kết quả thực nghiệm nào.**
- Mọi tuyên bố về độ chính xác, độ nhạy, tương quan lâm sàng trong repo là **giả thuyết**, cho đến khi có log đo thật.
- **Không** chẩn đoán đột quỵ, **không** thay thế đánh giá lâm sàng (FMA/ARAT/Box & Block), **không** phải robot phục hồi chức năng.
- **Không** thử trên người tham gia (kể cả người khỏe) trước khi hoàn tất quy trình IRB/SRC.
- Quy tắc chi tiết: [`AGENTS.md`](AGENTS.md).

---

## 1. Vấn đề

- Đột quỵ là nguyên nhân hàng đầu gây tàn tật lâu dài. Phần lớn người bệnh còn di chứng yếu/liệt tay, hạn chế sinh hoạt hằng ngày.
- Phục hồi chức năng bàn tay phụ thuộc vào **luyện tập tại nhà hằng ngày**, nhưng kỹ thuật viên chỉ gặp bệnh nhân mỗi **1–3 tháng**.
- Các công cụ đánh giá hiện tại (Fugl-Meyer, ARAT, Box & Block Test, lực kế Jamar, E-Link) cho **một "ảnh chụp" tại thời điểm đo**, tại cơ sở y tế, chi phí cao.
- → Khoảng giữa hai lần tái khám là một **"hộp đen"**: không biết bệnh nhân có tập không, tập đúng hay sai, đang tiến bộ hay chững lại.

## 2. Hướng giải quyết

Một **thiết bị đánh giá/theo dõi** (không phải máy tập):
bệnh nhân đeo găng tay trong các bài tập chuẩn tại nhà → hệ thống ghi lực theo **hướng và độ lớn** ở từng khớp ngón tay → trích xuất chỉ số chức năng → vẽ lại **mô hình bàn tay 3D** và dựng **đường cong tiến triển theo tuần** → kỹ thuật viên/bác sĩ xem từ xa.

## 3. Nguyên lý cảm biến (điểm kỹ thuật trung tâm)

```
Ngón tay chuyển động theo hướng X
        ↓
Ép vào vách khung cứng (exoskeleton) phía X
        ↓
Vật liệu piezoresistive (Velostat) trên vách đó bị nén
        ↓
Điện trở giảm → ADC đọc → lực hướng X
        ↓
Ghép nhiều kênh → suy luận hướng gập/duỗi từng khớp → dựng lại bàn tay 3D
```

**Khác biệt so với găng tay phổ biến trên thị trường:** các hệ thống hiện có thường dùng **IMU / flex sensor** để đo góc. Thiết kế này **không dùng IMU** — dùng chính cấu trúc khung cứng + **sensing element chế tạo từ vật liệu Velostat** để mã hóa **hướng** và **lực**.

Phân cấp thuật ngữ (bắt buộc dùng đúng): xem [`docs/bao_cao/GLOSSARY.md`](docs/bao_cao/GLOSSARY.md) —
**vật liệu Velostat** ≠ **sensing element** (Velostat + copper tape + cấu trúc sandwich) ≠ **mảng sensing element** ≠ **hệ thống cảm biến áp lực bàn tay** (mảng + ESP32-S3 + firmware).

## 4. Điểm mới — nói trung thực

| # | Thành phần | Mức mới | Ghi chú |
|---|---|---|---|
| 1 | **Cảm biến hướng qua vách khung cứng** (directional sensing through rigid-frame walls, không IMU) | Ứng viên chính | Prior art gần nhất dùng IMU để đo pose, Velostat chỉ đo lực tiếp xúc. Cần rà soát prior art kỹ trước khi claim |
| 2 | **Cặp sensing element đối xứng** triệt thành phần drift đồng pha (common-mode) | Kỹ thuật | Không claim là phát minh |
| 3 | **Theo dõi dọc (longitudinal) tại nhà + tái tạo 3D để chuyên gia xem từ xa** | Ứng dụng | Khoảng trống được xác nhận bởi hội đồng chuyên gia 2024 và KTV VLTL-PHCN |
| 4 | **Mô hình INT8 chạy trên NPU (RK3588)** | Kỹ thuật triển khai | Không mới về thuật toán; mới về triển khai biên cho bài toán này |

> Không claim "phát minh thế giới". Mức novelty nhắm tới là **ViSEF/ISEF**: thực thi tốt + tác động thật + sáng tạo vừa phải.
> Hành trình chọn đề tài và lý do các hướng khác bị loại: [`research/reviews/00_EXPLORATION_SUMMARY.md`](research/reviews/00_EXPLORATION_SUMMARY.md).

## 5. Kiến trúc phần cứng (chốt 2026-09-13)

```
12–24 sensing element (Velostat + copper tape) trên khung găng in 3D
        ↓
CD74HC4067 (16 kênh/MUX) × 1–2
        ↓ 1 kênh analog (chọn MUX bằng chân EN)
ESP32-S3
  · ADC1 12-bit + lấy trung bình N mẫu → ~11 bit hiệu dụng
  · Quét toàn bộ kênh → frame + CRC → BLE / UART
        ↓
Orange Pi 5 Pro (RK3588, NPU ~6 TOPS)
  · Bù ảnh hưởng drift (cặp đối xứng + ô tham chiếu)
  · Trích đặc trưng → vector lực
  · Suy luận hướng khớp → tái tạo bàn tay 3D
  · Mô hình INT8 (RKNN) chạy trên NPU
        ↓
Dashboard theo tuần → KTV / bác sĩ theo dõi từ xa
```

Chi tiết ngân sách độ phân giải, tốc độ khung hình và bố trí kênh: [`docs/04_Hardware_Architecture.md`](docs/04_Hardware_Architecture.md).

## 6. Bản đồ repo

| Nhóm | File | Nội dung |
|---|---|---|
| Đề tài | [`docs/01_Topic_Definition.md`](docs/01_Topic_Definition.md) | Tên, vấn đề, khoảng trống, novelty, RQ, pipeline |
| Lý thuyết | [`docs/02_Theoretical_Foundation.md`](docs/02_Theoretical_Foundation.md) | Phục hồi vận động sau đột quỵ, thang đo, cơ sinh học bàn tay, vật liệu piezoresistive, drift, edge-AI |
| Prior art | [`docs/03_Literature_Gap_Analysis_Plan.md`](docs/03_Literature_Gap_Analysis_Plan.md) | Kế hoạch rà soát khoảng trống 2011–2026 |
| Phần cứng | [`docs/04_Hardware_Architecture.md`](docs/04_Hardware_Architecture.md) | Bố trí kênh, MUX, ngân sách nhiễu/độ phân giải, tốc độ khung |
| Báo cáo | [`docs/bao_cao/`](docs/bao_cao/) | A.1–A.6 theo mẫu ViSEF + GLOSSARY |
| Outline | [`docs/OUTLINE_BAOCAO_VISEFD.md`](docs/OUTLINE_BAOCAO_VISEFD.md) | Khung báo cáo toàn văn A/B/C |
| GATE | [`research/protocols/06_glove_hand_GATE_experiment.md`](research/protocols/06_glove_hand_GATE_experiment.md) | Thí nghiệm quyết định đề tài sống/chết |
| Sổ sách | [`research/context/`](research/context/), [`research/claims/`](research/claims/), [`research/evidence/`](research/evidence/) | Decision log, snapshot, claim ledger, source ledger |

## 7. Thiết lập nhanh

Yêu cầu: Git, Python 3.10+, Bash.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

bash scripts/bootstrap_research_tooling.sh          # ghim commit tooling vào .tools/sources
python scripts/check_research_environment.py        # thêm --strict để fail khi thiếu dependency
```

## 8. Quy trình nghiên cứu có kiểm chứng

Mọi agent/tác giả tuân thủ [`AGENTS.md`](AGENTS.md): đọc snapshot → log truy vấn → cập nhật claim/source ledger → chạy review protocol khi có thay đổi lớn → cập nhật snapshot → `python scripts/build_context_bundle.py`.

**Bước tiếp theo bắt buộc:** chốt bố trí kênh + chế tạo mẫu sensing element, sau đó chạy **GATE 0** trong `research/protocols/06_glove_hand_GATE_experiment.md` trước khi viết bất kỳ kết luận nào.

## 9. Ghi chú về tên repo

- Tên đề tài đã đổi; tên **repo GitHub hiện tại vẫn là `velostat-smart-insole-dfu`** (di sản đề tài cũ).
- Agent phiên này **không có quyền Administration** trên repo (HTTP 403), nên không tự đổi tên được. Chủ dự án chạy:

```bash
gh repo rename smart-glove-stroke-hand-rehab --repo nhatvanngoc/velostat-smart-insole-dfu --yes
git remote set-url origin https://github.com/nhatvanngoc/smart-glove-stroke-hand-rehab.git
```

- Thư mục làm việc cục bộ vẫn giữ tên `velostat-smart-insole-dfu` (ràng buộc của phiên làm việc) — không ảnh hưởng nội dung khoa học.
