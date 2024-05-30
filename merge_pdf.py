"""
Merge PDF files
Required:
    - `PyMuPDF`

Usage:
    `python merge_pdf.py ./a.pdf ./b.pdf ...`
    or
    `python merge_pdf.py ./pdf_folder`
"""

import sys
import os

import fitz  # PyMuPDF

if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len < 2:
        print("Wrong input")
        sys.exit(1)

    pdf = None
    if arg_len == 2 and os.path.isdir(sys.argv[1]):
        files = [f for f in os.listdir(sys.argv[1]) if f.lower().endswith(".pdf")]
        files.sort()
        pdf = [sys.argv[1] + f for f in files]
    else:
        pdf = sys.argv[1:]

    merged_pdf = None
    for f in pdf:
        if merged_pdf is None:
            merged_pdf = fitz.open(f)
        else:
            merged_pdf.insert_pdf(fitz.open(f))
    merged_pdf.save("merged.pdf")
