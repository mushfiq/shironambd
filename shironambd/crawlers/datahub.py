#!/usr/bin/env python
# encoding: utf-8
"""
mongohub.py

Created by Caveman on 2013-01-31.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from bdnews24 import BdNews24
from banglanews24 import BanglaNews24
from celery.decorators import periodic_task
from datetime import timedelta
from celery import task


def crawl_bdnews24():
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_lead_news()
	bdN.get_latest_news()
	bdN.get_most_read()
	bdN.get_recent_stories()
	bdN.get_categorized_news()

@periodic_task(run_every=timedelta(seconds=5))	
def crawl_bdnews_latest_news():
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_latest_news()
	

def crawl_banglanews24():
	bUrl = 'http://banglanews24.com/'
	bn24 = BanglaNews24(bUrl)
	bn24.get_lead_news()
	bn24.get_latest_news()
	bn24.get_categorized_news()
	bn24.get_best24()
	bn24.get_most_read()
	
		


if __name__ == '__main__':
	# crawl_bdnews24()
	# crawl_banglanews24()
	crawl_bdnews_latest_news()

