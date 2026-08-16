# ARS Evidence Audit — Velostat + copper tape + SOFA heatmap

Ngày cập nhật: 2026-07-28

## 1. Mục tiêu audit

Tài liệu này dùng quy trình ARS để giảm ảo giác khi xây dựng cơ sở lí thuyết cho lớp cảm biến:

```text
Velostat 50 × 50 mm
+ copper tape sandwich electrode
+ SOFA mechanical pressure model
+ R(P) / ADC / heatmap
```

Các vai trò ARS được dùng nội tuyến:

```text
Source Verification Agent
Devil's Advocate Agent
Experiment Agent
```

Lưu ý: đây là phản biện nội tuyến trong cùng phiên làm việc, không phải nhiều mô hình độc lập. Nếu muốn cross-model/subagent thật, cần cấu hình runtime riêng và xác nhận nội dung được gửi ra ngoài.

---

## 2. Nguồn đã kiểm tra sơ bộ

| Mã | Nguồn | Loại nguồn | Claim hỗ trợ | Mức tin cậy |
|---|---|---|---|---|
| S1 | https://www.adafruit.com/product/1361 | Product page / vendor | Velostat/Linqstat là vật liệu dẫn điện nhạy áp; tấm 11 × 11 inch, 4 mil/0.1 mm; ép làm giảm điện trở | Trung bình cho thông số sản phẩm; thấp cho mô hình R(P) |
| S2 | https://www.mdpi.com/2673-4591/58/1/74 | Conference proceedings / peer-reviewed-like MDPI proceedings | Cảm biến Velostat dùng copper tape sandwich; có nonlinearity, hysteresis, drift; thử với quả cân 100–2000 g | Trung bình |
| S3 | https://www.mdpi.com/2571-8800/6/1/3 | Journal article | Velostat là polyethylene–carbon-black piezoresistive film; đáp ứng điện trở phi tuyến; dùng trong pressure tracking | Trung bình-khá |
| S4 | https://www.mdpi.com/2073-4360/12/12/2905 | Journal article | Velostat/polyethylene-carbon composite có nonlinearity, hysteresis, drift/creep; cần calibration và xử lí dữ liệu | Khá |
| S5 | https://inria.hal.science/inria-00319416/document | SOFA paper / technical framework | SOFA là framework open-source cho mô phỏng y sinh, soft-tissue, FEM, contact/multimodel | Khá |

---

## 3. Claim đã xác minh ở mức đủ dùng

### Claim 1 — Velostat là vật liệu nhạy áp

**Trạng thái:** đã có bằng chứng hỗ trợ.

Nguồn product page mô tả Velostat/Linqstat là vật liệu dẫn điện nhạy áp; khi bị ép, điện trở giảm. Đây là claim định tính phù hợp để dùng trong cơ sở lí thuyết.

**Không được suy diễn quá mức:** claim này không cung cấp đường R(P) định lượng cho cấu hình sensor của dự án.

### Claim 2 — Kích thước và độ dày vật liệu

**Trạng thái:** đã có bằng chứng hỗ trợ.

Thông số đang dùng:

```text
Kích thước tấm: 280 × 280 mm
Độ dày: 0.1 mm
```

Thông số này phù hợp với product page Adafruit và các trang phân phối liên quan.

### Claim 3 — Copper tape sandwich electrode là cấu hình hợp lí

**Trạng thái:** có bằng chứng hỗ trợ nhưng cần hiệu chuẩn riêng.

Một số nghiên cứu sử dụng copper tape phía trên và phía dưới Velostat như điện cực. Điều này hỗ trợ lựa chọn sandwich electrode cho dự án.

**Giới hạn:** hình học điện cực, lớp keo, độ nhám, độ mềm lớp phủ và điều kiện ép có thể làm thay đổi đáp ứng sensor.

### Claim 4 — Velostat có phi tuyến và hysteresis

**Trạng thái:** đã có bằng chứng hỗ trợ.

Các nghiên cứu về Velostat/polyethylene-carbon composite báo cáo đáp ứng phi tuyến, hysteresis, drift/creep và cần calibration. Đây là điểm phải đưa vào phần giới hạn và phương pháp hiệu chuẩn.

---

## 4. Claim chưa được phép khẳng định

| Claim | Vì sao chưa được phép khẳng định | Cần làm gì |
|---|---|---|
| Sensor 50 × 50 mm có đường R(P) cụ thể | Datasheet hiện tại không có đường R(P); mỗi cấu hình điện cực khác nhau | Hiệu chuẩn bằng quả cân |
| Heatmap có sai số mmHg cụ thể | Chưa có prototype thật và calibration | Thí nghiệm tải chuẩn + so sánh mô phỏng |
| Hệ thống đạt chuẩn y sinh/clinical-grade | Chưa có thử nghiệm lâm sàng, độ bền, an toàn điện, chuẩn thiết bị y tế | Chỉ nói prototype nghiên cứu |
| SOFA v0 cho pressure field chính xác | Scene hiện tại mới là distributed-force simplification | Nâng cấp contact + silicone support + validation |
| 32 mmHg là ngưỡng tuyệt đối | Đây chỉ là mốc tham chiếu phổ biến, không áp dụng tuyệt đối cho mọi mô/tình trạng bệnh nhân | Dùng như reference threshold, không diagnostic cutoff |

