#!/usr/bin/env python
# encoding: utf-8
"""
base.py

Created by Caveman on 2012-12-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import requests
from BeautifulSoup import BeautifulSoup

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
		
			
		


if __name__ == '__main__':
	main()

