"""
Remove table of contents in a PDF file
Required:
    - `PyMuPDF`

Usage:
    `python pdf_remove_toc.py ./a.pdf`
"""

import sys

import fitz

def remove_toc(file_path):
    pdf = fitz.open(file_path)
    pdf.set_toc([])

    output_file = "no_toc_" + file_path.split("\\")[-1]
    pdf.save(output_file)
    pdf.close()

if __name__ == "__main__":
    remove_toc(sys.argv[1])
