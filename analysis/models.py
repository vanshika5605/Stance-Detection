from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=250)
    img = models.ImageField(upload_to='postpics')
    target = models.CharField(max_length=100)
    sarcasm = models.IntegerField()
    sentiment = models.CharField(max_length=20)
    stance = models.CharField(max_length=20)
    date_added = models.DateField()
    author = models.CharField(max_length=100)