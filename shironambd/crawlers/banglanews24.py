#!/usr/bin/env python
# encoding: utf-8
"""
banglanews24.py

Created by Caveman on 2013-01-01.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


from base import BaseCrawler
from datetime import datetime
# from shironambd.home.models import News
from utils import build_news_object,is_valid

BASE_URL = 'http://banglanews24.com/'
TOTAL_MOST_READ = 7
TOTAL_RECENT_STORIES = 7


NEWS_CATEGORIES = {
'politics':'http://www.banglanews24.com/categorizednews.php?newtype=3',
'natinal':'http://www.banglanews24.com/categorizednews.php?newtype=15',
'ecoomy':'http://www.banglanews24.com/categorizednews.php?newtype=2'
}

def clean_text(text):
	return text.replace('&nbsp;', '')
	


class BanglaNews24(BaseCrawler):
	
	def get_tabs_news(self):
		soup = self.get_soup()
		return soup.find('div', {'class':'D01Tabs'})
	
	def process_and_save(self, news):
		news_object = build_news_object(news)
		if is_valid(news_object):
			news_object.link = BASE_URL+str(news_object.link)
			# print news_object
			self.do_save(news_object)
		
	
	def get_lead_news(self):
		soup = self.get_soup()
		raw_lead = soup.find('div',{'id':'eMythSlide'})
		lead_soup = raw_lead.findAll('li')
		for news in lead_soup:
			self.process_and_save(news)
			
	
	def get_latest_news(self):
		tabs = self.get_tabs_news()
		latest_soup = tabs.find('div',{'id':'tab1'})
		latest_news = latest_soup.findAll('li')
		for news in latest_news:
			self.process_and_save(news)
			
	def get_best24(self):
		tabs = self.get_tabs_news()
		
		best_24_soup = tabs.find('div', {'id':'tab2'})
		best_24_news = best_24_soup.findAll('li')
		for news in best_24_news:
			self.process_and_save(news)
			
	def get_most_read(self):
		tabs = self.get_tabs_news()
		most_read_soup = tabs.find('div', {'id':'tab3'})
		most_read_news = most_read_soup.findAll('li')
		if most_read_news:
			for news in most_read_news:
				# print news
				self.process_and_save(news)
		else:
			return None
		
		
	def get_categorized_news(self):
		for news_category,url in NEWS_CATEGORIES.iteritems():
			self.url = url
			soup = self.get_soup()
			categorized_news = soup.findAll('li', {'class':'liHead'})
			print "Geting %s News" % news_category
			for news in categorized_news:
				self.process_and_save(news)

if __name__ == '__main__':
	b_url = 'http://banglanews24.com/'
	BN24 = BanglaNews24(b_url)
	BN24.get_best24()