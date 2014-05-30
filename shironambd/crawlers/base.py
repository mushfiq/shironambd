#!/usr/bin/env python
# encoding: utf-8
"""
base.py

Created by Caveman on 2012-12-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""
import logging
import sys
import os
import requests
from BeautifulSoup import BeautifulSoup
from utils import is_valid

class BaseCrawler(object):
	
	def __init__(self, url):
		self.url = url
		
	def get_response(self):
		response = requests.get(self.url)
		return response
	
	def get_soup(self):
		if self.get_response().status_code == 200:
			soup = BeautifulSoup(self.get_response().content)
			return soup
		return None
		
	def do_save(self, news_object, tags=None, category=None):
		if tags != None:
			news_object.tags = tags
		if category != None:
			news_object.category = category
		try:
			if is_valid(news_object):
				news_object.save()
				return True
			else:
				logging.warn('Already exists!')
				return False
		except Exception, e:
			# import pdb;pdb.set_trace()
			logging.error("Error Occured! %s" % e)
			print "Error Occured! %s" % e
			pass
		


if __name__ == '__main__':
	main()

