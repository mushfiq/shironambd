
import setup_django
from shironambd.home.models import News, Source

SOURCE_URLS = ['http://www.prothom-alo.com/', 'http://bdnews24.com', 'http://banglanews24.com']

def get_source(name):
	source = Source.objects.get(name=name)
	return source

def update_source():
	PALO = get_source('ProthomAlo')
	BDNEWS = get_source('BDNEWS24.COM')
	BANGLANEWS = get_source('BanglaNews24.com')
	
	all_news = News.objects.all()
	for news in all_news:
		if news.link.find(SOURCE_URLS[1]) > -1:
			news.source = BDNEWS
			news.save()
			print "updated!!"
		
		
		

if __name__=='__main__':
	update_source()