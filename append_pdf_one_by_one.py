import PyPDF2

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
	pdfs = ['0000.pdf', 'out.pdf', 'out1.pdf','out2.pdf','out3.pdf','out4.pdf','out5.pdf','out6.pdf','out7.pdf','out8.pdf','out9.pdf','out10.pdf','out11.pdf','out12.pdf','out13.pdf', '0029.pdf']
	output = 'merge_file.pdf'
	PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__": 
	# calling the main function 
	main()