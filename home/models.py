from django.db import models

class News(models.Model):
	title = models.CharField(max_length = 255)
	pub_date = models.DateTimeField('date published')
	create_date = models.DateTimeField('date of creation')
	link = models.URLField(max_length = 255)
	total_comments = models.IntegerField()
	# source_id = models.ForeignKey(Source, to_field='id')
	# user_id = models.ForeignKey(User, to_field='id')
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		db_table = 'news'
		
class Source(models.Model):
	name = models.CharField(max_length = 50)
	website = models.CharField(max_length = 50)
	
	class Meta:
		db_table = 'source'