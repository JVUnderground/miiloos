from django.db import models

# Create your models here.

class ComedFiveMinFeed(models.Model):
    date = models.BigIntegerField()
    price = models.FloatField()
