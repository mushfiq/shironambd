from itertools import chain
from random import shuffle
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
import datetime
from shironambd.home.models import News, Source



def index(request):
	palo = Source.objects.get(name='ProthomAlo')
	bdnews  = Source.objects.get(name='BDNEWS24.COM')
	banglanews = Source.objects.get(name='BanglaNews24.com')
	palo_news = News.objects.filter(source=palo)[:10]
	bdnews = News.objects.filter(source=bdnews)[:10]
	bangla_news = News.objects.filter(source=banglanews)[:10]
	all_news = list(chain(palo_news, bdnews, bangla_news))
	shuffle(all_news)
	template = get_template('index.html')
	context = RequestContext(request, 
			{'all_news':all_news }
		)
	html = template.render(context)

	return HttpResponse(html)


