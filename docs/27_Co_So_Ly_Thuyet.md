# BÁO CÁO CƠ SỞ LÍ THUYẾT

## Hệ thống đệm khí thích ứng dựa trên mô hình áp suất - thời gian tích hợp cảm biến Velostat và giao tiếp hỗ trợ người hạn chế vận động trong phòng ngừa loét tì đè

**Ngày cập nhật:** 2026-07-28  
**Trạng thái tài liệu:** Bản cơ sở lí thuyết tổng hợp, dùng cho báo cáo nghiên cứu và phát triển mô phỏng.  
**Cấu hình thiết kế hiện tại:** Ma trận đệm `5 × 9`, tổng `45 cell`, patch Velostat `50 × 50 mm` mỗi cell.

---

## Tóm tắt

Loét tì đè là một vấn đề y sinh quan trọng ở người hạn chế vận động, đặc biệt trong các trường hợp bệnh nhân nằm lâu, suy giảm khả năng tự xoay trở hoặc phụ thuộc vào người chăm sóc. Cơ chế chính của loét tì đè liên quan đến áp lực kéo dài lên mô mềm, lực cắt, ma sát, độ ẩm, nhiệt độ và thời gian chịu tải. Do đó, một hệ thống đệm khí thích ứng không chỉ cần làm mềm bề mặt nằm mà còn cần đo được phân bố áp lực theo thời gian, phát hiện vùng nguy cơ và điều khiển lại áp suất khí để tái phân bố tải.

Báo cáo này trình bày cơ sở lí thuyết cho hệ thống đệm khí thích ứng sử dụng ma trận `5 × 9` cell khí, tích hợp cảm biến Velostat/Linqstat và điện cực copper tape theo cấu trúc sandwich. Mỗi cell được gắn một patch Velostat `50 × 50 mm` để thu nhận tín hiệu áp lực tại vùng tương ứng. Tín hiệu cảm biến được mô hình hóa theo chuỗi: áp suất cơ học `P(x,y,t)` → điện trở Velostat `R(t)` → điện áp chia áp `Vout(t)` → giá trị ADC → bản đồ nhiệt áp suất. Phần mô phỏng cơ học được định hướng triển khai bằng SOFA Framework ở chế độ batch/headless nhằm đảm bảo khả năng lặp lại, xuất dữ liệu định lượng và phục vụ đối chứng thực nghiệm.

Tài liệu cũng nêu rõ giới hạn hiện tại: datasheet sản phẩm Velostat chỉ cung cấp thông tin kích thước, độ dày và điện trở suất định tính, chưa cung cấp đường đặc tính áp suất - điện trở `R(P)` cho cấu hình cảm biến cụ thể. Vì vậy, mọi mô hình `R(P)` trong giai đoạn đầu chỉ được xem là giả định mô phỏng và bắt buộc phải thay bằng kết quả hiệu chuẩn thực nghiệm bằng tải trọng chuẩn. Báo cáo áp dụng quy trình kiểm soát ảo giác theo tinh thần ARS: phân loại claim thành đã xác minh, có bằng chứng hỗ trợ, giả định mô phỏng hoặc chưa xác minh.

---

## Từ khóa

Đệm khí thích ứng; loét tì đè; Velostat; Linqstat; copper tape; cảm biến áp lực mềm; SOFA Framework; bản đồ nhiệt áp suất; mô hình áp suất - thời gian; hiệu chuẩn cảm biến; người hạn chế vận động.

---

## 1. Bối cảnh nghiên cứu

Người hạn chế vận động có nguy cơ cao bị loét tì đè do khả năng tự thay đổi tư thế bị suy giảm. Khi một vùng cơ thể bị ép lên bề mặt giường hoặc đệm trong thời gian dài, áp lực có thể làm giảm tưới máu mô, gây thiếu oxy, tích tụ chất chuyển hóa và cuối cùng dẫn đến tổn thương da hoặc mô dưới da. Các vùng thường gặp nguy cơ cao gồm vùng cùng cụt, ụ ngồi, gót chân, bả vai, khuỷu tay và mấu chuyển.

Các loại đệm phòng loét truyền thống thường hoạt động theo một trong ba hướng:

1. **Đệm mềm thụ động:** phân tán lực bằng vật liệu mềm như foam, gel hoặc khí.
2. **Đệm khí luân phiên:** bơm/xả theo chu kỳ định sẵn, không nhất thiết dựa trên dữ liệu áp lực tức thời.
3. **Đệm thông minh:** đo áp lực, phân tích nguy cơ và điều khiển lại áp suất theo vùng.

