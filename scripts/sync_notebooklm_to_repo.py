# -*- coding: utf-8 -*-
import os
import shutil
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = r"D:\Desktop\AI Agent\smart-glove-hand-function-monitoring"
TARGET_DIR = os.path.join(REPO_DIR, "research", "notebooklm_sync")
DOWNLOAD_DIR = r"C:\Users\user\Downloads\gemini-notebook\smart_glove_artifacts\Stroke Rehabilitation and Robotic Glove"

os.makedirs(os.path.join(TARGET_DIR, "experiments"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "studio"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "chat_transcripts"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "audio"), exist_ok=True)

# 1. Ghi 5 tài liệu thực nghiệm kỹ thuật
experiments = [
    (
        "01_tong_ket_ky_thuat_chuoi_phan_cung_da_kenh.md",
        """# Tổng kết kỹ thuật toàn diện: Kiểm thử và xác thực chuỗi phần cứng đa kênh
(ESP32-S3 + ADS1115 + INA333 + CD74HC4067)

## 1. Mục tiêu thử nghiệm
Xác thực toàn bộ chuỗi phần cứng thu thập và tiền xử lý tín hiệu cho mảng cảm biến áp lực bàn tay trong dự án găng tay robot phục hồi chức năng:
`Tín hiệu đầu vào -> MUX 16 kênh CD74HC4067 -> Tầng khuếch đại đo lường INA333 (CJMCU-333) -> Bộ biến đổi tương tự - số ADC 16-bit ADS1115 -> Vi điều khiển ESP32-S3 (qua I2C & Serial Plotter)`.

## 2. Các mốc giải quyết bài toán phần cứng (Milestones)

### 2.1. Cân chỉnh tầng tiền khuếch đại INA333
* **Hiện tượng lỗi ban đầu:** Sóng ngõ ra bị suy hao biên độ ($V_{pp}$ vào 0.25V, ra 0.16V), méo nấc bậc thang, bẹp đáy (xén âm xuống -0.85V) do INA333 chạy nguồn đơn 3.3V bị vi phạm dải điện áp chế độ chung ($V_{CM}$) và thiếu mốc tham chiếu tĩnh $V_{REF}$.
* **Xử lý:**
  - Thêm tụ chặn AC 0.47 µF ngăn dòng DC rò từ nguồn phát xung.
  - Thiết lập điểm tĩnh DC $V_{REF} \\approx 1.500\\text{ mV} - 1.650\\text{ mV}$ (Virtual Ground) tại ngõ vào vi sai.
  - Cân chỉnh biến trở SMD $R_G$ (loại 1 vòng xoay 270°): Đạt hệ số khuếch đại $G \\approx 6.5$ lần ($V_{pp}$ đạt 1.55V, $V_{max} = 1.62\\text{V}$, $V_{min} = 0.06\\text{V}$ cách sàn GND an toàn, sóng sin tròn đều).
  - Khi tắt nguồn phát AC, $V_{OUT}$ giữ cố định tại $\\approx 1.500\\text{ mV}$ (chuẩn xác theo mốc tĩnh thiết kế).

### 2.2. Tích hợp và cấu hình ADC 16-bit ADS1115
* **Lựa chọn cấu hình:** Sử dụng kênh đơn $A_0$ đọc trực tiếp $V_{OUT}$ từ INA333; chân $A_1$ để trống để tránh sụt áp mốc $V_{REF}$ tĩnh trên bo mạch.
* **Tối ưu chế độ đọc:** Khảo sát chế độ Continuous Conversion kết hợp ngắt phần cứng ALRT (Conversion Ready) trên GPIO 10 ESP32-S3 và cơ chế đọc tuần tự đa kênh qua I2C 400kHz.

### 2.3. Mở rộng đa kênh với CD74HC4067
* **Kết nối điều khiển:** 4 chân GPIO (GPIO 4, 5, 6, 7) điều khiển chọn kênh $S_0 - S_3$, chân EN nối GND kích hoạt liên tục.
* **Tối ưu tốc độ & Settling Time:** Chèn khoảng trễ xác lập điện áp `delayMicroseconds(120)` sau mỗi lần chuyển kênh để xả sạch điện dung ký sinh trên chân SIG, ngăn ngừa hiện tượng nhớ áp giữa các kênh.
* **Kết quả đo kiểm trên Serial Plotter:**
  - Kênh 0 (GND): Ghim phẳng tuyệt đối tại $\\approx 0 - 20\\text{ mV}$.
  - Kênh 1: Duy trì áp tĩnh cao ổn định tại $\\approx 3.046\\text{ mV} - 3.100\\text{ mV}$.
  - Kênh 2: Bắt trọn dao động tuần hoàn từ 150 mV lên đỉnh 1.650 mV; khi ngắt nguồn phát, kênh lùi về mốc tĩnh đáy $\\approx 150\\text{ mV}$ dứt khoát.
  - Khả năng cách ly: Không xảy ra hiện tượng rò kênh hay nhiễu xuyên kênh (Crosstalk) giữa các kênh có độ lệch áp lớn (0V, 1.65V, 3.0V).

## 3. Bản chất hiện tượng "Sóng tam giác" trên Serial Plotter
* **Nguyên nhân:** Do phần mềm hiển thị nối các điểm rời rạc bằng đoạn thẳng (Linear Interpolation). Vì ADC phải chia thời gian quét tuần tự qua 4 kênh, số lượng mẫu thu thập trên mỗi chu kỳ sin của máy phát xung chỉ đạt từ 4 đến 6 điểm.
* **Đánh giá mức độ ảnh hưởng:** Hoàn toàn KHÔNG ảnh hưởng đến hệ thống thực tế. Cảm biến màng Velostat là tín hiệu điện trở DC biến thiên chậm theo lực tì/ép của ngón tay người ($0\\text{ Hz} - 3\\text{ Hz}$), thời gian thao tác kéo dài hàng trăm mili-giây nên mật độ lấy mẫu trên mỗi thao tác là rất dày đặc (hàng chục đến hàng trăm mẫu), cho ra đường đáp ứng lực trơn mượt tự nhiên.

## 4. Trạng thái hệ thống và Kế hoạch bước tiếp theo
* **Trạng thái:** Toàn bộ chuỗi phần cứng và firmware cơ sở đã hoàn thành kiểm chứng, độ tuyến tính và dải động đạt yêu cầu ($0\\text{ mV} - 3250\\text{ mV}$).
* **Bước kế tiếp:**
  - Tháo nguồn phát xung và tụ lọc AC 0.47 µF ra khỏi bo mạch.
  - Đấu nối các điểm cảm biến màng Velostat (theo cấu hình cầu phân áp) vào các cổng ngõ vào $C_0 - C_{15}$ của CD74HC4067.
  - Kích hoạt lại thuật toán Auto-Tare để tự động đưa mốc lực ban đầu của từng ngón tay về chuẩn $0.0\\text{ mV}$.
"""
    ),
    (
        "02_ket_qua_thuc_nghiem_quet_da_kenh_cd74hc4067_ina333_ads1115.md",
        """# Báo cáo thực nghiệm: Quét đa kênh CD74HC4067 kết hợp INA333 và ADS1115

## 1. Kết quả kiểm tra trên Serial Plotter
* **Hệ thống phần cứng:** ESP32-S3 điều khiển chuyển kênh CD74HC4067 ($S_0 - S_3$), tín hiệu sau dồn kênh đưa vào tầng khuếch đại vi sai INA333, chuyển đổi ADC 16-bit qua ADS1115 (giao tiếp I2C 400kHz, kênh đơn A0).
* **Hiện trạng các kênh:**
  - Kênh 0 (Xanh dương): Nối cố định GND -> Điện áp hiển thị phẳng tuyệt đối tại $0\\text{ mV}$. Hoàn toàn không bị dính nhiễu từ các kênh lân cận.
  - Kênh 2 (Xanh lá): Dao động tuần hoàn từ $\\approx 600\\text{ mV}$ lên kịch trần nguồn $3250\\text{ mV}$ ($3.25\\text{V}$, tương đương thanh nguồn Rail-to-Rail của INA333 và ADS1115 ở mức nguồn 3.3V).
  - Kênh 1 (Cam): Dao động tuần hoàn từ $0\\text{ mV}$ lên đỉnh $\\approx 1700\\text{ mV}$ ($1.7\\text{V}$).
  - Đồ thị xuất hiện dạng zíc-zắc gãy khúc do tốc độ lấy mẫu trên mỗi kênh bị chia 4 (quét tuần tự qua 4 kênh kèm thời gian trễ delay).

## 2. Kết luận kỹ thuật
* Bộ dồn kênh tương tự CD74HC4067 hoạt động chính xác: chuyển mạch đúng địa chỉ, cách ly kênh tốt, không xảy ra hiện tượng rò kênh sang Kênh 0.
* Chuỗi tín hiệu Analog -> Multiplexer -> Instrumentation Amplifier -> ADC 16-bit I2C -> ESP32-S3 đã thông suốt hoàn toàn về mặt phần cứng và firmware.
"""
    ),
    (
        "03_danh_gia_dang_song_quet_da_kenh_sau_toi_uu_toc_do.md",
        """# Báo cáo thực nghiệm: Đánh giá dạng sóng quét đa kênh sau tối ưu tốc độ

## 1. Phân tích kết quả đo trên Serial Plotter
* **Tốc độ Baudrate:** 115200 baud.
* **Kênh 0 (Trắng xám):** Duy trì sát mức $0\\text{ mV}$ (dao động nhỏ $\\approx 0 - 20\\text{ mV}$). Không bị nhiễu chéo từ các kênh điện áp cao.
* **Kênh 1 (Xanh lam):** Ổn định ở mức cao $\\approx 3.046\\text{ mV} - 3.100\\text{ mV}$, biến thiên nhẹ mượt mà.
* **Kênh 2 (Vàng):** Dao động tuần hoàn dạng tam giác từ $\\approx 150\\text{ mV}$ lên đỉnh $\\approx 1.650\\text{ mV}$. Đến mẫu thứ 55364, kênh 2 chuyển trạng thái tụt về mức nền $\\approx 150\\text{ mV}$ (khi ngừng kích xung hoặc tín hiệu dừng).

## 2. Kết luận
* CD74HC4067 chuyển mạch hoàn toàn ổn định và tin cậy giữa các kênh có độ lệch điện áp lớn (0V, 1.65V, 3.0V).
* Kênh 1 giữ điện áp cao ổn định mà không kéo theo Kênh 0 hay làm sụt Kênh 2.
* Hệ thống sẵn sàng cho bước tích hợp ma trận cảm biến Velostat.
"""
    ),
    (
        "04_ky_thuat_ghep_noi_ina333_ads1115_esp32s3_cho_velostat.md",
        """# Báo cáo kỹ thuật: Tầng tiền khuếch đại INA333, ADC ADS1115 và ESP32-S3 cho cảm biến Velostat

## 1. Thiết kế tầng tiền khuếch đại INA333 (Module CJMCU-333)
* **Hệ số khuếch đại (Gain):** Được xác định theo công thức $G = 1 + \\frac{100\\text{ k}\\Omega}{R_G}$. Biến trở SMD trên bo dùng để vi chỉnh $R_G$.
* **Xử lý điện áp phân cực chế độ chung ($V_{CM}$) và mốc DC ($V_{REF}$):**
  - Mạch hoạt động ở nguồn đơn (3.3V và GND). INA333 không thể xử lý hoặc xuất tín hiệu âm dưới 0V.
  - Chân VREF được duy trì ở mức $\\approx 1.65\\text{V}$ (half-supply) để thiết lập điểm tĩnh DC (baseline offset).
  - Tín hiệu ngõ ra chuẩn theo công thức: $V_{OUT} = G \\cdot (V_{IN+} - V_{IN-}) + V_{REF}$.
  - Khi chưa có lực ép tác động, $V_{OUT}$ giữ cố định ở $\\approx 1.500\\text{ mV} - 1.650\\text{ mV}$. Khi chịu lực ép, trở kháng Velostat giảm, kéo điện áp vi sai thay đổi và nâng $V_{OUT}$ một cách tuyến tính trong dải $0.1\\text{V} - 3.2\\text{V}$.

## 2. Ghép nối với bộ chuyển đổi tương tự - số (ADC) 16-bit ADS1115
* **Chế độ đọc:** Cấu hình kênh đơn A0 đọc ngõ ra $V_{OUT}$ từ INA333.
* **Tốc độ lấy mẫu & Chế độ hoạt động:** Cấu hình Continuous Conversion Mode đạt tốc độ tối đa $860\\text{ SPS}$ ($860\\text{ Hz}$).
* **Đồng bộ hóa ngắt phần cứng (Hardware Interrupt via ALRT Pin):**
  - Chân ALRT của ADS1115 kết nối với chân GPIO ngắt (GPIO 10) của ESP32-S3.
  - Sử dụng hàm `ads.startComparator_SingleEnded(0, 0)` trong thư viện Adafruit_ADS1X15 để kích hoạt chế độ Conversion Ready.
  - Mỗi khi hoàn tất chuyển đổi, ADS1115 phát xung hạ mức LOW kích hoạt ngắt phần cứng (Falling Edge ISR) trên ESP32-S3.
  - Triệt tiêu hoàn toàn hiện tượng jitter, trễ giao tiếp I2C và đảm bảo không bị rơi rụng mẫu (Zero stale/dropped samples).

## 3. Sơ đồ đấu nối phần cứng ESP32-S3 - INA333 - ADS1115
* **Nguồn:** Cấp 3.3V từ chân 3V3 của ESP32-S3 đồng thời vào chân 3.3V của INA333 và VDD của ADS1115 (chung GND toàn hệ thống).
* **I2C:** SDA -> GPIO 8, SCL -> GPIO 9, ADDR -> GND (địa chỉ 0x48).
* **Ngắt:** ALRT (ADS1115) -> GPIO 10 (ESP32-S3).
* **Tín hiệu:** VOUT (INA333) -> A0 (ADS1115).

## 4. Thuật toán phần mềm trên ESP32-S3: Tự động cân mốc 0 (Auto-Tare)
Để loại bỏ mức điện áp tĩnh DC ($V_{REF} \\approx 1.5\\text{V}$) khi chưa có lực tác động, hệ thống thực hiện Auto-Tare khi khởi động:
1. Cho mạch analog ổn định 500 ms.
2. Thu thập chính xác 100 mẫu liên tiếp qua ngắt phần cứng ALRT để tính trung bình cộng baseline:
   $$\\text{Baseline} = \\frac{1}{100} \\sum_{i=1}^{100} V_i$$
3. Giá trị lực hiển thị tức thời:
   $$V_{\\text{lực}} = V_{\\text{đo}} - \\text{Baseline}$$
Tín hiệu sau Tare bắt đầu từ đúng $0.0\\text{ mV}$, giúp tối ưu hóa dải đo và hỗ trợ các thuật toán nhận diện mẫu lực ép tay phục hồi chức năng sau đó.
"""
    ),
    (
        "05_nhat_ky_thuc_nghiem_do_kiem_ina333_ads1115_cd74hc4067.md",
        """# Nhật ký thực nghiệm: Đo kiểm INA333, Cấu hình ADS1115 và Thiết kế chuỗi đa kênh CD74HC4067

## 1. Kết quả đo kiểm và giải quyết bài toán tiền khuếch đại INA333 (CJMCU-333)
* **Thiết bị đo kiểm:** Máy hiện sóng cầm tay tích hợp FNIRSI 2C23T.
* **Hiện tượng lỗi ban đầu:**
  - Tín hiệu ngõ ra bị suy hao ($V_{pp}$ vào $0.25\\text{V} \\to$ ngõ ra chỉ đạt $0.16\\text{V}$, tương đương $G \\approx 0.64$).
  - Dạng sóng ngõ ra bị méo nấc bậc thang, bẹp đáy (clipping âm xuống $-0.85\\text{V}$).
  - Hiện tượng sập nguồn tức thời khi kẹp mass oscillo: do vỏ mass cổng BNC của FNIRSI thông ngầm, gây đoản mạch vòng mass (Ground Loop) khi kẹp vào điểm lệch thế.
* **Bản chất kỹ thuật & Giải pháp:**
  - INA333 chạy nguồn đơn 3.3V và GND (0V), không thể xử lý điện áp âm. Tín hiệu AC từ máy phát xung tụt dưới 0V kích hoạt diode bảo vệ ESD nội, làm tắc nghẽn tầng vi sai.
  - Bổ sung tụ chặn AC 0.47 µF để ngăn dòng một chiều từ nguồn phát.
  - Ghim điện áp phân cực DC tĩnh $V_{REF} \\approx 1.5\\text{V} - 1.65\\text{V}$ (Virtual Ground) vào ngõ vào vi sai.
  - Tinh chỉnh biến trở SMD $R_G$ (loại 1 vòng xoay 270°): Hệ số khuếch đại đạt $G \\approx 6.5$ lần ($V_{pp}$ từ 0.24V khuếch đại lên 1.55V), sóng sin trơn mượt, đáy sóng cách GND 60 mV, không còn hiện tượng xén ngọn.
  - Khi tắt máy phát xung AC, $V_{OUT}$ giữ cố định ở $\\approx 1.500\\text{ mV}$ (chuẩn xác theo mốc $V_{REF}$ tĩnh thiết kế).

## 2. Tối ưu hóa chuỗi chuyển đổi ADC 16-bit ADS1115 với ESP32-S3
* **Lý do phần cứng:** Thay thế ADC nội bộ của ESP32-S3 (vốn bị lỗi phi tuyến nặng ở 2 biên và nhiễu sóng RF) bằng ADS1115 qua I2C.
* **Cấu hình Continuous Conversion Mode & Ngắt phần cứng ALRT:**
  - Tốc độ lấy mẫu: Đặt tối đa 860 SPS (Samples Per Second).
  - Sử dụng chân ngắt phần cứng ALRT của ADS1115 nối vào GPIO 10 (ESP32-S3).
  - Kích hoạt chế độ Conversion Ready bằng hàm `ads.startComparator_SingleEnded(0, 0)` trong thư viện Adafruit_ADS1X15 mới.
  - Phục vụ ngắt sườn xuống (FALLING) lưu trong RAM (IRAM_ATTR): ESP32-S3 chỉ đọc dữ liệu khi phần cứng ADS1115 hoàn tất chuyển đổi (< 0.1 ms).
  - Loại bỏ hoàn toàn trễ giao tiếp I2C, triệt tiêu hiện tượng jitter thời gian thực và tránh đọc trùng/rớt mẫu (Zero Stale Data).

## 3. Kiến trúc chuỗi tín hiệu và Kế hoạch kế tiếp
* Khảo sát phương án: Quét 16 kênh cảm biến -> CD74HC4067 (chọn 1 kênh) -> 1 tầng INA333 -> ADS1115 (A0) -> ESP32-S3. Nội trở dẫn tiếp điểm $R_{ON} \\approx 70\\,\\Omega$ của 4067 không ảnh hưởng đến INA333 do trở kháng ngõ vào của INA333 lên tới $100\\text{ G}\\Omega$.
* Kiểm soát Settling Time và Crosstalk giữa các đường tín hiệu.
"""
    )
]

