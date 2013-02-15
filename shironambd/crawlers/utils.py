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
from shironambd.home.models import News


def build_news_object(soup_news):
	n = News()
	n.title = soup_news.find('a').text
	n.link = soup_news.find('a')['href']
	return n

def is_valid(news_obj):
	if len(News.objects.filter(link=news_obj.link)) == 0:
		return True
	return False

