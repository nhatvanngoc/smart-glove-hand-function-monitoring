# 06 — Thiết Kế Cơ Cấu Cơ Khí Khung Xương Ngoài (Exoskeleton Mechanics)

> **Ngày lập:** 2026-10-04  
> **Quyết định liên quan:** DEC-MECH-001 (Thiết kế nẹp ngón tay dạng mở bụng ngón có thanh gài), DEC-MECH-002 (Cơ cấu Print-in-Place toàn bộ bằng nhựa FDM), DEC-MECH-003 (Khớp rãnh trượt tự lựa bù sai số trục xoay giải phẫu), DEC-MECH-004 (Đốt ngoài cùng hở đầu ngón Open-Tip).  
> **Trạng thái:** **Mô hình CAD tham số 3D hoàn chỉnh & Đã xuất STL/STEP/FCStd** ([`3d_model/custom_exo/full_finger_modular/`](../3d_model/custom_exo/full_finger_modular/)).  
> **Công cụ thiết kế:** FreeCAD 1.1 Python API (`3d_model/generate_full_finger_modular.py`).

---

## 1. Đặt Vấn Đề Sinh Cơ Học (Biomechanical Background)

Trong các thiết bị găng tay nẹp phục hồi chức năng sau đột quỵ (Stroke Hand Exoskeleton), việc cố định các cảm biến và truyền lực trợ lực vận động đối mặt với 3 thách thức kỹ thuật cốt lõi:

1. **Hiện tượng Lệch Trục Động Học (Kinematic Axis Misalignment):**
   - Khớp liên đốt gần (PIP) và khớp liên đốt xa (DIP) của ngón tay người là các khớp bản lề giải phẫu có tâm xoay nằm sâu trong thân xương ngón tay.
   - Khi đặt bộ khung cơ khí ở mặt ngoài (mu ngón), trục quay của khung nằm cách tâm quay sinh học từ $12 - 15\,\text{mm}$.
   - Khi co ngón từ $0^\circ$ (duỗi thẳng) đến $85^\circ$ (nắm chặt), cung tròn của khung ngoài có bán kính lớn hơn ngón tay thật, khiến khoảng cách bề mặt mu ngón sinh học bị giãn dài ra theo công thức:
     $$\Delta s \approx r_{\text{offset}} \cdot \Delta \theta$$
     Với $r_{\text{offset}} \approx 13\,\text{mm}$ và $\Delta \theta \approx 1.3\,\text{rad}$ ($75^\circ$), mu ngón dài thêm khoảng $5 - 7\,\text{mm}$ tại mỗi khớp!
   - Nếu dùng chốt bản lề cố định khoảng cách (Fixed-length pivot), khung sẽ **ghì cứng, kéo giật ngón tay ra sau hoặc ép khớp sinh học gập theo trục nhân tạo**, gây đau, cấn khớp và làm cho bệnh nhân có ngón tay dài không thể co ngón thoải mái.

2. **Biến Thiên Chiều Dài Ngón Tay Giữa Các Bệnh Nhân:**
   - Chiều dài đốt ngón tay người lớn dao động rất lớn (từ phân vị 5% nữ đến 95% nam): Đốt 1 từ $35 - 48\,\text{mm}$, Đốt 2 từ $22 - 32\,\text{mm}$.
   - Thiết kế nguyên khối cố định không thể vừa vặn cho nhiều người bệnh nếu thiếu cơ cấu bù trừ kích thước.

3. **Yêu Cầu Tải Kéo Trước (Preload) Cho Cảm Biến Áp Trở Velostat:**
   - Theo nguyên tắc đo lường vi sai (`docs/04` §3.2, `docs/02` §5.5), mảng áp trở Velostat phải có một áp lực kéo trước ban đầu $p_0 = F_p / A_c$ xác định và ổn định thì mới có thể đo được cả hai chiều gập/duỗi quanh điểm làm việc. Thiết kế dạng ống kín thông thường rất khó kiểm soát lực ép này khi đeo vào tay bệnh nhân bị co cứng.

---

## 2. Giải Pháp Kỹ Thuật Được Triển Khai (Design Implementations)

