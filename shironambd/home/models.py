from datetime import datetime
import mongoengine as mongo


class Source(mongo.Document):
	name = mongo.StringField(max_length=50, required=True)
	website = mongo.StringField(max_length=50)
	logo = mongo.ImageField()
	
	def __unicode__(Source):
		return Source.name
		
	meta = {
		'collection': 'sources'
	}
	
	
class News(mongo.Document):
	title = mongo.StringField(required=True)
	source = mongo.ReferenceField(Source)
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
		
