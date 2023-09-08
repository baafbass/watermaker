import PyPDF2

with open('twopage.pdf','rb') as file: # we use 'rb' because we want to read a binary. The pdf is in a format of binary
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	print(reader.getPage(0))
	print(reader.getPage(1))
	#print(reader.rotate(180)) # we will get an error. because the object 'reader' can not be rotated. we need to get the page to be rotated.
	page = reader.getPage(0)
	print(page.rotate(180))