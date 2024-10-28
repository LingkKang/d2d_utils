"""
Merge PDF files
Required:
    - `PyMuPDF`

Usage:
    `python unlock_pdf.py ./a.pdf <password>`
"""

import sys

import fitz

if __name__ == "__main__":
    input_file = sys.argv[1]
    file_name = input_file.split("\\")[-1]
    output_file = "unlocked_" + file_name
    password = sys.argv[2]
    pdf = fitz.open(input_file)

    if not pdf.needs_pass:
        print("PDF is not password protected")
        sys.exit(0)
    if pdf.authenticate(password) == 0:
        print("Invalid password")
        sys.exit(1)
    pdf.save(output_file, encryption=fitz.PDF_ENCRYPT_NONE)
    print(f"PDF unlocked and saved as {output_file}")
