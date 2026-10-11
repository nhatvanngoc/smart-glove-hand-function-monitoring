# BÁO CÁO CHUYÊN MÔN: TỔNG QUAN THUẬT TOÁN AAN VÀ CƠ CHẾ PHỤC HỒI CHỨC NĂNG BÀN TAY SAU ĐỘT QUỴ

---

### 1. GIỚI THIỆU TỔNG QUAN VÀ NGUYÊN LÝ CAN THIỆP TỐI THIỂU (MINIMAL INTERVENTION) CỦA ALGORITHM AAN

#### 1.1. Bối cảnh Y tế và Đặt vấn đề Phục hồi Vận động Chi trên sau Đột quỵ
Suy giảm chức năng vận động là một trong những hệ lụy lâm sàng phổ biến và nghiêm trọng nhất sau đột quỵ, ảnh hưởng tới **từ 1/2 đến 3/4 (50% - 75%)** tổng số bệnh nhân. Tiến trình phục hồi tổn thương thần kinh - cơ diễn ra mạnh mẽ nhất trong cửa sổ thời gian vàng là **3 tháng đầu** sau biến cố mạch máu não. 

Tổn thương vận động chi trên (Upper Limb - UL) gây suy giảm trực tiếp khả năng thực hiện hành vi, tước đi tính độc lập trong sinh hoạt và hạn chế mức độ tham gia xã hội của người bệnh. Việc tối thiểu hóa khuyết tật vận động chi trên thông qua các liệu pháp can thiệp sớm đóng vai trò quyết định giúp bệnh nhân tái khôi phục sự tự chủ trong các hoạt động sinh hoạt hàng ngày (ADL) và tái hòa nhập cộng đồng bền vững.

#### 1.2. Khái niệm và Triết lý Can thiệp Tối thiểu (Minimal Intervention) của AAN
Trong kiến trúc điều khiển của Hệ thống Găng tay thông minh phục hồi chức năng, thuật toán Hỗ trợ theo nhu cầu (Assist-as-Needed - AAN) đóng vai trò trung tâm điều phối với triết lý can thiệp kỹ thuật - y sinh được xác định rõ:

*   **Định nghĩa Thuật toán AAN:** Là thuật toán điều khiển trợ lực thích ứng theo thời gian thực, có khả năng định lượng chính xác mức độ nỗ lực vận động chủ động của bệnh nhân và chỉ cung cấp một lượng lực cơ học vừa đủ để bù đắp đúng khoảng thiếu hụt chức năng.
*   **Triết lý Can thiệp Tối thiểu (Minimal Intervention):**
    *   *Triệt tiêu sự can thiệp thừa:* Hệ thống không bao giờ áp đặt cử động cưỡng bức khi bệnh nhân còn khả năng tự phát tín hiệu vận động nội sinh.
    *   *Kích hoạt nỗ lực vỏ não tối đa:* Bằng cách duy trì khoảng thiếu hụt lực tối thiểu, thuật toán bắt buộc vỏ não và các đường truyền thần kinh - cơ của bệnh nhân phải hoạt động ở ngưỡng nỗ lực chủ động tối đa, ngăn ngừa hiệu ứng "ỷ lại công nghệ" và hiện tượng thoái hóa do không sử dụng (Learned Non-use).

---

### 2. CƠ CHẾ NHẬN BIẾT NỔ LỰC CHỦ ĐỘNG QUA MẠCH VI SAI VELOSTAT (ACTIVE EFFORT INDEX - EI)

#### 2.1. Cấu trúc Cảm biến Vi sai 2 Vách Velostat Lòng - Mu Bàn tay
Giải pháp phần cứng của thiết bị ứng dụng vật liệu cảm biến áp suất Velostat — một polymer bán dẫn sở hữu đặc tính biến thiên điện trở tỷ lệ nghịch với áp lực cơ học tác động. Cảm biến được tích hợp đối xứng tại hai vách đối lập của ngón tay/bàn tay để ghi nhận chính xác động học cơ học hai chiều gập - duỗi.

