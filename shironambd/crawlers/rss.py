#!/usr/bin/env python
# encoding: utf-8
"""
bdnews24.py

Created by Caveman on 2012-12-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from base import BaseCrawler
from datetime import datetime

import setup_django
from shironambd.home.models import News, Source


def clean_date(date_string):
    date_string = date_string.replace('.0', '')
    date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S") 
    return date_obj



class RSSCrawler(BaseCrawler):
    
    def __init__(self, url):
        self.url = url
        self.source = Source.objects.get(urls=url)
        
    def get_title(self, entry):
        return entry.title    
    
    def get_link(self, entry):
        return entry.guid
        
    def get_category(self, entry):
        return 
        
    def get_author(self, entry):
        return entry.authorname
        
    def get_published_at(self, entry):
        return clean_date(entry.published)

    def process(self):
    	entries = self.get_entries()
        # latest_newses = soup.findAll('item')
    	for entry in entries:
            news = News()
            try:
                news.link = entry.guid
                news.source = self.source
                news.title  = self.get_title(entry)
                news.author = self.get_author(entry)
                news.published_at = self.get_published_at(entry)
                self.do_save(news)
                # print "goo"
            except Exception as e:
                print "Error Occured!", e
                pass
			# self.do_save(iter_soup_build_news(news), ['latest_news'])


if __name__=='__main__':
    # s = Source.objects.get(urls="http://bangla.bdnews24.com/?widgetName=rssfeed&widgetId=1151&getXmlFeed=true")
    url = "http://bangla.bdnews24.com/?widgetName=rssfeed&widgetId=1151&getXmlFeed=true"
    # url = "http://www.jugantor.com/rss.xml"
    r = RSSCrawler(url)
    r.process()
    # print r