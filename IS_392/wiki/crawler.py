from threading import Thread
import urllib2
import urlparse
from lxml import etree
import time

startUrl = ['https://en.wikipedia.org/wiki/Data_mining','https://en.wikipedia.org/wiki/Data_science']
relWords = ['data', 'mining', 'science', 'mine', 'python', 'regression', 'classification', 'dimension', 'cluster', 'reduction']
def checkPage(words,text):
	count = 0
	for x in words:
		if count >=2:
			return True
		if x.lower() in text.lower():
			count +=1
	return False

def savePage(url, text):
	name = url[url.rfind("/"):]
	with open("html/"+str(name)+".html", 'w+') as f:
		f.write(text)
	f.closed
	with open("crawled_pages.txt", 'a+') as t:
		t.write(url+"\n")
	t.closed

def get_links(html):
	"""Return a list of links from html"""
	try:
		root = etree.fromstring(html)
		return [ b.get('href') for b in root.iterfind(".//a") ]###webpage_regex.findall(html)
	except Exception as e:
		print e



def link_crawler(seed_url, wordlist):
	crawl_queue = list(seed_url)
	total = 0
	# keep track which URL's have seen before
	seen = list(crawl_queue)
	while crawl_queue:
		if total >= 600:
			with open("crawl_queue.txt", 'w') as f:
				f.write(crawl_queue)
			break
		url = crawl_queue.pop(0)
		html = download(url)
		try:
			if checkPage(wordlist, html):
				savePage(url, html)
				total +=1
			for href in get_links(html):
				try:
					if href.find('/wiki/') == 0 :
						link = "https://en.wikipedia.org"+href
						if link not in seen and link.find("#") == -1:
							seen.append(link)
							crawl_queue.append(link)
				except Exception as e:
					print e
		except Exception as e:
					print e


def download(url, user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', proxy='http://www.hidemyip.ml/', num_retries=2):
	time.sleep(1)
	print 'Downloading:', url
	with open("crawled_pages.txt", 'a+') as f:
		f.write(url+"\n")
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	opener = urllib2.build_opener()
	if proxy:
		proxy_params = {urlparse.urlparse(url).scheme: proxy}
		opener.add_handler(urllib2.ProxyHandler({'http': 'http://107.151.152.218:80'}))
		try:
			html = opener.open(request).read()
		except urllib2.URLError as e:
			print 'Download error:', e.reason
			html = None
			if num_retries > 0:
				if hasattr(e, 'code') and 500 <= e.code < 600:
					# retry 5XX HTTP errors
					html = download(url, user_agent, proxy, num_retries-1)
	return html

link_crawler(startUrl,relWords)
