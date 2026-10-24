# Vai trò mở rộng cho Camera + Orange Pi 5 Pro — 2026-10-21

**Trạng thái: ĐỀ XUẤT, chưa chọn và chưa đo thử.** Chủ dự án muốn nhánh camera có ảnh hưởng lớn hơn, nêu Depth Anything như một ví dụ. Đây là trao đổi phương án, không phải chỉ đạo sửa nguồn Drive hay bắt đầu code. Nguồn đề cương vẫn là bản chủ dự án sửa `1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3` (`DEC-PROP-019`).

## 1. Đề xuất trọng tâm

Giao Orange Pi nhiệm vụ **đánh giá chất lượng cầm–giữ–thả vật và điều phối bài tập theo kết quả**, thay vì chỉ phát nhãn thìa/vùng đích. Phân biệt vai trò:

- Flex: ngón thay đổi độ gập thế nào.
- Velostat: đáp ứng áp lực/tiếp xúc tương đối thay đổi thế nào.
- Camera: vật thực sự rời bàn, được giữ ổn định, đi vào vùng đích và được thả ra hay chưa.
- Orange Pi: đối chiếu các nguồn theo thời gian, phản hồi đúng lỗi quan sát được và đề xuất mức khó của lượt tiếp theo trong phạm vi đặt trước.

Đây là cách bổ sung đầu ra cho câu hỏi “đáp ứng cảm biến có tương ứng với thao tác hữu ích trên vật thật không?”. Không gọi quỹ đạo thìa là thang đo hồi phục ngón: chuyển động đưa thìa còn do cổ tay/cánh tay/thân người. Ưu tiên đại lượng gần chức năng ngón — giữ vật, trượt tương đối với bàn tay/nẹp, đóng/mở đúng pha — trước các điểm số đường đi tổng hợp.

### Các đầu ra ứng viên

| Đầu ra | Cách dùng dự kiến | Điều kiện cần |
|---|---|---|
| Nâng khỏi mặt bàn hay chỉ kéo trượt trên bàn | tránh tính một lượt kéo lê thành lượt gắp thành công | theo dõi thìa; quan hệ hình học với mặt bàn; nhãn đối chiếu |
| Độ cao nâng, vị trí đặt, diễn biến quỹ đạo | phản hồi nâng/đặt và mô tả chất lượng thao tác | hệ tọa độ đã hiệu chuẩn; số đo kiểm chứng bằng vật chuẩn độc lập |
| Vật dịch chuyển tương đối với bàn tay/nẹp | nhận ra lượt giữ không ổn định, thử phát hiện tuột vật | theo dõi được cả vật và tham chiếu trên tay/nẹp; xử lý che khuất |
| Vật ở vùng đích và tay đã nhả | tách “đến đích” khỏi “hoàn thành đặt–nhả” | phối hợp hình ảnh với Flex/Velostat; kiểm thử các trường hợp gây nhầm |
| Kết quả theo từng pha | chọn bài tiếp theo, không thưởng/giảm trợ lực chỉ vì vật đã đến đích | kết hợp mức trợ lực, cửa sổ thăm dò và cảm biến, không suy tính chủ động từ hình ảnh đơn thuần |

Không suy ra nguyên nhân sinh lý từ một lỗi: “vật chưa rời bàn” không chứng minh người tập yếu lực; có thể là tiếp xúc, tư thế, cơ cấu hay nhận biết ảnh. Camera không xác nhận lực Newton hoặc tự phát lệnh tăng lực kéo.

## 2. Depth Anything nằm ở đâu

Chuỗi ứng viên: **ảnh RGB → nhận biết/bám thìa và tham chiếu → ước lượng độ sâu → quy đổi vào hệ bàn thử → đại lượng thao tác → đối chiếu cảm biến**. Mô hình độ sâu không thay việc nhận biết thìa hoặc bám vật.

