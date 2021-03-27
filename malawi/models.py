from django.db import models


class News(models.Model):
    heading = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=10000)
    image = models.CharField(max_length=1000)
    source = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)