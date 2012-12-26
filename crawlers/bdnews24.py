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

class BdNews24(BaseCrawler):
	
	def get_lead_news(self):
		soup = self.get_soup()
		lead_news = soup.find('font',{'size':4})
		print lead_news.getString()
		
	def get_latest_news(self):
		soup = self.get_soup()
		latest_newses = soup.findAll('li',{'class':'latestnews'})
		latest_news = latest_newses[13:]
		print latest_newses


if __name__ == '__main__':
	bUrl = 'http://bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_lead_news()
	
	

