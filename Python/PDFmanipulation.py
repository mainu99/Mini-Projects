import sys

from PyPDF2 import PdfReader, PdfWriter, PdfMerger


def pdf_rotate():
    with open('./res/pdfs/dummy.pdf', 'rb') as pdf_file:
        print(pdf_file)
        reader = PdfReader(pdf_file)
        print(len(reader.pages))
        page = reader.pages[0]
        page.rotate(180)
        writer = PdfWriter()  #creates pdf writer obj
        writer.add_page(page)
        with open('./res/tilted_dummy.pdf', 'wb') as new_file:
            writer.write(new_file)


def pdf_merger():
    pdf_list = sys.argv[1:]
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('./res/pdfs/merged_pdfs.pdf')


def pdf_watermark():
    pdf_file = "./res/pdfs/merged_pdfs.pdf"
    watermark = "./res/pdfs/wtr.pdf"
    merged = "./res/pdfs/watermarked.pdf"

    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)

# pdf_rotate()
# pdf_merger()
# pdf_watermark()