Đề tài này đi theo hướng thứ ba. Mục tiêu không chỉ là tạo một bề mặt nằm mềm hơn, mà là xây dựng một hệ thống có khả năng:

```text
đo áp lực theo từng vùng
→ dựng bản đồ nhiệt áp suất
→ đánh giá áp lực tích lũy theo thời gian
→ điều khiển cell khí để tái phân bố tải
→ hỗ trợ cảnh báo/giao tiếp cho người hạn chế vận động
```

---

## 2. Cấu hình thiết kế đã chốt

### 2.1. Ma trận cell khí

Cấu hình cơ khí hiện tại được chốt như sau:

```text
Ma trận đệm:        5 × 9
Số cell:            45
Kích thước cell:    98 × 98 mm
Pitch lắp ráp:      100 mm
Kích thước module:  khoảng 500 × 900 mm
Velostat patch:     50 × 50 mm mỗi cell
```

Quy ước ma trận trong phần mềm:

```text
pressure_map.shape = (9, 5)
```

Trong đó:

```text
9 hàng:  vai → lưng → mông/cùng cụt → đùi trên
5 cột:   trái cơ thể → giữa → phải cơ thể
```

Cấu hình `5 × 9` được chọn vì cơ thể người khi nằm có dạng hình chữ nhật kéo dài theo trục vai - đùi, không phải hình vuông. So với ma trận `8 × 8`, cấu hình `5 × 9` giảm số cell từ `64` xuống `45`, giảm số van, ống khí và kênh cảm biến, đồng thời vẫn phủ được vùng chịu tải chính.

### 2.2. Lý do không chọn full-body trong giai đoạn đầu

Một hệ full-body thật sự cần phủ từ vai đến gót chân, có thể cần 15-17 hàng cell nếu dùng pitch khoảng 100 mm. Khi đó số cell có thể lên đến 75-100 cell, làm tăng mạnh độ phức tạp cơ khí, điện tử, điều khiển và hiệu chuẩn.

Do đó, giai đoạn hiện tại tập trung vào vùng:

```text
vai / bả vai
lưng
mông / cùng cụt
đùi trên
```

Gót chân vẫn là vùng nguy cơ quan trọng, nhưng nên được xử lí bằng module mở rộng riêng trong giai đoạn sau thay vì ép vào cùng một ma trận lớn ngay từ đầu.

---

## 3. Cơ sở sinh học và cơ học của loét tì đè

### 3.1. Cơ chế tổn thương mô

Loét tì đè hình thành do tác động kết hợp của:

- áp lực pháp tuyến lên mô;
- lực cắt giữa da và mô sâu;
- ma sát trên bề mặt da;
- độ ẩm và nhiệt độ;
- thời gian chịu tải;
- tình trạng dinh dưỡng, tuần hoàn và cảm giác của người bệnh.

Áp lực cao trong thời gian ngắn có thể gây tổn thương, nhưng áp lực vừa phải kéo dài cũng nguy hiểm. Vì vậy, hệ thống không nên chỉ đánh giá áp suất tức thời mà cần đánh giá cả tích lũy áp lực theo thời gian.

### 3.2. Mô hình áp suất - thời gian

Một mô hình phù hợp là Pressure-Time Index, viết tắt là PTI:

```text
PTI_i,j(t) = ∫ max(P_i,j(t) - P_ngưỡng, 0) dt
```

Trong đó:

```text
P_i,j(t)     = áp suất tại cell hàng i, cột j theo thời gian
P_ngưỡng     = ngưỡng áp suất tham chiếu
PTI_i,j(t)   = chỉ số tích lũy nguy cơ tại cell i,j
```

Nếu `P_i,j(t)` vượt ngưỡng trong thời gian dài, PTI tăng. Khi PTI vượt giới hạn cho phép, bộ điều khiển có thể kích hoạt xả khí hoặc tái phân bố áp lực sang vùng khác.

### 3.3. Ngưỡng 32 mmHg

Trong nhiều tài liệu về loét tì đè, giá trị 32 mmHg thường được nhắc đến như một mốc tham chiếu liên quan đến áp lực mao mạch. Tuy nhiên, không được trình bày 32 mmHg như ngưỡng tuyệt đối cho mọi người bệnh, mọi vùng mô và mọi thời gian. Trong đề tài này, 32 mmHg chỉ nên được dùng như:

