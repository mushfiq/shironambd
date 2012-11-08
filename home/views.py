# Create your views here.
from django.http import HttpResponse
# from django
from home.models import News

def index(request):
	news = News.objects.all()
	
	return HttpResponse(news)