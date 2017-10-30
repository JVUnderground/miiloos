from graphs.models import comedFiveMinFeed

import requests as r
import json

url_comed = 'https://rrtp.comed.com/api?type=5minutefeed'

result = r.get(url_comed)
prices = json.loads(result.content)

for instance in prices:
    date = instance['millisUTC']
    price = instance['price']

    try:
        ComedFiveMinFeed.objects.create(date=date, price=price)
    except:
        pass
