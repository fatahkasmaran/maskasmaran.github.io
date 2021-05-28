import json
import re
import csv
from csv import reader
import pandas as pd 
import numpy as np 
from csv import DictWriter, writer
from datetime import date, time, datetime

tweet_properties = {}

with open('TRANSLATED-covid-sentiment.csv', 'r', encoding="utf8") as f:
    cf = csv.DictReader(f)
    # for r in cf:
    #     print(r['date'])
    with open('TRANSLATED-covid-sentiment_clean.csv', 'w', encoding="utf8", newline='') as f:
        csv_writer = DictWriter(f, fieldnames=[
                                'conversation_id', 'date', 'time', 'user_id', 'username', 'tweet', 'mentions', 'replies_count', 'retweets_count', 'likes_count', 'hashtags'])
        csv_writer.writeheader()
        for row in cf:
                tweet_properties['tweet'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", row['translated'].lower())
            
                csv_writer.writerow({
                            'conversation_id': row['conversation_id'],
                            'date': row['date'],
                            'time': row['time'],
                            'user_id': row['user_id'],
                            'username': row['username'],
                            'tweet': tweet_properties['tweet'],
                            'mentions': row['mentions'],
                            'replies_count': row['replies_count'],
                            'retweets_count': row['retweets_count'],
                            'likes_count': row['likes_count'],
                            'hashtags': row['hashtags']
                        })

print("DONE!")
