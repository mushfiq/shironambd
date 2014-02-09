import requests
from celery.decorators import periodic_task
from datetime import timedelta
from datahub import crawl_bdnews24, crawl_banglanews24, crawl_palo

@periodic_task(run_every=timedelta(seconds=300))
def check_status():
	print "Staring operation......."
	crawl_bdnews24()
	crawl_banglanews24()
	crawl_palo()