### 2.1. Khớp Rãnh Trượt Tự Lựa (Floating Slotted Joint)
- **Cấu trúc:** Tại chạc đôi phía trước của Đốt 1 và Đốt 2, thay vì khoan lỗ tròn cố định, một **rãnh trượt thuôn dài (Oval Slotted Hole)** được bố trí dọc theo phương trục Z của ngón tay.
  - **Khớp PIP (Đốt 1 $\rightarrow$ Đốt 2):** Rãnh trượt dài **$7.5\,\text{mm}$** (bắt đầu từ $Z = 18.5$ đến $Z = 26.0\,\text{mm}$).
  - **Khớp DIP (Đốt 2 $\rightarrow$ Đốt 3):** Rãnh trượt dài **$6.0\,\text{mm}$** (bắt đầu từ $Z = 16.0$ đến $Z = 22.0\,\text{mm}$).
  - **Tổng hành trình bù trượt:** **$13.5\,\text{mm}$**.
- **Nguyên lý hoạt động:**
  - Khớp liên kết có **2 bậc tự do (2-DOF: 1 quay quanh trục X + 1 trượt tịnh tiến dọc trục Z)**.
  - Khi duỗi thẳng $0^\circ$: Chốt tịnh tiến về đầu rãnh và tiếp xúc với gờ cữ chặn chống lật ngửa (Hyperextension stop ledge).
  - Khi co gập ngón: Chốt trục tự do trượt tiến dọc theo rãnh theo đúng biến thiên chiều dài tự nhiên của ngón tay bệnh nhân, triệt tiêu $100\%$ lực kéo dọc trục có hại lên khớp.

### 2.2. Vỏ Đốt Rút Gọn & Khoảng Đệm Thoát Khớp (Joint Relief Spacing)
- Chiều dài vỏ đốt được tính toán chỉ ôm phần thân xương (Diaphysis), không lấn vào vùng nếp gấp da khớp:
  - **Đốt 1 (Proximal):** Đường kính trong $\varnothing 23.6\,\text{mm}$, chiều dài $16.0\,\text{mm}$.
  - **Đốt 2 (Middle):** Đường kính trong $\varnothing 21.6\,\text{mm}$, chiều dài $13.5\,\text{mm}$.
  - **Đốt 3 (Distal):** Đường kính trong $\varnothing 19.6\,\text{mm}$, chiều dài $11.5\,\text{mm}$.
- Khoảng cách đệm tự do giữa các vỏ dao động linh hoạt từ **$6.0\,\text{mm}$ đến $14.0\,\text{mm}$**, tạo không gian rộng rãi cho các gồ xương mu ngón (knuckles) khi co góc nhọn.

### 2.3. Đốt Ngoài Cùng Hở Đầu Ngón (Open-Tip Architecture)
- Loại bỏ hoàn toàn phần mũ vòm bịt đầu ngón tay ở Đốt 3.
- Máng ngón thông suốt 2 đầu giúp:
  - Móng tay thò ra tự do, không bị chèn ép gây đau.
  - Thích ứng với mọi chiều dài đầu ngón tay của người bệnh.
  - Giữ lại diện tích tiếp xúc xúc giác (tactile sensation) ở đầu vân tay khi tập luyện cầm nắm vật thể.
- Khối neo cáp gân được bố trí trên mu ngón với lỗ luồn cáp $\varnothing 2.0\,\text{mm}$ và hốc chặn cos/nút thắt cáp $\varnothing 3.4\,\text{mm}$ dạng bậc (stepped counterbore).

### 2.4. Bản Lề Bụng Ngón In Nguyên Khối Print-in-Place & Khóa Mỏ Quạ 5 Nấc Răng
- **Bản lề bụng ngón:** Dọc theo trục Z ở sườn trái, in nguyên khối ở tư thế mở $-100^\circ$. Khe hở hướng kính $0.35\,\text{mm}$, khe hở hướng trục $0.4\,\text{mm}$, vát mép chân $45^\circ$ chống chân voi.
- **Khóa mỏ quạ đa nấc (Multi-Step Ratchet Snap-Claw — 5 nấc to/nhỏ):** 
  - Sườn phải (+X) bố trí dải răng cưa Ratchet gồm **5 nấc liên tiếp** với bước răng $1.15\,\text{mm}$.
  - Góc nghiêng $45^\circ$ giúp ngàm trượt vào tanh tách khi bóp ngón tay, mặt sau phẳng $90^\circ$ khóa cứng chống tuột.
  - Cho phép điều chỉnh chu vi ngón tay tương đương đường kính từ **$\varnothing 18.0\,\text{mm}$ (nấc 5 - ngón thon nhỏ) đến $\varnothing 24.5\,\text{mm}$ (nấc 1 - ngón to mập)**.
  - Tích hợp **lẫy tỳ ngón cái (Thumb Release Tab)** vươn $3.8\,\text{mm}$ cho phép người dùng mở khóa chỉ bằng một tay.
