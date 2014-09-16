import requests
from celery.decorators import periodic_task
from datetime import timedelta
from datahub import crawl_bdnews, crawl_banglanews24, crawl_palo, crawl_jugantor

@periodic_task(run_every=timedelta(seconds=500))
def check_status():
    print "Staring operation......."
    print "crawling palo..."
    crawl_bdnews()
    crawl_jugantor()
    crawl_palo()
