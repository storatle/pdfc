#!/usr/bin/env python
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
import os
import math
import argparse

# document: https://pythonhosted.org/PyPDF2/
def pdf_merger(fname, newSize, pdf, output):
    numPages = pdf.getNumPages()
    pageWidth = math.ceil(pdf.getPage(0).mediaBox.getWidth())
    pageHeight = math.ceil(pdf.getPage(0).mediaBox.getHeight())
    pageDiagonal = math.sqrt(pageWidth**2 + pageHeight**2)

    numNewPages = 1 
    if (newSize == 'A4'):
        newWidth = 595
        newHeight = 842
        newDiagonal = 1031
        
    else:
        # A3
        newWidth = 842
        newHeight = 1190
        newDiagonal = 1457

    print('newWidth: {}, newHeight: {}, newDiagonal: {}'.format(newWidth,newHeight,newDiagonal))


    # Finn ut hvor mange sider du skal fylle
    print(numPages)
    print(round(pageDiagonal/newDiagonal,1))
    if (round(pageDiagonal/newDiagonal,1) == 0.7):
        numNewPages = math.ceil(numPages/2)
        print("# A5 -> A4 or A4 -> A3 , pages = {}".format(numNewPages))
        indices = create_matrix(2,1)
        indices = [[0,0],[1,0]]
        print(indices)
        rotate = 'landscape'

    elif(round(pageDiagonal/newDiagonal,1) == 0.5):
        numNewPages = math.ceil(numPages/4)
        indices = create_matrix(2,2)
        indices = [[0, 1], [1, 1], [0, 0], [1, 0]]
        print(indices)
        print("# A6 -> A4 or A5 -> A3, pages = {}".format(numNewPages))
        rotate = 'portrait'

    elif(round(pageDiagonal/newDiagonal,2) == 0.35):
        numNewPages = math.ceil(numPages/8)
        indices = create_matrix(4,2)
        rotate = 'landscape'
        print("# A6 -> A3, pages = {}".format(numNewPages))
    else: 
            print("Ukjent størrelse på ark")
    

    writer = PdfFileWriter()
        
    if (rotate == 'portrait'):
        translated_page = PageObject.createBlankPage(None, newWidth, newHeight) 
    else:
        translated_page = PageObject.createBlankPage(None, newHeight, newWidth) 

#        num_x = math.ceil(newWidth/pageWidth)
#        num_y = math.ceil(newHeight/pageHeight)
#        print('{} , {}'.format(num_x,num_y))
    
        #indices = create_matrix(num_x, num_y)
        #indices = [indices[i] for i in idx]

    i = 0 
    for page in range(numPages):
        print('{}_page'.format(page+1))
        sub_page = pdf.getPage(page)
        translated_page.mergeTranslatedPage(sub_page, indices[i][0]*pageWidth , indices[i][1]*pageHeight)
            #translated_page.mergeTranslatedPage(sub_page, indices[i][0]*pageHeight , indices[i][1]*pageWidth)
        i+=1
        if (i > len(indices)-1):
            print("New page")
            i = 0
            # create page to writer
            writer.addPage(translated_page)
            if (rotate == 'portrait'):
                translated_page = PageObject.createBlankPage(None, newWidth, newHeight) 
            else:
                translated_page = PageObject.createBlankPage(None, newHeight, newWidth) 
    with open(output, 'wb') as f:
        writer.write(f)

def create_matrix(n,m):
    matrix = []
    for i in range(m,0,-1):
        for j in range(n):
            matrix.append([j,i-1])
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

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file')
    parser.add_argument('-a', '--size', help='size of out paper a4 or a3')
    parser.add_argument('-b', '--backup', action='store_true', help="Backup the old PDF file")
    parser.add_argument('-s', '--split', action='store_true', help="Split into separate files")
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after compression')
    args = parser.parse_args()
    print('inputs: {}, size: {}'.format(args.input,args.size))
    pdf = PdfFileReader(args.input)
    fname = os.path.splitext(os.path.basename(args.input))[0]
    if not args.size:
        args.size = "A4"
    if not args.out:
        args.out = '{}_out.pdf'.format(fname)
    
    if args.split:
        pdf_splitter(fname)
    else:
        pdf_merger(fname, args.size, pdf, args.out)
 
if __name__ == '__main__':
   main() 
    

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


#    print("pageDiagonal: {}, newDiagonal: {}, ratio: {}, number of pages {}".format(pageDiagonal,newDiagonal, round(pageDiagonal/newDiagonal,2), round(pageDiagonal/newDiagonal,2)**2)) 


    
#    print(math.ceil(pdf.getPage(0).mediaBox.getWidth()))
#    if (numPages > 16):
#        print("To many files")
#
#    # Hvis A6
#    elif (numPages > 8 and pageSize > 298): # > A6
#        print("Du får ikke plass til alle")
#        print("# A6 -> A3 = 16")
#    elif (numPages > 4 and pageSize > 298): # > A6
#        print("# A5 - A3 = 8")
#        print("# A6 -> A4 = 8")
#    elif (numPages > 4 and pageSize > 420 ): # > A5
#        print("# A5 -> A3 = 8")
#    elif (numPages > 0 and pageSize > 402 ):
#        print("# A4 -> A3 = 4")
#    elif (numPages > 0 and pageSize < 420):
#        print("# A5 -> A4 = 4")
 
#           reader = PdfFileReader(open('{}_page_{}.pdf'.format(fname,page+1),'rb'))
#           sub_page = reader.getPage(0)

#    numPages = pdf.getNumPages()
#    pageSize = pdf.getPage(0).mediaBox.getWidth()
#    print(pdf.getNumPages())
#    print(math.ceil(pdf.getPage(0).mediaBox.getWidth()))
#    if (numPages > 16):
#        print("To many files")
#    elif (numPages > 8 and pageSize > 298): # > A6
#        print("Du får ikke plass til alle")
#        print("# A6 -> A3 = 16")
#    elif (numPages > 4 and pageSize > 298): # > A6
#        print("# A5 - A3 = 8")
#        print("# A6 -> A4 = 8")
#    elif (numPages > 4 and pageSize > 420 ): # > A5
#        print("# A5 -> A3 = 8")
#    elif (numPages > 0 and pageSize > 402 ):
#        print("# A4 -> A3 = 4")
#    elif (numPages > 0 and pageSize < 420):
#        print("# A5 -> A4 = 4")
 