- **Khoang âm cảm biến Velostat:** Kích thước $9.5 \times 6.8 \times 1.2\,\text{mm}$ nằm ở chính giữa mặt lòng của thanh gài. Khi bấm nấc sâu hơn, thanh gài ép tăng lực kéo trước (preload) xác định lên cảm biến Velostat, đảm bảo tín hiệu đo lực tiếp xúc luôn căng và tuyến tính cho mọi kích cỡ ngón tay.

### 2.5. Khớp Bấm Ngàm Bên Hông (Lateral Snap-Pivot — Không Cần Chốt Rời)
- **Đặt vấn đề:** Việc sử dụng các chốt trục rời $\varnothing 2.4\,\text{mm}$ in FDM gây ra tỷ lệ gãy cao do thớ in (layer delamination), ngạnh chốt khó nhét qua nhiều lỗ hẹp và cản trở không gian mu ngón.
- **Giải pháp Khớp Bấm Ngàm Bên Hông:**
  - **Chuyển trục xoay sang 2 bên sườn ngón tay:** Đúng với tâm xoay giải phẫu tự nhiên của khớp ngón tay người.
  - **Phía trước (Đốt 1 và Đốt 2):** 2 tay đòn bên hông vươn ra, trên mỗi tay đòn tích hợp **3 hốc lỗ tròn $\varnothing 3.2\,\text{mm}$** (khoảng cách bước $2.5\,\text{mm}$) kèm rãnh vát góc $45^\circ$ ở mặt trong làm nêm dẫn hướng.
  - **Phía sau (Đốt 2 và Đốt 3):** 2 chốt tròn lồi $\varnothing 3.0\,\text{mm}$, cao $1.8\,\text{mm}$ được **in liền khối** với vỏ sườn và vát mép đầu chốt.
  - **Thao tác lắp ráp:** Người dùng chỉ cần bóp nhẹ hai sườn và ấn chốt vào lỗ: **"CẠCH" một tiếng trong 2 giây** là ăn khớp hoàn toàn, không cần bất kỳ chốt rời, ốc vít hay dụng cụ nào.
  - **3 Nấc lựa chọn chiều dài:**
    - **Nấc 1 (Short):** Dành cho ngón tay ngắn (đệm hở $6.5\,\text{mm}$).
    - **Nấc 2 (Medium - Danh định):** Dành cho tay người lớn tiêu chuẩn (đệm hở $8.5\,\text{mm}$).
    - **Nấc 3 (Long):** Dành cho ngón tay dài (đệm hở $11.0\,\text{mm}$).
  - **Tối ưu hóa tuyệt đối cho Velostat:**
    - Toàn bộ bề mặt mu ngón (+Y) và bụng ngón (-Y) được giải phóng $100\%$ không gian phẳng sạch sẽ.
    - Dây điện tín hiệu từ màng Velostat chạy thẳng xuyên suốt dọc theo mu ngón về cổ tay mà không bị bất kỳ chạc đôi hay thanh bản lề nào đè cấn.
    - Lực uốn của ngón tay tác dụng vuông góc trọn vẹn lên màng Velostat trên vách khung mà không bị kẹt hay tiêu hao qua bản lề.

---

## 3. Bản Đồ File & Cấu Trúc Mã Nguồn

Toàn bộ mô hình được tạo tự động bằng mã Python FreeCAD có khả năng tham số hóa toàn diện:

- **Mã nguồn sinh mô hình:** [`3d_model/generate_full_finger_modular.py`](../3d_model/generate_full_finger_modular.py)
- **Mã nguồn kết xuất đồ họa:** [`3d_model/render_full_finger.py`](../3d_model/render_full_finger.py)
- **Thư mục sản phẩm 3D:** [`3d_model/custom_exo/full_finger_modular/`](../3d_model/custom_exo/full_finger_modular/)
  - `phalanx1_proximal_open.stl` & `.step`
  - `phalanx2_middle_open.stl` & `.step`
  - `phalanx3_distal_open.stl` & `.step`
  - `intersegment_hinge_pin_2_5mm.stl` & `.step`
  - `full_finger_assembly_straight.stl` & `.step`
  - `full_finger_assembly_flexed.stl` & `.step`
  - `full_finger_modular.FCStd`
  - `full_finger_preview.png`