Tài liệu chính thức phân biệt rõ các bản V2 dự đoán độ sâu tương đối với các bản tinh chỉnh metric. V2-Small có 24,8 triệu tham số; nhánh metric có bản trong nhà huấn luyện trên Hypersim và trả bản đồ theo mét. Đây là đặc tả mô hình, không phải độ chính xác đã đạt trên găng. [1](https://github.com/DepthAnything/Depth-Anything-V2) [5](https://github.com/depthanything/depth-anything-v2/blob/main/metric_depth/README.md)

**Ứng viên thử đầu:** V2-Small, ưu tiên kiểm tra biến thể metric trong nhà nếu cần báo độ cao/khoảng cách. Không dùng tên “Depth Anything” chung chung mà không ghi loại trọng số. Có bản DA3 với các nhóm any-view, monocular và metric riêng, nhưng không chọn model chỉ theo số phiên bản. [1](https://github.com/bytedance-seed/depth-anything-3)

Các việc phải giải quyết trước khi báo cm/mm hoặc quỹ đạo 3D:

- Hiệu chuẩn nội tại camera và hệ tọa độ mặt bàn; kiểm tra sai số trên nhiều vị trí/độ cao chuẩn. Chênh lệch khoảng cách theo tia nhìn không tự bằng độ cao so với mặt bàn.
- Đầu ra relative không biến thành số đo metric chỉ nhờ đổi thang màu. Không chuẩn hóa min–max riêng từng khung rồi dùng giá trị đó như một chuỗi khoảng cách.
- Kiểm tra độ ổn định theo thời gian; không lấy nhấp nháy dự đoán làm chuyển động thật.
- Thìa mỏng/phản quang, tay che cán thìa, thay đổi nền/ánh sáng là các tình huống thử, không giả định đã giải quyết.
- Dữ liệu mất vật/không đủ quan sát phải để không xác định; không nội suy ra “gắp thành công”.

**Đối chứng kỹ thuật:** giữ phương án RGB 2D với camera đặt góc hợp lý; nếu cho phép, thử dấu chuẩn có kích thước biết trước trên vật/nẹp. Phép biến đổi mặt bàn chỉ áp dụng cho điểm trên mặt phẳng, không dùng để đo độ cao vật đang nâng. Hai camera đã hiệu chuẩn hoặc RGB-D là phương án phần cứng khác khi cần độ sâu đo được; phải duyệt thêm chi phí/cấu hình, không tự coi thiết bị đã có.

## 3. Hai hướng khác hoặc bổ sung

### Điều chỉnh độ khó theo chất lượng thao tác — ưu tiên sau phép đo

Dựa trên kết quả giữ/thả vật, sai lệch vị trí, số lượt thất bại và mức trợ lực, Orange Pi có thể chọn yêu cầu lượt kế tiếp: vùng đích dễ/khó hơn, yêu cầu giữ vật hoặc chuỗi thao tác phù hợp. Bắt đầu bằng quy tắc minh bạch, không cần RL. Việc này chỉ thay yêu cầu bài tập trong tập lựa chọn đặt trước; không có nghĩa phần mềm tự dời vật thật, tự kê đơn hay tự tăng lực kéo.

Mức trợ lực do tầng thấp thực hiện theo giới hạn và phương pháp thăm dò đã chọn. Một lượt thành công khi servo kéo vẫn là thành công có trợ giúp, không phải chứng cứ vận động tự nguyện. Các ngưỡng chọn mức khó, thời gian quan sát và tiêu chí chuyển đều còn mở.

### Theo dõi tư thế cổ tay/vai/thân — hướng mở rộng

Có thể nghiên cứu quan hệ giữa vị trí đặt vật và tư thế cổ tay, vai/thân để tránh đánh đồng mọi lượt hoàn thành với chất lượng vận động như nhau. Hướng này cần góc nhìn rộng và nhận biết tư thế; depth không phải điều kiện bắt buộc. Vì dễ mở đề tài từ bàn tay sang toàn chi trên, không chọn làm mục tiêu chính của vòng nguyên mẫu hiện tại. Không gọi một mẫu tư thế là bù trừ bệnh lý nếu chưa có định nghĩa và đối chiếu chuyên môn; mọi bước có người giữ nguyên yêu cầu phê duyệt.

## 4. Thực tế triển khai trên Orange Pi

Chưa có benchmark của dự án cho mô hình độ sâu, bộ nhận biết hoặc toàn chuỗi. Thông số GPU máy tính lớn và thông số TOPS không thay thế phép đo trên bo đang có.

Kho RKNN3 Model Zoo có ví dụ Depth Anything V3, nhưng bảng nền tảng ghi **RK3588 Series + coprocessor RK1820/RK1828**. Không suy ra ví dụ này chạy bằng NPU tích hợp của Orange Pi 5 Pro không gắn chip bổ sung. [3](https://github.com/airockchip/rknn3-model-zoo)

Đã thấy báo cáo cộng đồng về chuyển Depth Anything V1/V2 sang RKNN, bao gồm lỗi xuất/chênh kết quả trên bo; đây chỉ là chỉ dẫn để điều tra, không xác nhận khả năng hay bất khả năng chạy hiện nay. [1](https://github.com/airockchip/rknn-toolkit2/issues/322) [2](https://github.com/rockchip-linux/rknn-toolkit2/issues/296)

Kế hoạch hợp lý là kiểm tra ích lợi của độ sâu trên video/bàn thử trước, rồi đo khả năng xuất/chạy đúng mô hình, bộ nhớ và độ trễ toàn chuỗi trên Orange Pi. Không đặt lại chỉ tiêu NPU ≤20 ms; ≤20 ms trong đề cương hiện hành thuộc cảm biến → lệnh servo. Không hồi sinh nhánh RL bù trôi/trễ hay nhiệm vụ “Nghi vấn” đã loại (`DEC-EDGE-001`). Nếu sau này cần RKNN như công cụ triển khai thị giác thì đó là lựa chọn triển khai cần duyệt, không tự tạo lại một trụ cột nghiên cứu INT8.

## 5. Câu hỏi kiểm chứng và bước nhỏ nhất

**Câu hỏi:** bổ sung độ sâu và cảm biến ngón có giảm nhầm lẫn giữa nâng thực, kéo trượt, tuột vật và đặt–nhả so với chỉ ảnh RGB không?

Trước hết dùng bàn thử/giàn và mô hình tay giả với thìa thật, tạo các tình huống có đối chiếu độc lập. So sánh trên cùng dữ liệu:

1. RGB 2D;
2. RGB + độ sâu;
3. RGB + độ sâu + Flex/Velostat khi các kênh đã được hiệu chuẩn.

Đo sai số độ cao/vị trí so với thước hoặc cữ chuẩn, bảng nhầm lẫn sự kiện, tỷ lệ không xác định, độ trễ đầu–cuối và độ ổn định qua khung. Tách dữ liệu chọn tham số khỏi dữ liệu đánh giá; ghi lỗi do cảm biến, nhận biết hoặc thiếu quan sát. Chưa đặt ngưỡng số hoặc số lượt tùy ý. Phần điều chỉnh bài tập được đánh giá sau khi đầu ra đo đủ tin cậy; không lấy ảnh chạy thử đẹp làm bằng chứng.

**Khuyến nghị:** ưu tiên phép đo cầm–giữ–thả vật và phản hồi theo lỗi; nối thêm điều phối độ khó bằng quy tắc. Depth Anything là một ứng viên cung cấp hình học, không phải tên chức năng chính. Chưa sửa B.3.2.6/C.6/C.7 trên Drive, chưa chọn model/camera cuối, chưa code hoặc chạy thử.

## Nguồn đã đối chiếu

- `SRC-DEPTH-ANYTHING-V2-DOCS`: README chính thức, phần pretrained models/usage/video (đọc nội dung liên quan, không đọc toàn bài báo).
- `SRC-DEPTH-ANYTHING-V2-METRIC`: README `metric_depth`, bảng model và đơn vị đầu ra.
- `SRC-DEPTH-ANYTHING-3-DOCS`: README chính thức, các nhóm model và ví dụ API.
- `SRC-RKNN3-PLATFORMS`: README chính thức, ví dụ DA3 và bảng Host SoC/Coprocessor.
- Hồ sơ dự án: `CLM-VISION-001`, `CLM-TASK-002`, `CLM-CTRL-001`; `docs/07_Vision_TaskState_Architecture.md`; protocol 09; nguồn chủ dự án ngày 21/10.
