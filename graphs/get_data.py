from graphs.models import ComedFiveMinFeed

import datetime
import requests as r
import json

def getComedFiveMinFeed():
    url_comed = 'https://rrtp.comed.com/api?type=5minutefeed'

    result = r.get(url_comed)
    prices = json.loads(result.content)

    for instance in prices:
        millisUTC = instance['millisUTC']
        price = instance['price']

        try:
            ComedFiveMinFeed.objects.create(millisUTC=millisUTC, price=price)
        except:
            pass


def round_down(num, divisor):
    return num - (num%divisor)