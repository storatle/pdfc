#!/usr/bin/env python
from PyPDF2.pdf import PageObject
from PyPDF2 import PdfFileReader, PdfFileWriter


reader = PdfFileReader(open("pg_0001.pdf",'rb'))
invoice_page = reader.getPage(0)
sup_reader = PdfFileReader(open("pg_0002.pdf",'rb'))
sup_page = sup_reader.getPage(0)  # We pick the second page here

translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight())
translated_page.mergeScaledTranslatedPage(sup_page, 1, 0, -400)  # -400 is approximate mid-page

translated_page.mergePage(invoice_page)

writer = PdfFileWriter()
writer.addPage(translated_page)

with open('out.pdf', 'wb') as f:
	writer.write(f)
