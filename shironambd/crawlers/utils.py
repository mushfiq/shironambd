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

#fix this: using django url validator
def validate_new_link(source, ref):
    if ref.find('http') == -1 and ref.find('/') != 0:
        link = source.website+'/'+ref
    elif ref.find('/') == 0:
        link = source.website+ref
    else:    
        link = s.find('a')['href']
    return link
    
def build_news_object(soup_news, source_name):
    s = soup_news.find('h2', {'class':'title'})
    source = Source.objects.get(name=source_name)
    n = News()
    n.title = s.find('a').text
    n.source = source
    ref = s.find('a')['href']
    n.link = validate_new_link(source, ref)
    return n

def is_valid(news_obj):
	if (len(News.objects.filter(link=news_obj.link))  > 0):
			return False
	return True

