"""Builds Deliverable 1 (Project Proposal) as a Word document."""

import re
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor

NAVY = RGBColor(0x1F, 0x3A, 0x53)
SLATE = RGBColor(0x2F, 0x48, 0x58)
GREY = RGBColor(0x5A, 0x63, 0x6B)

doc = Document()

# ------------------------------------------------------------------ page set-up
sec = doc.sections[0]
sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)          # A4 portrait
sec.top_margin = sec.bottom_margin = Cm(1.9)
sec.left_margin = sec.right_margin = Cm(1.8)
USABLE = 9864                                                  # dxa

normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10)
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.08

for name, size, color, before, after in [
    ("Heading 1", 13, NAVY, 14, 5),
    ("Heading 2", 11, SLATE, 10, 4),
    ("Heading 3", 10, SLATE, 8, 3),
]:
    st = doc.styles[name]
    st.font.name = "Calibri"
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = color
    st.paragraph_format.space_before = Pt(before)
    st.paragraph_format.space_after = Pt(after)
    st.paragraph_format.keep_with_next = True


# ------------------------------------------------------------------ helpers
TOKEN = re.compile(r"(\*\*.+?\*\*|\*.+?\*|`.+?`)")


def rich(p, text, size=None, color=None):
    """Adds text to a paragraph, honouring **bold**, *italic* and `mono`."""
    text = text.replace(" %", " %")          # keep a number and its % on one line
    for chunk in TOKEN.split(text):
        if not chunk:
            continue
        run = p.add_run()
        if chunk.startswith("**") and chunk.endswith("**"):
            run.text, run.bold = chunk[2:-2], True
        elif chunk.startswith("`") and chunk.endswith("`"):
            run.text, run.font.name = chunk[1:-1], "Consolas"
            run.font.size = Pt((size or 10) - 1.5)
        elif chunk.startswith("*") and chunk.endswith("*"):
            run.text, run.italic = chunk[1:-1], True
        else:
            run.text = chunk
        if size and run.font.size is None:
            run.font.size = Pt(size)
        if color:
            run.font.color.rgb = color
    return p


def para(text, style=None, size=None, color=None, space_after=6,
         align=None, indent=None):
    p = doc.add_paragraph(style=style)
    rich(p, text, size=size, color=color)
    p.paragraph_format.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    if indent is not None:
        p.paragraph_format.left_indent = Cm(indent)
    return p


def heading(text, level=1):
    h = doc.add_heading(level=level)
    rich(h, text)
    return h


def bullet(text, size=10, indent=0.0):
    p = doc.add_paragraph(style="List Bullet")
    rich(p, text, size=size)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.65 + indent)
    p.paragraph_format.line_spacing = 1.05
    return p


def shade(cell, hex_fill):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hex_fill)
    cell._tc.get_or_add_tcPr().append(el)


def fixed_layout(table):
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)


def row_props(row, header=False):
    """Keeps a row whole across a page break; repeats it if it is a header."""
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    if header:
        trPr.append(OxmlElement("w:tblHeader"))


def build_table(headers, rows, widths, font=7.6, head_fill="1F3A53",
                zebra="F2F5F8", first_col_bold=True, keep_together=False):
    """keep_together=True keeps a short table on one page; the header row always
    stays with the first data row."""
    if doc.paragraphs:
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    fixed_layout(t)

    row_props(t.rows[0], header=True)
    for i, text in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.width = Pt(widths[i] / 20)
        shade(cell, head_fill)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(font)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for n, row in enumerate(rows):
        tr = t.add_row()
        row_props(tr)
        cells = tr.cells
        for i, text in enumerate(row):
            cells[i].width = Pt(widths[i] / 20)
            if zebra and n % 2 == 1:
                shade(cells[i], zebra)
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.line_spacing = 1.0
            if keep_together and n < len(rows) - 1:
                p.paragraph_format.keep_with_next = True
            rich(p, text, size=font)
            if i == 0 and first_col_bold:
                for r in p.runs:
                    r.bold = True
    return t


def add_page_footer():
    footer = sec.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Group Project — Deliverable 1 — Project Proposal   ·   page ")
    r.font.size = Pt(8)
    r.font.color.rgb = GREY
    for instr, kind in [(None, "begin"), ("PAGE", "instrText"), (None, "end")]:
        run = p.add_run()
        run.font.size = Pt(8)
        run.font.color.rgb = GREY
        el = OxmlElement("w:fldChar") if kind != "instrText" else OxmlElement("w:instrText")
        if kind == "instrText":
            el.set(qn("xml:space"), "preserve")
            el.text = " PAGE "
        else:
            el.set(qn("w:fldCharType"), kind)
        run._r.append(el)


def rule(space_before=2, space_after=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    pPr = p._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "BFC7CE")
    borders.append(bottom)
    pPr.append(borders)


add_page_footer()
