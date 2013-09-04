#!/usr/bin/env python
# encoding: utf-8
"""
mongohub.py

Created by Caveman on 2013-01-31.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import logging

import setup_django
from shironambd.home.models import News
from bdnews24 import BdNews24
from banglanews24 import BanglaNews24
from palo import PAlo
from django.core.exceptions import MultipleObjectsReturned


def configire_logging():
	logging.basicConfig(format='%(asctime)s %(message)s',filename='crawler.log',level=logging.DEBUG)
	
def crawl_bdnews24():
	logging.info("started bdnews24 crawling on ")
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_lead_news()
	bdN.get_latest_news()
	bdN.get_most_read()
	bdN.get_recent_stories()
	bdN.get_categorized_news()
	logging.info("crawling ended!")

def crawl_bdnews_latest_news():
	logging.info("started bdnews24 latest crawling on ")
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_latest_news()
	logging.info("crawling ended!")
	
	

def crawl_banglanews24():
	logging.info("started banglanews24 crawling on ")
	bUrl = 'http://banglanews24.com/'
	bn24 = BanglaNews24(bUrl)
	bn24.get_lead_news()
	bn24.get_latest_news()
	bn24.get_categorized_news()
	bn24.get_best24()
	bn24.get_most_read()
	logging.info("crawling ended!")
	
	
def crawl_palo():
	logging.info("started Prothom ALo crawling.")
	pUrl = 'http://prothom-alo.com'
	palo = PAlo(pUrl)
	palo.get_lead_news()
	palo.get_featured_news()
	palo.get_categorized_news()
	logging.info("crawling ended!")

def remove_duplicates_by_link():
	all_news_links = News.objects.values_list('link')
	counter = 0
	for link in all_news_links:
		try:
			News.objects.get(link=link)
		except News.MultipleObjectsReturned:
			dup = News.objects.filter(link=link)
			dup[0].delete()
			counter+=1
		
	print "Total %d news deleted!" % counter
	
	return 
	
def remove_duplicates_by_title():
	all_news_links = News.objects.values_list('title')
	counter = 0
	for title in all_news_links:
		try:
			News.objects.get(title=title)
		except News.MultipleObjectsReturned:
			dup = News.objects.filter(title=title)
			dup[0].delete()
			counter+=1
		
	print "Total %d news deleted!" % counter
	
	return
	
if __name__ == '__main__':
	# crawl_bdnews24()
	crawl_banglanews24()
	# remove_duplicates_by_title()
	# crawl_bdnews_latest_news()
	# crawl_palo()
	# remove_duplicates()

