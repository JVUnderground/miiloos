from django.db import models
from datetime import datetime, timezone

# Create your models here.

class ComedFiveMinFeed(models.Model):
    millisUTC = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()

    def save(self, *args, **kwargs):
        date = datetime.utcfromtimestamp(int(self.millisUTC)/1000)
        self.date = date.replace(tzinfo=timezone.utc)
        super(ComedFiveMinFeed, self).save(*args, **kwargs)
