import argparse
import setup_django

from shironambd.home.models import Source


def create_source(name, website, urls, parser_name):
    source = Source()
    source.name = name
    source.website = website
    # source.logo = logo
    source.parser_name = parser_name
    source.urls = [urls]
    
    try:
        source.save()
        print "Source saved successfully :)"
    except Exception as e:
        print e
        pass
        
def parse_arguments():
    parser = argparse.ArgumentParser(description="create new news source")
    
    parser.add_argument('--name')
    parser.add_argument('--website')
    parser.add_argument('--parser_name')
    # parser.add_argument('--logo')
    parser.add_argument('--urls')
    args = parser.parse_args()
    create_source(args.name, args.website, args.urls, args.parser_name)

if __name__=='__main__':
    # create_source()
    parse_arguments()