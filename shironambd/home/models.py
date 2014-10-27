from datetime import datetime
import mongoengine as mongo


class Source(mongo.Document):
    name = mongo.StringField(max_length=50, required=True)
    website = mongo.StringField(max_length=50)
    logo = mongo.ImageField()
    parser_name = mongo.StringField(default=None, required=True)
    urls = mongo.ListField(mongo.StringField(max_length=500))
    def __unicode__(Source):
    	return Source.name
	
    meta = {
    	'collection': 'sources'
    }
	
    def aggregate():
        return
	
class News(mongo.Document):
    title = mongo.StringField(required=True)
    source = mongo.ReferenceField(Source)
    author = mongo.StringField(default=None)
    published_at = mongo.DateTimeField(default=datetime.now())
    created_at = mongo.DateTimeField(default=datetime.now())
    link = mongo.URLField(required=True)
    total_comments = mongo.IntField(default=0)
    tags = mongo.ListField(mongo.StringField(max_length=50))
    category = mongo.StringField(max_length=20)
    is_featured = mongo.BooleanField(default=False)

    def __unicode__(News):
    	return News.title

    meta = {
    	'collection' : 'news',
    	'indexes' : ['title'],
    	'ordering' : ['-published_at']
    }
		
    class Meta:
    	get_latest_by = 'created_at'
