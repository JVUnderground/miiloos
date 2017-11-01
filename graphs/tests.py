from django.test import TestCase
from graphs.models import ComedFiveMinFeed

# Create your tests here.
class ComedFiveMinFeedTestCase(TestCase):
    def setUp(self):
        ComedFiveMinFeed.objects.create(millisUTC="1509245400000", price="2.8")

    def test_COMED_date_converts_correctly(self):
        """Objects millisUTC converts correctly to a UTC date"""
        from datetime import datetime, timezone
        comed = ComedFiveMinFeed.objects.get(millisUTC="1509245400000")
        date = datetime.utcfromtimestamp(1509245400000/1000)
        date = date.replace(tzinfo=timezone.utc)
        self.assertEqual(comed.date, date)