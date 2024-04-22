

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

def generate_blank_invoice(output_filename):
    # Create a blank PDF
    c = canvas.Canvas(output_filename, pagesize=A4)

    # Set up the font and font size
    c.setFont("Helvetica", 12)

    # Add your design elements here (text, lines, shapes, etc.)
    # For example:
    c.drawString(50, 750, "Invoice")
    c.drawString(50, 730, "Date:")
    c.drawString(120, 730, "XXXX-XX-XX")
    c.drawString(50, 710, "Customer:")
    c.drawString(120, 710, "Customer Name")
    c.drawString(50, 690, "Address:")
    c.drawString(120, 690, "Customer Address")
    c.drawString(50, 670, "Email:")
    c.drawString(120, 670, "customer@example.com")
    c.drawString(50, 650, "Phone:")
    c.drawString(120, 650, "123-456-7890")
    c.drawString(50, 630, "Invoice #:")
    c.drawString(120, 630, "123456")
    c.drawString(50, 600, "Description")
    c.drawString(300, 600, "Amount")

    # Save the PDF
    c.save()

def remove_text(input_filename, output_filename):
    input_pdf = PdfFileReader(open(input_filename, "rb"))
    output_pdf = PdfFileWriter()

    # Remove text by creating a copy of each page
    for page in range(input_pdf.getNumPages()):
        page_obj = input_pdf.getPage(page)
        page_obj.compressContentStreams()  # Compress content for easier removal (optional)
        output_pdf.addPage(page_obj)

    # Write the modified PDF to a file
    with open(output_filename, "wb") as output_file:
        output_pdf.write(output_file)

if __name__ == "__main__":
    blank_invoice_filename = "blank_invoice.pdf"
    filled_invoice_filename = "filled_invoice.pdf"

    # Generate a blank invoice PDF
    generate_blank_invoice(blank_invoice_filename)

    # Remove text from the blank invoice PDF to create the filled invoice PDF
    remove_text(blank_invoice_filename, filled_invoice_filename)

    print("Filled invoice PDF generated successfully.")