| Cảm biến Mặt Lòng bàn tay (Palmar Sensor) | Cảm biến Mặt Mu bàn tay (Dorsal Sensor) |
| :--- | :--- |
| **Vị trí:** Tích hợp tại mặt lòng bàn tay và mặt dưới các ngón tay. | **Vị trí:** Tích hợp tại mặt mu bàn tay và mặt trên các ngón tay. |
| **Tín hiệu:** Đo lường áp lực cơ học sinh ra khi bệnh nhân nỗ lực **Gập ngón tay (Flexion)**. | **Tín hiệu:** Đo lường áp lực cơ học sinh ra khi bệnh nhân nỗ lực **Duỗi ngón tay (Extension)**. |
| **Đặc tính:** Điện trở Velostat giảm tỷ lệ thuận với sự tăng áp lực gập chủ động. | **Đặc tính:** Điện trở Velostat giảm tỷ lệ thuận với sự tăng áp lực duỗi chủ động. |

#### 2.2. Phương pháp Tính toán Chỉ số Nỗ lực Chủ động (Active Effort Index - EI)
Để trích xuất trung thực tín hiệu nỗ lực thần kinh - cơ từ vỏ não xuống chi trên, hệ thống triển khai giải pháp mạch xử lý vi sai nhằm loại bỏ nhiễu cơ học thụ động và các nhiễu đồng pha (Common-mode artifacts) phát sinh do rung động phần cứng, trọng lực hoặc trương lực cơ nghỉ.

Chỉ số Nỗ lực Chủ động ($EI$) được trích xuất thời gian thực theo công thức toán học - y sinh:

> $$EI = |S_{palmar} - S_{dorsal}| - S_{resting\_tone}$$
>
> *Trong đó:*
> * $EI$ *(Active Effort Index)*: Chỉ số phản ánh mức độ nỗ lực phát tín hiệu thần kinh - cơ chủ động của vỏ não tại thời điểm thực hiện cử động.
> * $S_{palmar}$: Tín hiệu điện áp trích xuất từ vách cảm biến mặt lòng.
> * $S_{dorsal}$: Tín hiệu điện áp trích xuất từ vách cảm biến mặt mu.
> * $|S_{palmar} - S_{dorsal}|$: Cấu trúc vi sai thực hiện triệt nhiễu đồng pha (Common-Mode Rejection) do chuyển động cơ học ngoại dung và lực cản thụ động.
> * $S_{resting\_tone}$: Ngưỡng điện áp đại diện cho trương lực cơ nghỉ (baseline resting tone), được trừ loại để triệt tiêu hoàn toàn đáp ứng co cơ thụ động hoặc co cứng (spasticity) nền.

Chỉ số $EI$ là thước đo định lượng trực tiếp cường độ phát xung từ vỏ não vận động qua bó tháp xuống các cơ ngón tay tại thời điểm thực thi.

---

### 3. CÔNG THỨC TÍNH TOÁN VÀ MÔ HÌNH TRỢ LỰC THÍCH ỨNG (RAL VÀ GAP)

#### 3.1. Xác định Khoảng Thiếu hụt Chức năng (Deficit Gap - GAP)
Khoảng thiếu hụt chức năng ($GAP$) đại diện cho lượng nỗ lực vận động còn thiếu giữa mục tiêu cơ học cần đạt và nỗ lực thực tế bệnh nhân bỏ ra. Thuật toán xác định $GAP$ liên tục thông qua chu trình phản hồi kín thời gian thực (Real-time Closed-Loop Feedback):

1.  **Thiết lập Ngưỡng Mục tiêu ($Target$):** Xác định ngưỡng nỗ lực cơ học $Target$ tối thiểu cần đạt để hoàn thành trọn vẹn quỹ đạo không gian của cử động chức năng (gập/duỗi ngón).
2.  **Đo lường Nỗ lực Thực tế ($EI$):** Mạch cảm biến vi sai Velostat thu thập tín hiệu điện trở biến thiên và tính toán chỉ số $EI$ ngay khi bệnh nhân bộc lộ ý định vận động.
3.  **Tính toán $GAP$ Thời gian thực:**
    $$GAP = Target - EI$$
