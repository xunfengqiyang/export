from reportlab.platypus import SimpleDocTemplate , Paragraph , Spacer , Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas

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


def getFirstPage(c, doc):
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
    c.showPage()


def myLaterPages(canvas , doc):
    canvas.saveState()
    draw_header(canvas)
    canvas.restoreState()


def go():
    doc = SimpleDocTemplate('phello.pdf')

    Story= []



    Story = [Spacer(1, 0.1 * inch)]
    for i in range(100):
        bogustext = ("This is Paragraph number %s.  " % i) * 10
        style = styles["Normal"]
        p = Paragraph(bogustext , style)
        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story, onLaterPages=myLaterPages)


if __name__ == "__main__":
    go()
