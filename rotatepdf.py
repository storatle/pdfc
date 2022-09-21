#!/usr/bin/env python3

import PyPDF2
import argparse

parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument('input', help='Relative or absolute path of the input PDF file', nargs='*')
args = parser.parse_args()
 
pdfIn = open(args.input[0], 'rb') # exchange the 'original.pdf' with a name of your file 
pdfReader = PyPDF2.PdfFileReader(pdfIn)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    page.rotateClockwise(90)
    pdfWriter.addPage(page)

pdfOut = open('rotated.pdf', 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()
