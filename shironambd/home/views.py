from itertools import chain
from random import shuffle
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
import datetime
from shironambd.home.models import News, Source

from utils import get_latest_x_news



def index(request):
    all_sources = Source.objects.all()
    all_news = []
    #TODO:optmiize this code 
    for source in all_sources:
        news = News.objects.filter(source=source)[:10]
        if len(news):
            for n in news:
                all_news.append(n)
        
    template = get_template('index.html')
    context = RequestContext(request, 
    {'all_news':all_news }
    )
    html = template.render(context)

    return HttpResponse(html)


def aboutus(request):
    template = get_template('about-us.html')
    context = RequestContext(request)
    html = template.render(context)
    return HttpResponse(html)
    
def contactus(request):
    return HttpResponse('contact-us')
    
    
def legal(request):
    return HttpResponse('legal')