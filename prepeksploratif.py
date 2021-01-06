import json
import re
import pandas as pd 
import numpy as np 
from csv import DictWriter, writer
from datetime import date, time, datetime
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

with open("YOURFILENAME.json", "r") as data_read:
    json_data = json.load(data_read)

tweet_properties = {}
listStopword = set(stopwords.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()   

with open('YOURNEWFILENAME.csv', 'w') as f:
    csv_writer = DictWriter(f, fieldnames=[
                            'tanggal', 'username', 'followers', 'tweet', 'likes', 'retweet', 'komentar', 'location'])
    csv_writer.writeheader()
    for data in json_data:
        if "RT @" not in data['text']: #cleaning
            if 'extended_tweet' in data:
                tweet_properties['tweet'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data['extended_tweet']['full_text'].lower())
            else:
                tweet_properties['tweet'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data['text'].lower())
            
            tweet_properties['location'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                                                  " ", str(data['user']['location']).lower())
            
            csv_writer.writerow({
                'tanggal': datetime.strptime(
                    data['created_at'], "%a %b %d %X %z %Y").strftime("%d-%m-%Y %X"),
                'username': data['user']['screen_name'],
                'followers': data['user']['followers_count'],
                'tweet': tweet_properties['tweet'],
                'likes': data['favorite_count'],
                'retweet': data['retweet_count'],
                'komentar': data['reply_count'],
                'location': tweet_properties['location']
            })

print("DONE!")
