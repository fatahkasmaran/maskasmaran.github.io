from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber
import json
import re
import pandas as pd
from csv import DictWriter, writer
from datetime import date, time, datetime
import nltk
from google_trans_new import google_translator


translator = google_translator()

tb = Blobber(analyzer=NaiveBayesAnalyzer())

df = pd.read_csv('FILECSV.csv')

tweet_properties = {}

hoho = {'tanggal': [], 'user_id': [], 'username': [], 'tweet': [], 'likes': [], 'retweet': [], 'sentimen': []}

for date in df.date:
    hoho['tanggal'].append(date)

for ids in df.user_id:
    hoho['user_id'].append(ids)

for user in df.username:
    hoho['username'].append(user)

for likes in df.likes_count:
    hoho['likes'].append(likes)

for retweet in df.retweets_count:
    hoho['retweet'].append(retweet)

for tweet in df.tweet:
    tweet_properties['tweet'] = re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.lower())
    hoho['tweet'].append(tweet_properties['tweet'])
    hoho['sentimen'].append(tb(translator.translate(
            tweet_properties['tweet'])).polarity)


df = pd.DataFrame(hoho)
df.to_csv('NEWFILENAME.csv', encoding='utf-8', index=False)
