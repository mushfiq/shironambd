#!/usr/bin/env python
# encoding: utf-8
## -*- coding: utf-8 -*-
"""
palo.py

Created by Caveman on 2013-03-07.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
import logging

logging.basicConfig(format='%(asctime)s %(message)s',filename='logs/crawler.log',level=logging.DEBUG)

from pyquery import PyQuery as pq
from BeautifulSoup import BeautifulSoup
from base import BaseCrawler
from utils import build_news_object
from utils import is_valid



BASE_URL = 'http://prothom-alo.com'

LEAD_NEWS_DIV_IDS = ['div_1242', 'div_1245']

NEWS_CATEGORIES = ['sports','entertainment','technology','national',
				'international','lifestyle','economy', 'technology_research', 'art_and_literature']
				
LIFESTYLE_SUB_CATEGORIES = ['occupation','travel','advice','recipe','fashion']

SOURCE_NAME = 'ProthomAlo'
				
class PAlo(BaseCrawler):
	
	
	def soup_to_news(self):
		soup = self.get_soup()
		if soup != None:
			return  soup.findAll('h2', {'class':'title'})
		return None
		
	def process_and_save(self, all_news, tags=None, category=None):
		print "HERE I AM"
		for news in all_news:
			news_object = build_news_object(news, SOURCE_NAME)
			try:
				if(self.do_save(news_object, tags=tags, category=category)):
					print "saved"
			except Exception,e:
				logging.error("Error Ocurred! %s" %e)
				print "Error",e
				pass
			# print title.text_content().encode('utf-8')
	def get_lead_news(self):
		soup = self.get_soup()
		for div_id in LEAD_NEWS_DIV_IDS:
			div_soup = soup.find('div', {'id':div_id})
			self.soup = div_soup
			all_news = self.soup_to_news()
			self.process_and_save(all_news, tags=['lead_news'])
				
	def get_featured_news(self):
		self.url = BASE_URL+'/home/featured'
		self.soup = self.get_soup()
		all_news = self.soup_to_news()
		self.process_and_save(all_news, tags=['featured'])
		
	def get_categorized_news(self):
		for category in NEWS_CATEGORIES:
			if category != 'lifestyle':
				self.url = BASE_URL+'/'+category
				# soup = self.get_soup()
				all_news = self.soup_to_news()
				if all_news != None:
					self.process_and_save(all_news, category=category)
			else:
				for sub_life_style in LIFESTYLE_SUB_CATEGORIES:
					self.url = BASE_URL+'/lifestyle_'+sub_life_style
					all_news = self.soup_to_news()
					self.process_and_save(all_news, tags=['lifestyle_'+sub_life_style], category=category)
					
