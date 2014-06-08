from datetime import datetime

from rss import RSSCrawler
import setup_django
from shironambd.home.models import News, Source

class JugnatorCrawler(RSSCrawler):
    
    def get_published_at(self, entry):
        pub_str = entry.published[:-6] if entry.has_key('published') else None
        published_at = datetime.strptime(pub_str, '%a, %d %b %Y, %H:%M:%S') 
        return published_at
    
    def process(self):
        entries = self.get_entries()

        for entry in entries:
            news = News()
            try:
                news.link = entry.guid
                news.source = self.source
                news.title  = self.get_title(entry)
                news.published_at = self.get_published_at(entry)
                self.do_save(news)
            except Exception as e:
                print "Error Occured!", e
                pass
        return
        
if __name__=='__main__':
    url = "http://www.jugantor.com/rss.xml"
    j = JugnatorCrawler(url)
    j.process()
