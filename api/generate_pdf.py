from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def gen_pdf(pdf_path, wykres1_path, wykres2_path):
    
    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)

    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Raport zdrowia zespolu", styles["Title"]))
    elements.append(Paragraph("Sen", styles["Title"]))
    elements.append(Image(wykres1_path, width=400, height=300))  
    elements.append(Paragraph("Stress", styles["Title"]))
    elements.append(Image(wykres2_path, width=400, height=300))  

    pdf.build(elements)
    print(f"PDF with plot created successfully: {pdf_path}")
