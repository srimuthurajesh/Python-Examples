import requests
from bs4 import BeautifulSoup

def web_crawler(url):
	source_code = requests.get(url)
	soup = BeautifulSoup(source_code.text,features="lxml")
	for link in soup.findAll('a'):
		href = 'http://wallpaperswide.com'+link.get('href') 
		title = link.string
		print(href)
		print(title)
		#web_crawler(href)

web_crawler('http://wallpaperswide.com')
