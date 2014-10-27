import requests
from celery.decorators import periodic_task
from celery import Celery
from celery import task
from datetime import timedelta
from datahub import crawl_bdnews, crawl_banglanews24, crawl_palo, crawl_jugantor
from celeryconfig import BROKER_URL


celery = Celery('tasks', broker=BROKER_URL)

    
@task()
def palo():
    crawl_palo()

@task()
def jugantor():
    crawl_jugantor()

@task()    
def bdnews():
    crawl_bdnews()

@periodic_task(run_every=timedelta(seconds=300))
def check_status():
    palo.delay()
    bdnews.delay()
    jugantor.delay()