4.  **Phân nhánh Phản hồi:**
    *   Nếu $EI \ge Target \Rightarrow GAP = 0$: Bệnh nhân tự chủ hoàn thành cử động, hệ thống triệt tiêu hoàn toàn lực trợ giúp ($RAL = 0$).
    *   Nếu $EI < Target \Rightarrow GAP > 0$: Bệnh nhân không đủ nỗ lực nội sinh, tín hiệu $GAP$ chính là biên độ thiếu hụt cần trợ lực.

#### 3.2. Mô hình Điều khiển Trợ lực Thích ứng (Required Assist Level - RAL)
Mức độ Trợ lực Yêu cầu ($RAL$) do cơ cấu chấp hành (Actuator) cung cấp được tính toán dựa trên mô hình thích ứng động:

$$RAL = f(GAP) = k \cdot GAP$$

*(trong đó $k$ là hệ số tăng cường thích ứng - Adaptation Gain Factor)*

**Cá nhân hóa Thuật toán dựa trên Chỉ số Sinh học MEP (Neurophysiological Tuning):**
*   **Nhóm bệnh nhân $MEP+$ (Bó tháp CST còn nguyên vẹn):** Hệ thống cài đặt đường cong giảm lực trợ giúp $RAL$ có độ dốc cao (tăng tốc độ giảm $k$ theo thời gian). Điều này tạo ra "áp lực thần kinh" buộc vỏ não tái kích hoạt nhanh chóng các đường truyền CST vốn còn khả năng dẫn truyền.
*   **Nhóm bệnh nhân $MEP-$ (Bó tháp CST tổn thương nặng):** Hệ thống duy trì một hệ số $k_{baseline}$ điều chỉnh thích hợp nhằm cung cấp trợ lực nền đủ lớn, giúp hoàn thành cử động đại thể (gross movement), ngăn ngừa hiện tượng mỏi cơ thứ phát, co cứng cơ hoặc hiện tượng "ỷ lại thần kinh".

**Sơ đồ Luồng Logic Điều khiển Thích ứng (Text-based Conditional Logic Flowchart):**

```
                  [Ý định Vận động từ Vỏ não]
                               │
                               ▼
            ┌─────────────────────────────────────┐
            │ Đo lường Tín hiệu Vi sai Velostat  │
            │ Trích xuất Active Effort Index (EI) │
            └──────────────────┬──────────────────┘
                               │
                               ▼
            ┌─────────────────────────────────────┐
            │       Tính toán GAP Thời gian thực  │
            │          (GAP = Target - EI)        │
            └──────────────────┬──────────────────┘
                               │
                               ▼
                    /───────────────────────\
                   /   Kiểm tra Điều kiện    \
                  <      GAP = Target - EI    >
                   \                         /
                    \───────────────────────/
                      /                   \
           If EI ≥ Target               If EI < Target
            (GAP ≤ 0)                    (GAP > 0)
                │                            │
                ▼                            ▼
┌──────────────────────────────┐ ┌──────────────────────────────┐
│ Ngắt Trợ lực Cơ học          │ │ Kích hoạt Trợ lực Thích ứng  │
│ RAL = 0                      │ │ RAL = k * GAP                │
│ (Tối đa hóa Nỗ lực Chủ động)│ │ (Hệ số k tùy biến MEP+/-)    │
└───────────────┬──────────────┘ └──────────────┬───────────────┘
                │                               │
                └──────────────┬────────────────┘
                               │
                               ▼
             ┌──────────────────────────────────┐
             │ Cơ cấu Chấp hành (Actuator)      │
             │ Tác động Lực kéo/Đẩy Ngón tay    │
             └─────────────────┬────────────────┘
                               │
                               ▼
             [Phản hồi Cảm giác Bản thể (Proprioception)]
             [  Trở lại Vỏ não Vận động (Hebbian Loop)  ]
```

