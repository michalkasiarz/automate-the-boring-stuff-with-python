import PyPDF2, os

# PyPDF2 module

# opening PDF file in read-binary mode
pdf_file = open(r"C:\Users\micha\Documents\Training\meetingminutes1.pdf", "rb")

# reading file with PyPDF2
reader = PyPDF2.PdfFileReader(pdf_file)

# printing number of PDF file
print(reader.numPages)  # 19

# creating a page object
page = reader.getPage(0)    # getting page number 0

# extracting the text from page number 0
page_text = page.extractText()

# printing the text from page number 0
print(page_text)

print(" BEGINNING OF THE FILE ".center(100, "-"))

# looping for over all of the pages
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

print(" END OF FILE ".center(100, "-"))
