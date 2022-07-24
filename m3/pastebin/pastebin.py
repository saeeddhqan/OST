import google
import re
import requests

results = google.run('owasp site:pastebin.com', limit=1)
pages = []
page_results = ''
# removing ads
for i in range(len(results)):
	link = results[i]['href']
	search = re.search(r"https://pastebin\.com/([\w]+)", link)
	if search is None:
		del results[i]
	else:
		make_raw = f"https://pastebin.com/raw/{search.group(1)}"
		pages.append(make_raw)


for i in pages:
	try:
		req = requests.get(i)
	except Exception as e:
		print('Connection Error!')
	else:
		page_results += req.text

open('results.txt', 'w').write(page_results)