from itertools import chain
from random import shuffle
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
import datetime
from shironambd.home.models import News, Source

from utils import get_latest_x_news



def index(request):
    palo = Source.objects.get(name='ProthomAlo')
    # bdnews  = Source.objects.get(name='BDNEWS24.COM')
    # banglanews = Source.objects.get(name='BanglaNews24.com')
    # all_news = list(chain(palo_news, bdnews, bangla_news))
    # shuffle(all_news)
    palo_news = News.objects.filter(source=palo).order_by('-created_at')


    template = get_template('index.html')
    context = RequestContext(request, 
    {'all_news':palo_news }
    )
    # print 'Total news', len(all_news)
    html = template.render(context)

    return HttpResponse(html)


