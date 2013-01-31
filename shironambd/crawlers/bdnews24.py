#!/usr/bin/env python
# encoding: utf-8
"""
bdnews24.py

Created by Caveman on 2012-12-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

import setup_django
from base import BaseCrawler
from datetime import datetime
from shironambd.home.models import News
	

BASE_URL = 'http://bangla.bdnews24.com/'
POLITICS_INDEX = 0
CRICKET_INDEX = 1
ENTERTAINMENT_INDEX = 2
SCIENCE_INDEX = 3
CAMPUS_INDEX = 4
BUSSINESS_INDEX = 5
TECHNOLOGY_INDEX = 6
LIFESTYLE_INDEX = 7
HEALTH_INDEX = 8
ENVIRONMENT_INDEX = 9


TOTAL_MOST_READ = 7
TOTAL_RECENT_STORIES = 7


NEWS_CATEGORIES = ['health','science','environment',
				'lifestyle','politics','sport','economy']
	

def iter_soup_build_news(soup):
	for news in soup:
		try:
			link = news.find('a')['href']
		except TypeError:
			link = news['href']
		title = news.text.replace('&#39;', "'")
		news = News()
		news.link = link
		news.title = title
		# news.published_at ?? 
		news.created_at = datetime.now()
		yield news

class BdNews24English(BaseCrawler):
	
	def get_tab_soup(self):
		soup = self.get_soup()
		tab_soup = soup.find('div', {'id':'tabs-2'})
		return tab_soup

	def get_lead_news(self):
		soup = self.get_soup()
		coulumns = soup.findAll('div', {'class':'column-1'})
		others_lead = coulumns[1].findAll('h3')
		for news in others_lead:
			print news.text	
		
	def get_latest_news(self):
		soup = self.get_soup()
		latests_soup = soup.find('div',{'id':'latest_news2'})
		latest_newses = latests_soup.findAll('a')
		for news in latest_newses:
			print news.text
		
	def most_read(self):
		tab_soup = self.get_tab_soup()
		raw_newses_titles = tab_soup.findAll('li')[3:TOTAL_MOST_READ+3]
		for news in raw_newses_titles:
			yield news.text
			
	def recent_stories(self):
		tab_soup = self.get_tab_soup()
		raw_newses_titles = tab_soup.findAll('li')[TOTAL_MOST_READ+3:]
		for news in raw_newses_titles:
			yield news.text	
		
	def get_categorized_news(self):
		for category in NEWS_CATEGORIES:
			self.url = BASE_URL+category 
			print 'GETTING ...%s NEWS' % category
			self.get_lead_news()
			print '------------------------'
		

if __name__ == '__main__':
	# bUrl = 'http://bdnews24.com/bangla'
	bUrl = 'http://bangla.bdnews24.com/'
	# bUrl = 'http://scrape.local/'
	# bUrl = 'http://bdnews24.com'
	bdN = BdNews24English(bUrl)
	# print bdN.recent_stories()
	# print bdN.get_lead_news(bdN.get_soup())
	bdN.get_categorized_news()
	# for n in bdN.recent_stories():
	# 		print n
	

