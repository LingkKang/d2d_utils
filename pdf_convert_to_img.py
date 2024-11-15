"""
Convert PDF pages to images

Required:
    - `PyMuPDF`

Usage:
    `python pdf_convert_to_img.py ./input.pdf`
"""

import sys

import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_path, output_pattern):
    pdf = fitz.open(pdf_path)
    for i in range(pdf.page_count):
        page = pdf[i]
        image = page.get_pixmap(dpi=400)
        image.save(output_pattern % (i + 1))

    pdf.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_convert_img.py ./input.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pattern = "ICM_%04d.png"
    convert_pdf_to_images(input_pdf, output_pattern)
