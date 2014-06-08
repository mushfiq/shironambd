#!/usr/bin/env python
# encoding: utf-8
"""
bdnews24.py

Created by Caveman on 2012-12-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from rss import RSSCrawler
from datetime import datetime
from utils import build_news_object

import setup_django
from shironambd.home.models import News

BASE_URL = 'http://bdnews24.com/bangla'
TOTAL_MOST_READ = 7
TOTAL_RECENT_STORIES = 7


NEWS_CATEGORIES = ['health','science','environment',
				'lifestyle','politics','sport','economy']

SOURCE_NAME = 'BDNEWS24.COM'

def iter_soup_build_news(soup):
	# import pdb;pdb.set_trace();
	try:
		link = soup.find('a')['href']
	except TypeError:
		link = soup['href']

	title = soup.text.replace('&#39;', "'")

	news = News()
	news.link = link
	news.title = title
	# news.published_at ??
	news.created_at = datetime.now()
	# print news
	return news
		


# class BdNews24(RSSCrawler):
#     
#         def get_published_at(self, entry):
#             pub_str = entry.published[:-6] if entry.has_key('published') else None
#             published_at = datetime.strptime(pub_str, '%a, %d %b %Y, %H:%M:%S') 
#             return published_at
#     
#         def process(self):
#             entries = self.get_entries()
# 
#             for entry in entries:
#                 news = News()
#                 try:
#                     news.link = entry.guid
#                     news.source = self.source
#                     news.title  = self.get_title(entry)
#                     news.published_at = self.get_published_at(entry)
#                     self.do_save(news)
#                 except Exception as e:
#                     print "Error Occured!", e
#                     pass
#             return
        
if __name__=='__main__':
    url = "http://bangla.bdnews24.com/?widgetName=rssfeed&widgetId=1151&getXmlFeed=true"
    b = RSSCrawler(url)
    b.process()
	