```text
mốc tham chiếu ban đầu cho thuật toán cảnh báo và mô phỏng
```

Không nên dùng nó như một ngưỡng chẩn đoán lâm sàng tuyệt đối.

---

## 4. Cơ sở cơ học của cell khí thích ứng

### 4.1. Vai trò của cell khí

Mỗi cell khí là một phần tử nâng đỡ mềm. Khi áp suất khí trong cell tăng, cell có xu hướng nâng vùng cơ thể phía trên lên và nhận nhiều tải hơn. Khi áp suất khí giảm, cell mềm hơn, vùng cơ thể tương ứng lún xuống nhiều hơn và tải có thể được chuyển sang các cell lân cận.

Bộ điều khiển cần đạt cân bằng giữa hai mục tiêu:

```text
giảm áp tại vùng nguy cơ cao
vẫn duy trì tư thế cơ thể ổn định và thoải mái
```

Nếu xả khí quá nhiều tại một cell, áp lực có thể tăng ở cell lân cận. Vì vậy, điều khiển phải xét toàn ma trận, không chỉ từng cell độc lập.

### 4.2. Quan hệ lực - áp suất - diện tích

Áp suất cơ học được xác định bởi:

```text
P = F / A
```

Trong đó:

```text
P = áp suất, đơn vị Pa hoặc mmHg
F = lực tác dụng, đơn vị N
A = diện tích chịu lực, đơn vị m²
```

Đổi đơn vị:

```text
1 mmHg = 133.322 Pa
```

Với patch Velostat `50 × 50 mm`:

```text
A = 0.05 × 0.05 = 0.0025 m²
```

Nếu đặt vật nặng 1 kg lên đúng diện tích patch:

```text
F = m × g = 1 × 9.81 = 9.81 N
P = 9.81 / 0.0025 = 3924 Pa
P = 3924 / 133.322 ≈ 29.4 mmHg
```

Bảng tham chiếu tải trọng cho patch `50 × 50 mm`:

| Khối lượng | Lực xấp xỉ | Áp suất xấp xỉ |
|---:|---:|---:|
| 0.25 kg | 2.45 N | 7.4 mmHg |
| 0.50 kg | 4.91 N | 14.7 mmHg |
| 1.00 kg | 9.81 N | 29.4 mmHg |
| 1.50 kg | 14.72 N | 44.1 mmHg |
| 2.00 kg | 19.62 N | 58.9 mmHg |
| 2.50 kg | 24.53 N | 73.6 mmHg |

Bảng này là cơ sở để thiết kế thí nghiệm hiệu chuẩn cảm biến.

---

## 5. Cơ sở vật liệu Velostat/Linqstat

### 5.1. Mô tả vật liệu

Velostat, còn được gọi là Linqstat, là vật liệu polymer dẫn điện có tính nhạy áp. Theo mô tả sản phẩm của Adafruit, vật liệu này có tính chất pressure-sensitive: khi bị ép, điện trở giảm, nên có thể dùng để tạo cảm biến mềm trong các ứng dụng wearable/sensor hacking [1].

Thông số sản phẩm đã xác minh từ nguồn nhà cung cấp:

```text
Kích thước tấm:        11 × 11 inch ≈ 280 × 280 mm
Độ dày:                4 mil ≈ 0.1 mm
Khối lượng:            18.66 g
Giới hạn nhiệt độ:     -45°C đến 65°C
Heat sealable:         Có
Volume resistivity:    < 500 ohm·cm
Surface resistivity:   < 31,000 ohms/sq.cm
```

Các thông số này đủ để xác định kích thước hình học ban đầu cho mô hình, nhưng chưa đủ để xác định chính xác quan hệ áp suất - điện trở.

### 5.2. Không suy diễn trực tiếp R(P) từ điện trở suất thể tích

Nếu lấy công thức vật liệu đồng nhất:

```text
R = ρ × L / A
```

với:

```text
ρ < 500 ohm·cm
L = 0.01 cm
A = 25 cm²
```

thì:

```text
R < 500 × 0.01 / 25 = 0.2 ohm
```

Giá trị này không đại diện cho cảm biến Velostat thực tế trong cấu trúc copper tape sandwich. Điện trở đo được trong thực tế còn bị chi phối bởi:

- điện trở tiếp xúc giữa copper tape và Velostat;
- độ nhám bề mặt;
- diện tích điện cực thực sự tiếp xúc;
- lớp keo của copper tape;
- biến dạng của lớp phủ và túi silicone;
- phân bố áp lực không đều;
- hysteresis, drift và creep của vật liệu.

