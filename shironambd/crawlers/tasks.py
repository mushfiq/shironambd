import requests
from celery.decorators import periodic_task
from datetime import timedelta
from datahub import crawl_bdnews_latest_news

@periodic_task(run_every=timedelta(seconds=15))
def check_status():
	print "Staring operation......."
	crawl_bdnews_latest_news()
	# res = requests.get(url)
	# print res.status_code
