import os
import re
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_run_font(run, font_name='Times New Roman', font_size_pt=13, color=None, bold=False, italic=False, subscript=False, superscript=False):
    run.font.name = font_name
    run.font.size = Pt(font_size_pt)
    run.bold = bold
    run.italic = italic
    if subscript:
        run.font.subscript = True
    if superscript:
        run.font.superscript = True
    if color:
        run.font.color.rgb = color
    # Ensure EastAsia & ComplexScript fonts are explicitly set in XML
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)
    rFonts.set(qn('w:eastAsia'), font_name)

def set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    # top/bottom/left/right in dxa (1 pt = 20 dxa)
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def set_table_grid(table, col_widths):
    tblGrid = parse_xml(f'<w:tblGrid {nsdecls("w")}/>')
    for w in col_widths:
        if hasattr(w, 'inches'):
            dxa_val = int(w.inches * 1440)
        else:
            dxa_val = int(float(w) * 1440)
        gridCol = parse_xml(f'<w:gridCol {nsdecls("w")} w:w="{dxa_val}"/>')
        tblGrid.append(gridCol)
    table._tbl.insert(table._tbl.index(table._tbl.tblPr) + 1, tblGrid)

def make_header_row(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def make_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def add_page_number(run):
    fldSimple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    run._r.append(fldSimple)

def render_math_expression(paragraph, expr_str, font_size_pt=13, color=None, bold=False, italic=False):
    s = expr_str.strip('$').strip()
    s = s.replace(r'\le', '≤').replace(r'\ge', '≥').replace(r'\alpha', 'α')
    s = s.replace(r'\theta', 'θ').replace(r'\cdot', '·').replace(r'\to', '→')
    s = s.replace(r'\Delta', 'Δ')
    s = re.sub(r'Δ\s+V', 'ΔV', s)
    s = s.replace(r'^\circ', '°').replace(r'^{\circ}', '°')
    s = re.sub(r'\\text\{\s*([^}]*)\}', r' \1', s)
    s = s.replace('{,}', ',')

    pattern = re.compile(r'([A-Za-zΔ])_\{([^{}]+)\}|([A-Za-zΔ])_([A-Za-z0-9]+)')
    last_idx = 0
    for match in pattern.finditer(s):
        start, end = match.span()
        if start > last_idx:
            r = paragraph.add_run(s[last_idx:start])
            set_run_font(r, font_size_pt=font_size_pt, color=color, bold=bold, italic=italic)
        var = match.group(1) or match.group(3)
        sub = match.group(2) or match.group(4)
        r_var = paragraph.add_run(var)
        set_run_font(r_var, font_size_pt=font_size_pt, color=color, bold=bold, italic=True)
        r_sub = paragraph.add_run(sub)
        set_run_font(r_sub, font_size_pt=font_size_pt, color=color, bold=bold, italic=False, subscript=True)
        last_idx = end

    if last_idx < len(s):
        r = paragraph.add_run(s[last_idx:])
        set_run_font(r, font_size_pt=font_size_pt, color=color, bold=bold, italic=italic)

def parse_inline_formatting(paragraph, text, default_font_size=13, default_color=None, bold_all=False, italic_all=False):
    pattern = re.compile(r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*|`.*?`|\$\$.*?\$\$|\$.*?\$|[^`\*\$]+)')
    tokens = pattern.findall(text)

    for token in tokens:
        if not token:
            continue

        if token.startswith('$$') and token.endswith('$$') and len(token) >= 4:
            render_math_expression(paragraph, token, font_size_pt=default_font_size, color=default_color, bold=bold_all)
            continue
        if token.startswith('$') and token.endswith('$') and len(token) >= 2:
            render_math_expression(paragraph, token, font_size_pt=default_font_size, color=default_color, bold=bold_all, italic=italic_all)
            continue
        if token.startswith('`') and token.endswith('`') and len(token) >= 2:
            r = paragraph.add_run(token[1:-1])
            set_run_font(r, font_name='Consolas', font_size_pt=default_font_size - 1.5, color=default_color, bold=bold_all, italic=False)
            continue

        cur_bold = bold_all
        cur_italic = italic_all
        content = token

        if token.startswith('***') and token.endswith('***') and len(token) >= 6:
            cur_bold = True
            cur_italic = True
            content = token[3:-3]
        elif token.startswith('**') and token.endswith('**') and len(token) >= 4:
            cur_bold = True
            content = token[2:-2]
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            cur_italic = True
            content = token[1:-1]

        if '$' in content:
            sub_parts = re.split(r'(\$.*?\$)', content)
            for sp in sub_parts:
                if not sp:
                    continue
                if sp.startswith('$') and sp.endswith('$'):
                    render_math_expression(paragraph, sp, font_size_pt=default_font_size, color=default_color, bold=cur_bold, italic=cur_italic)
                else:
                    r = paragraph.add_run(sp)
                    set_run_font(r, font_size_pt=default_font_size, color=default_color, bold=cur_bold, italic=cur_italic)
        else:
            r = paragraph.add_run(content)
            set_run_font(r, font_size_pt=default_font_size, color=default_color, bold=cur_bold, italic=cur_italic)

def ensure_composite_figures():
    """Build composite images for Figure 2 and Figure 7 if not already existing."""
    from PIL import Image

    # Figure 2 composite: Homunculus [5] + Somatic Nervous System [6]
    f2_out = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\hinh2_homunculus_scan_combined.png'
    p_im2 = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\image2.jpeg'
    p_im3 = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\image3.jpeg'
    if os.path.exists(p_im2) and os.path.exists(p_im3) and not os.path.exists(f2_out):
        im2 = Image.open(p_im2)
        im3 = Image.open(p_im3)
        h = 500
        w2 = int(im2.width * (h / im2.height))
        w3 = int(im3.width * (h / im3.height))
        im2_r = im2.resize((w2, h), Image.Resampling.LANCZOS)
        im3_r = im3.resize((w3, h), Image.Resampling.LANCZOS)
        spacing = 30
        comp = Image.new('RGB', (w2 + w3 + spacing, h), (255, 255, 255))
        comp.paste(im2_r, (0, 0))
        comp.paste(im3_r, (w2 + spacing, 0))
        comp.save(f2_out)
        print("Generated Figure 2 composite image.")

    # Figure 7 composite: Sandwich sensor structure + Dual-wall differential
    f7_out = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\hinh7_sandwich_visai_combined.png'
    p_im5 = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\image5.png'
    p_im6 = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\image6.png'
    if os.path.exists(p_im5) and os.path.exists(p_im6) and not os.path.exists(f7_out):
        im5 = Image.open(p_im5)
        im6 = Image.open(p_im6)
        h = 700
        w5 = int(im5.width * (h / im5.height))
        w6 = int(im6.width * (h / im6.height))
        im5_r = im5.resize((w5, h), Image.Resampling.LANCZOS)
        im6_r = im6.resize((w6, h), Image.Resampling.LANCZOS)
        spacing = 40
        comp = Image.new('RGB', (w5 + w6 + spacing, h), (255, 255, 255))
        if im5_r.mode == 'RGBA':
            comp.paste(im5_r, (0, 0), im5_r)
        else:
            comp.paste(im5_r, (0, 0))
        if im6_r.mode == 'RGBA':
            comp.paste(im6_r, (w5 + spacing, 0), im6_r)
        else:
            comp.paste(im6_r, (w5 + spacing, 0))
        comp.save(f7_out)
        print("Generated Figure 7 composite image.")

def build_docx(md_path, docx_path):
    print(f"Reading markdown from {md_path}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    ensure_composite_figures()

    doc = docx.Document()

    # Configure page setup (A4, standard VN academic margins: Left 30mm, Right 20mm, Top 20mm, Bottom 20mm)
    section = doc.sections[0]
    section.page_width = Inches(8.27)    # A4 210mm
    section.page_height = Inches(11.69)  # A4 297mm
    section.top_margin = Inches(0.79)    # 20mm
    section.bottom_margin = Inches(0.79) # 20mm
    section.left_margin = Inches(1.18)   # 30mm
    section.right_margin = Inches(0.79)  # 20mm

    # Configure Header & Footer
    section.different_first_page_header_footer = True

    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KỸ THUẬT — PHỤC HỒI CHỨC NĂNG BÀN TAY SAU ĐỘT QUỴ")
    set_run_font(hrun, font_size_pt=8.5, color=RGBColor(110, 110, 110), italic=True)

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("Trang ")
    set_run_font(frun, font_size_pt=9.5, color=RGBColor(100, 100, 100))
    add_page_number(frun)

    # 9 Figures matching Section A, B, C exactly
    figures_map = {
        1: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures\p1_ganh_nang_dot_quy.png',
            'caption': 'Hình 1: Tỉ lệ đột quỵ tại Việt Nam và di chứng bàn tay kéo dài [1, 2, 3]',
            'width': Inches(5.5)
        },
        2: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\hinh2_homunculus_scan_combined.png',
            'caption': 'Hình 2: Bản đồ Homunculus [5] và sự phân bổ chi phối bàn tay [6]',
            'width': Inches(5.0)
        },
        3: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures\d5_channel-1.png',
            'caption': 'Hình 3: Sơ đồ chức năng của bộ ba ngón trụ cột trong thao tác kẹp 3 chấu và bố trí các điểm cảm biến [12]',
            'width': Inches(4.2)
        },
        4: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures\hinh4_kien_truc_phan_tan_4_tang_bctt-1.png',
            'caption': 'Hình 4: Sơ đồ khối kiến trúc phân tán 3 nhóm của hệ thống găng tay phục hồi chức năng',
            'width': Inches(5.6)
        },
        5: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures\hinh5_so_do_nguyen_ly_bctt-1.png',
            'caption': 'Hình 5: Sơ đồ nguyên lý hoạt động (vòng phản hồi cơ học và thị giác đón trước Depth Anything V2)',
            'width': Inches(5.6)
        },
        6: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\image4.png',
            'caption': 'Hình 6: Khung nẹp ngàm xoay phương án 9 (khớp bản lề kép) và bố trí 3 tang',
            'width': Inches(4.2)
        },
        7: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\hinh7_sandwich_visai_combined.png',
            'caption': 'Hình 7: Cấu tạo mặt cắt cảm biến Sandwich và vi sai hai vách lòng - mu',
            'width': Inches(5.2)
        },
        8: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\extracted_images\image9.png',
            'caption': 'Hình 8: Quá trình tiến hóa và thử nghiệm 9 thế hệ cơ khí khóa nẹp in 3D (MECH 1 – MECH 9)',
            'width': Inches(5.2)
        },
        9: {
            'path': r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\de_cuong\figures\hinh9_dsp_pipeline_bctt-1.png',
            'caption': 'Hình 9: Chuỗi xử lý tín hiệu số (DSP) 4 bước trên mạch đọc trực tiếp ADS1115 ở Vòng lặp 2',
            'width': Inches(5.8)
        }
    }

    def insert_figure(fig_num, caption_text=None):
        if fig_num in figures_map:
            finfo = figures_map[fig_num]
            fpath = finfo['path']
            if os.path.exists(fpath):
                fp = doc.add_paragraph()
                fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                fp.paragraph_format.space_before = Pt(4)
                fp.paragraph_format.space_after = Pt(1)
                fp.paragraph_format.keep_with_next = True
                run = fp.add_run()
                run.add_picture(fpath, width=finfo['width'])

                # Caption
                cp = doc.add_paragraph()
                cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cp.paragraph_format.space_before = Pt(1)
                cp.paragraph_format.space_after = Pt(4)
                final_caption = caption_text if caption_text else finfo['caption']
                parse_inline_formatting(cp, final_caption, default_font_size=10.5, default_color=RGBColor(50, 50, 50), italic_all=True)

    def flush_table(tbl_lines):
        if not tbl_lines:
            return
        rows_data = []
        for line in tbl_lines:
            line_str = line.strip()
            if not line_str.startswith('|') or not line_str.endswith('|'):
                continue
            cells = [c.strip() for c in line_str.split('|')[1:-1]]
            if all(re.match(r'^:?-+:?$', c) for c in cells if c):
                continue
            rows_data.append(cells)
            
        if not rows_data:
            return

        num_cols = max(len(r) for r in rows_data)
        for r in rows_data:
            while len(r) < num_cols:
                r.append('')

        table = doc.add_table(rows=len(rows_data), cols=num_cols)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table, color="B0C4DE", sz="4", val="single")

        # Column widths for Table 1 (sum = 6.25 in)
        if num_cols == 4:
            col_widths = [Inches(1.05), Inches(2.25), Inches(1.25), Inches(1.70)]
        else:
            col_widths = [Inches(6.25 / num_cols)] * num_cols

        set_table_grid(table, col_widths)

        tbl_font_size = 10.0

        for r_idx, row_data in enumerate(rows_data):
            row = table.rows[r_idx]
            is_header = (r_idx == 0)
            if is_header:
                make_header_row(row)
            else:
                make_cant_split(row)

            for c_idx, cell_value in enumerate(row_data):
                cell = row.cells[c_idx]
                cell.width = col_widths[c_idx]
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                set_cell_margins(cell, top=70, bottom=70, left=110, right=110)

                if is_header:
                    set_cell_shading(cell, "1B365D") # Navy blue
                else:
                    if r_idx % 2 == 1:
                        set_cell_shading(cell, "F4F7FA") # Soft zebra
                    else:
                        set_cell_shading(cell, "FFFFFF")

                p = cell.paragraphs[0]
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                
                if is_header:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    parse_inline_formatting(p, cell_value, default_font_size=tbl_font_size, default_color=RGBColor(255, 255, 255), bold_all=True)
                else:
                    if c_idx == 0 or c_idx == 2 or len(cell_value) < 8 or re.match(r'^\d+(\s*-\s*\d+)?\s*(s|s)?$', cell_value):
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    else:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    parse_inline_formatting(p, cell_value, default_font_size=tbl_font_size, default_color=RGBColor(30, 30, 30))

        # Add space after table
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(4)

    # ================= PAGE 1: TITLE, METADATA & TABLE OF CONTENTS =================
    # Document Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(3)
    p_title.paragraph_format.keep_with_next = True
    parse_inline_formatting(p_title, "ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KĨ THUẬT", default_font_size=15, default_color=RGBColor(0, 32, 96), bold_all=True)

    # Project Name
    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_proj.paragraph_format.space_before = Pt(0)
    p_proj.paragraph_format.space_after = Pt(5)
    p_proj.paragraph_format.keep_with_next = True
    parse_inline_formatting(p_proj, "**Tên dự án:** Nghiên cứu và phát triển găng tay hỗ trợ phục hồi chức năng sau đột quỵ cho vận động tinh", default_font_size=11.5, default_color=RGBColor(25, 25, 25))

    # Metadata
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(0)
    p_meta.paragraph_format.space_after = Pt(4)
    p_meta.paragraph_format.line_spacing = 1.15
    p_meta.paragraph_format.keep_with_next = True
    parse_inline_formatting(p_meta, "Lĩnh vực: Hệ thống nhúng (Embedded Systems)  ·  Đơn vị: Trường THPT Quảng Trị\nHọc sinh thực hiện: Văn Ngọc Nhật Anh (11A2), Nguyễn Duy Quân (12A1)  ·  GVHD: Lê Công Long", default_font_size=9.5, default_color=RGBColor(80, 80, 80), italic_all=True)

    # Decorative rule
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_before = Pt(0)
    p_div.paragraph_format.space_after = Pt(4)
    p_div.paragraph_format.keep_with_next = True
    r_div = p_div.add_run("—" * 28)
    set_run_font(r_div, font_size_pt=8.5, color=RGBColor(180, 180, 180))

    # MỤC LỤC Title
    p_toc_head = doc.add_paragraph()
    p_toc_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_head.paragraph_format.space_before = Pt(3)
    p_toc_head.paragraph_format.space_after = Pt(4)
    p_toc_head.paragraph_format.keep_with_next = True
    parse_inline_formatting(p_toc_head, "MỤC LỤC", default_font_size=12, default_color=RGBColor(0, 32, 96), bold_all=True)

    # TOC hierarchical entries with page numbers and dot leaders
    toc_items = [
        ("A. VẤN ĐỀ NGHIÊN CỨU", 1, "Trang 2"),
        ("1. Lí do chọn đề tài", 2, "Trang 2"),
        ("2. Cơ sở lý thuyết y sinh (Đại diện Hebbian, GAP & độ tin cậy)", 2, "Trang 2"),
        ("3. Xác định vấn đề nghiên cứu", 2, "Trang 3"),
        ("4. Mục tiêu nghiên cứu", 2, "Trang 3"),
        ("5. Tiêu chí của dự án", 2, "Trang 4"),
        ("B. GIẢI PHÁP VÀ THIẾT KẾ", 1, "Trang 4"),
        ("I. Tổng quan đề tài", 2, "Trang 4"),
        ("II. Bất cập, giới hạn giải pháp hiện tại và giải pháp đề tài", 2, "Trang 5"),
        ("III. Nguyên lý và cơ chế hoạt động của hệ thống", 2, "Trang 5"),
        ("3.1. Sơ đồ khối kết nối phân tán 3 nhóm hệ thống", 3, "Trang 5"),
        ("3.2. Sơ đồ nguyên lý hoạt động", 3, "Trang 6"),
        ("Nhóm 1: Cơ khí nẹp đeo, cảm biến tiếp xúc và cơ cấu trợ lực", 3, "Trang 6"),
        ("Nhóm 2: Mạch thu nhận đa kênh, xử lý DSP và điều khiển AAN", 3, "Trang 7"),
        ("Nhóm 3: Thị giác không gian 3D Depth Anything V2 và lượng hóa tác vụ", 3, "Trang 9"),
        ("C. KẾ HOẠCH CHẾ TẠO VÀ PHƯƠNG PHÁP THỬ NGHIỆM", 1, "Trang 10"),
        ("Nhóm 1: Chế tạo cơ khí nẹp đeo, bố trí cảm biến và kiểm thử cơ cấu trợ lực", 2, "Trang 10"),
        ("Nhóm 2: Chế tạo mạch thu nhận, lập trình DSP và kiểm thử điều khiển AAN", 2, "Trang 11"),
        ("Nhóm 3: Triển khai thị giác không gian Depth Anything V2 và tích hợp toàn hệ thống", 2, "Trang 12"),
        ("TÀI LIỆU THAM KHẢO", 1, "Trang 13")
    ]

    for item_text, level, page_str in toc_items:
        ptoc = doc.add_paragraph()
        ptoc.paragraph_format.line_spacing = 1.05
        ptoc.paragraph_format.keep_with_next = True
        ptoc.paragraph_format.tab_stops.add_tab_stop(Inches(6.30), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        if level == 1:
            ptoc.paragraph_format.space_before = Pt(3.0)
            ptoc.paragraph_format.space_after = Pt(0.5)
            ptoc.paragraph_format.left_indent = Inches(0)
            parse_inline_formatting(ptoc, item_text, default_font_size=9.5, default_color=RGBColor(0, 32, 96), bold_all=True)
            ptoc.add_run('\t')
            r_page = ptoc.add_run(page_str)
            set_run_font(r_page, font_size_pt=9.0, color=RGBColor(0, 32, 96), bold=True)
        elif level == 2:
            ptoc.paragraph_format.space_before = Pt(0.5)
            ptoc.paragraph_format.space_after = Pt(0.5)
            ptoc.paragraph_format.left_indent = Inches(0.18)
            parse_inline_formatting(ptoc, item_text, default_font_size=9.0, default_color=RGBColor(30, 30, 30))
            ptoc.add_run('\t')
            r_page = ptoc.add_run(page_str)
            set_run_font(r_page, font_size_pt=8.5, color=RGBColor(70, 70, 70))
        elif level == 3:
            ptoc.paragraph_format.space_before = Pt(0.2)
            ptoc.paragraph_format.space_after = Pt(0.2)
            ptoc.paragraph_format.left_indent = Inches(0.36)
            parse_inline_formatting(ptoc, item_text, default_font_size=8.5, default_color=RGBColor(70, 70, 70), italic_all=True)
            ptoc.add_run('\t')
            r_page = ptoc.add_run(page_str)
            set_run_font(r_page, font_size_pt=8.0, color=RGBColor(100, 100, 100), italic=True)

    # ================= PARSE BODY LINES =================
    lines = md_text.split('\n')
    i = 0
    n = len(lines)

    table_lines = []
    inserted_figs = set()
    first_section_a = True

    while i < n:
        raw_line = lines[i]
        line = raw_line.strip()

        # Check if table row
        if line.startswith('|') and line.endswith('|'):
            table_lines.append(line)
            i += 1
            continue
        else:
            if table_lines:
                flush_table(table_lines)
                table_lines = []

        if not line:
            i += 1
            continue

        # Skip raw header/title/divider in markdown since Page 1 Cover & TOC handled it
        if line == '**ĐỀ CƯƠNG DỰ ÁN KHOA HỌC KĨ THUẬT**' or line.startswith('**Tên dự án:'):
            i += 1
            continue
        if line == '---':
            i += 1
            continue

        # Level 1 Major Heading: **A. ...**, **B. ...**, **C. ...**, **TÀI LIỆU THAM KHẢO**
        # or markdown ## A. ...
        m_l1 = re.match(r'^(?:##\s+|\*\*)?([A-C]\.\s+.*|TÀI LIỆU THAM KHẢO.*)(?:\*\*)?$', line)
        if m_l1 and not re.match(r'^\d', m_l1.group(1)):
            h_text = m_l1.group(1).strip()
            p = doc.add_paragraph()
            # Clean page breaks: Section A on Page 2, Section C on Page 11 (keeps Fig 8 + Table 1 together), References on Page 13
            if (first_section_a and h_text.startswith('A.')) or h_text.startswith('C.') or h_text.startswith('TÀI LIỆU'):
                p.paragraph_format.page_break_before = True
                if h_text.startswith('A.'):
                    first_section_a = False
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            parse_inline_formatting(p, h_text, default_font_size=14, default_color=RGBColor(0, 32, 96), bold_all=True)
            i += 1
            continue

        # Group Heading: ### Nhóm 1: ..., ### Nhóm 2: ..., ### Nhóm 3: ...
        m_group = re.match(r'^(?:###\s+)?(Nhóm\s+[1-3]:\s+.*)$', line)
        if m_group:
            h_text = m_group.group(1).strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            parse_inline_formatting(p, h_text, default_font_size=13, default_color=RGBColor(15, 60, 120), bold_all=True)
            i += 1
            continue

        # Level 4 Sub-sub-sub Heading: #### 3.2.1. ... or #### 1. ... or **3.2.1. ...**
        m_l4 = re.match(r'^(?:####\s+|\*\*)?(\d+\.\d+\.\d+\.\s+.*|\d+\.\s+[A-ZÀ-Ỹ].*)(?:\*\*)?$', line)
        if m_l4 and not line.startswith('1. Lí do') and not line.startswith('2. Mục tiêu') and not line.startswith('3. Phương pháp') and not line.startswith('4. Kế hoạch') and not line.startswith('5. Đóng góp') and not line.startswith('6. Dự kiến') and not line.startswith('7. Kinh phí'):
            h_text = m_l4.group(1).strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            parse_inline_formatting(p, h_text, default_font_size=12, default_color=RGBColor(45, 45, 45), bold_all=True)
            i += 1
            continue

        # Level 3 Sub-sub Heading: **2.1. ...**, **3.1. ...**
        m_l3 = re.match(r'^(?:\*\*)?(\d+\.\d+\.\s+.*)(?:\*\*)?$', line)
        if m_l3:
            h_text = m_l3.group(1).strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            parse_inline_formatting(p, h_text, default_font_size=12.5, default_color=RGBColor(35, 35, 35), bold_all=True)
            i += 1
            continue

        # Level 2 Sub Heading: **1. Lí do...**, **I. Tổng quan...**
        m_l2 = re.match(r'^(?:\*\*)?((?:\d+|[IVXLCDM]+)\.\s+.*)(?:\*\*)?$', line)
        if m_l2:
            h_text = m_l2.group(1).strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            parse_inline_formatting(p, h_text, default_font_size=13, default_color=RGBColor(31, 78, 121), bold_all=True)
            i += 1
            continue

        # Figure placeholder line: Hình X. ...
        m_fig = re.match(r'^\*?[Hh]ình\s+([1-9])[\.:\s]*(.*)\*?$', line.strip())
        if m_fig:
            fnum = int(m_fig.group(1))
            caption_rest = m_fig.group(2).strip().rstrip('*').strip()
            if caption_rest:
                caption_to_use = f"Hình {fnum}: {caption_rest}"
            else:
                caption_to_use = figures_map.get(fnum, {}).get('caption', f"Hình {fnum}")
            if fnum not in inserted_figs:
                insert_figure(fnum, caption_to_use)
                inserted_figs.add(fnum)
            i += 1
            continue

        # Table caption line: Bảng 1. ...
        m_tbl_cap = re.match(r'^\*?[Bb]ảng\s+(\d+)[\.:\s]*(.*)\*?$', line.strip())
        if m_tbl_cap:
            tnum = m_tbl_cap.group(1)
            trest = m_tbl_cap.group(2).strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            parse_inline_formatting(p, f"Bảng {tnum}: {trest}", default_font_size=10.5, default_color=RGBColor(31, 78, 121), italic_all=True, bold_all=True)
            i += 1
            continue

        # Academic Reference Item: [1] ...
        m_ref = re.match(r'^\[(\d+)\]\s+(.*)$', line)
        if m_ref:
            ref_num = m_ref.group(1)
            ref_body = m_ref.group(2).strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.first_line_indent = Inches(-0.4)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            
            r_num = p.add_run(f"[{ref_num}] ")
            set_run_font(r_num, font_size_pt=11.5, color=RGBColor(31, 78, 121), bold=True)
            parse_inline_formatting(p, ref_body, default_font_size=11.5, default_color=RGBColor(30, 30, 30))
            i += 1
            continue

        # Bullet list item: - ... or * ...
        if line.startswith('- ') or line.startswith('* '):
            list_text = line[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(0.5)
            p.paragraph_format.space_after = Pt(1.5)
            p.paragraph_format.line_spacing = 1.18
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

            is_sub_bullet = raw_line.startswith('   ') or raw_line.startswith('\t') or raw_line.startswith('  ')
            if is_sub_bullet:
                p.paragraph_format.left_indent = Inches(0.65)
                p.paragraph_format.first_line_indent = Inches(-0.2)
                bullet_run = p.add_run("– ")
                set_run_font(bullet_run, font_size_pt=12, color=RGBColor(80, 80, 80))
            else:
                p.paragraph_format.left_indent = Inches(0.4)
                p.paragraph_format.first_line_indent = Inches(-0.2)
                bullet_run = p.add_run("• ")
                set_run_font(bullet_run, font_size_pt=12, color=RGBColor(31, 78, 121))

            parse_inline_formatting(p, list_text, default_font_size=12.5)
            i += 1
            continue

        # Numbered list item: 1. ...
        m_num = re.match(r'^(\d+)\.\s+(.*)$', line)
        if m_num:
            num_str = m_num.group(1)
            item_text = m_num.group(2)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.first_line_indent = Inches(-0.25)
            p.paragraph_format.space_before = Pt(0.5)
            p.paragraph_format.space_after = Pt(2.0)
            p.paragraph_format.line_spacing = 1.18
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

            num_run = p.add_run(f"{num_str}. ")
            set_run_font(num_run, font_size_pt=12.5, color=RGBColor(31, 78, 121), bold=True)

            parse_inline_formatting(p, item_text, default_font_size=12.5)
            i += 1
            continue

        # Regular Body Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.22
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3.5)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # Indent body paragraphs by 1 cm (~0.4 in), skip for formulas or centered notes
        is_centered = line.startswith('$$') or line.startswith('*Phiên bản')
        if not is_centered:
            p.paragraph_format.first_line_indent = Inches(0.4)

        parse_inline_formatting(p, line, default_font_size=13, default_color=RGBColor(20, 20, 20))
        i += 1

    if table_lines:
        flush_table(table_lines)

    # Save to primary destination
    print(f"Saving generated document to {docx_path}...")
    doc.save(docx_path)
    print("Primary docx save successful!")

def docx_to_pdf(docx_path, pdf_path):
    import win32com.client
    import pythoncom
    
    pythoncom.CoInitialize()
    abs_docx = os.path.abspath(docx_path)
    abs_pdf = os.path.abspath(pdf_path)
    
    print(f"Converting {abs_docx} -> {abs_pdf} via Word COM...")
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(abs_docx, ReadOnly=True)
        # 17 = wdExportFormatPDF
        doc.ExportAsFixedFormat(
            OutputFileName=abs_pdf,
            ExportFormat=17,
            OpenAfterExport=False,
            OptimizeFor=0,    # wdExportOptimizeForPrint
            CreateBookmarks=1 # wdExportCreateWordBookmarks
        )
        page_count = doc.ComputeStatistics(2) # 2 = wdStatisticPages
        print(f"Word reports total pages: {page_count}")
        doc.Close(SaveChanges=False)
        print("Export to PDF successful!")
        return page_count
    finally:
        word.Quit()
        pythoncom.CoUninitialize()

if __name__ == '__main__':
    src_md = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\DE_CUONG_NOP_TRUONG.md'
    out_docx1 = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\DE_CUONG_NOP_TRUONG.docx'
    out_docx2 = r'C:\Users\user\Downloads\DE_CUONG_NOP_TRUONG.docx'
    out_pdf1 = r'D:\Desktop\AI Agent\smart-glove-hand-function-monitoring\docs\DE_CUONG_NOP_TRUONG.pdf'
    out_pdf2 = r'C:\Users\user\Downloads\DE_CUONG_NOP_TRUONG.pdf'

    build_docx(src_md, out_docx1)

    print(f"Copying docx to {out_docx2}...")
    try:
        shutil.copyfile(out_docx1, out_docx2)
        print(f"Copied docx to {out_docx2}")
    except Exception as e:
        print(f"Notice: Could not copy to {out_docx2} (file may be open in Word): {e}")

    total_pages = docx_to_pdf(out_docx1, out_pdf1)

    print(f"Copying pdf to {out_pdf2}...")
    try:
        shutil.copyfile(out_pdf1, out_pdf2)
        print(f"Copied pdf to {out_pdf2}")
    except Exception as e:
        print(f"Notice: Could not copy to {out_pdf2}: {e}")
    print(f"All tasks completed successfully! Total PDF pages: {total_pages}")