Do đó, điện trở suất trong datasheet chỉ dùng để mô tả tính dẫn điện tổng quát, không dùng để thay thế thí nghiệm hiệu chuẩn `R(P)`.

### 5.3. Phi tuyến, hysteresis và drift

Các nghiên cứu về Velostat/polyethylene-carbon composite cho thấy vật liệu này có đáp ứng phi tuyến, có hysteresis và cần xử lí dữ liệu hoặc hiệu chuẩn để cải thiện độ chính xác. Dzedzickis và cộng sự chỉ ra rằng cảm biến dựa trên Velostat cần quá trình loading/unloading/reloading ban đầu trước khi hiệu chuẩn, đồng thời vật liệu có hysteresis đáng kể và có vấn đề drift/settling theo tải và thời gian [4]. Một nghiên cứu khác về cảm biến Velostat dùng copper tape cũng ghi nhận tính phi tuyến, hysteresis và voltage drift khi thử với tải trọng chuẩn [2].

Vì vậy, trong báo cáo không được viết rằng Velostat là cảm biến tuyến tính hoặc có độ chính xác cao sẵn có. Cách diễn đạt đúng là:

```text
Velostat là vật liệu nhạy áp chi phí thấp, mềm và dễ tích hợp, nhưng cần hiệu chuẩn thực nghiệm do đáp ứng phi tuyến, hysteresis và drift.
```

---

## 6. Cấu trúc cảm biến Velostat + copper tape

### 6.1. Lựa chọn cấu trúc sandwich

Cấu trúc cảm biến được chọn cho mô hình chính là sandwich electrode:

```text
Lớp vải/TPU phủ phía trên
Copper tape điện cực trên
Velostat 50 × 50 mm
Copper tape điện cực dưới
Lớp nền mềm / túi silicone
```

Lý do chọn sandwich:

1. Hình học đơn giản, dễ chế tạo.
2. Dễ mô hình hóa hơn điện cực răng lược.
3. Lực ép và dòng điện chủ yếu đi theo phương gần vuông góc với bề mặt.
4. Phù hợp với thí nghiệm hiệu chuẩn bằng quả cân.
5. Có bằng chứng từ nghiên cứu trước về việc dùng copper tape ở trên và dưới Velostat để tạo cảm biến áp lực [2].

### 6.2. Vai trò của copper tape

Copper tape không phải là phần tử cảm biến chính. Vai trò của nó là điện cực dẫn điện để đưa dòng điện qua Velostat và thu tín hiệu điện áp. Copper tape có ưu điểm là rẻ, dễ mua, dễ cắt và dễ dán. Tuy nhiên, nó cũng có nhược điểm:

- có thể làm cứng vùng cảm biến;
- mép đồng có thể sắc nếu không được phủ bảo vệ;
- lớp keo có thể làm thay đổi điện trở tiếp xúc;
- có thể nứt hoặc bong nếu bị uốn lặp lại nhiều lần.

Do đó, trong bản prototype, copper tape cần được phủ bằng lớp vải hoặc TPU mỏng, không để tiếp xúc trực tiếp với da hoặc túi silicone ở mép sắc.

### 6.3. Kích thước patch và điện cực

Thông số đề xuất:

```text
Velostat patch:        50 × 50 mm
Copper electrode:      40-45 × 40-45 mm
Cell outer size:       98 × 98 mm
Silicone bag base:     khoảng 90 × 90 mm
```

Patch Velostat không cần phủ toàn bộ cell. Kích thước `50 × 50 mm` giúp cân bằng giữa độ nhạy, vật liệu sử dụng và khả năng phân giải theo cell.

---

## 7. Mô hình điện của cảm biến

### 7.1. Mạch chia áp

Một cấu hình đọc tín hiệu đơn giản là:

```text
3.3V ---- Velostat ---- ADC node ---- R_fixed ---- GND
```

Điện áp tại ADC:

```text
Vout = Vcc × R_fixed / (R_velostat + R_fixed)
```

Với cấu hình này:

```text
áp suất tăng
→ R_velostat giảm
→ Vout tăng
→ ADC tăng
```

Nếu dùng ADC 12-bit:

```text
ADC = round(Vout / Vcc × 4095)
```

Cần thống nhất chiều tín hiệu trong phần cứng và phần mềm. Nếu đảo vị trí `R_fixed` và Velostat, chiều ADC sẽ ngược lại.

