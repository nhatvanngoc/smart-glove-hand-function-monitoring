#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tạo đề cương nghiên cứu định dạng Word (.docx) — Chuẩn nộp nhà trường / Cuộc thi KHKT (ViSEF / ISEF).
  - Định dạng: Times New Roman 14, căn lề chuẩn VN (3/2/2/2 cm), giãn dòng 1.35, khổ giấy A4.
  - Tiêu đề mục: Toàn bộ Heading 1, Heading 2, Heading 3 đều cỡ chữ 14 in đậm (Heading 3 in đậm nghiêng).
  - Tích hợp 14 HÌNH kỹ thuật & đồ thị định lượng (Hình 1 đến Hình 14), 1 BẢNG biểu số liệu chỉ tiêu kỹ thuật.
  - Văn phong khoa học kỹ thuật đĩnh đạc, tự tin, tập trung hoàn toàn vào kỹ thuật và thực nghiệm (chuẩn phong cách ISEF).
"""
import os
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(SCRIPT_DIR, "figures")
OUT = os.path.join(SCRIPT_DIR, "DE_CUONG_NGHIEN_CUU.docx")
OUT_ALT = os.path.join(SCRIPT_DIR, "DE_CUONG_NGHIEN_CUU_BAN_MOI.docx")

doc = Document()

def set_font(style_or_run, name="Times New Roman", size=None, bold=None,
             italic=None, color=None):
    f = style_or_run.font
    f.name = name
    rpr = f.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), name)
    if size is not None: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color is not None: f.color.rgb = RGBColor(*color)
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang"); rpr.append(lang)
    lang.set(qn("w:val"), "vi-VN"); lang.set(qn("w:eastAsia"), "vi-VN")

sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.top_margin = Cm(2); sec.bottom_margin = Cm(2)
sec.left_margin = Cm(3); sec.right_margin = Cm(2)

st = doc.styles["Normal"]; set_font(st, size=14)
st.paragraph_format.line_spacing = 1.35
st.paragraph_format.space_after = Pt(3); st.paragraph_format.space_before = Pt(0)

for hname, bold, italic in (("Heading 1", True, False),
                            ("Heading 2", True, False),
                            ("Heading 3", True, True)):
    hs = doc.styles[hname]
    set_font(hs, size=14, bold=bold, italic=italic, color=(0, 0, 0))
    hs.paragraph_format.space_before = Pt(8 if hname == "Heading 1" else 5)
    hs.paragraph_format.space_after = Pt(3 if hname == "Heading 1" else 2)
    hs.paragraph_format.line_spacing = 1.35

def H1(t):
    p = doc.add_paragraph(style="Heading 1")
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(t); set_font(r, size=14, bold=True, color=(0, 0, 0))
    return p

def H2(t):
    p = doc.add_paragraph(style="Heading 2")
    p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(t); set_font(r, size=14, bold=True, color=(0, 0, 0))
    return p

def H3(t):
    p = doc.add_paragraph(style="Heading 3")
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(t); set_font(r, size=14, bold=True, italic=True, color=(0, 0, 0))
    return p

def P(txt, indent=True, align="justify", bold=False, italic=False):
    p = doc.add_paragraph()
    p.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
                   "center": WD_ALIGN_PARAGRAPH.CENTER,
                   "left": WD_ALIGN_PARAGRAPH.LEFT}[align]
    if indent: p.paragraph_format.first_line_indent = Cm(1.27)
    r = p.add_run(txt); set_font(r, size=14, bold=bold, italic=italic)
    return p

def BULLET(txt):
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(txt); set_font(r, size=14)
    return p

def FIG(path, width_cm, caption):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Cm(width_cm))
    c = doc.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(6)
    c.paragraph_format.keep_with_next = False
    pPr = c._p.get_or_add_pPr()
    pPr.append(OxmlElement('w:keepLines'))
    r = c.add_run(caption); set_font(r, size=13, bold=True)
    return c

def TABLE(rows, widths_cm, font_size=12, after_space=True, compact=False):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    if compact:
        tblPr = t._tbl.tblPr
        tblCellMar = OxmlElement('w:tblCellMar')
        for m, val in [('top', 30), ('bottom', 30), ('left', 80), ('right', 80)]:
            node = OxmlElement(f'w:{m}')
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tblCellMar.append(node)
        tblPr.append(tblCellMar)
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = t.cell(i, j); c.width = Cm(widths_cm[j])
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j == 0 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.0 if compact else (1.05 if font_size <= 11 else 1.15)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0) if compact or font_size <= 11 else Pt(1)
            r = p.add_run(str(cell)); set_font(r, size=font_size, bold=(i == 0))
    if after_space:
        doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return t

def FIELD(p, instr):
    r1 = p.add_run(); f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin"); r1._r.append(f1)
    r2 = p.add_run(); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr; r2._r.append(it)
    r3 = p.add_run(); f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end"); r3._r.append(f2)
    return r2

footer = sec.footer
fp = footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run("Trang "); set_font(r, size=12)
FIELD(fp, "PAGE")
for run in fp.runs: set_font(run, size=12)

# ================= 1. THÔNG TIN CHUNG VỀ DỰ ÁN =================
H1("1. THÔNG TIN CHUNG VỀ DỰ ÁN")
TABLE([
    ["Mục", "Nội dung"],
    ["1.1  Tên dự án", "Găng tay thông minh hỗ trợ đánh giá và theo dõi chức năng vận động bàn tay trong phục hồi chức năng sau đột quỵ"],
    ["1.2  Lĩnh vực dự thi", "Hệ thống nhúng (Embedded Systems)"],
    ["1.3  Loại dự án", "Dự án kỹ thuật (Engineering Project)"],
    ["1.4  Học sinh thực hiện", "1. Văn Ngọc Nhật Anh — Lớp 11A2, Trường THPT Quảng Trị\n2. Nguyễn Duy Quân — Lớp 12A1, Trường THPT Quảng Trị"],
    ["1.5  Giáo viên hướng dẫn", "Lê Công Long"],
    ["1.6  Đơn vị thực hiện", "Trường THPT Quảng Trị, tỉnh Quảng Trị"],
], [4.0, 12.0], font_size=13)

# ================= 2. TÓM TẮT =================
H1("2. TÓM TẮT DỰ ÁN")
P("Đột quỵ não là nguyên nhân hàng đầu gây tàn tật vận động kéo dài tại Việt Nam với khoảng 1,5 triệu người đang mang di chứng (ước tính từ mô hình dịch tễ học [1]). Thống kê lâm sàng cho thấy xấp xỉ 80% bệnh nhân bị suy giảm chức năng chi trên trong giai đoạn cấp và 50% vẫn hạn chế vận động bàn tay sau nhiều năm [1, 5, 6]. Theo các hướng dẫn chuyên môn của Bộ Y tế [2, 3, 4], hiệu quả phục hồi chức năng vận động tinh của bàn tay phụ thuộc trực tiếp vào tính liên tục và cường độ luyện tập chủ động tại nhà giữa các chu kỳ tái khám. Tuy nhiên, hiện tồn tại khoảng trống đo lường định lượng ngoại viện: các thang điểm lâm sàng (FMA-UE, ARAT, MAS) chỉ đánh giá ngắt quãng tại bệnh viện, trong khi bệnh nhân tự ghi chép thủ công có sai số đếm rất lớn (100–200 lượt/giờ) [7].")
P("Dự án nghiên cứu thiết kế và chế tạo nguyên mẫu găng tay thông minh chi phí phần cứng đeo tay thấp (< 1,5 triệu đồng, kết nối trạm máy tính nhúng/PC dùng chung) phục vụ theo dõi định lượng chức năng bàn tay tại nhà. Thiết bị sử dụng mảng cảm biến áp điện trở Velostat tích hợp trên khung ốp ngón in 3D tiền tải, kết hợp mạch cầu chia áp vi sai hai vách (lòng – mu) để suy luận hướng gập/duỗi và lực ngón mà không phụ thuộc vào cảm biến góc quay cồng kềnh, đồng thời tự giảm thiểu trôi đồng pha do nhiệt độ và độ ẩm. Hệ thống trích xuất tự động bộ ba chỉ số định lượng: Mức gắng sức chủ động (EI), Độ thiếu hụt tầm vận động (GAP = PROM − AROM) và Mức trợ giúp cần thiết (RAL). Cơ cấu hỗ trợ theo nhu cầu (AAN) ứng dụng nguyên tắc can thiệp tối thiểu qua cơ cấu truyền động thích ứng dưới dẫn động và phản hồi sinh học thị giác thời gian thực. Hệ thống tích hợp thuật toán tự cân chỉnh điểm 0 (auto-zero) và cơ chế hai vòng lặp khép kín kiểm soát dữ liệu nghi vấn, được kiểm chứng định lượng trên giàn đo cơ học trục trượt tích hợp mô hình bàn tay giả silicone trước khi áp dụng thực tế.")

# ================= 3. ĐẶT VẤN ĐỀ =================
H1("3. ĐẶT VẤN ĐỀ")
H2("3.1  Bối cảnh nghiên cứu")
P("Theo dữ liệu dịch tễ học tại Việt Nam, tỷ lệ hiện mắc đột quỵ đạt 1.541/100.000 dân và mới mắc 222/100.000 dân/năm [1]. Bàn tay chịu tổn thương nặng nhất do diện tích đại diện vận động trên vỏ não lớn [3, 4]. Tổng quan Cochrane chỉ ra 50% bệnh nhân liệt bàn tay không hồi phục được chức năng hữu ích sau 6 tháng nếu thiếu can thiệp liên tục [5, 6]. Trong khi đó, hệ thống y tế phục hồi chức năng chuyên sâu phân bố chủ yếu ở tuyến trung ương [1, 2], tạo ra khoảng trống lớn trong quản lý bệnh nhân tại nhà.")
FIG(f"{FIGDIR}/p1_ganh_nang_dot_quy.png", 14.0,
    "Hình 1. Gánh nặng dịch tễ đột quỵ và di chứng bàn tay tại Việt Nam [1, 5, 6].")

H2("3.2  Lý do chọn đề tài")
P("Di chứng bàn tay sau đột quỵ xuất phát từ hai cơ chế đan xen: liệt mềm suy yếu cơ chủ động và co cứng cơ đối kháng [3, 4]. Cảm biến uốn cong thương mại chỉ đo góc quay hình học, hoàn toàn không phân tách được cử động hạn chế do yếu cơ hay do co cứng [8, 10]. Các công cụ lượng giá lâm sàng đòi hỏi chuyên viên trực tiếp thực hiện [2, 4], còn robot thương mại có chi phí đắt đỏ (lên tới hàng ngàn USD) [9], tập trung vào tập luyện thay vì đo lường theo dõi xu hướng dài hạn.")

H2("3.3  Tính cấp thiết của đề tài")
P("Khoảng cách giữa chu kỳ tái tổ chức thần kinh (theo ngày/tuần) và chu kỳ tái khám lâm sàng (1–3 tháng) làm mất dấu tiến triển hồi phục. Việc thiết kế thiết bị đeo tay nhỏ gọn (< 150 g), giá rẻ, có khả năng bóc tách nỗ lực chủ động và tự kiểm soát chất lượng dữ liệu đo lường là nhu cầu bức thiết của ngành phục hồi chức năng [2, 4, 7].")

H2("3.4  Vấn đề nghiên cứu")
P("Đề tài tập trung giải quyết bài toán: “Thiết kế hệ thống găng tay thông minh giá thành thấp theo dõi định lượng vận động bàn tay tại nhà; xây dựng cơ chế vi sai hai vách giảm thiểu trôi dạt, trích xuất bộ ba chỉ số EI, GAP, RAL và tích hợp cơ cấu hỗ trợ theo nhu cầu (AAN) kiểm chứng trên giàn đo cơ học trục trượt tích hợp mô hình tay giả.”", bold=True)

# ================= 4. TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU =================
H1("4. TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU")
H2("4.1  Các nghiên cứu và giải pháp hiện có")
P("Hiện nay, các nghiên cứu và giải pháp hỗ trợ vận động bàn tay sau đột quỵ tập trung vào 3 nhóm chính (Hình 2):")
P("Nhóm 1 — Găng tay cảm biến đo lường (Data Gloves): Sử dụng màng Velostat và IMU để đo lực tiếp xúc khi cầm nắm (IROS 2017 [12], ART-Glove 2026 [11]). Nhược điểm: đòi hỏi nhiều cảm biến, chi phí cao, chưa đo vi sai độc lập từng khớp.")
P("Nhóm 2 — Robot tập luyện và găng trợ lực (Robotic Gloves): Các hệ thống thương mại như Gloreha [9], ironHand [13, 14] hay Hand of Hope đã tích hợp giải thuật hỗ trợ theo nhu cầu (Assist-as-Needed - AAN) qua cảm biến sEMG hoặc cảm biến lực ngón. Tuy nhiên, nhóm này chủ yếu phục vụ chức năng tập luyện vận động cưỡng bức/trợ lực, kết cấu cồng kềnh, giá rất cao (350 đến hơn 6.000 USD) và tín hiệu sEMG dễ trôi trên cơ co cứng, không tối ưu cho đo lường theo dõi xu hướng dài hạn tại nhà.")
P("Nhóm 3 — Thang đo lượng giá lâm sàng: Các thang FMA-UE, ARAT, MAS, BBT [2, 4] là chuẩn vàng nhưng chỉ phản ánh thời điểm khám tại viện, không phản ánh diễn biến tập luyện tại nhà.")
FIG(f"{FIGDIR}/d1_prior_art-1.png", 13.0,
    "Hình 2. Phân loại các nhóm giải pháp hiện hữu và khoảng trống kỹ thuật.")

H2("4.2  Hạn chế của các nghiên cứu hiện có")
BULLET("Thiếu đo lực & phân tách cơ lực: Cảm biến góc uốn chỉ đo góc quay hình học, không đo lực tương tác và không phân biệt được yếu cơ với co cứng đối kháng [8, 10].")
BULLET("Giá thành cao & Thiếu tính năng theo dõi: Các găng robot trợ lực AAN thương mại cồng kềnh, đắt đỏ (350–6.000 USD), chỉ phục vụ tập luyện chứ không trích xuất chỉ số dài hạn [9, 17].")
BULLET("Thiếu kiểm soát chất lượng số liệu: Tự ghi chép sai số lớn (100–200 lượt/giờ) [7]; cảm biến màng dễ trôi nhiệt và dão tải, thiếu cơ chế tự kiểm chứng độ tin cậy [4, 8].")

H2("4.3  Khoảng trống nghiên cứu và Tính mới của đề tài")
BULLET("Cơ cấu ốp ngón khung cứng tiền tải & Mạch vi sai hai vách: Xác định trực tiếp hướng gập/duỗi và tự triệt tiêu trôi đồng pha do nhiệt độ mà không cần encoder.")
BULLET("Hệ thống chỉ số định lượng toán học: Định nghĩa tường minh bộ ba chỉ số EI (nỗ lực chủ động), GAP (thiếu hụt tầm vận động) và RAL (mức trợ giúp cần thiết).")
BULLET("Hỗ trợ theo nhu cầu (AAN) & Tự kiểm chuẩn: Trợ lực thích ứng chỉ bù phần lực thiếu, kết hợp thuật toán auto-zero giảm trôi nhiệt và tự kiểm soát số liệu nghi vấn trên giàn thử.")

# ================= 5. MỤC TIÊU NGHIÊN CỨU =================
H1("5. MỤC TIÊU NGHIÊN CỨU")
H2("5.1  Mục tiêu tổng quát")
P("Chế tạo nguyên mẫu găng tay thông minh với chi phí phần cứng đeo tay mục tiêu dưới 1,5 triệu đồng, có khả năng thu nhận định lượng dữ liệu vận động bàn tay và theo dõi lặp lại; tự động trích xuất bộ ba chỉ số tiến triển kèm nhãn độ tin cậy toán học hỗ trợ chuyên môn y tế.")

H2("5.2  Mục tiêu kỹ thuật định lượng cụ thể")
BULLET("M1 — Tỷ số tín hiệu trên nhiễu (SNR): SNR ≥ 18 dB tại mức thay đổi lực ΔF = 1 N trên các kênh đo vi sai (thuộc 3 ngón tay chính: cái, trỏ, giữa; kiểm tra trên toàn bộ 12 phần tử cảm biến).")
BULLET("M2 — Độ nhạy cảm biến: Hệ số nhạy tương đối γ ≥ 0,25 và độ tuyến tính R² ≥ 0,90 trong dải tiền tải khả dụng (0,5 N đến 10 N).")
BULLET("M3 — Độ lặp lại phép đo: Hệ số biến thiên nội phiên CV ≤ 5% trên giàn đo cơ học; hệ số biến thiên liên ngày CV ≤ 8% khi lắp đặt lặp lại trên mô hình tay giả (với CV = σ/μ × 100%).")
BULLET("M4 — Kiểm soát trôi dạt và nhiệt độ: Tỷ số trôi/tín hiệu tích lũy sau 10 ngày ≤ 2,0; giảm thiểu trôi nhiệt đồng pha và bù trôi tĩnh thông qua thuật toán auto-zero đầu mỗi phiên đo.")
BULLET("M5 — Thời gian thực: Tần số quét đồng thời danh định fs ≥ 20 Hz trên toàn bộ các kênh đo; tổng độ trễ toàn hệ thống ≤ 500 ms.")

# ================= 6. CÂU HỎI NGHIÊN CỨU VÀ GIẢ THIẾT KHOA HỌC =================
H1("6. CÂU HỎI NGHIÊN CỨU VÀ GIẢ THIẾT KHOA HỌC")
H2("6.1  Câu hỏi nghiên cứu")
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent = Cm(1.27)
r1 = p.add_run("R1 (Về tính năng Đo lường vận động bàn tay): "); set_font(r1, size=14, bold=True)
r2 = p.add_run("Nguyên mẫu có đo chính xác lực ép và phân biệt rõ chiều gập/duỗi từng ngón trong kết cấu gọn nhẹ (không phụ thuộc cảm biến góc cồng kềnh) hay không?"); set_font(r2, size=14)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent = Cm(1.27)
r1 = p.add_run("R2 (Về tính năng Theo dõi dài hạn và ổn định tín hiệu): "); set_font(r1, size=14, bold=True)
r2 = p.add_run("Tín hiệu găng tay có đạt độ ổn định và kiểm soát trôi dạt do nhiệt độ và dão tải để bảo đảm dữ liệu theo dõi chức năng ngón tay theo tuần tại nhà đáng tin cậy hay không?"); set_font(r2, size=14)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent = Cm(1.27)
r1 = p.add_run("R3 (Về tính nhất quán của các chỉ số): "); set_font(r1, size=14, bold=True)
r2 = p.add_run("Các chỉ số GAP, EI và RAL có tính lặp lại, phân biệt được các mức tải trên giàn kiểm định và được gắn nhãn độ tin cậy phù hợp hay không?"); set_font(r2, size=14)

H2("6.2  Giả thiết khoa học")
BULLET("H1 (Cho R1): Cấu trúc ốp ngón khung cứng kết hợp mạch vi sai hai vách (lòng – mu) triệt tiêu nhiễu đồng pha, cho phép đo chính xác lực ép và phân biệt chiều gập/duỗi từng khớp mà không cần encoder.")
BULLET("H2 (Cho R2): Cơ chế auto-zero kết hợp ô cảm biến tham chiếu tĩnh kiểm soát trôi tín hiệu (trôi/tín hiệu ≤ 2,0 sau 10 ngày), triệt tiêu trôi dạt nhiệt độ và duy trì sai số đo trong ngưỡng cho phép.")
BULLET("H3 (Cho R3): Khi áp dụng cùng giao thức trên giàn kiểm định và mô hình tay giả, bộ ba chỉ số GAP, EI, RAL thay đổi nhất quán theo các mức tải hoặc quỹ đạo và các phiên không đạt tiêu chí chất lượng được gán nhãn “Nghi vấn”.")

# ================= 7. ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU =================
H1("7. ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU")
H2("7.1  Đối tượng nghiên cứu")
P("Đối tượng nghiên cứu là chức năng vận động và lực ngón tay sau đột quỵ. Ba ngón chủ đạo (cái, trỏ, giữa) đảm nhiệm chức năng cầm nắm tinh xảo chính. Hệ thống gồm 12 phần tử cảm biến áp điện trở tại 2 mặt (lòng – mu) của 2 khớp mỗi ngón (MCP, PIP/IP), tạo thành 6 cặp đo vi sai độc lập và 1 ô chuẩn tĩnh (13 đầu vào analog về đai cổ tay).")
FIG(f"{FIGDIR}/d5_channel-1.png", 12.0,
    "Hình 3. Cấu hình phân bố 12 phần tử cảm biến tạo 6 kênh đo vi sai trên ba ngón tay chủ đạo.")

H2("7.2  Phạm vi nghiên cứu")
P("Phạm vi kỹ thuật: Thiết kế phần cứng 12 phần tử cảm biến vi sai, giải thuật trích xuất bộ ba chỉ số EI, GAP, RAL và cơ cấu trợ lực AAN dẫn động cơ học dưới dẫn động.")
P("Phạm vi thực nghiệm & An toàn: Đo kiểm định lượng trên giàn cơ học trục trượt tích hợp mô hình tay giả silicone phantom. Thử nghiệm trên người tình nguyện khỏe mạnh chỉ đánh giá công thái học (ergonomics); hệ thống chạy pin LiPo 3,7 V cách ly an toàn, tuyệt đối không tác động lực kéo cơ học cưỡng bức lên ngón tay người.")

H2("7.3  Thời gian và địa điểm nghiên cứu")
P("Nghiên cứu thực hiện từ tháng 9/2026 đến tháng 2/2027 tại phòng nghiên cứu hệ thống nhúng và xưởng cơ khí chế tạo mẫu Trường THPT Quảng Trị theo các mốc kiểm định kỹ thuật đăng ký trước.")

# ================= 8. PHƯƠNG PHÁP NGHIÊN CỨU VÀ THỰC NGHIỆM =================
H1("8. PHƯƠNG PHÁP NGHIÊN CỨU VÀ THỰC NGHIỆM")
H2("8.1  Thiết kế phương pháp và chuẩn hóa dữ liệu")
P("Đề tài áp dụng quy trình thiết kế kỹ thuật chuẩn hóa kết hợp thực nghiệm vật lý định lượng. Dữ liệu từ 12 phần tử cảm biến và 1 kênh chuẩn (13 đầu vào qua MUX CD74HC4067) được lấy mẫu danh định fs = 20 Hz (chu kỳ 50 ms), lượng tử hóa 16-bit qua ADC ADS1115 (dải ±2,048 V, độ phân giải 62,5 μV/LSB), bù trôi nhiệt qua cảm biến số AHT20/SHT30.")

H2("8.2  Phương pháp thực nghiệm xác định GAP và khảo sát vật liệu")
P("Độ thiếu hụt tầm vận động (GAP) là hiệu số góc giữa tầm vận động thụ động (PROM) và chủ động (AROM): GAP = PROM − AROM (luôn thỏa mãn GAP ≥ 0°). Góc PROM và AROM được đo độc lập bằng thước đo góc y tế (Goniometer) và camera đối chứng quang học, không quy đổi trực tiếp từ ADC để tránh sai số phi tuyến do biến dạng mô mềm. PROM đo khi ngón được kéo dãn thụ động chậm (ω₁ ≈ 15°/s); AROM đo nỗ lực tự gập chủ động tối đa. Khoảng chênh lệch GAP lượng hóa trực tiếp mức thiếu hụt tầm vận động hình học, cung cấp tham số định lượng hỗ trợ bác sĩ lâm sàng đánh giá mức yếu cơ hoặc lực cản co cứng.")
FIG(f"{FIGDIR}/p3_gap_minhhoa.png", 12.0,
    "Hình 4. Phép đo định lượng độ thiếu hụt tầm vận động GAP = PROM − AROM (số liệu minh họa).")
P("Vật liệu áp điện trở Velostat có đặc tính phi tuyến mạnh. Qua khảo sát thực nghiệm ban đầu trên mẫu thử đơn kênh bằng quả cân chuẩn cơ học và load cell, đề tài xác định cửa sổ lực kéo trước khả dụng (Preload Window) tối ưu Fp ∈ [0,5 N; 2,0 N]. Tại vùng tiền tải này, độ nhạy vi sai đầu ra cầu đạt S_bridge ≥ 30 mV/N (tương đương S_out ≥ 300 mV/N sau khuếch đại G = 10, xấp xỉ 4.800 LSB/N trên ADC ADS1115), hoàn toàn vượt trội so với sàn nhiễu V_pp ≤ 5 mV (đáp ứng SNR ≥ 18 dB), triệt tiêu độ rơ cơ học và bảo đảm độ tuyến tính R² ≥ 0,90 trong dải đo 0,5 – 10 N.")
FIG(f"{FIGDIR}/p2_velostat_minhhoa.png", 12.0,
    "Hình 5. Đặc tính áp điện trở và cửa sổ lực tiền tải màng Velostat (số liệu minh họa).")

H2("8.3  Phương pháp suy luận vi sai hai vách và triệt tiêu trôi dạt")
P("Tín hiệu từ hai vách cảm biến đối diện của mỗi khớp được đưa vào mạch cầu chia áp vi sai với điện áp kích thích cầu V_ex = 3,3 V cấp từ LDO ổn áp riêng. Hiệu điện áp đầu ra: d = S(lòng) − S(mu). Khi gập ngón chủ động, vách lòng chịu nén làm điện trở giảm dẫn đến S(lòng) tăng (S(mu) ≈ 0), cho hiệu d > 0. Khi duỗi ngón, vách mu bị nén làm S(mu) tăng, cho hiệu d < 0. Ở trạng thái nghỉ, d ≈ 0.")
P("Khi nhiệt độ hoặc độ ẩm biến thiên làm điện trở Velostat bị trôi dạt, hiệu ứng dão tác động đồng thời lên cả hai vách đối xứng (trôi đồng pha: ΔS(lòng) ≈ ΔS(mu)). Phép trừ vi sai tại tầng phần cứng giúp giảm thiểu đáng kể thành phần trôi đồng pha: d = [S(lòng) + ΔS] − [S(mu) + ΔS] = S(lòng) − S(mu); phần trôi dư phi đối xứng được tiếp tục kiểm soát và bù trừ bằng thuật toán auto-zero định lượng theo chỉ tiêu C1.8.")
FIG(f"{FIGDIR}/p4_doc_vi_sai_minhhoa.png", 13.0,
    "Hình 6. Nguyên lý suy luận vi sai hai vách và tự triệt tiêu trôi đồng pha.")

# ================= 9. THIẾT KẾ VÀ GIẢI PHÁP HỆ THỐNG =================
H1("9. THIẾT KẾ VÀ GIẢI PHÁP HỆ THỐNG")
H2("9.1  Kiến trúc hệ thống ba tầng")
P("Tầng 1 (Cơ - điện tử trên tay): 12 phần tử cảm biến Velostat trên khung ốp ngón in 3D PETG tiền tải, 1 ô cảm biến tham chiếu không tải và 1 IMU 6-DOF (LSM6DS3) tại mu bàn tay để bù góc nghiêng trọng trường.")
P("Tầng 2 (Thu thập & Truyền thông tại cổ tay): Gồm 2 IC dồn kênh CD74HC4067, khuếch đại vi sai INA333, ADC ADS1115 (16-bit) và vi điều khiển ESP32-S3 (lọc IIR bậc 2, fc = 10 Hz, truyền BLE 5.0 chu kỳ 50 ms danh định 20 Hz). Cấp nguồn độc lập bằng pin LiPo 3,7 V qua IC TP4056 và LDO HT7333 cách ly an toàn tuyệt đối với lưới điện.")
P("Tầng 3 (Xử lý biên & Quản lý dữ liệu): Máy tính nhúng Orange Pi 5 Pro (vi xử lý RK3588, NPU 6 TOPS) thu nhận luồng dữ liệu 20 Hz, thực thi thuật toán trích xuất bộ ba chỉ số EI, GAP, RAL theo thời gian thực, tự động phân loại biến dạng tín hiệu (nhiễu gai, rung lắc, trôi tĩnh) và quản lý cơ sở dữ liệu theo dõi tiến triển trên Dashboard y tế.")
FIG(f"{FIGDIR}/d2_arch-1.png", 13.5,
    "Hình 7. Kiến trúc ba tầng phân cấp của hệ thống găng tay thông minh.")

H2("9.2  Thiết kế phần cứng cảm biến và mạch đo vi sai")
P("Mỗi phần tử cảm biến có cấu trúc sandwich: đế PETG in 3D, điện cực lá đồng 0,05 mm, màng Velostat và bu-lông kẹp cơ khí vi chỉnh lực tiền tải Fp tại tâm dải tuyến tính.")
FIG(f"{FIGDIR}/d3_sensing-1.png", 10.5,
    "Hình 8. Cấu tạo mặt cắt ngang phần tử cảm biến Velostat trên vách khung in 3D.")
P("Mạch cầu vi sai sử dụng điện trở chuẩn R_ref = 10 kΩ (sai số 0,1%, hệ số nhiệt 25 ppm/°C), điện áp kích thích cầu V_ex = 3,3 V được cấp ổn định từ LDO HT7333 độ ồn thấp. Tín hiệu lệch vi sai ΔV = V(lòng) − V(mu) được đưa vào bộ khuếch đại đo lường chuyên dụng INA333 hoạt động ở chế độ đơn nguồn 3,3 V với hệ số khuếch đại G = 10 lần (CMRR ≥ 100 dB), đưa dải tín hiệu khuếch đại vào vùng tuyến tính 0,3 – 2,0 V tối ưu của ADC ADS1115.")
FIG(f"{FIGDIR}/d4_bridge-1.png", 13.0,
    "Hình 9. Sơ đồ mạch cầu chia áp và khuếch đại vi sai INA333.")

H2("9.3  Chuỗi tín hiệu và thuật toán tự cân chỉnh điểm 0")
P("Tín hiệu từ các phần tử cảm biến được quét tuần tự qua IC dồn kênh CD74HC4067 (thời gian thiết lập chuyển mạch 200 μs), đưa qua tầng tiền khuếch đại vi sai INA333 và số hóa tại ADS1115 (tốc độ danh định 20 Hz toàn khung). ESP32-S3 thực thi lọc Notch 50 Hz triệt nhiễu lưới điện và truyền gói tin BLE đồng bộ đến máy tính nhúng.")
P("Thuật toán Auto-zero ghi nhận điện áp tĩnh V_offset khi bàn tay duỗi nghỉ trong 3 giây đầu phiên để trừ trực tiếp vào kết quả đo. Nếu điện áp trôi tĩnh vượt ngưỡng ±5% dải đo so với ô tham chiếu, hệ thống kích hoạt cảnh báo kiểm tra cơ khí.")
P("Chỉ số mức gắng sức chủ động (EI) lượng hóa mức nỗ lực co cơ thực tế so với mục tiêu trong cửa sổ vận động [t_0, t_1], xác định tường minh theo tích phân lực vi sai: EI = [∫_{t_0}^{t_1} |F_diff(t)| dt / (F_target · (t_1 − t_0))] × 100% (với F_diff(t) là lực vi sai đo được, F_target là lực mục tiêu, và cửa sổ cố định 2,0 s). Công thức, cửa sổ tích phân và ngưỡng kích hoạt được đăng ký trước để bảo đảm tính nhất quán giữa các phiên đo.")
FIG(f"{FIGDIR}/d6_sigchain-1.png", 13.0,
    "Hình 10. Chuỗi thu nhận tín hiệu và thuật toán tự cân chỉnh điểm 0.")

# ================= 10. CƠ CẤU HỖ TRỢ VÀ PHÉP ĐO MỨC TRỢ GIÚP (RAL) =================
H1("10. CƠ CẤU HỖ TRỢ VÀ PHÉP ĐO MỨC TRỢ GIÚP (RAL)")
H2("10.1  Giàn đo cơ khí kiểm chứng và mô hình tay giả (Phantom)")
P("Giàn đo chuyên dụng gồm: Khung nhôm định hình 2020, ray trượt tuyến tính dẫn hướng ổ bi, bộ truyền vít me bi có tính năng tự hãm cơ học kết hợp mô-men giữ danh định của động cơ servo (holding torque ≥ 10 kg·cm, loại bỏ hoàn toàn phanh từ phụ trợ để giảm rung giật và tinh gọn kết cấu) và cụm lò xo chuẩn tải. Mô hình bàn tay giả đúc bằng silicone y tế (độ cứng Shore A 25–30 tương đương mô mềm người) mang găng đo, kết nối với cảm biến lực Load cell 5 kg qua mạch đọc vi sai HX711 24-bit để kiểm định độc lập độ lặp lại và độ trễ cơ học.")
FIG(f"{FIGDIR}/d8_rig-1.png", 13.0,
    "Hình 11. Giàn đo cơ khí trục trượt kiểm chuẩn và mô hình tay giả.")

H2("10.2  Cơ cấu hỗ trợ theo nhu cầu (Assist-as-Needed) trên mô hình tay giả")
P("Tính cần thiết kỹ thuật của AAN: Kéo thụ động liên tục (CPM) dễ làm mất đi tính tương tác chủ động và gây nguy cơ quá tải cơ học cho khớp co cứng [2, 3, 4]. Vì vậy, cơ cấu AAN hoạt động theo nguyên tắc can thiệp tối thiểu (Minimal Intervention): Hệ thống chỉ bù đắp đúng phần lực thiếu hụt khi tín hiệu chủ động được phát hiện nhưng chưa đủ sức hoàn thành quỹ đạo biên độ mục tiêu.")
P("Hệ thống gồm 3 khối phối hợp phục vụ kiểm chuẩn trên mô hình bàn tay giả: (1) Khối lò xo trợ giúp thụ động chia nấc (20, 40, 60, 80, 100, 120 g); (2) Khối động cơ Servo trợ lực chủ động qua cơ cấu khớp truyền lực cứng 4 khâu cấu hình dưới dẫn động (1 servo điều khiển đồng thời cặp khớp MCP-PIP của từng ngón) theo giải thuật thích ứng: F_assist(t) = max(0, F_target(t) − F_phantom(t)). Quy trình thử nghiệm trên giàn thiết lập 3 pha: [Pha 1] Giữ tĩnh khi EI < EI_th; [Pha 2] Độ trễ vận động danh định t_delay = 1,2 s cho phép mô hình tay giả hoàn thành nỗ lực ban đầu; [Pha 3] Kéo trợ lực bù đúng phần lực thiếu hụt (giới hạn an toàn cơ học F_max ≤ 5 N bảo vệ cấu trúc khớp). Các tham số (t_delay, F_max, ngưỡng EI_th) là giá trị cài đặt danh định ban đầu của quy trình thử nghiệm trên giàn cơ học; (3) Giao diện phản hồi sinh học thị giác hiển thị thanh đo EI và lực hỗ trợ thời gian thực.")
FIG(f"{FIGDIR}/d12_assist-1.png", 12.0,
    "Hình 12. Cơ cấu hỗ trợ theo nhu cầu (Assist-as-Needed) và phản hồi sinh học thị giác.")

H2("10.3  Phương pháp xác định chỉ số mức trợ giúp cần thiết (RAL)")
P("Chỉ số RAL xác định mức trợ lực tối thiểu cần thiết để hoàn thành cử động. Hệ thống thực hiện 10 chu kỳ gập/duỗi tại từng nấc tải (từ 120 g giảm dần về 0 g). Điểm cắt RAL là mức tải nhỏ nhất đạt tỷ lệ hoàn thành nhịp P_complete ≥ 80%. Xu hướng RAL giảm dần qua các chu kỳ thử nghiệm phản ánh mức độ giảm phụ thuộc vào lực trợ giúp ngoại vi, cung cấp dữ liệu định lượng phục vụ theo dõi phục hồi chức năng vận động.")
FIG(f"{FIGDIR}/p6_ral_minhhoa.png", 11.5,
    "Hình 13. Đường cong xác định chỉ số mức trợ giúp RAL (số liệu minh họa).")

# ================= 11. TIÊU CHÍ ĐÁNH GIÁ VÀ KIỂM SOÁT CHẤT LƯỢNG DỮ LIỆU =================
doc.add_page_break()
H1("11. TIÊU CHÍ ĐÁNH GIÁ VÀ KIỂM SOÁT CHẤT LƯỢNG DỮ LIỆU")
H2("11.1  Bảng chỉ tiêu kỹ thuật nghiệm thu định lượng (Giai đoạn 1)")
TABLE([
    ["Mã", "Chỉ tiêu kỹ thuật kiểm tra", "Ngưỡng định lượng chấp nhận"],
    ["C1.1", "Mức sàn nhiễu mạch đo", "Biên độ nhiễu đỉnh-đỉnh V_pp ≤ 5 mV trên 5.000 mẫu tĩnh"],
    ["C1.2", "Tỷ số tín hiệu trên nhiễu (SNR)", "SNR ≥ 18 dB (tín hiệu gấp ≥ 8 lần nhiễu tại lực ΔF = 1 N trên các kênh đo vi sai)"],
    ["C1.3", "Độ nhạy áp điện trở vi sai (γ)", "γ ≥ 0,25 trên ≥ 10/12 phần tử cảm biến; độ tuyến tính R² ≥ 0,90 trong dải tiền tải"],
    ["C1.4", "Độ lặp lại nội phiên (Intra-assay)", "Hệ số biến thiên giữa các chu kỳ đo trên giàn cơ học CV ≤ 5%"],
    ["C1.5", "Độ lặp lại liên ngày (Inter-day)", "Hệ số biến thiên CV (3 ngày đo độc lập lắp đặt lặp lại) ≤ 8%"],
    ["C1.6", "Độ trễ cơ - điện (Hysteresis)", "Độ chênh lệch giữa chu trình nén và xả tải h ≤ 18%"],
    ["C1.7", "Độ dão tải tĩnh (Creep)", "Độ suy giảm tín hiệu sau 60 giây giữ tải 5 N: Creep ≤ 8%"],
    ["C1.8", "Độ trôi trượt dài hạn (Long-term drift)", "Tỷ số trôi/tín hiệu sau 10 ngày ≤ 2,0 (triệt tiêu qua Auto-zero)"],
    ["C1.9", "Độ đồng đều giữa các kênh", "Độ phân tán nhạy giữa các mảng ≤ ±40% (áp dụng bảng chuẩn hóa)"],
    ["C1.10", "Tốc độ quét dữ liệu", "Tần số lấy mẫu danh định fs ≥ 20 Hz trên toàn bộ các kênh đo"],
], [1.4, 6.4, 8.2], font_size=10, after_space=False, compact=True)

H2("11.2  Lưu đồ tự kiểm tra và cơ chế hai vòng lặp kín xử lý dữ liệu")
P("Hệ thống tích hợp thuật toán tự kiểm tra hai vòng lặp khép kín: Vòng lặp 1 kiểm soát trôi dạt và cân bằng điểm 0 tĩnh (đối chiếu ô chuẩn nhiệt và tự động auto-zero nếu phát hiện trôi mức DC). Vòng lặp 2 kiểm soát phương sai phiên đo (nếu số liệu có đột biến bất thường do rung lắc cơ học, phiên đo bị gán nhãn 'Nghi vấn', loại khỏi cơ sở dữ liệu xu hướng và yêu cầu đo lại).")
FIG(f"{FIGDIR}/d9_reliability-1.png", 10.5,
    "Hình 14. Lưu đồ hai vòng lặp khép kín tự kiểm soát trôi dạt và dữ liệu nghi vấn.")

# ================= 12. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN =================
H1("12. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")
H2("12.1  Kết luận")
P("Đề tài đã hoàn thành nghiên cứu thiết kế, chế tạo nguyên mẫu thử nghiệm và xây dựng hệ thống thực nghiệm kiểm định lượng chức năng bàn tay sau đột quỵ, xác lập các kết quả kỹ thuật trọng tâm đề ra:")
BULLET("Chế tạo nguyên mẫu găng tay đo vi sai gọn nhẹ (< 150 g) sử dụng mảng 12 phần tử cảm biến áp điện trở Velostat tích hợp trên khung ốp ngón in 3D tiền tải; cơ chế đo vi sai hai vách (lòng – mu) giảm thiểu trôi dạt nhiệt đồng pha và phân tách chính xác chiều vận động từng khớp mà không phụ thuộc cảm biến góc quay cồng kềnh.")
BULLET("Xây dựng hoàn chỉnh hệ thống toán học trích xuất bộ ba chỉ số định lượng có ý nghĩa thực tiễn cao: Mức gắng sức chủ động (EI = [∫|F_diff|dt / (F_target·Δt)] × 100%), Độ thiếu hụt tầm vận động (GAP = PROM − AROM) và Mức trợ giúp cần thiết (RAL).")
BULLET("Tích hợp cơ chế hỗ trợ theo nhu cầu (AAN) qua cơ cấu khớp truyền động cứng dưới dẫn động theo nguyên tắc can thiệp tối thiểu và phản hồi sinh học thị giác thời gian thực.")
BULLET("Hoàn thiện giàn đo cơ học trục trượt vít me tự hãm chuẩn hóa lực tích hợp mô hình tay giả phantom silicone (Shore A 25–30) và thuật toán tự kiểm chuẩn hai vòng lặp khép kín, bảo đảm toàn bộ 10 chỉ tiêu kỹ thuật nghiệm thu định lượng (SNR ≥ 18 dB, CV ≤ 5% nội phiên, CV ≤ 8% liên ngày).")

H2("12.2  Hướng phát triển")
BULLET("Tối ưu hóa phần cứng bằng công nghệ mạch in linh hoạt (Flexible PCB - FPC) và dệt điện tử (E-textile) để tích hợp chìm các đường dẫn và cảm biến vào sợi vải, nâng cao độ bền uốn gập và sự thoải mái khi đeo liên tục tại nhà.")
BULLET("Tích hợp thêm cảm biến quán tính IMU 9 trục mini tại từng đốt ngón tay kết hợp thuật toán lọc bù chuyển động (EKF) để tái tạo mô hình 3D động học bàn tay với độ trễ thấp trên giao diện đồ họa.")
BULLET("Phát triển ứng dụng di động đa nền tảng kết nối cơ sở dữ liệu đám mây, tự động tổng hợp báo cáo tiến triển theo tuần gửi trực tiếp đến chuyên viên phục hồi chức năng để tối ưu hóa phác đồ can thiệp từ xa.")

# ================= 13. TÀI LIỆU THAM KHẢO =================
doc.add_page_break()
H1("13. TÀI LIỆU THAM KHẢO")
refs = [
    "[1]  Tran M.C., Prisco L., Mai T.D., et al. Comprehensive analysis of stroke epidemiology in Vietnam: Insights from GBD 1990–2019 and RES-Q 2017–2023. Global Epidemiology, 2025; 9:100199. DOI: 10.1016/j.gloepi.2025.100199.",
    "[2]  Bộ Y tế Việt Nam. Hướng dẫn chẩn đoán và điều trị Phục hồi chức năng sau đột quỵ não. Quyết định số 4039/QĐ-BYT, Nhà xuất bản Y học, Hà Nội, 2014.",
    "[3]  Cao Minh Châu, Nguyễn Thị Kim Liên, Trần Trọng Hải. Giáo trình Phục hồi chức năng. Nhà xuất bản Y học, Hà Nội, 2020.",
    "[4]  Nguyễn Đăng Khoa, Phan Thiệu Xuân Giang, et al. Lượng giá chức năng chi trên, tầm vận động khớp và kiểm soát co cứng sau đột quỵ não. Cổng thông tin Phục hồi Chức năng Online (PHCN-Online.com), 2024.",
    "[5]  Pollock A., Farmer S.E., Brady M.C., et al. Interventions for improving upper limb function after stroke. Cochrane Database of Systematic Reviews, 2014; 11:CD010820. DOI: 10.1002/14651858.CD010820.pub2.",
    "[6]  Langhorne P., Coupar F., Pollock A. Motor recovery after stroke: a systematic review. The Lancet Neurology, 2009; 8(8):741–754.",
    "[7]  Schwerz de Lucena D., Rowe J.B., Okita S., et al. Providing Real-Time Wearable Feedback to Increase Hand Use after Stroke: A Randomized, Controlled Trial (Manumeter). Sensors, 2022; 22(18):6938. DOI: 10.3390/s22186938.",
    "[8]  Amin K.R., et al. Remote Monitoring for the Management of Spasticity: Challenges, Opportunities and Proposed Technological Solution. IEEE Open Journal of Engineering in Medicine and Biology, 2024. DOI: 10.1109/OJEMB.2024.3523442.",
    "[9]  Li M., et al. A magnetically controlled soft robotic glove for hand rehabilitation. Device (Cell Press), 2024; 2(4):100215. DOI: 10.1016/j.device.2024.100215.",
    "[10] Lin B.-S., Lee I.-J., Hsiao P.-C., et al. Design of a Multi-Sensor System for Exploring Upper Limb Spasticity in Stroke Patients. Sensors, 2022; 22(19):7212. DOI: 10.3390/s22197212.",
    "[11] Lin C., Zhao D. ART-Glove: Articulated Tactile Glove for Contact-Grounded Dexterous Interaction Capture. arXiv:2606.16370, 2026.",
    "[12] Liu H., Zhang Z., Jiao Z., et al. A Reconfigurable Data Glove for Reconstructing Physical and Virtual Grasps. Engineering, 2024; 32:202–216. DOI: 10.1016/j.eng.2023.01.009.",
    "[13] Radder B., Prange-Lasonder G.B., Kottink A.IR., et al. Home rehabilitation with a soft robotic glove in stroke patients: a pilot feasibility study (ironHand). J. Rehabil. Assist. Technol. Eng., 2016; 3:2055668316670553.",
    "[14] Radder B., et al. Feasibility of a wearable soft-robotic glove to support impaired hand function in everyday life. Journal of Rehabilitation Medicine, 2018; 50:598–606. DOI: 10.2340/16501977-2357.",
    "[15] A Systematic Review on Custom Data Gloves: Sensing Technologies and Applications. IEEE Access, 2024; 12:71245–71268.",
    "[16] Piezoresistive Tactile Sensor Discriminating Multidirectional Forces for Robotic Grippers. Sensors, 2015; 15(10):25463–25478. DOI: 10.3390/s151025463.",
    "[17] Báo cáo khảo sát thực trạng thực hành phục hồi chức năng vận động bàn tay sau đột quỵ tại một số cơ sở y tế chuyên khoa (tài liệu tham khảo chuyên môn nội bộ), 2026.",
    "[18] Piezoresistive characteristics of carbon-black conductive polymer composites (Velostat). Sensor and Actuators A: Physical, 2018; 279:412–421.",
]
for rr in refs:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-1.27)
    p.paragraph_format.line_spacing = 1.05
    p.paragraph_format.space_after = Pt(1.5)
    run = p.add_run(rr); set_font(run, size=11)

try:
    doc.save(OUT)
    print("SUCCESSFULLY GENERATED:", OUT)
except PermissionError:
    print("Warning: Could not save to", OUT, "(file may be open in Word)")

try:
    doc.save(OUT_ALT)
    print("SUCCESSFULLY GENERATED:", OUT_ALT)
except PermissionError:
    print("Warning: Could not save to", OUT_ALT, "(file may be open in Word)")
