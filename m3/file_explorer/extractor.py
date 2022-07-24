import pdf
import os
import re

text = ''
for i in range(30):
	if os.path.exists(f"{i}.pdf"):
		print(f"{i}.pdf")
		text += pdf.read_pdf(f"{i}.pdf")

# reg = r'[\w\.]+@owasp.org'
reg2 = r'[\w\.]+@[A-z0-9\.]+'
users_reg = r'\b@[A-z0-9\-\_]+'

emails = re.findall(reg2, text)
users = re.findall(users_reg, text)
print(emails)
print(users)