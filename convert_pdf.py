"""
Convert PDF to images
Required:
    - `PyMuPDF`

Usage:
    `python convert_pdf.py ./sample.pdf`
    `python convert_pdf.py ./sample.pdf jpg`
"""

import sys
from datetime import datetime

import fitz  # PyMuPDF


def convert_pdf(pdf_path, img_fmt="png"):
    current_time = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    pdf = fitz.open(pdf_path)
    for page in pdf:
        dpi = 600
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
        img = fitz.Pixmap(pix)
        img.save(f"{current_time}.{page.number}.{img_fmt}")
    pdf.close()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        convert_pdf(sys.argv[1], sys.argv[2])
    else:
        convert_pdf(sys.argv[1])
    sys.exit(0)