### 7.2. Mô hình R(P) tạm thời

Do datasheet hiện tại chưa cung cấp đường `R(P)`, giai đoạn mô phỏng ban đầu có thể dùng mô hình phi tuyến dạng Hill/logistic:

```text
R(P) = R_min + (R_max - R_min) / (1 + (P / P50)^γ)
```

Trong đó:

```text
P       = áp suất hiệu dụng trên patch
R(P)    = điện trở đo giữa hai điện cực
R_max   = điện trở khi không tải hoặc tải rất nhỏ
R_min   = điện trở khi tải lớn
P50     = áp suất tại vùng chuyển tiếp
γ       = hệ số độ dốc
```

Mô hình này chỉ phản ánh xu hướng định tính:

```text
áp suất tăng → điện trở giảm
```

Các tham số `R_min`, `R_max`, `P50`, `γ` chưa được xác minh cho prototype của dự án. Vì vậy, mọi kết quả ADC/mmHg từ mô hình này phải ghi là **placeholder** cho tới khi có hiệu chuẩn thực nghiệm.

### 7.3. Mô hình tích phân theo pressure field

Khi SOFA tạo được trường áp suất `P(x,y,t)` trên patch, mô hình cảm biến có thể nâng cấp từ áp suất trung bình sang mô hình tích phân:

```text
G_total(t) = ∫_A σ(P(x,y,t)) dA / h
R_total(t) = 1 / G_total(t)
```

Trong đó:

```text
G_total     = điện dẫn tổng
σ(P)        = độ dẫn điện phụ thuộc áp suất
A           = vùng điện cực tác dụng
h           = độ dày Velostat
P(x,y,t)    = trường áp suất theo không gian và thời gian
```

Mô hình này thuyết phục hơn áp suất trung bình, nhưng chỉ nên dùng khi có dữ liệu thực nghiệm đủ để fit `σ(P)` hoặc `R(P)`.

---

## 8. Đọc nhiều cảm biến và dựng heatmap

### 8.1. Số kênh đọc

Với ma trận `5 × 9`, hệ thống có:

```text
45 cell
45 patch Velostat
45 tín hiệu cảm biến
```

Giai đoạn R&D nên đọc từng sensor độc lập qua multiplexer analog thay vì dùng ma trận hàng-cột, vì ma trận hàng-cột dễ gặp ghosting khi nhiều điểm bị ép cùng lúc.

Phương án đề xuất:

```text
3 × CD74HC4067
```

Vì:

```text
1 module CD74HC4067 = 16 kênh
3 module = 48 kênh
```

Dư 3 kênh để dự phòng.

### 8.2. Dữ liệu heatmap

Sau khi đọc ADC, phần mềm chuyển mỗi frame thành ma trận:

```text
ADC_map.shape = (9, 5)
pressure_map.shape = (9, 5)
```

Trong đó:

```text
pressure_map[0, :]  = vùng vai
pressure_map[4-5,:] = vùng mông/cùng cụt
pressure_map[8, :]  = vùng đùi trên
```

Các loại bản đồ cần có:

1. **Raw ADC heatmap:** dữ liệu thô từ ADC.
2. **Calibrated pressure heatmap:** ADC đã chuyển sang mmHg.
3. **Risk mask:** vùng vượt ngưỡng tham chiếu.
4. **PTI heatmap:** tích lũy áp lực theo thời gian.

---

## 9. Cơ sở mô phỏng SOFA

### 9.1. Vì sao không dùng Gazebo làm nền chính

Gazebo phù hợp với robot cơ khí cứng, link, joint, rigid-body và va chạm cơ bản. Tuy nhiên, bài toán của đề tài gồm:

```text
vật liệu mềm
lớp cảm biến mỏng
túi silicone biến dạng
contact pressure
đáp ứng điện trở phụ thuộc áp lực
```

Đây không phải miền mạnh của Gazebo/URDF. Nếu dùng Gazebo, phải viết plugin riêng để biến contact force thành điện trở cảm biến, trong khi phần soft-body/contact vẫn không thật sự thuận lợi.

### 9.2. Vì sao chọn SOFA

SOFA là framework mô phỏng vật lí hướng đến mô phỏng y sinh, soft tissue, FEM và hệ đa mô hình. Các tài liệu về SOFA mô tả framework này như một nền tảng open-source cho mô phỏng y sinh, có khả năng mô hình hóa thành phần như state vector, mass, force field, constraint, topology, integration scheme và solver [5]. SOFA vì vậy phù hợp hơn cho việc mô phỏng lớp cảm biến mềm và tương tác cơ học với tải.

