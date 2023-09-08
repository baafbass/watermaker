import PyPDF2

with open('dummy.pdf','rb') as file: # we use 'rb' because we want to read a binary. The pdf is in a format of binary
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	page.rotateCounterClockwise(90)

	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf','wb') as new_file:
		writer.write(new_file)