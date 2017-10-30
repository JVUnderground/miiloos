from django.db import models
from datetime import datetime

# Create your models here.

class ComedFiveMinFeed(models.Model):
    millisUTC = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()

    def save(self, *args, **kwargs):
        self.date = datetime.utcfromtimestamp(int(self.millisUTC)/1000)
        super(ComedFiveMinFeed, self).save(*args, **kwargs)
