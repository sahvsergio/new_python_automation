# Getting Creative with PDF Files and Documents
"""In this chapter, we will discuss two more binary file formats: .pdf and .docx. 
You'll build knowledge on generating and reading PDF files, copying them and even 
manipulating them to build your own header and footer formats. Do you know you could 
merge many PDF files with a simple Python recipe?

This chapter also takes you on a journey of working with Word documents. 
It helps you build knowledge on reading and writing data into Word files. 
Adding tables, images, charts, you name it and this chapter covers it.
Sounds interesting? Then this chapter is definitely for you!"""


# modules needed
# PyPDF2 (https://pythonhosted.org/PyPDF2/)
# fpdf (https://pyfpdf.readthedocs.io/)
# python-docx (http://python-docx.readthedocs.io/en/latest/)

# importing it
from PyPDF2 import PdfReader, PdfMerger
from PyPDF2 import PdfReader, PdfWriter
from fpdf import FPDF
from fpdf import FPDF
import fpdf
import PyPDF2
# PdfFileReader was deprecated and removed in PyPD2 3.0.0 use PdfReader instead
# from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

# creating the PDF file reader object
pdf = open("diveintopython3-r802.pdf", 'rb')
# readerObj=PdfFileReader(pdf)
readerObj = PdfReader(pdf)
print('PDF reader Object is :', readerObj)
print('*'*100)
print('Details of diveintopython book')
# deprecated use len(reader.pages) instead
# print('Number of pages:',readerObj.getNumPages())
# get number of pages
print('Number of pages:', len(readerObj.pages))
# deprecated, use metadata instead
# print('Title:',readerObj.getDocumentInfo().title)
print('Title', readerObj.metadata.title)
print('Author:', readerObj.metadata.author)
print('*'*100)
print('pdf content')
print('Reading Page 1')

# deprecated use reader.pages[page_number]      )
# page=readerObj.getPage(1)
# reading the pages
page = readerObj.pages[1]
# deprecated use extract_text instead
# print(page.extractText())
print('*'*50)
print('This is the content of the book in page 1 ')
print(page.extract_text())
print('*'*100)
print('end of the 1st page')

print('Book outline')
# deprecated use outline instead
# for heading in readerObj.getOutlines():
for heading in readerObj.outline:
    if type(heading) is not list:
        print(dict(heading).get('/Title'))

# Creating and copying PDF documents
# PDFFIleWriter and PDFileReader have been deprecated use PdfWriter
# addBlankPage was deprecated use add_blank_page addPage was deprecated use  add_page
print('*'*20, 'Creating and copying PDF documents', '*'*30)
# reading the input file

infile = PdfReader(open('A la Carga Gung Ho.pdf', 'rb')
                   )  # read the original file
# creating the instance of the output file

outfile = PdfWriter()
# prepare  a blank page with  the dimensions 612,792
outfile.add_blank_page(612, 792)
# read the page #1 of the input file
page = infile.pages[1]
# add the 1st page of the input file to the output file
outfile.add_page(page)
# open the output file
with open('mypdf.pdf', 'wb') as f:
    # write/dump the content of output file into the actual file
    outfile.write(f)
    f.close()

print('*'*30, 'creating a pdf from scratch', '*'*30)
# create a pdf from scratch


# instantiating the FPDF class
pdf = FPDF(format='letter')  # The fpdf module supports
# multiple formats, such as A3, A4, A5, Letter, and Legal.

# start inserting content into the file
# adding a page
pdf.add_page()
# setting phone family and size
pdf.set_font('Arial', size=12)
# adding content
pdf.cell(200, 10, txt='Sergio Herrera\'s CV', ln=1, align='C')
pdf.cell(200, 10, 'Address', 0, 1, 'C')
pdf.output('Sergio_Herrera.pdf')
print('*'*100)
print('Manipulating PDFs (adding header/footer, merge, split, delete)')
"""
Issues with bookmarks of one or several pdfs 

print('Merging Pfs')
#PdfFileMerger is deprecated use PdfMerger
from PyPDF2 import PdfReader,PdfMerger
import os

merger=PdfMerger()
files=[x for x in os.listdir('.') if x.endswith('.pdf') ]
for fname in sorted(files):
    merger.append(PdfReader(open(os.path.join('.',fname),'rb')))
    merger.write('output-merge.pdf')
    
"""
print('Creating Header and Footer')


