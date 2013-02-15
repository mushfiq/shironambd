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


def crawl_bdnews24():
	bUrl = 'http://bangla.bdnews24.com/'
	bdN = BdNews24(bUrl)
	bdN.get_lead_news()
	bdN.get_latest_news()
	bdN.get_most_read()
	bdN.get_recent_stories()
	bdN.get_categorized_news()
	


if __name__ == '__main__':
	crawl_bdnews24()

