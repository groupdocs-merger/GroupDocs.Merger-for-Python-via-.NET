# test_files.py
# This module defines paths to test files.

import os
from os.path import join
import platform
import inspect

license_path = "C:/Licenses/GroupDocs.Merger.Python_via_NET.lic"
sample_path = "./Examples/Resources/SampleFiles/"
output_path = "./Examples/Output/"

def get_sample_file_path(file_path):
    if platform.system() == 'Windows':
        return join(sample_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, sample_path, file_path)

def get_output_file_path(file_path):
    if platform.system() == 'Windows':
        return join(output_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, output_path, file_path)

sample_doc = get_sample_file_path("sample.doc")
sample_docx = get_sample_file_path("sample.docx")
sample_docm = get_sample_file_path("sample.docm")
sample_pptx = get_sample_file_path("sample.pptx")
sample_xlsx = get_sample_file_path("sample.xlsx")
sample_vsdx = get_sample_file_path("sample.vsdx")
sample_pdf = get_sample_file_path("sample.pdf")
sample_simple_pdf = get_sample_file_path("sample_simple.pdf")
sample_one = get_sample_file_path("sample.one")
sample_jpg = get_sample_file_path("sample.jpg")
sample_tiff = get_sample_file_path("sample.tiff")
sample_bmp = get_sample_file_path("sample.bmp")
sample_gif = get_sample_file_path("sample.gif")
sample_wav = get_sample_file_path("sample.wav")
sample_zip = get_sample_file_path("sample.zip")
sample_tar = get_sample_file_path("sample.tar")
sample_rar = get_sample_file_path("sample.rar")
sample_seven_zip = get_sample_file_path("sample.7z")
sample_epub = get_sample_file_path("sample.epub")
sample_html = get_sample_file_path("sample.html")
sample_txt = get_sample_file_path("sample.txt")
sample_png = get_sample_file_path("sample.png")

output_docx = get_output_file_path("output.docx")
output_pptx = get_output_file_path("output.pptx")
output_xlsx = get_output_file_path("output.xlsx")
output_vsdx = get_output_file_path("output.vsdx")
output_pdf = get_output_file_path("output.pdf")
output_one = get_output_file_path("output.one")
output_jpg = get_output_file_path("output.jpg")
output_tiff = get_output_file_path("output.tiff")
output_bmp = get_output_file_path("output.bmp")
output_wav = get_output_file_path("output.wav")
output_zip = get_output_file_path("output.zip")
output_tar = get_output_file_path("output.tar")
output_seven_zip = get_output_file_path("output.7z")
output_epub = get_output_file_path("output.epub")
output_html = get_output_file_path("output.html")
output_txt = get_output_file_path("output.txt")
output_png = get_output_file_path("output.png")