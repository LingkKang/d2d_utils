"""
Merge PDF files
Required:
    - `PyMuPDF`

Usage:
    `python merge_pdf.py ./a.pdf ./b.pdf ...`
"""

import sys

import fitz  # PyMuPDF

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_pdf.py ./a.pdf ./b.pdf ...")
        sys.exit(1)
    for i, pdf in enumerate(sys.argv[1:]):
        if i == 0:
            merged_pdf = fitz.open(pdf)
        else:
            merged_pdf.insert_pdf(fitz.open(pdf))
    merged_pdf.save("merged.pdf")
