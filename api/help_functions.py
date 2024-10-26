import fitz 
import matplotlib.pyplot as plt
from PIL import Image
import io

def push_data_to_db(data):
    pass

def get_team_data_from_db(id):
    dni=[
    "2024-10-20", "2024-10-21", "2024-10-22", "2024-10-23", "2024-10-24",
    "2024-10-25", "2024-10-26", "2024-10-27", "2024-10-28", "2024-10-29",
    "2024-10-30", "2024-10-31", "2024-11-01", "2024-11-02", "2024-11-03",
    "2024-11-04", "2024-11-05", "2024-11-06", "2024-11-07", "2024-11-08",
    "2024-11-09", "2024-11-10", "2024-11-11", "2024-11-12", "2024-11-13",
    "2024-11-14", "2024-11-15", "2024-11-16", "2024-11-17", "2024-11-18"
  ]
    dlugosc_spania=[
        8.0, 7.5, 6.5, 8.5, 7.0,
        7.5, 8.0, 6.0, 7.5, 7.0,
        8.0, 7.0, 6.5, 8.5, 7.0,
        7.5, 8.0, 6.5, 7.5, 8.0,
        6.5, 7.0, 8.5, 6.5, 7.0,
        8.0, 7.5, 6.0, 8.0, 7.5
    ]
    dlugosc_dobrego_spania=[
        6.0, 5.5, 4.5, 6.5, 5.0,
        5.5, 6.0, 4.0, 5.5, 5.0,
    6.0, 5.0, 4.5, 6.5, 5.0,
    5.5, 6.0, 4.5, 5.5, 6.0,
    4.5, 5.0, 6.5, 4.5, 5.0,
    6.0, 5.5, 4.0, 6.0, 5.5
  ]
    
    dlugosc_stresu = [
    1.0, 1.5, 1.2, 1.7, 0.9, 
    1.8, 2.0, 1.5, 1.3, 5.0, 
    1.4, 1.1, 1.0, 1.6, 2.0, 
    1.2, 0.7, 1.3, 1.0, 5.0,  
    1.1, 1.4, 1.5, 0.8, 1.0, 
    1.2, 1.3, 1.0, 1.5, 1.2 
]
    return dni, dlugosc_spania,dlugosc_dobrego_spania, dlugosc_stresu


def display_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page and convert to image
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)
        
        # Render the page to a pixmap
        pix = page.get_pixmap()
        
        # Convert the pixmap to PNG bytes
        img_bytes = pix.tobytes("png")
        
        # Convert bytes to a PIL Image
        img = Image.open(io.BytesIO(img_bytes))
        
        # Display the image using matplotlib
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.title(f"Page {page_num + 1}")
        plt.show()

    pdf_document.close()  # Close the document