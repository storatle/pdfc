#!/usr/bin/env python
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
import os

# document: https://pythonhosted.org/PyPDF2/
def pdf_merger(fname, newSize, pdf):
    numPages = pdf.getNumPages()
    pageWidth = round(pdf.getPage(0).mediaBox.getWidth())
    pageHeight = round(pdf.getPage(0).mediaBox.getHeight())
    
    if (newSize == 'A4'):
        newWidth = 595
        newHeight = 842
    else:
        # A3
        newWidth = 842
        newHeight = 1190

    translated_page = PageObject.createBlankPage(None, newWidth, newHeight) 
    num_x = round(newWidth/pageWidth)
    num_y = round(newHeight/pageHeight)
    print('{} , {}'.format(num_x,num_y))
    
    indices = create_matrix(num_x, num_y)
    

    for page in range(numPages):
        print('{}_page_{}.pdf'.format(fname,page+1))
        
#       reader = PdfFileReader(open('{}_page_{}.pdf'.format(fname,page+1),'rb'))
#       sub_page = reader.getPage(0)
        sub_page = pdf.getPage(page)
        translated_page.mergeTranslatedPage(sub_page, indices[page][0]*pageWidth , indices[page][1]*pageHeight)
        

#    reader = PdfFileReader(open("pg_0001.pdf",'rb'))
#    invoice_page = reader.getPage(0)# the page number of first pdf
#    sup_reader = PdfFileReader(open("pg_0002.pdf",'rb'))
#    sup_page = sup_reader.getPage(0)# the page number of second pdf
#
#    # create blank page & merge second pdf in right side
#    print(sup_page.mediaBox.getWidth())
#    print(sup_page.mediaBox.getHeight())
#    translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth()+invoice_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight()+invoice_page.mediaBox.getHeight())
#    translated_page.mergeTranslatedPage(sup_page, sup_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight())
#    #translated_page.mergeScaledTranslatedPage(sup_page, 0, 100, 1)

#   # merge first pdf into this blank page
#    translated_page.mergePage(invoice_page)

    # create page to writer
    writer = PdfFileWriter()
    writer.addPage(translated_page)

    with open('outc.pdf', 'wb') as f:
        writer.write(f)

def create_matrix(n,m):
    matrix = []
    for i in range(n):
        for j in range(m):
            matrix.append([i,j])
    print(matrix)
    return matrix



# pdf_splitter.py
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))
    return pdf

if __name__ == '__main__':
    
    
   # pagewidth = 595.00
   # pageheight = 842.00

    path = 'L1.pdf'
    pdf = pdf_splitter(path)
    numPages = pdf.getNumPages()
    pageSize = pdf.getPage(0).mediaBox.getWidth()
    print(pdf.getNumPages())
    print(round(pdf.getPage(0).mediaBox.getWidth()))
    if (numPages > 16):
        print("To many files")
    elif (numPages > 8 and pageSize > 298): # > A6
        print("Du får ikke plass til alle")
        print("# A6 -> A3 = 16")
    elif (numPages > 4 and pageSize > 298): # > A6
        print("# A5 - A3 = 8")
        print("# A6 -> A4 = 8")
    elif (numPages > 4 and pageSize > 420 ): # > A5
        print("# A5 -> A3 = 8")
    elif (numPages > 0 and pageSize > 402 ):
        print("# A4 -> A3 = 4")
    elif (numPages > 0 and pageSize < 420):
        print("# A5 -> A4 = 4")
    

    fname = os.path.splitext(os.path.basename(path))[0]
    pdf_merger(fname, 'A4', pdf)

