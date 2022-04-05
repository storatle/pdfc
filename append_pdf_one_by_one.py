import PyPDF2
import argparse

def PDFmerge(pdfs, output):
	pdfMerger = PyPDF2.PdfFileMerger()
	# appending pdfs one by one 
	for pdf in pdfs:
		with open(pdf, 'rb') as f:
			pdfMerger.append(f) 
		  
	# writing combined pdf to output pdf file 
	with open(output, 'wb') as f:
		pdfMerger.write(f) 

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file', nargs='*')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file')
    parser.add_argument('-c', '--compress', type=int, help='Compression level from 0 to 4')
    parser.add_argument('-b', '--backup', action='store_true', help="Backup the old PDF file")
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after compression')
    args = parser.parse_args()
    pdfs = args.input
    print(args.input)
    output = 'merge_file.pdf'
    PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__": 
	# calling the main function 
	main()
