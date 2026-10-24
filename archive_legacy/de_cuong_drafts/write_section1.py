# -*- coding: utf-8 -*-
import docx
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

file_path = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\DE_CUONG_NGHIEN_CUU_COBROWSE.docx'

doc = docx.Document()

# Thiết lập khổ A4 và lề chuẩn Bộ GD&ĐT / ViSEF
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.top_margin = Cm(2)
sec.bottom_margin = Cm(2)
sec.left_margin = Cm(3)
sec.right_margin = Cm(2)

def set_font(run, name='Times New Roman', size=14, bold=False, italic=False, color=(0,0,0)):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(*color)
    rpr = run._r.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts')
        rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), name)

# Tiêu đề tài liệu
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(0)
p_title.paragraph_format.space_after = Pt(4)
r = p_title.add_run('ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC KỸ THUẬT')
set_font(r, size=15, bold=True)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_before = Pt(0)
p_sub.paragraph_format.space_after = Pt(14)
r_sub = p_sub.add_run('NGHIÊN CỨU VÀ PHÁT TRIỂN GĂNG TAY THÔNG MINH HỖ TRỢ ĐÁNH GIÁ VÀ THEO DÕI CHỨC NĂNG VẬN ĐỘNG BÀN TAY TRONG PHỤC HỒI CHỨC NĂNG SAU ĐỘT QUỴ')
set_font(r_sub, size=14, bold=True)

# PHẦN 1
p_h1 = doc.add_paragraph()
p_h1.paragraph_format.space_before = Pt(12)
p_h1.paragraph_format.space_after = Pt(6)
r_h1 = p_h1.add_run('1. LÝ DO CHỌN ĐỀ TÀI VÀ TÍNH CẤP THIẾT')
set_font(r_h1, size=14, bold=True)

