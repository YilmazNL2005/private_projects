import json

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



# 0) Create document

fileName = "Factuur_Yilmaz.pdf"
documentTitle = "Document title!"
title = "Factuur"
subTitle = "The largest carnivorous marsupial"

def laad_json_bestand(bestandsnaam):
    with open(bestandsnaam, "r") as json_bestand:
        gegevens = json.load(json_bestand)
    return gegevens
# invoering = input("Voer wat in")


textLines = [
    "Zonnebloemstraat 73",
    "3353TE",
    "Papendrecht",
    "Factuurdatum-25-04-2024",
    f"Factuur-nr: 1029473",
    f"Yilmaz Güney",
    f"Btw-nummer: 3362782",
    f"Kvk-nummer: 3336447"
]

factuuradres = [
    "Factuuradres",
    "Sofia Philips",
    "Overalstraat 123",
    "1234 AB Beekstad",
    "Verzendadres"
]

bedrijfsgegevens = [
    "Klantenservice",
    "123 - 4567890",
    "321 - 4567890",
    "info@pocketmates.nl",
    "Bedrijfsgegevens",
    "KVK: 3362782",
    "KVK-nummer: 3336447"
]

kosten = [
    "Subtotaal:",
    "Verzending:",
    "BTW(21%):",
    "Totaal:"
]


artikelomschrijving = "Artikelomschrijving"
aantal = "Aantal"
prijs = "Prijs"
totaalprijs = "Totaal"

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
pdf.setFont("Helvetica-Bold", 36)
pdf.drawString(235, 750, title)
#pdf.drawString(270, 770, invoering)


######################################
# 2) Subtitle :: 

# pdf.setFillColorRGB(0, 0, 255)
# pdf.setFont("Courier-Bold", 24)
# pdf.drawCentredString(290, 720, subTitle)


##############################################
# 3) Draw a line
pdf.line(40, 560, 550, 560)
pdf.line(40, 510, 550, 510)
# pdf.line(40, 410, 550, 410)
pdf.line(40, 310, 550, 310)
pdf.line(40, 100, 550, 100)


# 4) Benodigde Tekst wat er standaard in staat.

pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(400, 735, textLines[0])
pdf.drawString(400, 720, textLines[1])
pdf.drawString(400, 705, textLines[2])
pdf.drawString(400, 655, textLines[3])
pdf.drawString(400, 595, textLines[4])

pdf.setFont("Helvetica-Bold", 12)

#############################################
# Kopjes
pdf.drawString(450, 530, totaalprijs)
pdf.drawString(350, 530, prijs)
pdf.drawString(250, 530, aantal)
pdf.drawString(80, 530, artikelomschrijving)


pdf.setFont("Helvetica-Bold", 10)

##########################################
# Factuuradres
pdf.drawString(80, 285, factuuradres[0])
pdf.drawString(80, 265, factuuradres[1])
pdf.drawString(80, 245, factuuradres[2])
pdf.drawString(80, 225, factuuradres[3])

##########################################
# Verzendadres
pdf.drawString(80, 185, factuuradres[4])
pdf.drawString(80, 165, factuuradres[1])
pdf.drawString(80, 145, factuuradres[2])
pdf.drawString(80, 125, factuuradres[3])

##########################################
# Kosten
# pdf.drawString(350, 285, kosten[0])
# pdf.drawString(350, 265, kosten[1])
# pdf.drawString(350, 245, kosten[2])
# pdf.drawString(350, 225, kosten[3])

gegevens = laad_json_bestand("pdf-generator/2000-965.json")


y_pos = 490  
for product in gegevens["order"]["producten"]:
    pdf.drawString(80, y_pos, str(product["productnaam"]))
    pdf.drawString(250, y_pos, str(product["aantal"]))
    pdf.drawString(350, y_pos, str(product["prijs_per_stuk_excl_btw"]))
    pdf.drawString(450, y_pos, str(product["aantal"] * product["prijs_per_stuk_excl_btw"]))
    y_pos -= 20

# BTW
subtotaal = sum(product["aantal"] * product["prijs_per_stuk_excl_btw"] for product in gegevens["order"]["producten"])
btw = subtotaal * 0.21
verzending = 6.95
totaal = subtotaal + btw
pdf.drawString(350, 285, f"Subtotaal: {subtotaal:.2f}")
pdf.drawString(350, 265, f"BTW (21%): {btw:.2f}")
pdf.drawString(350, 245, f"Verzending: {verzending:.2f}")
pdf.drawString(350, 225, f"Totaal: {totaal:.2f}")

# Klantenservice
pdf.drawString(80, 80, bedrijfsgegevens[0])
pdf.drawString(80, 60, bedrijfsgegevens[1])
pdf.drawString(80, 40, bedrijfsgegevens[2])
pdf.drawString(80, 20, bedrijfsgegevens[3])

# Bedrijfsgegevens
pdf.drawString(450, 80, bedrijfsgegevens[4])
pdf.drawString(450, 60, bedrijfsgegevens[5])
pdf.drawString(450, 40, bedrijfsgegevens[6])







###############

pdf.save()