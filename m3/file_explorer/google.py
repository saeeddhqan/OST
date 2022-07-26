
from lxml import html
import requests
import json

url = 'https://www.google.com/search'

root = '//div[@class="g"]|//div[@class="g tF2Cxc"]|//div[@class="g Ww4FFb tF2Cxc"]'
a = './/div[@class="yuRUbf"]/a'
title = './/h3[1]'
snip = './/div[@data-content-feature="1"]|.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"]'
cite = './/div[@class="yuRUbf"]/a//cite'

def run(query, limit=3, count=10):
	pager = lambda x: (x - 1) * count

	page = 1
	params = {'q': query, 'start': pager(page), 'num': count, 'ie': 'utf-8', 'oe': 'utf-8'}
	headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
	_pages = ''
	attempts = 0
	while True:
		print(f'Searching through the {page}...')
		try:
			req = requests.get(url, params=params, headers=headers)
		except Exception as e:
			print(e)
			attempts += 1
			if attempts == limit:
				break
		else:
			if req.status_code in (503, 429):
				print('Google captcha triggered.')
				break
			if req.status_code in (301, 302):
				redirect = req.headers['location']
				req = requests.get(redirect, headers=headers)

			_pages += req.text
			open('test.html','w').write(_pages)
			page += 1
			params['start'] = pager(page)
			if page >= limit:
				break

	tree = html.fromstring(_pages)
	results = tree.xpath(root)
	outcome = []

	for i in results:
		result = {}
		link = i.xpath(a)
		result['href'] = link[0].get('href')
		result['title'] = link[0].xpath(title)[0].text_content().strip()
		if i is not None:
			if i.xpath(snip):
				result['content'] = i.xpath(snip)[0].text_content().strip()
			if i.xpath(cite):
				result['cite'] = i.xpath(cite)[0].text_content().strip()
		outcome.append(result)

	json.dump(outcome, open('results.json', 'w'))
	return outcome