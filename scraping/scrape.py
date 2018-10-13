import urllib
from bs4 import BeautifulSoup
import codecs
import locale
import json

f = open("urls.txt")
f = f.read()
urls = f.split()

for i in range(len(urls)):
	data = {}
	page = urllib.urlopen(urls[i])
	page = page.read()
	soup = BeautifulSoup(page, 'html.parser')
#soup.prettify()
	main = soup.findAll("div", {"class": "detail-view"})
	for r in main:
		print r.text.encode('utf-8')
	
	#sub = main.findAll("div", {"class": "detail-panel"})
	#assert(len(sub)==5)
	'''for x in main :
		data[x.h4.get_text()] = x.p.get_text()
                print x.p.get_text().encode('utf-8')
		with open("data/{}.json".format(i),"w") as out_file:
				json.dump(data,out_file)'''
	print("{} done".format(i))