content = [
    ('1.1. Bối cảnh dịch tễ đột quỵ và gánh nặng suy giảm chức năng bàn tay tại Việt Nam', True),
    ('Đột quỵ não (tai biến mạch máu não) hiện là một trong những nguyên nhân hàng đầu gây tử vong và để lại di chứng tàn tật nặng nề nhất trên toàn cầu cũng như tại Việt Nam. Theo các báo cáo dịch tễ học toàn diện giai đoạn 1990–2019 (GBD) và cơ sở dữ liệu đăng kiểm đột quỵ RES-Q giai đoạn 2017–2023 (Trần et al., 2025), Việt Nam ghi nhận hơn 200.000 ca đột quỵ mới mỗi năm với tỷ lệ tử vong và tàn phế thuộc nhóm cao trong khu vực Đông Nam Á. Trong số những bệnh nhân may mắn sống sót, có tới 70% đến 80% trường hợp phải đối mặt với di chứng suy giảm hoặc mất hoàn toàn chức năng vận động chi trên, đặc biệt là sự khéo léo của bàn tay và các ngón tay.', False),
    ('Bàn tay con người là cơ quan vận động tinh xảo, chiếm tới hơn 90% các hoạt động chức năng sinh hoạt hàng ngày (Activities of Daily Living - ADL) như cầm nắm thức ăn, cài cúc áo, cầm bút, nâng cốc nước hay vệ sinh cá nhân. Khác với các khớp lớn ở chi dưới vốn chủ yếu phục vụ chức năng nâng đỡ và di chuyển thô, việc phục hồi chức năng vận động bàn tay đòi hỏi sự phối hợp thần kinh - cơ cực kỳ phức tạp giữa khả năng điều khiển độc lập từng khớp ngón, kiểm soát lực bóp chính xác và điều hòa trương lực cơ đối kháng. Mất đi chức năng bàn tay đồng nghĩa với việc người bệnh mất đi tính độc lập cá nhân, trở thành gánh nặng kinh tế và tâm lý to lớn cho gia đình cũng như hệ thống an sinh xã hội.', False),
    ('1.2. Khoảng trống lâm sàng: "Hộp đen 1–3 tháng" giữa các kỳ tái khám', True),
    ('Trong thực hành lâm sàng Phục hồi chức năng (PHCN) hiện nay tại Việt Nam, quy trình điều trị cho bệnh nhân đột quỵ sau giai đoạn cấp cứu được phân định thành hai môi trường tách biệt: can thiệp tại bệnh viện và tự tập luyện duy trì tại gia đình. Do tình trạng quá tải bệnh viện và hạn chế về điều kiện kinh tế, phần lớn bệnh nhân sau giai đoạn điều trị nội trú ngắn hạn đều phải xuất viện và tiếp tục phục hồi chức năng tại nhà, chỉ quay lại cơ sở y tế tái khám định kỳ sau mỗi 1 đến 3 tháng.', False),
    ('Khoảng thời gian 1 đến 3 tháng giữa hai lần tái khám lâm sàng thực chất là một "HỘP ĐEN" (nguyên văn ghi nhận từ phỏng vấn sâu kỹ thuật viên VLTL-PHCN tuyến đầu). Bác sĩ và chuyên viên phục hồi chức năng hoàn toàn mất dấu vết dữ liệu về quá trình tập luyện thực tế của người bệnh tại nhà: không thể biết bệnh nhân có duy trì tập luyện hay không, cường độ tập có đủ kích hoạt tính dẻo thần kinh (Neuroplasticity) hay không, và quan trọng nhất là các động tác gập duỗi ngón tay được thực hiện đúng hay sai.', False),
    ('Việc thiếu giám sát liên tục tại nhà dẫn đến hai nguy cơ bệnh học nghiêm trọng: (1) Nếu tập sai kỹ thuật hoặc gắng sức co kéo cưỡng bức khi chưa kiểm soát được trương lực cơ, người bệnh rất dễ kích hoạt các phản xạ co cứng bệnh lý (Spasticity), dẫn đến hiện tượng co rút gân cơ vĩnh viễn, biến dạng khớp ngón tay và chèn ép thần kinh ngoại vi; (2) Nếu người bệnh nản lòng không tập đủ liều lượng do thiếu sự phản hồi tiến triển rõ ràng, "cửa sổ vàng" phục hồi thần kinh trong 6 tháng đầu sẽ trôi qua, khiến chức năng bàn tay bị chững lại và tàn phế suốt đời.', False),
    ('1.3. Bất cập của các giải pháp đánh giá và thiết bị hiện hữu', True),
    ('Để giải quyết bài toán trên, các giải pháp hiện tại trên thị trường và trong nghiên cứu bộc lộ những hạn chế cố hữu:', False),
    ('• Các thang đo lâm sàng chuẩn vàng (FMA-UE, ARAT, Box and Block, Jamar, E-Link): Mang bản chất là các "ảnh chụp tại một thời điểm" (Cross-sectional snapshot) chỉ thực hiện được khi bệnh nhân đến bệnh viện, đòi hỏi kỹ thuật viên có chuyên môn thao tác trực tiếp, tốn kém thời gian và chi phí, hoàn toàn bất khả thi cho việc theo dõi liên tục hàng ngày tại nhà.', False),
    ('• Nhật ký tập luyện tự ghi chép (Self-reported logs): Dữ liệu do người bệnh hoặc người nhà tự ghi lại có độ sai lệch cực lớn (sai số từ 100 đến 200 lượt tập mỗi giờ theo y văn quốc tế), không mang giá trị định lượng khách quan để bác sĩ ra quyết định điều chỉnh phác đồ.', False),
    ('• Các hệ thống Robot tập phục hồi chức năng thương mại (Gloreha, Syrebo, Merinco): Chủ yếu là các thiết bị tập vận động thụ động liên tục (CPM) dùng buồng khí nén hoặc động cơ kéo cưỡng bức cồng kềnh, giá thành quá cao (từ hàng chục đến hàng trăm triệu đồng, vượt xa khả năng chi trả của đa số bệnh nhân Việt Nam), và đặc biệt KHÔNG được thiết kế để đo lường định lượng, không bóc tách được nỗ lực chủ động của cơ và không theo dõi được xu hướng tiến triển dài hạn.', False),
    ('1.4. Ý tưởng cốt lõi và mục tiêu giải quyết của đề tài', True),
    ('Xuất phát từ thực tiễn cấp bách trên, đề tài tập trung nghiên cứu và phát triển một hệ sinh thái găng tay thông minh giá thành thấp (< 1,5 triệu VNĐ) hướng tới mục tiêu: ĐÓNG VAI TRÒ LÀ CÔNG CỤ ĐÁNH GIÁ ĐỊNH LƯỢNG VÀ THEO DÕI DỌC (Longitudinal Monitoring) CHỨC NĂNG BÀN TAY TẠI NHÀ, lấp đầy khoảng trống "hộp đen" giữa hai lần tái khám định kỳ.', False),
    ('Bằng việc ứng dụng nguyên lý mạch cầu vi sai áp điện trở 2 vách (Lòng – Mu) tích hợp trên khung găng công thái học kết hợp bộ thu thập tín hiệu vi sai tốc độ cao (ESP32-S3 + CD74HC4067 + INA333 + ADS1115), thiết bị có khả năng tự triệt tiêu trôi dạt môi trường, bóc tách chính xác nỗ lực co cơ chủ động (Effort Index - EI) khỏi lực cản co cứng cơ đối kháng, trích xuất bộ ba chỉ số chức năng có ý nghĩa lâm sàng (EI, GAP, RAL) và theo dõi sự phục hồi liên tục của bệnh nhân qua từng ngày với độ tin cậy được kiểm chứng thực nghiệm chặt chẽ.', False)
]

for text, is_sub in content:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = Pt(18)  # 1.35x của 14pt (14 * 1.35 = 18.9 pt)
    p.paragraph_format.space_before = Pt(8 if is_sub else 2)
    p.paragraph_format.space_after = Pt(2)
    if is_sub:
        p.paragraph_format.first_line_indent = Inches(0)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        set_font(r, size=14, bold=True)
    else:
        p.paragraph_format.first_line_indent = Inches(0.4)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(text)
        set_font(r, size=14, bold=False)

doc.save(file_path)
print("Updated successfully Section 1 into:", file_path)
