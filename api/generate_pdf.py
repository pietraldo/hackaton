from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a canvas object with the specified page size
pdf_file = "api/data/raport.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Set title and add text
c.setFont("Helvetica", 12)
c.drawString(100, 750, "Raport dla HR")


# Save the PDF
c.save()
print(f"PDF created successfully: {pdf_file}")
