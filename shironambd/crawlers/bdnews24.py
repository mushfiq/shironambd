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
		main_box = soup.find('div',{'id':'thdivbox'})
		latest_newses = main_box.findAll('li',{'class':'latestnews'})
		latest_news = latest_newses[13:]
		for news in latest_newses:
			print news.text
		# print latest_news[1].text
		# for news in latest_news:
		# 		yield news
		
	def get_box_news(self):
		soup = self.get_soup()
		box_soup_left = soup.findAll('div',{'id':'hmdivbox1'})
		box_soup_right = soup.findAll('div',{'id':'hmdivbox2'})
		box_left = []
		box_right = []
		for box in box_soup_left:
			box_left.append(box.find('span').text)
		
		for box in box_soup_right:
			box_right.append(box.find('span').text)
		
		return box_left+box_right
			

if __name__ == '__main__':
	bUrl = 'http://scrape.local/'
	bdN = BdNews24(bUrl)
	bdN.get_box_news()
	
	

