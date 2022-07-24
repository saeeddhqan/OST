

import requests


def run(query, limit=3):
	limit = limit

	page = ''
	_json = []
	url = f"https://api.qwant.com/v3/search/web"
	params = {'q': query, 'count': '10', 'locale': 'en_GB', 'offset': '0'}
	paging = lambda x: (x-1)*10
	count = 1

	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding':'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Sec-Fetch-Dest': 'document',
		'Cache-Control': 'max-age=0'
	}

	while True:
		print(count)
		try:
			req = requests.get(url, params=params, headers=headers)
		except Exception as e:
			print('Connection Error!')
		else:
			if req.status_code == 429:
				print('too many requests')
				break
			page += req.text
			try:
				_json.append(req.json())
			except Exception as e:
				pass
			else:
				if limit == count:
					break
				count += 1
				params['offset'] = str(paging(count))



	results = []
	for p in _json:
		resp = p.get('data', {}).get('result', {}).get('items', {})
		if resp:
			resp = resp.get('mainline', {})
		for i in resp:
			inside_mainline = i.get('items', {})
			for j in inside_mainline:
				a = j['url']
				r = {
					'url': a,
					'title': j['title'],
					'text':  '-' if 'desc' not in j else j.get('desc')
				}
				results.append(r)
	return results
