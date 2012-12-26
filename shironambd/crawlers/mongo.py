import setup_django
from bdnews24 import *
from shironambd.home.models import News



def run():
	bUrl = 'http://scrape.local/'
	bdN = BdNews24(bUrl)	
	for ne in bdN.get_box_news():
		n = News()
		n.title = ne
		n.link = 'http://dummy.com'
		n.save()
		print n.title+"saved"
		
	
if __name__=='__main__':
	run()