### 9.3. Vai trò của SOFA trong đề tài

SOFA phụ trách mô hình cơ học:

```text
lực/tải cơ thể
→ biến dạng lớp phủ, Velostat, silicone
→ trường áp suất P(x,y,t)
```

Python hoặc module xử lý riêng phụ trách mô hình điện và heatmap:

```text
P(x,y,t)
→ R(t)
→ Vout(t)
→ ADC(t)
→ pressure_map(t)
→ heatmap
```

### 9.4. Batch/headless simulation

Trong WSL, GUI SOFA có thể không ổn định do OpenGL/WSLg. Vì vậy, dự án chuyển sang batch/headless workflow. Đây không phải điểm yếu; ngược lại, batch mode phù hợp hơn với nghiên cứu vì:

- dễ lặp lại;
- dễ ghi CSV/log;
- dễ sweep tham số;
- không phụ thuộc GUI;
- dễ tích hợp vào pipeline báo cáo.

Scene hiện tại:

```text
simulation/sofa/scenes/single_velostat_patch_batch.py
```

Đây là scene v0 dùng lực phân bố lên patch Velostat `50 × 50 × 0.1 mm`. Nó chưa phải contact model hoàn chỉnh, nhưng là bước kiểm tra đầu tiên để xác nhận pipeline:

```text
SOFA mechanics → CSV → postprocess → pressure/ADC plot
```

---

## 10. Quy trình hiệu chuẩn thực nghiệm

### 10.1. Mục tiêu

Hiệu chuẩn nhằm thay thế mô hình `R(P)` giả định bằng quan hệ thực nghiệm:

```text
mass → pressure → resistance/ADC
```

hoặc trực tiếp:

```text
ADC → pressure
```

### 10.2. Cấu hình thí nghiệm đề xuất

Một sensor mẫu gồm:

```text
copper tape trên
Velostat 50 × 50 mm
copper tape dưới
R_fixed trong mạch chia áp
ADC 12-bit
lớp phủ/vải giống điều kiện sử dụng
nền silicone hoặc nền mềm tương đương
```

Tải trọng chuẩn:

```text
0 kg
0.25 kg
0.50 kg
1.00 kg
1.50 kg
2.00 kg
2.50 kg
```

Quy trình:

1. Đặt sensor trên nền giống điều kiện sử dụng thật.
2. Dùng tấm ép phẳng `50 × 50 mm` để phân bố tải đều.
3. Đặt tải, chờ ổn định 5-10 giây.
4. Ghi ADC trong 3-5 giây.
5. Lặp lại ít nhất 3 lần.
6. Thực hiện cả chu kỳ tăng tải và giảm tải để đo hysteresis.
7. Fit mô hình `ADC(P)` hoặc `R(P)`.

### 10.3. Chỉ số đánh giá

Các chỉ số cần báo cáo:

```text
MAE  = sai số tuyệt đối trung bình
RMSE = căn trung bình bình phương sai số
R²   = hệ số xác định của đường fit
CV   = hệ số biến thiên giữa các lần lặp
Hysteresis error
Drift theo thời gian
Response time
```

Nếu chưa có các chỉ số này, không được khẳng định hệ thống đo áp suất có độ chính xác định lượng.

---

## 11. Mô hình điều khiển đệm khí

### 11.1. Đầu vào điều khiển

Bộ điều khiển nhận:

```text
pressure_map(t)
PTI_map(t)
trạng thái van
trạng thái bơm
áp suất khí từng cell nếu có cảm biến áp suất khí
```

### 11.2. Logic điều khiển ban đầu

Một luật điều khiển ban đầu:

```text
Nếu P_i,j > P_ngưỡng trong thời gian T_ngưỡng:
    xả hoặc giảm áp cell i,j
    kiểm tra áp lực các cell lân cận
    tránh tạo hotspot mới
```

Một luật dựa trên PTI:

```text
Nếu PTI_i,j > PTI_ngưỡng:
    kích hoạt tái phân bố áp lực
```

### 11.3. Điều kiện an toàn

Điều khiển đệm khí cần tránh:

- xả khí quá nhanh;
- bơm quá căng;
- thay đổi áp suất liên tục gây khó chịu;
- phản ứng sai do cảm biến nhiễu;
- tạo vùng áp lực cao mới ở cell lân cận.

