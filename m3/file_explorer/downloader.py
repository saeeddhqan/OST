import requests
import concurrent.futures
import google

# files = open('files.txt').read().split()
files = google.run('ext:pdf blackhat')
files = [x['href'] for x in files]

def download(i, file):
	f = requests.get(file)
	if f.status_code == 200:
		open(f"{i}.pdf", 'wb').write(f.content)
	print('.'*i, end='\r')


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
	[executor.submit(download, i, files[i]) for i in range(len(files))]