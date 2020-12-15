from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber
import json
import re
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from google_trans_new import google_translator
from textblob import TextBlob

#please remember that translating needs stable connection
translator = google_translator()
tb = Blobber(analyzer=NaiveBayesAnalyzer())

with open("FILENAME.json", "r") as data_read:
    json_data = json.load(data_read)

tweet_properties = {}
listStopword = set(stopwords.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()

hoho = {'tanggal': [], 'sentimen': []}
for data in json_data:
    if "RT @" not in data['text']:  # cleaning
        if 'extended_tweet' in data:
            tweet_properties['tweet'] = re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data['extended_tweet']['full_text'].lower())
        else:
            tweet_properties['tweet'] = re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data['text'].lower())
        
        hoho['tanggal'].append(data['created_at'])
        hoho['sentimen'].append(tb(translator.translate(
            tweet_properties['tweet'])).polarity)
        
df = pd.DataFrame(hoho)
df.to_csv('NEWFILENAME.csv', encoding='utf-8', index=False)
