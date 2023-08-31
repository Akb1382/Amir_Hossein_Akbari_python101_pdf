#! C:\Users\SamRayaneh\Desktop\Phython\AmirHosseinAkbari_python101_pdf\myenv\Scripts\python.exe

import os
os.chdir(r"C:\Users\SamRayaneh\Desktop\Phython\AmirHosseinAkbari_python101_pdf")

from pdf2image import convert_from_bytes

images = convert_from_bytes(open(r'C:\Users\SamRayaneh\Desktop\Phython\AmirHosseinAkbari_python101_pdf\flower.pdf', 'rb').read(
), poppler_path = r"C:\Users\SamRayaneh\Desktop\Phython\AmirHosseinAkbari_python101_pdf\Release-23.08.0-0\poppler-23.08.0\Library\bin")
for i in range(len(images)):
	# Save pages as images in the pdf
    images[i].save(f'image_{i+1}.png', 'PNG')

