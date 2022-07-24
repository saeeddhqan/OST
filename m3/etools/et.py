import requests


def run(query):
	page = ''
	_json = {}
	url = f"https://www.etools.ch/partnerSearch.do?partner=Carrot2Json&query={query}&dataSourceResults=40&maxRecords=200&safeSearch=true&dataSources=all&language=en&country=web"

	headers = {
		'Host': 'www.etools.ch',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding':'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Cookie': 'JSESSIONID=5869A6F49B3AC96824823F52DE0CD263',
		'Upgrade-Insecure-Requests': '1',
		'Sec-Fetch-Dest': 'document',
		'Cache-Control': 'max-age=0'
	}

	try:
		req = requests.get(url, headers=headers)
	except Exception as e:
		print('Connection Error!')
	else:
		page = req.text
		try:
			_json = req.json()
		except Exception as e:
			pass

	resp = _json['response']['mergedRecords']
	# for r in resp:
	# 	print(r['title'])
	# 	print(r['text'])
	# 	print(r['url'])
	# 	print()
	return resp