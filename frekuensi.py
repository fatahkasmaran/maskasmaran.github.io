import numpy as np
import pandas as pd
import re
import json

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()
listStopword = set(stopwords.words('indonesian'))

stopwot = [FILL YOUR STOPWORDS]

data = pd.read_csv('FILENAME.csv')

tweets = []
for word in data.tweet:
    text = str(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                      " ", word.lower()))
    tweets.append(word_tokenize(text))

words = []
for t in tweets:
    for word in t:
        if word not in stopwot and word not in listStopword:
            words.append(word)

frequency = {}

for word in words:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])

print(frequency)

df = pd.DataFrame.from_dict(frequency, orient="index").sort_values(by=0, ascending=False)

df.to_csv('NEWFILENAME.csv')
