#!/usr/bin/env python
# encoding: utf-8
## -*- coding: utf-8 -*-
"""
palo.py

Created by Caveman on 2013-03-07.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

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
				


class PAlo(BaseCrawler):
	
	# def __init__(self):
	# 		self.call_me()
		
	# def get_soup(self):
	# 	if self.get_response().status_code == 200:
	# 		soup = pq(self.get_response().content)
	# 		return soup
		
	def get_news(self, category):
		soup = self.get_soup()
		# titles = soup('h2.title')
		titles = soup.findAll('h2', {'class':'title'})
		# print titles.eq(2).html()
		# print titles.eq(3).html()
		for news in titles:
			news_object = build_news_object(news)
			try:
				self.do_save(news_object, tags=["category_news"], category=category)
				print "saved"
			except Exception,e:
				print "Error",e
				pass
			# print title.text_content().encode('utf-8')
			
	def get_lead_news(self):
		soup = self.get_soup()
		for div_id in LEAD_NEWS_DIV_IDS:
			div_soup = soup.find('div', {'id':div_id})
			titles = div_soup.findAll('h2', {'class':'title'})
			for title in titles:
				# print title.text
				print title
		
	def get_categorized_news(self):
		for category in NEWS_CATEGORIES:
			if category != 'lifestyle':
				self.url = BASE_URL+'/'+category
				print self.url
				self.get_news(category)
			else:
				for sub_life_style in LIFESTYLE_SUB_CATEGORIES:
					self.url = BASE_URL+'/lifestyle_'+sub_life_style
					print self.url
					self.get_news(category)
					

	


if __name__ == '__main__':
	p = PAlo(BASE_URL)
	p.get_categorized_news()

