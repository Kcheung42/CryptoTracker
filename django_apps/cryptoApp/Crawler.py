# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Crawler.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/11 16:54:54 by kcheung           #+#    #+#              #
#    Updated: 2018/02/28 12:23:59 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3

'''
This Script will Scrape coinmarketcaps website for all Coins and USD price.
Data will be saved in a CSV formated file

This example implements a Queue and Debug Logging
'''
from __future__ import unicode_literals
from django.conf import settings
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from queue import Queue
import threading
import django
import os
import sys
import logging

script_path = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(script_path,'..','..'))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_config.settings.local")
django.setup()
from django_apps.cryptoApp.models import Crypto

#1 debug =detailed info
#2 info =detailed info
#3 warning =detailed info
#4 error =detailed info
#5 critical =detailed info

class Crawler:
	logging.basicConfig(filename='WebScraperlogfile.log',level=logging.DEBUG,
						format='[%(levelname)s] (%(threadName) - 10s) %(message)s',
						)

	def get_coin(self, page):
		container = page.findAll("div", {"class" : "row bottom-margin-1x"})
		container = container[0]
		symbol = container.findAll("small", {"class" : "bold hidden-xs"})[0].text
		symbol = symbol.strip('()')
		return(symbol)

	def get_price(self, page):
		container = page.findAll("div", {"class" : "row bottom-margin-1x"})
		container = container[0]
		price = container.findAll("span", {"id" : "quote_price"})[0]["data-usd"]
		return(price)

	def get_img(self, page):
		container = page.findAll("div", {"class" : "row bottom-margin-1x"})
		container = container[0]
		img = container.findAll("img")[0]["src"]
		return(img)

	def get_tool(self, page):
		container = page.findAll("div", {"id" : "tools"})
		container = container[0]
		tool_script = container.findAll("textarea", {"class" : "form-control"})[0].text
		tool_script = tool_script.strip()
		return(tool_script)

	def get_banner(self, page):
		container = page.findAll("div", {"class" : "row bottom-margin-1x"})
		container = container[0]
		ret = {}
		n = container.findAll("h1")[0].text.strip(' ')
		img = container.findAll("img")[0]["src"]
		pr = container.findAll("span", {"id" : "quote_price"})[0]["data-usd"]
		symb = container.findAll("small", {"class" : "bold hidden-xs"})[0].text.strip('()')
		ret["name"] = n
		ret["symbol"] = symb
		ret["image"] = img
		ret["price"] = pr
		return (ret)

	def worker(self, q):
		# print(threading.currentThread().getName(), 'starting')
		logging.debug('starting')
		while not q.empty():
			url = q.get()
			page_html = urlopen(url).read()
			page_soup = soup(page_html, "html.parser")
			# coin = self.get_coin(page_soup)
			# price = self.get_price(page_soup)
			# img = self.get_img(page_soup)
			banner = self.get_banner(page_soup)
			name = banner['name']
			symbol = banner['symbol']
			image = banner['image']
			price = banner['price']
			try:
				price = float(price)
			except:
				price = 0
			tool_script = self.get_tool(page_soup)
			# print(name + ":" + symbol  + " : " + str(price) + " : " + image + " : " + tool_script)
			new_entry, created = Crypto.objects.update_or_create(
				symbol = symbol,
				defaults = {
					'name' : name,
					'image' : image,
					'price' : price,
					'tool' : tool_script,
				}
			)
			if created:
				print("created new entry:" + symbol)
			else:
				print("update:{} = {}".format(symbol, price))
			q.task_done()
		# print(threading.currentThread().getName(), 'Exiting')
		logging.debug('exiting')

	def initialScrape(self):
		index_html = urlopen('https://coinmarketcap.com/all/views/all/').read()
		index_soup = soup(index_html, "html.parser")
		containers = index_soup.findAll("a", {"class" : "currency-name-container"})
		links = []
		for container in containers:
			links.append(container['href'])

	# Put links into Queue for processing
		q = Queue()
		base = 'https://coinmarketcap.com'
		links = list(map(lambda x: base+x, links))
		for l in links:
			q.put(l)
		return (q)

	def __init__(self):
		startTime = datetime.now()
		q = self.initialScrape()
		for i in range(10):
			t = threading.Thread(name='worker:'+ str(i), target=self.worker,args=(q,))
			t.start()
		q.join()
		# f.close()
		print (datetime.now() - startTime)

# if __name__ == '__main__':
# 	Scraper()
