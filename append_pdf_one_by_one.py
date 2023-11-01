"""Append pdf files to one pdf file
Merge all given files into one pdf-file. 
Default filenane is merge_file.pdf
"""
#!/usr/bin/env python
from PyPDF2 import PdfFileMerger
import argparse
import sys
import subprocess

def PDFmerge(pdfs, output):
    pdfMerger = PdfFileMerger()
#    pdfWriter = PdfFileWriter()

    # appending pdfs one by one 
    for pdf in pdfs:
        print(pdf)
        f = open(pdf,'rb')
        pdfMerger.append(pdf)
        #with open(pdf, 'rb') as f:
#        pdfReader = PdfFileReader(f)
#        print(pdfReader.numPages)
#        for pageNum in range(pdfReader.numPages):
#            pageObj = pdfReader.getPage(pageNum)
#            pdfWriter.addPage(pageObj)

        f.close()

	# writing combined pdf to output pdf file 
    pdfOutputfile = open(output,'wb')
    pdfMerger.write(pdfOutputfile)
    #pdfWriter.write(pdfOutputfile)
    pdfOutputfile.close()

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file', nargs='*')
    parser.add_argument('-o', '--output', default='merge_file.pdf', help='Relative or absolute path of the output PDF file, (default: merge_file.pdf)')
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after merging')
    args = parser.parse_args()
    pdfs = args.input
    PDFmerge(args.input, args.output)
    print('........................................')
    print('{} is written'.format(args.output))


    if args.open:
        if sys.platform == "win32":
            subprocess.call(["explorer.exe", args.output])
        else:
            subprocess.call(["evince", args.output])



if __name__ == "__main__": 
	# calling the main function 
	main()
