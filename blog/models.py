from django.db import models
import datetime

class Blog(models.Model):
	username = models.CharField(max_length=20)
	create_date = models.DateTimeField('date created')
	modify_date = models.DateTimeField('date modified')
	blog_title = models.CharField(max_length=30)
	blog_text=models.TextField()
	published_date = models.DateTimeField('date published', null=True)
