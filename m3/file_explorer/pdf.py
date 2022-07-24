from PyPDF2 import PdfReader

def read_pdf(file):
	try:
		reader = PdfReader(file)
		txt = ''
		for i in range(len(reader.pages)):
			page = reader.pages[i]
			txt += page.extract_text()
	except Exception as e:
		print(file)
		return ''
	else:
		return txt

