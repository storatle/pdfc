#!/usr/bin/env python3

import argparse
import subprocess
import os.path
import sys
import shutil
from PyPDF2 import PdfFileReader

def combine(filename):
#    subprocess.call(["pdftk", filename, 'burst'])
    input1 = PdfFileReader(open('pg_0001.pdf', 'rb'))
    print(input1.getPage(0).mediaBox.getWidth())
   
    subprocess.call(["pdfjam", 'pg_0001.pdf', 'pg_0002.pdf', 'pg_0003.pdf', 'pg_0004.pdf', '--nup 2x2', '--outfile filename_out.pdf'])

   # subprocess.call([gs, '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
   #                 '-dPDFSETTINGS={}'.format(quality[power]),
   #                 '-dNOPAUSE', '-dQUIET', '-dBATCH',
   #                 '-sOutputFile={}'.format(output_file_path),
   #                  input_file_path]
   # )


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file')
    parser.add_argument('-c', '--compress', type=int, help='Compression level from 0 to 4')
    parser.add_argument('-b', '--backup', action='store_true', help="Backup the old PDF file")
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after compression')
    args = parser.parse_args()
    combine(args.input)

if __name__ == '__main__':
    main()
