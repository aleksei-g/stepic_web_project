# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Question (models.Model):
#	title = models.CharField(max_length=255)
#	text = models.TextField()
#	added_at = models.DateTimeField(auto_now_add=True)
#	rating = models.IntegerField(default=0)
#	author = models.ForeignKey(User)
#	likes = models.TextField()
#	#likes = models.ForeignKey(User, related_name= 'likes',blank=True)
#
#
#class Answer (models.Model):
#	text = models.TextField()
#	added_at = models.DateTimeField(auto_now_add=True)
#	question = models.ForeignKey(Question)
#	author = models.ForeignKey(User)

class Question (models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null = True)
	#likes = models.TextField()
	#likes = models.ForeignKey(User, related_name= 'likes',blank=True)


class Answer (models.Model):
	text = models.TextField(verbose_name="Ответить")
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, null = True)