class PDF(FPDF):

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Automate it', 1, 0, 'C')
        self.ln(20)


pdf = PDF(format='A5')
pdf.add_page()
pdf.set_font('Times', size=12)


for i in range(1, 50):
    pdf.cell(0, 10, 'This is my new line,line number is %s %i :', ln=1, align='C')
    pdf.output('header_footer.pdf')

print(' want to remove blank pages from PDF files?')
# read the file
infile = PdfReader('mypdf.pdf', 'rb')
output = PdfWriter()

for i in range(len(infile.pages)):
    p = infile.pages[i]
    # getContents was deprecated
    if p.get_contents():
        output.add_page(p)
with open('mypdf_wo_blank.pdf', 'wb')as f:
    output.write(f)


print('edit metadata')
# create the merger object
mergerObj = PdfMerger()
# open the file with the metadata
fp = open('mypdf.pdf', 'wb')
# create the metadata dict
metadata = {'Edited': 'ByPdfFileMerger'}

# add the metadata to the merger object
# mergerObj.addMetadata(metadata)
mergerObj.add_metadata(metadata)
# write the file into the merger object
mergerObj.write(fp)
fp.close()
pdf = open('mypdf.pdf', 'rb')
readerObj = PdfReader(pdf)
print('Document info:', readerObj.metadata)
pdf.close()

print('Rotate the pages')
fp = open('output-merge.pdf', 'rb')
readerObj = PdfReader(fp)
page = readerObj.pages[0]
# page.rotateCounterClockwise(90)
page.rotate(90)
writer = PdfWriter()
writer.add_page(page)
fw = open('RotatedExcercise.pdf', 'wb')
writer.write(fw)
fw.close()
fp.close()


""" 
print('Practical Project: Automating generation of payslips for finance department')
from datetime import datetime

employee_data=[ 
     { 'id': 123, 'name': 'John Sally', 'payment': 10000,
       'tax': 3000, 'total': 7000 },
     { 'id': 245, 'name': 'Robert Langford', 'payment': 12000,
       'tax': 4000, 'total': 8000 }, 
]
from fpdf import FPDF, HTMLMixin

class PaySlip(FPDF, HTMLMixin):
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial','I',8)
        self.cell(0,10,'Page %s'%self.page_no(),0,0,'C')
    
    def header(self):
        self.set_font('Arial','B',15)
        self.cell(80)
        self.cell(30,10,'Gooogle',1,0,'C')
        self.ln(20)
        
def generate_payslip(data):
    month=datetime.now().strftime('%B')
    year=datetime.now().strftime('%Y')
    pdf=PaySlip(format='letter')
    pdf.add_page()
    pdf.set_font('Times',size=12)
    pdf.cell(200,10,txt='Payslip for %s,%s,'%(month,year),ln=3, align='C')
    pdf.cell(50)
    pdf.cell(100,10,txt='Employee Id: %s'%data['id'],ln=1,align='L')
    pdf.cell(50)
    pdf.cell( 100, 10,txt='Employee Name: %s'%data['name'],ln=3,align='L')
    html="""
"""
    <table border='0'align='center' width='50>
        <thead>
            <tr>
                <th align='left' width='50%'>Pay Slip Details<th/>
                <th align='right' width='50%'>Amount in US</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Payments</td>
                <td align='right'>"""  """"+str(data['payment'])+"""</td>
                """
            </tr>
                
            <tr>
              <td>Tax</td>
              <td align='right'>"""+str(data['tax'])+""" </td>
                          
            </tr>
            <tr>
                <td>Total</td>
                <td align='right'>""" """+str(data['total'])+"""  """</td>
            </tr>
        </tbody>
    </table> 
    
    
    pdf.write_html(html)
    pdf.output('PaySlip_.pdf'%data['id'])
for emp in employee_data:
    generate_payslip(emp)
    
        
 """
#encrypt the pdf

from PyPDF2 import PdfWriter,PdfReader

fp=open('mypdf_wo_blank','rb')
readerObj=PdfWriter(fp)
writer=PdfWriter()

for page in range(readerObj.numpages):
    writer.add_page(readerObj.pages(page))
writer.encrypt('P@$$w0rd')
newfp=open('EncryptedExcercise.pdf','wb')
writer.write(newfp)
newfp.close()
fp.close()

