from django.db import models

# Create your models here.

class ComedFiveMinFeed(models.Model):
    date = models.BigIntegerField(primary_key=True)
    price = models.FloatField()
