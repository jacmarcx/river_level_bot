import pandas as pd
import twitter
import pandas as pd
import twitter
import os
import datetime
from os import environ
import time
from matplotlib import pyplot as plt

while True:
    # get data
    url = 'https://data.winnipeg.ca/resource/q8w3-jhjb.csv'

    data = pd.read_csv(url)
    data['reading_date'] = pd.to_datetime(data['reading_date'])
    data.index = data['reading_date']
    first_value = data.iloc[0]['james_feet']
    date = data.index[0].strftime('%b %d, %Y')
    hour = data.index[0].strftime('%H:%M')
    next_update = datetime.datetime.now() + datetime.timedelta(hours=3)
    next_update = next_update.strftime('%#I:%M %p')
        
    # send tweet
    # api details
    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_TOKEN']
    access_secret = environ['ACCESS_SECRET']
    

    #charting data
    chr = data.iloc[0:360,[2]]
    plt.figure(figsize=(9,4.8), dpi=60)
    plt.plot(chr.index, chr['james_feet'], color='#00607a', alpha=0.8, linewidth=5)
    plt.title(str(datetime.datetime.now()), fontsize=22, pad=10) #Last 12 months of James Ave gauge readings
    plt.xticks(fontsize=16, rotation=15)
    plt.yticks(fontsize=16)
    plt.tight_layout()        
    plt.savefig('chart.png', dpi=60)
   
    t = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

    t.PostUpdate(status=('The Red River level for ' + date +
                         ' is: ' + str(first_value) + ' feet James.\nNext update at: ' + str(next_update) + '.'),
                         media='chart.png')

    #time.sleep(10800)
    time.sleep(180)