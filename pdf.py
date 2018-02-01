#coding=utf-8
from reportlab.graphics.shapes import Drawing , Rect
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate , Paragraph , Spacer , Image , Table , TableStyle , PageBreak
from reportlab.lib.styles import getSampleStyleSheet , ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont


styles = getSampleStyleSheet()

def draw_homepage(c):

    c.drawImage('./static/pdf/logo.jpg', 0.16667 * inch, 9 * inch, 3.58666 * inch, 0.88 * inch)

    c.setFillColorRGB(0.4314, 0.7333, 0.3843)
    c.rect(3.16 * inch, 4.8 * inch, 5.10667 * inch, 1.25298 * inch, fill=1, stroke=0)

    c.setFillColorRGB(1, 1, 1)
    c.setFontSize(22)
    c.drawString(86 * mm, 138 * mm, "Data Auditing and Profiling")
    c.setFillColorRGB(0.4314, 0.7333, 0.3843)

    c.setFontSize(16)
    c.drawString(144 * mm, 114 * mm, "-- Onfire Team")
    c.showPage()


def draw_home():
    image_logo = Image('./static/pdf/logo.jpg' , 3.58666 * inch, 0.88 * inch)


def draw_header(c):
    c.drawImage("./static/pdf/pageHeader.png", 0 * inch, 10.91 * inch, 5.28 * inch, 0.78 * inch)
    c.setFillColorRGB(1, 1, 1)
    c.setFontSize(20)
    c.drawString(0.9 * inch, 11.2 * inch, 'AI Segmentation')


def myFirstPage(c, doc):
    c.saveState()

    c.drawImage('./static/pdf/logo.jpg', 0.16667 * inch, 9 * inch, 3.58666 * inch, 0.88 * inch)

    c.setFillColorRGB(0.4314, 0.7333, 0.3843)
    c.rect(3.16 * inch, 4.8 * inch, 5.10667 * inch, 1.25298 * inch, fill=1, stroke=0)

    c.setFillColorRGB(1, 1, 1)
    c.setFontSize(22)
    c.drawString(86 * mm, 138 * mm, "Data Auditing and Profiling")
    c.setFillColorRGB(0.4314, 0.7333, 0.3843)

    c.setFontSize(16)
    c.drawString(144 * mm, 114 * mm, "-- Onfire Team")

    c.restoreState()


def myLaterPages(canvas , doc):
    canvas.saveState()
    draw_header(canvas)
    canvas.restoreState()


def getReportConf():
    json_dir = './conf/report.json'
    content = open(json_dir).read()
    dict = eval(content)
    return dict


def getChartConf():
    json_dir = './conf/profiling.json'
    content = open(json_dir).read()
    dict = eval(content)
    return dict['chart'][0]


def create_paragraph_style(name, font_name, **kwargs):
    ttf_path = "C:/Windows/Fonts/{}.ttf"
    family_args = {}  # store arguments for the font family creation
    for font_type in ("normal", "bold", "italic", "boldItalic"):  # recognized font variants
        if font_type in kwargs:  # if this type was passed...
            font_variant = "{}-{}".format(font_name, font_type)  # create font variant name
            registerFont(TTFont(font_variant, ttf_path.format(kwargs[font_type])))
            family_args[font_type] = font_variant  # add it to font family arguments
    registerFontFamily(font_name, **family_args)  # register a font family
    return ParagraphStyle(name=name, fontName=font_name, fontSize=10, leading=12)


def draw_content(Story, style):
    configer = getReportConf()
    # segment name
    seg_name = Paragraph('<font color="#3f8f38" size=18>Segment name</font>' , style)
    Story.append(seg_name)
    Story.append(Spacer(1 , 0.2 * inch))

    # searched text
    search_text = "- " + configer["searchText"]
    p_s_text = Paragraph('<font color="#444444" size=9>' + search_text + '</font>' , style)
    Story.append(p_s_text)
    Story.append(Spacer(1 , 0.2 * inch))

    text_level = '<font color="#6ebb62" size=14>● </font>' + '<font color="#000000" size=14>' + configer[
        'level'] + '</font>'
    text_size = '<font color="#8baee4" size=14>● </font>' + '<font color="#000000" size=14>' + configer[
        'size'] + '</font>'
    txt_level_desc = '<font color="#000000" size=8>CONFIDENCE LEVEL</font>'
    txt_size_desc = '<font color="#000000" size=8>AUDIENCE SIZE</font>'

    data = [[Paragraph(text_level , style) , Paragraph(text_size , style)] ,
            [Paragraph(txt_level_desc , style) , Paragraph(txt_size_desc , style)]]
    t = Table(data)
    t.setStyle(TableStyle([('TEXTCOLOR' , (0 , 1) , (1 , 1) , '#000000')]))
    Story.append(t)


def draw_chart(Story, style):
    d = Drawing(0, 10)
    Story.append(Spacer(1 , 0.3 * inch))

    conf = getChartConf()

    title = '<font color="#6ebb62" size=14>' + conf['title'] + '</font>'
    Story.append(Paragraph(title, style))

    d.add(Rect(0, 0, 520, 2, fillColor="#7fa1b4", strokeColor=colors.white))
    Story.append(d)

    image_chart = Image('./static/pdf/ShotChart.png' , 3.58 * inch , 2.68 * inch)
    items = conf["items"]
    i = 0
    while i < items.length:
        item = items[i]

        i = i + 1


def go():
    doc = SimpleDocTemplate('phello.pdf', leftMargin=0.4*inch, rightMargin=0.4*inch)

    style = styles["Normal"]
    Story = [PageBreak()]

    draw_content(Story, style)
    draw_chart(Story, style)

    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)



if __name__ == "__main__":
    go()
