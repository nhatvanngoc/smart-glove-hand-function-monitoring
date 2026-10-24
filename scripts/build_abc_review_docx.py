#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dựng bản Word (.docx) ĐỂ RÀ SOÁT từ đề cương Markdown A/B/C.

  python3 scripts/build_abc_review_docx.py [input.md] [output.docx]
  python3 scripts/build_abc_review_docx.py input.md output.docx --no-meta --check

Bản sạch để biên tập/nộp: --no-meta bỏ toàn bộ bảng thông tin dựng và banner.
Nếu nguồn có bìa + "## MỤC LỤC", script tách bìa, mục lục, nội dung thành trang
riêng; --cover-version=YYYY-MM-DD đặt một dòng nhỏ ở chân trang bìa.
--size=13 --spacing=1.15 đổi cỡ chữ thật của cả nội dung và bảng, không chỉ style.
Mục lục lấy nguyên đề mục trong nguồn, không tự gán số trang chưa được dàn.

Mặc định:
  input  = docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md
  output = exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx

Định dạng bám theo quy ước đã dùng trong `de_cuong/build_docx.py` của repo:
  - Times New Roman 14, khổ A4, lề VN 3/2/2/2 cm, giãn dòng 1.35;
  - Heading 1/2/3 đều 14 pt in đậm (Heading 3 in đậm nghiêng);
  - bảng dùng style `Table Grid`, dòng tiêu đề in đậm;
  - liên kết nội bộ repo được render thành "chữ (đường dẫn)" dạng chữ thường,
    KHÔNG tạo hyperlink, để bản Word không chứa liên kết gãy.

Ranh giới trung thực (không được bỏ khi sửa script này):
  - Script CHỈ chuyển đổi nội dung Markdown đã có; nó KHÔNG sinh thêm số liệu,
    KHÔNG tự điền ngưỡng và KHÔNG đổi trạng thái duyệt của tài liệu.
  - Mặc định output là BẢN RÀ SOÁT; --no-meta chỉ đổi trình bày, không tự duyệt nội dung.
  - Không ghi đè `11A2.docx` / `11A2.pdf` / `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx`
    trên Google Drive.

Phụ thuộc: python-docx (không nằm trong requirements.txt vì đó là file cho mô phỏng/đồ thị).
  Cài:  pip install python-docx