for filename, content in experiments:
    path = os.path.join(TARGET_DIR, "experiments", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Written experiment log:", filename)

# 2. Copy các studio artifacts tải về
for fname in os.listdir(DOWNLOAD_DIR):
    src_file = os.path.join(DOWNLOAD_DIR, fname)
    if fname.endswith(".m4a"):
        dst_file = os.path.join(TARGET_DIR, "audio", fname)
        shutil.copy2(src_file, dst_file)
        print("Copied audio:", fname)
    else:
        dst_file = os.path.join(TARGET_DIR, "studio", fname)
        shutil.copy2(src_file, dst_file)
        print("Copied studio artifact:", fname)

# 3. Tạo README.md tổng hợp cho notebooklm_sync
readme_content = """# NotebookLM Research & Technical Knowledge Base Sync

Thư mục này đồng bộ toàn bộ tài liệu nghiên cứu, nhật ký thực nghiệm phần cứng, sản phẩm Studio và biên bản thảo luận học thuật từ Google NotebookLM:
- **Notebook:** `Stroke Rehabilitation and Robotic Glove`
- **ID:** `b7170836-6696-4e0f-8985-dafd233d135f`
- **Tổng số nguồn tài liệu:** 43 nguồn (Y học phục hồi chức năng, cảm biến áp điện trở Velostat, cơ cấu AAN, vi sai 2 vách, ART-Glove 2026, chuẩn đo lường lâm sàng).

## Cấu trúc thư mục

```
research/notebooklm_sync/
├── experiments/             # 5 tài liệu nhật ký & báo cáo thực nghiệm đo kiểm phần cứng
│   ├── 01_tong_ket_ky_thuat_chuoi_phan_cung_da_kenh.md
│   ├── 02_ket_qua_thuc_nghiem_quet_da_kenh_cd74hc4067_ina333_ads1115.md
│   ├── 03_danh_gia_dang_song_quet_da_kenh_sau_toi_uu_toc_do.md
│   ├── 04_ky_thuat_ghep_noi_ina333_ads1115_esp32s3_cho_velostat.md
│   └── 05_nhat_ky_thuc_nghiem_do_kiem_ina333_ads1115_cd74hc4067.md
├── studio/                  # Báo cáo tổng hợp, Sơ đồ tư duy, Bảng thuật ngữ, Trắc nghiệm
│   ├── Stroke Rehabilitation and Robotic Glove.md
│   ├── Bảng Tổng Hợp Thuật Ngữ và Thông Số Dự Án Găng Tay Thông Minh.csv
│   ├── Sơ đồ tư duy Dự án Găng tay Thông minh Phục hồi Chức năng.json
│   ├── Tai biến Sơ đồ tư duy.json
│   └── Găng tay Trắc nghiệm.json
├── chat_transcripts/        # Toàn văn đối thoại phản biện học thuật & thiết kế mạch
│   └── 2026-10_chat_transcript_stroke_rehab_notebooklm.md
└── audio/                   # Audio Overviews tóm tắt dự án (.m4a - gitignored)
```

## Các điểm nhấn kỹ thuật quan trọng đã xác thực:
1. **INA333:** Thiết lập mốc tĩnh $V_{REF} \\approx 1.65\\text{V}$ (Virtual Ground), $G \\approx 6.5$ lần, dải động an toàn $0.06\\text{V} - 1.62\\text{V}$.
2. **ADS1115 + ESP32-S3:** Ngắt phần cứng chân `ALRT` nối GPIO 10 (`Falling Edge ISR`), Continuous Mode 860 SPS triệt tiêu jitter và rớt mẫu.
3. **CD74HC4067:** Chèn thời gian trễ xác lập `delayMicroseconds(120)` sau mỗi lần chuyển kênh triệt tiêu nhớ áp ký sinh trên chân SIG.
4. **Auto-Tare:** Lấy trung bình 100 mẫu baseline sau 500 ms đầu khởi động để tự động cân bằng mốc 0 về $0.0\\text{ mV}$.
"""

with open(os.path.join(TARGET_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content.strip() + "\n")
print("Written README.md for notebooklm_sync")