---

### 4. CƠ SỞ KHOA HỌC THẦN KINH VÀ TÍNH DẺO THẦN KINH (NEUROPLASTICITY)

#### 4.1. Học thuyết Hebbian và Cơ chế Tính dẻo Thần kinh (Neuroplasticity)
Thuật toán AAN được xây dựng dựa trên nền tảng Sinh học Thần kinh hiện đại, cốt lõi là **Học thuyết Hebbian** (*"Neurons that fire together, wire together"*). 

Khi bệnh nhân phát ra ý định vận động chủ động (Motor Intention) từ vỏ não, tín hiệu thần kinh xuôi dòng (Efferent Motor Command) được truyền đi. Đúng vào thời điểm đó, găng tay AAN nhận biết chỉ số $EI$ và lập tức trợ lực hoàn thành cử động ngón tay, kích hoạt luồng tín hiệu cảm giác bản thể (Proprioceptive Sensorimotor Feedback) ngược dòng (Afferent Input) trở lại vỏ não. Sự đồng bộ chính xác về mặt thời gian (Temporally matched co-activation) giữa ý định chủ động nội sinh và phản hồi cảm giác ngoại sinh giúp tái củng cố các liên kết synap, kích thích tính dẻo thần kinh (Neuroplasticity) và phục hồi các đường truyền thần kinh bị tổn thương, đặc biệt là **bó tháp (Corticospinal Tract - CST)**.

#### 4.2. So sánh Đối chiếu: AAN Chủ động Thích ứng vs. Tập Thụ động Cưỡng bức (CPM)

| Tiêu chí So sánh | Tập Thụ động Cưỡng bức (CPM) | Trợ lực Thích ứng AAN (Assist-as-Needed) |
| :--- | :--- | :--- |
| **Cơ chế kích thích vỏ não** | Thụ động hoàn toàn; không kích hoạt tín hiệu vận động xuôi dòng từ vỏ não. | Bắt buộc vỏ não vận động phát ý định chủ động ($EI$) mới giải phóng trợ lực. |
| **Tính linh hoạt trợ lực** | Cố định theo chu kỳ máy móc, hoàn toàn vô cảm với trạng thái mệt mỏi hay tiến bộ của cơ bắp. | Thích ứng thời gian thực; Mức trợ lực $RAL$ tự động điều chỉnh theo từng miligiây dựa vào $GAP$. |
| **Kích hoạt tính dẻo thần kinh** | Rất hạn chế; dễ dẫn đến hiện tượng **ỷ lại thần kinh (Learned Non-use)**. | Tối đa hóa khả năng tái cấu trúc thần kinh nhờ kết hợp chặt chẽ efferent drive và afferent feedback. |
| **Hiệu quả phục hồi tinh vi** | Chỉ duy trì tầm vận động khớp thụ động (ROM), không khôi phục điều khiển thần kinh. | Hỗ trợ tái khôi phục khả năng kiểm soát vận động tinh và cử động ngón tay độc lập. |

#### 4.3. Ranh giới Thần kinh - Cơ và Bằng chứng Dự báo Lâm sàng từ Chỉ số Sinh học (Biomarkers)

**Ranh giới Phục hồi Vận động Tinh (Fine) vs. Vận động Thô (Gross):**
Bằng chứng điện sinh lý từ nghiên cứu của Ackerley và cộng sự khẳng định một ranh giới giải phẫu - thần kinh then chốt:
*   **Bệnh nhân $MEP+$ (Motor Evoked Potential positive):** Tính toàn vẹn của bó tháp CST được bảo tồn, cho phép phục hồi các cử động vận động tinh, linh hoạt và độc lập từng ngón tay (individuated finger movement) — đây chính là mục tiêu điều khiển vi sai ngón tay mà găng tay AAN hướng tới.
*   **Bệnh nhân $MEP-$ (Motor Evoked Potential negative):** Do sự mất mát tính toàn vẹn chức năng của bó tháp CST, bệnh nhân không thể khôi phục vận động tinh vi ngón tay. Tuy nhiên, họ vẫn có thể phục hồi vận động đại thể chi trên hoặc động tác gập/duỗi thô toàn bộ bàn tay nhờ vào các đường truyền thần kinh phụ trợ (như đường lưới - tủy / corticoreticulospinal tract).