"""
import os
import re
import sys
import datetime

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_IN = os.path.join(REPO, "docs", "DE_CUONG_A_B_C_DRAFT_2026-10-19.md")
DEFAULT_OUT = os.path.join(REPO, "exports", "11A2_CAP_NHAT_DU_THAO_2026-10-20.docx")

FONT = "Times New Roman"
SIZE = 14


# --------------------------------------------------------------------------- #
# helper định dạng
# --------------------------------------------------------------------------- #
def set_font(obj, name=FONT, size=None, bold=None, italic=None,
             color=None, strike=None, underline=None):
    """Đặt font cho một style hoặc một run, kể cả font phức (cs/eastAsia)."""
    f = obj.font
    f.name = name
    rpr = f.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), name)
    if size is not None:
        f.size = Pt(size)
    if bold is not None:
        f.bold = bold
    if italic is not None:
        f.italic = italic
    if underline is not None:
        f.underline = underline
    if strike is not None:
        f.strike = strike
    if color is not None:
        f.color.rgb = RGBColor(*color)
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr.append(lang)
    lang.set(qn("w:val"), "vi-VN")
    lang.set(qn("w:eastAsia"), "vi-VN")


def add_page_number_footer(section):
    footer = section.footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    set_font(run, size=12)
    fld1, instr, fld2 = OxmlElement("w:fldChar"), OxmlElement("w:instrText"), OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1)
    run._r.append(instr)
    run._r.append(fld2)


# --------------------------------------------------------------------------- #
# inline markdown -> runs
# --------------------------------------------------------------------------- #
INLINE = re.compile(
    r"(\*\*.+?\*\*"          # bold
    r"|~~.+?~~"              # strike
    r"|`[^`]+`"              # code
    r"|\[[^\]]*\]\([^)]*\)"  # link
    r"|\*[^*\n]+\*)"         # italic
)


def norm_target(target):
    """Bỏ '../' để đường dẫn repo đọc được trong bản Word."""
    t = target.strip()
    while t.startswith("../"):
        t = t[3:]
    return t


def _label_is_path(label, target):
    """True nếu nhãn liên kết ĐÃ LÀ đường dẫn/tên tệp -> không lặp lại trong ngoặc."""
    lab = re.sub(r"[`*_]", "", label).strip()
    tgt = norm_target(target)
    base = tgt.rsplit("/", 1)[-1]
    if not lab:
        return False
    if lab == tgt or lab == target:
        return True
    if lab.endswith(base) or lab.rsplit("/", 1)[-1] == base:
        return True
    return False


def emit_inline(par, text, base_bold=False, base_italic=False, size=SIZE):
    """Chuyển một đoạn markdown inline thành các run của paragraph `par`."""
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            emit_inline(par, part[2:-2], True, base_italic, size)
        elif part.startswith("~~") and part.endswith("~~") and len(part) > 4:
            r = par.add_run()
            emit_plain(r, part[2:-2])
            set_font(r, size=size, bold=base_bold or None, italic=base_italic or None, strike=True)
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            r = par.add_run()
            emit_plain(r, part[1:-1])
            set_font(r, size=size, bold=base_bold or None, italic=base_italic or None)
            r.font.name = "Consolas"
        elif part.startswith("[") and "](" in part and part.endswith(")"):
            # part = "[nhan](target)" ; part[1:-1] da bo "[" va ")" nen KHONG cat them
            label, target = part[1:-1].split("](", 1)
            emit_inline(par, label, base_bold, base_italic, size)
            if target and not target.startswith("#") and not _label_is_path(label, target):
                r = par.add_run(" (%s)" % norm_target(target))
                set_font(r, size=size - 2, italic=True, color=(0x44, 0x44, 0x44))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            emit_inline(par, part[1:-1], base_bold, True, size)
        else:
            r = par.add_run()
            emit_plain(r, part)
            set_font(r, size=size, bold=base_bold or None, italic=base_italic or None)


def emit_plain(run, text):
    run.text = text.replace("\\*", "*").replace("\\_", "_").replace("\\|", "|")


# --------------------------------------------------------------------------- #
# block markdown -> document
# --------------------------------------------------------------------------- #
def is_table_row(line):
    return line.lstrip().startswith("|") and line.rstrip().endswith("|")


def split_row(line):
    body = line.strip().strip("|")
    cells, cur, depth = [], "", 0
    for ch in body:
        if ch == "`":
            depth ^= 1
        if ch == "|" and not depth:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def is_sep_row(cells):
    return all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c != "")


def add_table(doc, block, size=SIZE):
    rows = [split_row(l) for l in block]
    rows = [r for r in rows if not is_sep_row(r)]
    if not rows:
        return
    ncol = max(len(r) for r in rows)
    table = doc.add_table(rows=0, cols=ncol)
    table.style = "Table Grid"
    for ri, cells in enumerate(rows):
        row = table.add_row()
        props = row._tr.get_or_add_trPr()
        props.append(OxmlElement("w:cantSplit"))
        if ri == 0:
            props.append(OxmlElement("w:tblHeader"))
        for ci in range(ncol):
            cell = row.cells[ci]
            par = cell.paragraphs[0]
            par.paragraph_format.line_spacing = 1.15
            par.paragraph_format.space_after = Pt(1)
            txt = cells[ci] if ci < len(cells) else ""
            if ri == 0:
                emit_inline(par, txt, base_bold=True, size=size - 2)
            else:
                emit_inline(par, txt, size=size - 2)
            for run in par.runs:
                set_font(run, size=size - 2, bold=(True if ri == 0 else run.bold),
                         italic=run.italic)
    doc.add_paragraph()


def build(md_path, out_path, extra_meta=None,
          banner="BẢN RÀ SOÁT — KHÔNG PHẢI BẢN NỘP",
          status="bản làm việc để rà soát; chưa được duyệt toàn văn",
          spacing=1.35, size=None, no_meta=False, cover_version=None):
    with open(md_path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    font_size = SIZE if size is None else size
    if font_size < 8 or spacing <= 0:
        raise ValueError("Cỡ chữ phải >= 8 pt và giãn dòng phải dương")
    if cover_version is not None:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cover_version):
            raise ValueError("Phiên bản bìa phải có dạng YYYY-MM-DD")
        datetime.date.fromisoformat(cover_version)
    report_layout = no_meta and "## MỤC LỤC" in lines
    if cover_version is not None and not report_layout:
        raise ValueError("--cover-version cần --no-meta và nguồn có mục lục")

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(2), Cm(2)
    sec.left_margin, sec.right_margin = Cm(3), Cm(2)

    st = doc.styles["Normal"]
    set_font(st, size=font_size)
    st.paragraph_format.line_spacing = spacing
    st.paragraph_format.space_after = Pt(3)
    st.paragraph_format.space_before = Pt(0)

    for hname, bold, italic, before in (("Heading 1", True, False, 10),
                                        ("Heading 2", True, False, 7),
                                        ("Heading 3", True, True, 5)):
        hs = doc.styles[hname]
        set_font(hs, size=font_size, bold=bold, italic=italic, color=(0, 0, 0))
        hs.paragraph_format.space_before = Pt(before)
        hs.paragraph_format.space_after = Pt(3)
        hs.paragraph_format.line_spacing = spacing
        hs.paragraph_format.keep_with_next = True

    add_page_number_footer(sec)
    if report_layout:
        sec.different_first_page_header_footer = True
        if cover_version:
            footer = sec.first_page_footer.paragraphs[0]
            footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_font(footer.add_run("Phiên bản: " + cover_version), size=10)

    if not no_meta:
        # ---- khối thông tin bản dựng (metadata, không phải nội dung đề cương) ----
        meta = doc.add_paragraph()
        meta.paragraph_format.space_after = Pt(6)
        r = meta.add_run(banner)
        set_font(r, size=font_size, bold=True, color=(0x99, 0x00, 0x00))

        try:
            src_rel = os.path.relpath(md_path, REPO).replace(os.sep, "/")
        except ValueError:
            src_rel = os.path.abspath(md_path).replace(os.sep, "/")
        try:
            out_rel = os.path.relpath(out_path, REPO).replace(os.sep, "/")
        except ValueError:
            out_rel = os.path.abspath(out_path).replace(os.sep, "/")
        # ngày theo giờ Việt Nam (UTC+7); máy dựng có thể đang ở múi giờ khác
        stamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).date().isoformat()
        meta_rows = [
            ("Nguồn Markdown", src_rel),
            ("Ngày dựng", stamp),
            ("Script", "scripts/build_abc_review_docx.py"),
            ("Tệp ra", out_rel),
            ("Trạng thái nội dung", status),
        ]
        if extra_meta:
            meta_rows.extend(extra_meta)
        mt = doc.add_table(rows=0, cols=2)
        mt.style = "Table Grid"
        for k, v in meta_rows:
            row = mt.add_row()
            for cell, txt, bold in ((row.cells[0], k, True), (row.cells[1], v, False)):
                par = cell.paragraphs[0]
                par.paragraph_format.line_spacing = 1.15
                par.paragraph_format.space_after = Pt(1)
                run = par.add_run(txt)
                set_font(run, size=font_size - 2, bold=bold or None)
        row = mt.add_row()
        par = row.cells[0].paragraphs[0]
        run = par.add_run("Quy tắc bằng chứng")
        set_font(run, size=font_size - 2, bold=True)
        par = row.cells[1].paragraphs[0]
        par.paragraph_format.line_spacing = 1.15
        run = par.add_run('Mọi ô số ghi "OPEN" là để trống có chủ đích. Không có ngưỡng, kích thước, '
                          "thời gian hay số đo nào được script này sinh ra. Chức năng mô tả là mục tiêu "
                          "thiết kế, không phải kết quả đã chế tạo hoặc đã đạt.")
        set_font(run, size=font_size - 2)
        doc.add_paragraph()

    # ---- thân tài liệu ----
    in_cover = report_layout
    in_toc = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            i += 1
            continue

        if is_table_row(line):
            block = []
            while i < n and is_table_row(lines[i]):
                block.append(lines[i])
                i += 1
            add_table(doc, block, size=font_size)
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level, text = len(m.group(1)), m.group(2)
            toc_heading = report_layout and text == "MỤC LỤC"
            after_toc = in_toc and level == 2 and not toc_heading
            if toc_heading:
                in_cover = False
                in_toc = True
            elif after_toc:
                in_toc = False
            if level == 1:
                p = doc.add_paragraph(style="Heading 1")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                emit_inline(p, text, base_bold=True, size=font_size)
                for run in p.runs:
                    set_font(run, size=font_size + 1, bold=True, color=(0, 0, 0))
            else:
                p = doc.add_paragraph(style="Heading %d" % min(level - 1, 3))
                emit_inline(p, text, base_bold=True, size=font_size)
                for run in p.runs:
                    set_font(run, size=font_size, bold=True,
                             italic=(True if level >= 4 else False), color=(0, 0, 0))
            if report_layout:
                if level == 1 and in_cover:
                    p.paragraph_format.space_before = Pt(85)
                    p.paragraph_format.space_after = Pt(28)
                if toc_heading:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                if toc_heading or after_toc or text.startswith("PHỤ LỤC"):
                    p.paragraph_format.page_break_before = True
            i += 1
            continue

        if stripped.startswith(">"):
            # mỗi dòng trích dẫn là một ghi chú có nhãn riêng -> một đoạn riêng
            while i < n and lines[i].strip().startswith(">"):
                text = re.sub(r"^\s*>\s?", "", lines[i]).strip()
                i += 1
                if not text:
                    continue
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.6)
                p.paragraph_format.line_spacing = 1.25
                p.paragraph_format.space_after = Pt(4)
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                emit_inline(p, text, size=font_size)
                for run in p.runs:
                    set_font(run, size=font_size - 1, bold=run.bold, italic=run.italic,
                             color=(0x33, 0x33, 0x33))
            continue

        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if m:
            indent, marker, text = m.group(1), m.group(2), m.group(3)
            ordered = marker[0].isdigit()
            # giữ nguyên số/dấu đầu dòng của Markdown (không dùng style tự đánh số,
            # vì đánh số tự động có thể tiếp nối danh sách trước đó và hiển thị sai)
            p = doc.add_paragraph()
            depth = len(indent) // 2
            bullet = marker if ordered else "\u2013"
            p.paragraph_format.left_indent = Cm(0.75 + 0.6 * depth)
            p.paragraph_format.first_line_indent = Cm(-0.65 if ordered else -0.45)
            p.paragraph_format.line_spacing = min(spacing, 1.3)
            p.paragraph_format.space_after = Pt(2)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r = p.add_run(bullet + (" " if ordered else "\u2002"))
            set_font(r, size=font_size)
            emit_inline(p, text, size=font_size)
            if in_toc:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = Pt(0)
                for run in p.runs:
                    set_font(run, size=12)
            i += 1
            continue

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        emit_inline(p, stripped, size=font_size)
        if in_cover:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(24)
        elif in_toc:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(0)
            for run in p.runs:
                set_font(run, size=12)
        i += 1

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    doc.save(out_path)
    return out_path


def verify(docx_path, md_path, no_meta=False):
    """Kiểm tra bản dựng: không sót cú pháp Markdown, không cắt nhầm đường dẫn,
    bảng đăng ký trước chỉ số giữ đủ số dòng/cột, metadata ngày hợp lệ."""
    d = Document(docx_path)
    paras = [p.text for p in d.paragraphs]
    cells = [c.text for t in d.tables for r in t.rows for c in r.cells]
    alltext = "\n".join(paras + cells)
    fails = []

    for pat, why in ((r"\*\*", "bold Markdown chưa được render"),
                     (r"(?<![\w])`", "code span chưa được render"),
                     (r"\]\(", "liên kết Markdown chưa được render"),
                     (r"~~", "gạch ngang Markdown chưa được render"),
                     (r"\.m\)", "đường dẫn .md bị cắt mất ký tự cuối")):
        hits = re.findall(pat, alltext)
        if hits:
            fails.append("%s: %d lần (%s)" % (pat, len(hits), why))

    if len(d.tables) < 2:
        fails.append("thiếu bảng (chỉ thấy %d)" % len(d.tables))
    else:
        # bảng đăng ký trước chỉ số: nhận diện theo tiêu đề, không theo kích thước,
        # vì bản cô đọng (2026-10-20) gộp một số chỉ số nên số cột/dòng thay đổi.
        prereg = [t for t in d.tables
                  if "Chỉ số" in t.rows[0].cells[0].text
                  and any("Mục tiêu" in c.text for c in t.rows[0].cells)]
        if not prereg:
            fails.append("không tìm thấy bảng đăng ký trước chỉ số (dòng đầu phải có 'Chỉ số' và một cột 'Mục tiêu…')")
        else:
            t = max(prereg, key=lambda x: len(x.rows))
            head = " | ".join(c.text for c in t.rows[0].cells)
            for col in ("Cách đo", "Mục tiêu", "Căn cứ"):
                if col not in head:
                    fails.append("bảng đăng ký trước thiếu cột '%s' (thấy: %s)" % (col, head))
            if len(t.rows) < 10:
                fails.append("bảng đăng ký trước phải có >= 10 dòng (1 tiêu đề + >= 9 chỉ số), thấy %d"
                             % len(t.rows))

    ngay = "không chèn metadata"
    metadata = [t for t in d.tables if t.rows and t.rows[0].cells[0].text == "Nguồn Markdown"]
    if metadata:
        if len(metadata[0].rows) < 2 or len(metadata[0].rows[1].cells) < 2:
            fails.append("bảng metadata thiếu ngày dựng")
        else:
            ngay = metadata[0].rows[1].cells[1].text.strip()
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ngay):
                fails.append("ngày dựng không hợp lệ: %r" % ngay)
    if no_meta:
        for marker in ("Nguồn Markdown", "Ngày dựng", "Script", "Tệp ra",
                       "Quy tắc bằng chứng", "Trạng thái nội dung",
                       "BẢN RÀ SOÁT — KHÔNG PHẢI BẢN NỘP"):
            if marker in alltext:
                fails.append("bản sạch còn thông tin vận hành: " + marker)

    if len(alltext.split()) < 1000:
        fails.append("bản dựng quá ngắn (%d từ) — có thể thiếu nội dung" % len(alltext.split()))

    # mọi đề mục A/B/C của nguồn phải xuất hiện trong bản dựng
    with open(md_path, encoding="utf-8") as f:
        src = f.read()
    for m in re.finditer(r"^##\s+(.+)$", src, re.M):
        head = re.sub(r"[*`]", "", m.group(1)).strip()
        if head and head not in alltext:
            fails.append("thiếu đề mục: %s" % head)

    return fails, {"paragraphs": len(paras), "tables": len(d.tables),
                   "words": len(alltext.split()), "ngay_dung": ngay}


def _flag(argv, name, default=None):
    pre = "--%s=" % name
    for a in argv:
        if a.startswith(pre):
            return a[len(pre):]
    return default


def main(argv):
    pos = [a for a in argv[1:] if not a.startswith("--")]
    md = os.path.abspath(pos[0]) if len(pos) > 0 else DEFAULT_IN
    out = os.path.abspath(pos[1]) if len(pos) > 1 else DEFAULT_OUT
    kw = {}
    if _flag(argv, "banner") is not None:
        kw["banner"] = _flag(argv, "banner")
    if _flag(argv, "status") is not None:
        kw["status"] = _flag(argv, "status")
    if _flag(argv, "spacing") is not None:
        kw["spacing"] = float(_flag(argv, "spacing"))
    if _flag(argv, "size") is not None:
        kw["size"] = int(_flag(argv, "size"))
    extra = _flag(argv, "meta")
    if extra:
        kw["extra_meta"] = [tuple(x.split("=", 1)) for x in extra.split(";") if "=" in x]
    if "--no-meta" in argv:
        kw["no_meta"] = True
    if _flag(argv, "cover-version") is not None:
        kw["cover_version"] = _flag(argv, "cover-version")
    if "--check" in argv:
        build(md, out, **kw)
        fails, info = verify(out, md, no_meta=kw.get("no_meta", False))
        print("File : %s" % out)
        for k, v in sorted(info.items()):
            print("  %-11s %s" % (k + ":", v))
        if fails:
            print("FAIL (%d):" % len(fails))
            for f in fails:
                print("  - " + f)
            sys.exit(1)
        print("PASS: khong sot cu phap Markdown, duong dan khong bi cat, du bang va de muc.")
        return
    if not os.path.exists(md):
        sys.exit("KHONG TIM THAY nguon: %s" % md)
    build(md, out, **kw)
    print("Da dung: %s" % out)
    print("Nguon : %s" % md)


if __name__ == "__main__":
    main(sys.argv)
