from django.db import models

# Create your models here.

class comedFiveMinFeed(models.Model):
    date = models.BigIntegerField()
    price = models.FloatField()
