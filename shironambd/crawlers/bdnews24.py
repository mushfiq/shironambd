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
	

BASE_URL = 'http://bdnews24.com/'
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
		
def build_news_object(soup_news):
	# news_object = {}
	# title = 
	# news_object['title'] = soup_news.text.encode('utf8')
	n = News()
	n.title = soup_news.find('a').text
	n.link = soup_news.find('a')['href']
	return n
	# print repr(soup_news.text.decode('utf8'))
	# print news_object
	# news_object.update({'title':str(title)})
	# news_object.update({'link':soup_news.find('a')['href']})
	# return news_object
		

class BdNews24(BaseCrawler):
	
	def __inti__(self):
		self.get_lead_news()
		self.get_lead_news()
		self.get_latest_news()
		self.get_most_read()
		self.get_recent_stories()
		self.get_categorized_news()
		
		
	def do_save(self, news_object, tags=None, category=None):
		if tags != None:
			news_object.tags = tags
		if category != None:
			news_object.category = category
		try:
			print news_object
			news_object.save()
		except Exception, e:
			print "Error Occured! %s" % e
		
	def get_tab_soup(self):
		soup = self.get_soup()
		tab_soup = soup.find('div', {'id':'tabs-2'})
		return tab_soup

	def get_lead_news(self, is_categorized=False):
		soup = self.get_soup()
		coulumns = soup.findAll('div', {'class':'column-1'})
		others_lead = coulumns[1].findAll('h3')
		for news in others_lead:
			if is_categorized != True:
				self.do_save(build_news_object(news), ['lead_news'])
			else:
				yield build_news_object(news)
		
	def get_latest_news(self):
		soup = self.get_soup()
		latests_soup = soup.find('div',{'id':'latest_news2'})
		latest_newses = latests_soup.findAll('li')
		for news in latest_newses:
			self.do_save(build_news_object(news), ['latest_news'])
					
	def get_most_read(self):
		tab_soup = self.get_tab_soup()
		raw_newses_titles = tab_soup.findAll('li')[3:TOTAL_MOST_READ+3]
		for news in raw_newses_titles:
			self.do_save(build_news_object(news), ['most_read'])

	def get_recent_stories(self):
		tab_soup = self.get_tab_soup()
		raw_newses_titles = tab_soup.findAll('li')[TOTAL_MOST_READ+3:]
		for news in raw_newses_titles:
			self.do_save(build_news_object(news), ['recent_stories'])
		
	def get_categorized_news(self):
		for category in NEWS_CATEGORIES:
			self.url = BASE_URL+category 
			print 'GETTING ...%s NEWS' % category
			for news in self.get_lead_news(is_categorized=True):
				self.do_save(news, tags="test", category=category)
		

if __name__ == '__main__':
	# bUrl = 'http://bdnews24.com/bangla'
	bUrl = 'http://bangla.bdnews24.com/'
	# bUrl = 'http://scrape.local/'
	# bUrl = 'http://bdnews24.com'
	bdN = BdNews24(bUrl)
	bdN.get_recent_stories()
	# print bdN.recent_stories()
	# print bdN.get_lead_news(bdN.get_soup())
	# bdN.get_categorized_news()
	# for n in bdN.recent_stories():
	# 		print n
	