Do đó, bộ điều khiển cần có lọc tín hiệu, hysteresis điều khiển, giới hạn tốc độ bơm/xả và cơ chế fail-safe.

---

## 12. Giao tiếp hỗ trợ người hạn chế vận động

Ngoài chức năng cơ khí và cảm biến, hệ thống còn hướng đến hỗ trợ giao tiếp. Khi người bệnh không thể tự xoay trở hoặc gọi người chăm sóc, hệ thống có thể:

```text
hiển thị heatmap áp lực
cảnh báo vùng nguy cơ
đề xuất đổi tư thế
gửi tín hiệu yêu cầu hỗ trợ
kết hợp giao diện AAC hoặc eye-tracking trong giai đoạn sau
```

Phần giao tiếp không thay thế chăm sóc y tế, nhưng đóng vai trò tăng khả năng phản hồi và giảm thời gian vùng mô phải chịu áp lực kéo dài.

---

## 13. Kiểm soát ảo giác và phân loại claim

Theo quy trình ARS, các claim trong đề tài được phân loại như sau:

| Claim | Trạng thái | Cách dùng |
|---|---|---|
| Velostat/Linqstat là vật liệu nhạy áp, ép làm giảm điện trở | Đã có nguồn hỗ trợ | Có thể dùng trong cơ sở lí thuyết |
| Tấm Velostat có kích thước 280 × 280 mm, dày 0.1 mm | Đã xác minh từ product page | Có thể dùng trong thiết kế |
| Velostat có phi tuyến, hysteresis, drift | Có nguồn nghiên cứu hỗ trợ | Phải đưa vào giới hạn và hiệu chuẩn |
| Copper tape sandwich có thể dùng làm điện cực | Có bằng chứng hỗ trợ | Dùng cho prototype, cần hiệu chuẩn riêng |
| Đường R(P) chính xác của sensor 50 × 50 mm | Chưa xác minh | Không được khẳng định |
| Sai số mmHg của hệ thống thật | Chưa xác minh | Chỉ có sau calibration |
| SOFA v0 cho pressure field hoàn chỉnh | Chưa đúng | V0 chỉ là kiểm tra pipeline |
| Hệ thống đạt chuẩn y tế | Chưa xác minh | Không được khẳng định |

Quy tắc quan trọng:

```text
Không biến giả định mô phỏng thành kết luận thực nghiệm.
Không biến product description thành bằng chứng định lượng về R(P).
Không dùng heatmap mô phỏng để khẳng định độ chính xác của prototype thật.
```

---

## 14. Giới hạn hiện tại

Các giới hạn cần nêu rõ trong báo cáo:

1. Datasheet Velostat hiện tại chưa cung cấp đường áp suất - điện trở `R(P)`.
2. Mô hình `R(P)` đang dùng trong mô phỏng chỉ là placeholder.
3. Velostat có phi tuyến, hysteresis, drift và cần hiệu chuẩn.
4. Copper tape có thể làm thay đổi độ mềm và điện trở tiếp xúc.
5. Scene SOFA hiện tại mới là v0 force-controlled, chưa phải contact model đầy đủ.
6. Ma trận `5 × 9` chưa phủ toàn bộ cơ thể, đặc biệt chưa phủ riêng vùng gót chân.
7. Bản đồ áp lực bề mặt không hoàn toàn đại diện cho ứng suất sâu trong mô.
8. Chưa có thử nghiệm lâm sàng, nên không được tuyên bố tính năng y tế/clinical-grade.

---

## 15. Lộ trình phát triển tiếp theo

### 15.1. Giai đoạn mô phỏng

```text
1. Hoàn thiện SOFA batch single-patch.
2. Sweep tải trọng 0.25-2.5 kg.
3. Xuất pressure/ADC curve từ mô hình.
4. Nâng cấp từ distributed force sang contact plate.
5. Thêm silicone support đàn hồi.
6. Mở rộng 3 × 3 để đánh giá crosstalk cơ học.
7. Mở rộng 5 × 9 để dựng heatmap toàn module.
```

### 15.2. Giai đoạn thực nghiệm

```text
1. Chế tạo 1 sensor Velostat + copper tape.
2. Đo ADC với tải trọng chuẩn.
3. Đánh giá repeatability, hysteresis, drift.
4. Fit mô hình ADC(P) hoặc R(P).
5. Nhân rộng lên 5 sensor một hàng.
6. Nhân rộng lên 45 sensor.
7. So sánh heatmap thực nghiệm với mô phỏng.
```

### 15.3. Giai đoạn điều khiển

