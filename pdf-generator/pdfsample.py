# Help
def drawMyRuler(pdf):
    pdf.drawString(100,810, "x100")
    pdf.drawString(200,810, "x200")
    pdf.drawString(300,810, "x300")
    pdf.drawString(400,810, "x400")
    pdf.drawString(500,810, "x500")

    pdf.drawString(10,100, "y100")
    pdf.drawString(10,200, "y200")
    pdf.drawString(10,300, "y300")
    pdf.drawString(10,400, "y400")
    pdf.drawString(10,500, "y500")
    pdf.drawString(10,600, "y600")
    pdf.drawString(10,700, "y700")
    pdf.drawString(10,800, "y800")
    pdf.drawString(10,900, "y900")
# 0) Create document

fileName = "MyDoc.pdf"
documentTitle = "Document title!"
title = "Factuur"
subTitle = "The largest carnivorous marsupial"
invoering = input("Voer wat in")


textLines = [
    "The Tasmanian devil (Sarcophilus harrisii) is",
    "a carnivorous marsupial of the family",
    "Dasyutidae."
]

# Image = 

from reportlab.pdfgen import canvas

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)


drawMyRuler(pdf)
# #############################################
# 1) Title :: Set fonts
# Print available fonts
for font in pdf.getAvailableFonts():
    print(font)
# pdf.drawString(270, 770, title)
pdf.drawString(270, 770, invoering)

######################################
# 2) Subtitle :: 

pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)

##############################################
# 3) Draw a line
pdf.line(30, 710, 550, 710)








###############

pdf.save()