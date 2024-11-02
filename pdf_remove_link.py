"""
Remove hyperlinks in a PDF file
Required:
    - `PyMuPDF`

Usage:
    `python remove_link.py ./a.pdf`
"""

import sys

import fitz


def remove_hyperlinks(file_path):
    pdf = fitz.open(file_path)
    for page_num in range(pdf.page_count):
        page = pdf.load_page(page_num)

        for link in page.get_links():
            page.delete_link(link)

    output_file = "no_links_" + file_path.split("\\")[-1]
    pdf.save(output_file)
    pdf.close()


if __name__ == "__main__":
    input_file = sys.argv[1]
    remove_hyperlinks(input_file)
