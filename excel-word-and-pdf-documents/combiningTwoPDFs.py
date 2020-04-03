import PyPDF2, os

# PyPDF2 module

# opening PDF files in read-binary mode
pdf1_file = open(r"C:\Users\micha\Documents\Training\meetingminutes1.pdf", "rb")
pdf2_file = open(r"C:\Users\micha\Documents\Training\meetingminutes2.pdf", "rb")

# creating reader objects
reader1 = PyPDF2.PdfFileReader(pdf1_file)
reader2 = PyPDF2.PdfFileReader(pdf2_file)

# changing directory
os.chdir(r"C:\Users\micha\Documents\Training")

# creating writer object
writer = PyPDF2.PdfFileWriter()

# adding pages to the file
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

output_file = open("combinedTwoPDFs.pdf", "wb")

try:
    writer.write(output_file)
    print("File created at " + os.getcwd())
except:
    "Error occured"

# closing files
output_file.close()
pdf1_file.close()
pdf2_file.close()
