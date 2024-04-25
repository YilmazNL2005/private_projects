import json
from reportlab.pdfgen import canvas

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

# Functie om gegevens uit de JSON te laden
def laad_json_bestand(bestandsnaam):
    with open(bestandsnaam, "r") as json_bestand:
        gegevens = json.load(json_bestand)
    return gegevens

# Functie om een PDF-factuur te maken
def maak_factuur():
    # 0) Create document
    fileName = "MyDoc.pdf"
    documentTitle = "Document title!"
    title = "Factuur"

    # Load JSON data
    gegevens = laad_json_bestand("pdf-generator/2000-965.json")

    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    drawMyRuler(pdf)

    # 1) Title :: Set fonts
    pdf.setFont("Helvetica-Bold", 36)
    pdf.drawString(235, 750, title)

    # 3) Draw a line
    pdf.line(40, 560, 550, 560)
    pdf.line(40, 510, 550, 510)
    pdf.line(40, 410, 550, 410)
    pdf.line(40, 310, 550, 310)
    pdf.line(40, 100, 550, 100)

    # 4) Required Text
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(400, 735, gegevens["order"]["klant"]["naam"])
    pdf.drawString(400, 720, gegevens["order"]["klant"]["adres"])
    pdf.drawString(400, 705, f"{gegevens['order']['klant']['postcode']} {gegevens['order']['klant']['stad']}")
    pdf.drawString(400, 655, f"Factuurdatum: {gegevens['order']['orderdatum']}")
    pdf.drawString(400, 595, f"Factuur-nr: {gegevens['order']['ordernummer']}")

    y_pos = 490  # Startpositie voor de productgegevens
    for product in gegevens["order"]["producten"]:
        pdf.drawString(80, y_pos, product["productnaam"])
        pdf.drawString(250, y_pos, str(product["aantal"]))
        pdf.drawString(350, y_pos, str(product["prijs_per_stuk_excl_btw"]))
        pdf.drawString(450, y_pos, str(product["aantal"] * product["prijs_per_stuk_excl_btw"]))
        y_pos -= 20  # Verplaats naar de volgende regel

    subtotaal = sum(product["aantal"] * product["prijs_per_stuk_excl_btw"] for product in gegevens["order"]["producten"])
    btw = subtotaal * 0.21  # 21% BTW
    totaal = subtotaal + btw
    pdf.drawString(350, 285, f"Subtotaal: {subtotaal:.2f}")
    pdf.drawString(350, 265, f"BTW (21%): {btw:.2f}")
    pdf.drawString(350, 245, f"Totaal: {totaal:.2f}")

    # Sla de PDF op
    pdf.save()

# Roep de functie aan om de factuur te maken
maak_factuur()
