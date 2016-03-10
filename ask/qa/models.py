from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Question (models.Model):
#	title = models.CharField(max_length=255)
#	text = models.TextField()
#	added_at = models.DateTimeField()
#	rating = models.IntegerField()
#	author = models.ForeignKey(User)
#	#likes = models.TextField()
#	likes = models.ForeignKey(User, related_name= 'likes',blank=True)
#
#
#class Answer (models.Model):
#	text = models.TextField()
#	added_at = models.DateTimeField()
#	question = models.ForeignKey(Question)
#	author = models.ForeignKey(User)

class Question (models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField(blank=True)
	#author = models.ForeignKey(User, blank=True)
	#likes = models.TextField()
	#likes = models.ForeignKey(User, related_name= 'likes',blank=True)


class Answer (models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey(Question)
	#author = models.ForeignKey(User)