```text
1. Tạo thuật toán phát hiện hotspot.
2. Tính PTI theo cell.
3. Điều khiển van/bơm theo vùng nguy cơ.
4. Đánh giá khả năng giảm hotspot.
5. Tích hợp cảnh báo và giao tiếp hỗ trợ.
```

---

## 16. Kết luận

Cơ sở lí thuyết của hệ thống đệm khí thích ứng được xây dựng trên sự kết hợp của bốn miền chính:

```text
1. Sinh học loét tì đè:
   áp lực kéo dài và lực cắt gây nguy cơ tổn thương mô.

2. Cơ học đệm khí:
   cell khí thay đổi áp suất để tái phân bố lực nâng đỡ cơ thể.

3. Cảm biến Velostat:
   vật liệu nhạy áp làm thay đổi điện trở khi bị nén, nhưng có phi tuyến, hysteresis và cần hiệu chuẩn.

4. Mô phỏng SOFA và heatmap:
   SOFA mô phỏng biến dạng/contact, Python chuyển áp suất thành điện trở, ADC và bản đồ nhiệt.
```

Cấu hình `5 × 9` với patch Velostat `50 × 50 mm` là lựa chọn hợp lí cho giai đoạn đầu vì cân bằng giữa vùng phủ cơ thể, chi phí vật liệu, số lượng van/cảm biến và độ phức tạp hiệu chuẩn. Tuy nhiên, để đạt mức nghiên cứu nghiêm túc, mọi kết luận định lượng về áp suất phải dựa trên hiệu chuẩn thực nghiệm và đối chứng mô phỏng, không dựa riêng vào datasheet hoặc mô hình placeholder.

---

## Tài liệu tham khảo

[1] Adafruit. **Pressure-Sensitive Conductive Sheet (Velostat/Linqstat), Product ID 1361.** Truy cập 2026-07-28. URL: https://www.adafruit.com/product/1361

[2] Sharma, M. D., & Binong, J. **Performance Evaluation of a Specialized Pressure Sensor for Pick and Place Operations.** *Engineering Proceedings*, 58(1), 74, 2023. DOI: https://doi.org/10.3390/ecsa-10-16586. URL: https://www.mdpi.com/2673-4591/58/1/74

[3] Dzedzickis, A., Sutinys, E., Bucinskas, V., Samukaite-Bubniene, U., Jakstys, B., Ramanavicius, A., & Morkvenaite-Vilkonciene, I. **Polyethylene-Carbon Composite (Velostat®) Based Tactile Sensor.** *Polymers*, 12(12), 2905, 2020. DOI: https://doi.org/10.3390/polym12122905. URL: https://www.mdpi.com/2073-4360/12/12/2905

[4] Allard, J., Cotin, S., Faure, F., Bensoussan, P. J., Poyer, F., Duriez, C., Delingette, H., & Grisoni, L. **SOFA — An Open Source Framework for Medical Simulation.** INRIA/HAL. URL: https://inria.hal.science/inria-00319416/document

[5] Soft Robotics Toolkit. **Modeling, Simulation and Control of Soft Robots with SOFA.** URL: https://softroboticstoolkit.com/book/export/html/882426

---

## Phụ lục A — Công thức chính

### A.1. Áp suất từ tải trọng

```text
P = F / A
F = m × g
P(mmHg) = P(Pa) / 133.322
```

### A.2. Mạch chia áp

```text
Vout = Vcc × R_fixed / (R_velostat + R_fixed)
ADC = round(Vout / Vcc × 4095)
```

### A.3. Mô hình R(P) placeholder

```text
R(P) = R_min + (R_max - R_min) / (1 + (P / P50)^γ)
```

### A.4. Pressure-Time Index

```text
PTI_i,j(t) = ∫ max(P_i,j(t) - P_ngưỡng, 0) dt
```

---

## Phụ lục B — Trạng thái bằng chứng

```text
Đã xác minh:
- Kích thước và độ dày Velostat theo product page.
- Tính chất nhạy áp định tính của Velostat.
- Tồn tại nghiên cứu dùng Velostat + copper tape.
- Velostat có phi tuyến/hysteresis/drift.

Cần kiểm chứng bằng thực nghiệm:
- R(P) của sensor 50 × 50 mm.
- Sai số chuyển ADC sang mmHg.
- Độ ổn định dài hạn trên đệm khí.
- Crosstalk giữa các cell.
- Hiệu quả giảm hotspot của điều khiển van/bơm.
```
