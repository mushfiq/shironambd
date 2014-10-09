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
from shironambd.home.models import News, Source
# from bdnews24 import BdNews24
from banglanews24 import BanglaNews24
from jugantor import JugnatorCrawler
from palo import PAlo
from django.core.exceptions import MultipleObjectsReturned

from jugantor import JugnatorCrawler
from rss import RSSCrawler

def configire_logging():
	logging.basicConfig(format='%(asctime)s %(message)s',filename='logs/crawler.log',level=logging.DEBUG)
	    
def crawl_jugantor():
    logging.info("started crawling jugantor")
    
    source = Source.objects.get(name="jugantor")
    urls = source.urls
    for url in urls:
        jugantor = JugnatorCrawler(url)
        jugantor.process()
    
    logging.info("ended crawling jugantor")
    
        
def crawl_bdnews():
    logging.info("started crawling bdnews24")
    
    source = Source.objects.get(name="bdnews24")
    urls = source.urls
    for url in urls:
        import pdb;pdb.set_trace()
        rss = RSSCrawler(url)
        rss.process()

    logging.info("ended crawling bdnews24")



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
	#check next two methods for dom scraping!
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
    
#fix
def remove_broken_news_by_link(source_name):
    source = Source.objects.get(name=source_name)
    all_links = [news.link for news in News.objects.filter(source=source)]  
    # links = set(all_links)
    c = 0
    
    for link in all_links:
        if link.find('com//') > -1:
            try:
                dup = News.objects.get(link=link)
            except News.MultipleObjectsReturned:
                dup = News.objects.filter(link=link)
                
            
            except News.DoesNotExist:
               pass
             
            dup.delete()
            
            c+=1

    print "Total %d articles deleted" % c
    
	
if __name__ == '__main__':
    #url validation error
    crawl_palo()
    # remove_broken_news_by_link('ProthomAlo')
    # crawl_bdnews()
    # crawl_jugantor()

