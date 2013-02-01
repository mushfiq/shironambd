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
from utils import build_news_object

BASE_URL = 'http://banglanews24.com/'
TOTAL_MOST_READ = 7
TOTAL_RECENT_STORIES = 7

def clean_text(text):
	return text.replace('&nbsp;', '')

class BanglaNews24(BaseCrawler):
	
	def get_lead_news(self):
		soup = self.get_soup()
		raw_lead = soup.find('div',{'id':'eMythSlide'})
		lead_soup = raw_lead.findAll('li')
		for news in lead_soup:
			try:
				n = build_news_object(news)
				n.title = clean_text(n.title)
				print n
			except Exception,e:
				print "Error Occured! %s" %e
				pass
				
	def get_tabs_news(self):
		soup = self.get_soup()
		return soup.find('div', {'class':'D01Tabs'})
	
	def get_latest_news(self):
		tabs = self.get_tabs_news()
		latest_soup = tabs.find('div',{'id':'tab1'})
		latest_news = latest_soup.findAll('li')
		for news in latest_news:
			return build_news_object(news)
			
		
		


if __name__ == '__main__':
	b_url = 'http://banglanews24.com/'
	BN24 = BanglaNews24(b_url)
	BN24.get_latest_news()

