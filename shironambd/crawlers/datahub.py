#!/usr/bin/env python
# encoding: utf-8
"""
mongohub.py

Created by Caveman on 2013-01-31.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os

import setup_django
from shironambd.home.models import News
from bdnews24 import BdNews24
from banglanews24 import BanglaNews24



def crawl_bdnews24():
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_lead_news()
	bdN.get_latest_news()
	bdN.get_most_read()
	bdN.get_recent_stories()
	bdN.get_categorized_news()

def crawl_bdnews_latest_news():
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_latest_news()
	

def crawl_banglanews24():
	bUrl = 'http://banglanews24.com/'
	bn24 = BanglaNews24(bUrl)
	bn24.get_lead_news()
	bn24.get_latest_news()
	bn24.get_categorized_news()
	bn24.get_best24()
	bn24.get_most_read()

def remove_duplicates():
	all_news_links = News.objects.values_list('link')
	distinct_links = set(all_news_links)
	duplicate_links = []
	for link in distinct_links:
		if len(News.objects.filter(link=link)) != 1:
			duplicate_links.append(link)
	print len(duplicate_links)
	for link in duplicate_links:
		if len(News.objects.filter(link=link)) > 1:
			# News.objects.filter(link=link)[0].delete()
			print News.objects.filter(link=link)

			

if __name__ == '__main__':
	# crawl_bdnews24()
	# crawl_banglanews24()
	# crawl_bdnews_latest_news()
	remove_duplicates()

