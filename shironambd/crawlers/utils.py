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
# from banglanews24 import BASE_URL


def build_news_object(soup_news, source_name):
	# import pdb;pdb.set_trace()

	s = soup_news.find('h2', {'class':'title'})
	source_object = Source.objects.get(name=source_name)
	n = News()
	n.title = s.find('a').text
	n.link = s.find('a')['href']
	n.source = source_object
	return n

def is_valid(news_obj):
	if (len(News.objects.filter(link=news_obj.link))  > 0):
			return False
	return True

