"""
Extract PDF pages
Required:
    - `PyMuPDF`

Usage:
    `python pdf_extract_pages.py ./a.pdf <begin> <end>`
"""

import sys
import os

import fitz  # PyMuPDF


def extract_pages(file_path, begin_page, end_page):
    try:
        pdf = fitz.open(file_path)
        if begin_page > end_page or begin_page < 0 or end_page > pdf.page_count:
            raise ValueError("Invalid page range")
        new_pdf = fitz.open()

        for page_num in range(begin_page - 1, end_page):
            # index is 0-based
            new_pdf.insert_pdf(pdf, from_page=page_num, to_page=page_num)

        original_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file_name = f"{original_name}-{begin_page}-{end_page}.pdf"
        output_path = os.path.join(os.getcwd(), output_file_name)

        new_pdf.save(output_path)
        new_pdf.close()
        pdf.close()

        print(
            f"Page(s) {begin_page} to {end_page} extracted and saved as ./{output_file_name}"
        )

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pdf_extract_pages.py ./a.pdf <begin> <end>")
        sys.exit(1)
    file_path = sys.argv[1]
    begin_page = int(sys.argv[2])
    end_page = int(sys.argv[3])
    extract_pages(file_path, begin_page, end_page)
