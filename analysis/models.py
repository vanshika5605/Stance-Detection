from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=250,blank=True, null=True)
    img = models.ImageField(upload_to='postpics',blank=True, null=True)
    target = models.CharField(max_length=100,blank=True, null=True)
    sarcasm = models.CharField(max_length=20,blank=True, null=True)
    sentiment = models.CharField(max_length=20,blank=True, null=True)
    stance = models.CharField(max_length=20,blank=True, null=True)
    date_added = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100,blank=True, null=True)