```
Tổn thương Thần kinh Chi trên
        │
        ├───────────────────────────┬───────────────────────────┐
        ▼                                                       ▼
  Trạng thái MEP+                                         Trạng thái MEP-
 (CST Còn Nguyên vẹn)                                   (CST Mất Chức năng)
        │                                                       │
        ▼                                                       ▼
Khôi phục Vận động Tinh Ngón tay                        Khôi phục Vận động Thô / Gập-Duỗi Bàn tay
(Individuated Finger Movement)                          (Gross Hand Opening / Closing)
        │                                                       │
        ▼                                                       ▼
Thuật toán AAN Ngón tay Thích ứng                       Thuật toán AAN Trợ lực Nền Baseline
```

**Bằng chứng Định lượng từ Mô hình Dự báo PREP2:**
Mô hình dự báo phục hồi chi trên PREP2 kết hợp đánh giá lâm sàng SAFE (Shoulder Abduction and Finger Extension) vào ngày thứ 3 và chỉ số sinh học $MEP$ từ kích thích từ xuyên sọ (TMS) trong vòng 7 ngày đầu post-stroke mang lại giá trị chứng cứ cao:
*   **Độ chính xác Tổng thể:** Mô hình PREP2 đạt độ chính xác tổng thể **75%** trong dự báo khả năng phục hồi chức năng chi trên ở mốc 3 tháng.
*   **Độ chính xác Phân nhóm Tổn thương Nặng:** Đạt độ chính xác rất cao đối với các tiên lượng phục hồi Hạn chế (**85%**) và Kém (**90%**).
*   **Độ Bền vững Tiên lượng:** Tính chính xác của dự báo PREP2 duy trì ổn định lên tới **80%** ở thời điểm **2 năm** sau đột quỵ.
*   **Độ Nhạy Thời gian (Temporal Sensitivity):** Nếu việc thu thập chỉ số sinh học $MEP$ bị trì hoãn đến tuần thứ 2 (2 weeks post-stroke), độ chính xác dự báo của mô hình sụt giảm nghiêm trọng từ **75% xuống chỉ còn 60%**.

**Điểm Tin cậy Lâm sàng (Clinical Care Points):**
*   *Hạn chế của Đánh giá Lâm sàng Đơn thuần:* Dự báo phục hồi chi trên nếu chỉ dựa vào cảm quan lâm sàng ban đầu thường thiếu chính xác (đặc biệt ở bệnh nhân tổn thương vừa đến nặng), dẫn đến phân bổ nguồn lực phục hồi không hiệu quả.
*   *Tầm quan trọng của MEP Thu được từ TMS:* Chỉ số sinh học $MEP$ thu thập trong 7 ngày đầu sau đột quỵ là công cụ duy nhất xác định chính xác khả năng phục hồi vận động tinh ngón tay độc lập ở mốc 3 tháng.
*   *Tích hợp Chỉ số Sinh học vào Thuật toán Robot:* Thiết lập thông số thuật toán AAN ($k$, $Target$) theo trạng thái $MEP$ giúp tối ưu hóa tiến trình phục hồi thần kinh, ngăn ngừa mệt mỏi và hiện tượng learned non-use.

---

### 5. Ý NGHĨA KỸ THUẬT, TÍNH KINH TẾ VÀ VỊ THẾ TRONG CUỘC THI ViSEF

#### 5.1. Giá trị Kỹ thuật và Tối ưu Hóa Chi phí Sản xuất (< 1,5 Triệu VNĐ)

