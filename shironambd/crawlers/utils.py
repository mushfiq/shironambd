#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Created by Caveman on 2012-12-27.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

import setup_django
from shironambd.home.models import News, Source

def build_news_object(soup_news, source_name):
    s = soup_news.find('h2', {'class':'title'})
    source_object = Source.objects.get(name=source_name)
    n = News()
    n.title = s.find('a').text
    n.source = source_object
    ref = s.find('a')['href']
    if ref.find('http') == -1:
        n.link = source_object.website+'/'+ref
    else:    
        n.link = s.find('a')['href']
        print n.link

    return n

def is_valid(news_obj):
	if (len(News.objects.filter(link=news_obj.link))  > 0):
			return False
	return True

