import pandas as pd
import twitter
import os
import datetime
from os import environ
import time

while True:
    # get data
    url = 'https://data.winnipeg.ca/resource/q8w3-jhjb.csv'

    data = pd.read_csv(url)
    first_date = data.iloc[0]['james_feet']
    date = pd.to_datetime(data.iloc[0]['reading_date']).strftime('%B %d, %Y')
    hour = pd.to_datetime(data.iloc[0]['reading_date']).strftime('%H:%M')
    next_update = datetime.datetime.now() + datetime.timedelta(hours=2)
    next_update = next_update.strftime('%#I:%M %p')
        
    # send tweet
    # api details
    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_TOKEN']
    access_secret = environ['ACCESS_SECRET']
    

    t = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

    t.PostUpdate(status=('Bartley Kives says:\n"The Red River level for ' + date +
                         ' is: ' + str(first_date) + ' feet James. Next update at: ' + str(next_update) + '.'))

    time.sleep(150)