> **ĐỘT PHÁ KỸ THUẬT VÀ TÍNH KINH TẾ VƯỢT TRỘI**
>
> Dự án đã tích hợp thành công thuật toán điều khiển AAN phức tạp và giải pháp mạch cảm biến vi sai Velostat lên hệ thống phần cứng tối ưu với chi phí chế tạo **đẩy xuống dưới 1,5 triệu VNĐ** (~60 USD). Đây là một bước tiến đột phá kỹ thuật, giúp bình dân hóa công nghệ robot phục hồi chức năng cao cấp, mang lại khả năng tiếp cận rộng rãi cho số đông bệnh nhân đột quỵ tại Việt Nam so với các hệ thống Robot ngoại vi đắt đỏ nhập khẩu có giá thành từ **100.000 USD trở lên**.

#### 5.2. Tính Thực tiễn Đóng góp cho Cộng đồng và Mức độ Hòa nhập của Bệnh nhân
Nghiên cứu thực chứng trên 126 người bệnh đột quỵ điều trị ngoại trú tại Bệnh viện Hữu nghị Việt Tiệp cung cấp các luận cứ thực tế quan trọng:
*   **Điểm Hòa nhập Cộng đồng Tổng thể (CIQ):** Đạt điểm trung bình **26,64 ± 8,03**.
*   **Điểm Lĩnh vực Cụ thể:** Hòa nhập gia đình đạt điểm cao nhất (**9,36 ± 3,39**), trong khi hòa nhập mạng lưới xã hội đạt điểm thấp nhất (**4,42 ± 2,33**).
*   **Mối Tương quan Chất lượng Cuộc sống (EQ-5D-5L):** Mô hình hồi quy đa biến khẳng định chất lượng cuộc sống có mối tương quan thuận mạnh mẽ, có ý nghĩa thống kê với mức độ hòa nhập cộng đồng (**B = 6,937; p = 0,046**).

Việc ứng dụng Găng tay thông minh AAN phục hồi vận động tinh bàn tay giúp bệnh nhân nhanh chóng lấy lại khả năng tự chăm sóc (Self-care), trực tiếp nâng cao chỉ số EQ-5D-5L, từ đó thúc đẩy sự hòa nhập gia đình và tái hòa nhập mạng lưới xã hội.

#### 5.3. Vị thế Tính Đột phá và Triển vọng của Dự án tại Cuộc thi ViSEF
Dự án Găng tay thông minh trợ lực AAN khẳng định vị thế vượt trội tại Cuộc thi Khoa học Kỹ thuật Quốc gia (ViSEF) nhờ hội tụ đầy đủ ba trụ cột tri thức khoa học:

1.  **Nền tảng Khoa học Thần kinh Vững chắc:** Thiết kế thuật toán bám sát Học thuyết Hebbian, cơ chế tính dẻo thần kinh (Neuroplasticity), và ranh giới phục hồi bó tháp CST ($MEP+/MEP-$).
2.  **Sáng tạo Kỹ thuật Y sinh Xuất sắc:** Trích xuất thành công Chỉ số Nỗ lực Chủ động ($EI$) bằng mạch vi sai Velostat triệt nhiễu đồng pha và điều khiển trợ lực thích ứng chu trình kín $EI \rightarrow GAP \rightarrow RAL$ theo thời gian thực.
3.  **Tác động Kinh tế - Xã hội Toàn diện:** Giải quyết bài toán bình dân hóa thiết bị y tế cao cấp với chi phí < 1,5 triệu VNĐ, đáp ứng trực tiếp nhu cầu phục hồi chức năng vận động bàn tay cho hàng triệu bệnh nhân đột quỵ, nâng cao chỉ số CIQ và EQ-5D-5L trong bối cảnh y tế Việt Nam.

Với sự kết hợp hoàn hảo giữa lý thuyết thần kinh học tiên tiến, giải pháp kỹ thuật y sinh thông minh và giá trị nhân văn sâu sắc, đề tài sở hữu năng lực cạnh tranh mạnh mẽ, hứa hẹn trở thành một dự án tiên phong, đạt giải cao tại cuộc thi ViSEF và có khả năng ứng dụng thực tiễn rộng rãi.