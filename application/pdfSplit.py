from PyPDF2 import PdfFileReader, PdfFileWriter

def seperate_CornerRecord(upload_PDfFile):

    with open(upload_PDfFile, 'rb') as infile:
        reader = PdfFileReader(infile)
        info = reader.getDocumentInfo()
        pages = reader.getNumPages()

        # ========================================================
        # Print information to see what data are being delt with
        print("===== PDf FILE INFORMATION ======")
        print("number of pages: " + str(pages))
        page1 = reader.getPage(0)
        print("====== page1 ======")
        print(page1)
        # print("===== Extract Text =====")
        # Extracting text from a scaned document will not be able to extract text from the pdf file.
        # print(page1.extractText())
        # ========================================================

        cornerRecord_count = 0
        page_end = pages
        for page in range(0, page_end):
            if page % 2 != 0:
                cornerRecord_count = cornerRecord_count + 1
                pdf_writer = PdfFileWriter()
                first_cornerRecord_Page = reader.getPage(page - 1)
                second_cornerRecord_Page = reader.getPage(page)
                pdf_writer.addPage(first_cornerRecord_Page)
                pdf_writer.addPage(second_cornerRecord_Page)
                outputFileName = "output/example-cornerRecord-{}.pdf".format(cornerRecord_count)
                with open(outputFileName, "wb") as out:
                    pdf_writer.write(out)
                    print("created", outputFileName)
                    out.close()
        infile.close()
seperate_CornerRecord("samplePDF/CR 2019-0511 0515 0580-0594.pdf")
