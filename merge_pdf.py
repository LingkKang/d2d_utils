"""
Merge PDF files
Required:
    - `PyMuPDF`

Usage:
    `python merge_pdf.py ./a.pdf ./b.pdf ...`
"""

import sys

import fitz  # PyMuPDF

REFRESH_TOC = True


def get_file_name(file_path):
    return file_path.split("\\")[-1].split(".")[0]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_pdf.py ./a.pdf ./b.pdf ...")
        sys.exit(1)

    toc = []
    pages = 0
    for i, pdf in enumerate(sys.argv[1:]):
        new_pdf = fitz.open(pdf)
        if REFRESH_TOC:
            toc.append([1, get_file_name(pdf), pages + 1])
        else:
            for item in new_pdf.get_toc():
                toc.append([item[0], item[1], item[2] + pages])
        pages += new_pdf.page_count
        if i == 0:
            merged_pdf = new_pdf
        else:
            merged_pdf.insert_pdf(new_pdf)

    merged_pdf.set_toc(toc)
    merged_pdf.save("merged.pdf")
