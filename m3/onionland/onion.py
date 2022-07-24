from lxml import html
import requests
import re

query = 'amazon'
limit = 3
pages = ''
urls = [f'https://onionlandsearchengine.com/search?q={query}&page={i}' for i in range(1, limit+1)]
max_attempt = len(urls)
plen = 0
headers = {
	"Host": "onionlandsearchengine.com",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"Alt-Used": "onionlandsearchengine.com",
	"Connection": "keep-alive",
	"Cookie": "_ga=GA1.1.1924848199.1654452149; _hjSessionUser_2993985=eyJpZCI6ImU2YjUxMGU3LWUyYzgtNTMxYy05YTkwLTU2ZDlmMjc5N2MzZiIsImNyZWF0ZWQiOjE2NTQ0NTIxNTA1OTcsImV4aXN0aW5nIjp0cnVlfQ==; _ga_TS3XCR2TKW=GS1.1.1657661681.2.1.1657661773.0; 3bb_session=eyJpdiI6Ijh2b09BRVN2K0xOSk9RbFFiTFRpc0E9PSIsInZhbHVlIjoiMW50M1JjS0xscVR5akM5a1pNaDNOcEZVOWR2cTRsM1NYNkJPaXZ4K2ZMazE4bHQwd09UWUtPWjl4cThvN1VLdSIsIm1hYyI6ImRjODVlNGMwZDE1YTE2YzVhMWVkZmQ0MTNjNWJkYjY5M2M4MWE5ZGE4NDhlYWJmYTM5ODY3NmVkZTk3ODRiMWIifQ%3D%3D; _hjIncludedInSessionSample=0; _hjSession_2993985=eyJpZCI6IjQ3NmM4NWE4LWU2MzgtNDQ5My1hMjRmLTMyZmQ1ZjkwMjc2YSIsImNyZWF0ZWQiOjE2NTc2NjE2ODI3NTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0",
	"Upgrade-Insecure-Requests": "1"
}


for url in range(len(urls)):
	try:
		req = requests.get(urls[url], headers=headers)
	except Exception as e:
		print('Connection error!')
		max_attempt -= 1
		if max_attempt == 0:
			print('we lost onionlandsearchengine!')
			break
	else:
		pages += req.text
		if plen == 0:
			plen = len(re.findall('<span class="page">', req.text))
		if plen-1 == url:
			break

root = '//div[@class="result-block"]'
link = './/div[@class="link"]'
title = './/div[@class="title"]'
desc = './/div[@class="desc"]'

tree = html.fromstring(pages)
results = tree.xpath(root)
json_output = []

for result in results:
	r = {}
	r['link'] = result.xpath(link)[0].text_content().strip()
	r['title'] = result.xpath(title)[0].text_content().strip()
	r['description'] = result.xpath(desc)[0].text_content().strip()
	json_output.append(r)

print(json_output)
import json

json.dump(json_output, open('results.json', 'w'), indent=4)