---

## 5. Devil's Advocate — phản biện nội tuyến

### 5.1. Agent A — Người ủng hộ mô hình

**Luận điểm:**

```text
Velostat + copper tape sandwich đủ hợp lí để tạo sensor áp lực chi phí thấp.
SOFA mô phỏng cơ học mềm tốt hơn Gazebo.
Heatmap 5 × 9 đủ cho vùng vai - đùi trên.
```

**Điểm mạnh:**

- Phù hợp ngân sách và chế tạo nhanh.
- Có nguồn hỗ trợ việc dùng Velostat với copper tape.
- SOFA phù hợp hơn Gazebo cho vật liệu mềm.

### 5.2. Agent B — Phản biện cảm biến/điện tử

**Phản biện:**

```text
Velostat không tuyến tính, có hysteresis và drift.
Dữ liệu R(P) không có trong datasheet.
Copper tape và lớp keo có thể chi phối điện trở tiếp xúc.
Một sensor đơn có thể hoạt động, nhưng 45 sensor có thể lệch nhau rất lớn.
```

**Mức độ:** Major.

**Phản hồi/kế hoạch xử lí:**

- Không khẳng định độ chính xác trước hiệu chuẩn.
- Làm calibration từng sensor hoặc calibration theo nhóm.
- Ghi nhận hysteresis bằng chu kỳ tăng tải/giảm tải.
- Dùng mô hình `ADC → P` fit từ thực nghiệm thay cho R(P) giả định khi có dữ liệu.

### 5.3. Agent C — Phản biện cơ học/SOFA

**Phản biện:**

```text
Scene SOFA v0 hiện chỉ dùng distributed force, chưa có contact plate thật.
Silicone support mới là visual hoặc giả định cố định đáy.
Do đó chưa thể gọi là pressure field thực sự của cell khí.
```

**Mức độ:** Major.

**Phản hồi/kế hoạch xử lí:**

- Ghi rõ v0 là force-controlled verification scene.
- Bước tiếp theo phải thêm contact plate và silicone elastic support.
- Sau đó mới mở rộng 3 × 3 để đo crosstalk cơ học.

### 5.4. Agent D — Phản biện học thuật/lâm sàng

**Phản biện:**

```text
Ngưỡng 32 mmHg dễ bị trình bày sai thành ngưỡng tuyệt đối.
Áp suất bề mặt không hoàn toàn đại diện cho ứng suất sâu trong mô.
Ma trận vai - đùi trên chưa bao phủ gót chân.
```

**Mức độ:** Major.

**Phản hồi/kế hoạch xử lí:**

- Viết 32 mmHg là mốc tham chiếu, không phải chẩn đoán tuyệt đối.
- Dùng pressure-time index thay vì chỉ áp suất tức thời.
- Ghi rõ phạm vi module 5 × 9 là vùng vai - đùi trên; gót chân là module mở rộng về sau.

---

## 6. Consensus sau phản biện

### Quyết định giữ lại

```text
Ma trận 5 × 9
Velostat patch 50 × 50 mm
Sandwich copper electrode
SOFA làm nền mô phỏng cơ học chính
Batch/headless simulation làm pipeline định lượng
```

### Điều chỉnh bắt buộc

1. Tất cả tham số R(P) hiện tại phải ghi là placeholder.
2. Không viết hệ thống đo được mmHg chính xác nếu chưa có calibration.
3. SOFA v0 chỉ là scene kiểm tra, chưa phải contact model hoàn chỉnh.
4. Phần báo cáo phải có mục hysteresis, drift, nonlinearity và calibration.
5. Khi có dữ liệu TinyFish hoặc paper mới, phải đưa vào source matrix trước khi tổng hợp.

---

## 7. Câu hỏi phản biện cần trả lời ở vòng tiếp theo

1. Velostat 50 × 50 mm có đáp ứng đủ nhạy trong dải 7–75 mmHg không?
2. Sensor có cần tiền xử lí/cyclic preconditioning trước calibration không?
3. Copper tape nên dùng diện tích bao nhiêu để tối ưu độ nhạy và độ mềm?
4. Có cần conductive fabric thay copper tape để giảm cấn/cứng không?
5. SOFA contact model cần vật liệu silicone thông số nào?
6. Có nên dùng model Kelvin-Voigt/viscoelastic cho drift và creep không?
7. Cần bao nhiêu lần lặp tải để báo cáo repeatability?
8. Có cần calibration riêng cho từng cell hay dùng calibration chung?

---

## 8. Kết luận audit

Cấu hình hiện tại có cơ sở hợp lí để tiếp tục, nhưng không được trình bày như hệ đo áp suất định lượng hoàn chỉnh cho tới khi có hiệu chuẩn thực nghiệm. Hướng đúng là:

```text
SOFA mô phỏng cơ học
+ calibration thực nghiệm Velostat
+ mô hình điện ADC
+ heatmap 5 × 9
+ phản biện ARS theo từng checkpoint
```

Đây là đường đi giảm ảo giác và phù hợp hơn với mục tiêu nghiên cứu nghiêm túc.
