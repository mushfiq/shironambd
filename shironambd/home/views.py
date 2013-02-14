from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
import datetime
from shironambd.home.models import News

def index(request):
	all_news = News.objects.all()[:20]
	template = get_template('index.html')
	context = RequestContext(request, 
			{'all_news':all_news }
		)
	html = template.render(context)

	return HttpResponse(html)


