from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import numpy as np
from PIL import Image
import stylecloud
from matplotlib import colors

import re
import collections
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
from PIL import Image
import matplotlib.pyplot as plt 

listStopword = set(stopwords.words('indonesian'))

#tambahin hashtagnya di stopwot ini
stopwot = ['gue', 'lu', 'lo', 'kalo', 'kak', 'ya', 'yg', 'ga', 'gk', 'sm', 'deh',
           'gua', 'jg', 'tp', 'iya', 'si', 'pa', 'eh', 'w', 'ma', 'emang', 'emg', 'emng', 'kaya',
           'bgt', 'aja', 'lg', 'ak', 'sih', 'jd', 'ah', 'doang', 'kayak', 'tau', 'nya', 'klo', 'yaa',
           'wkwk', 'wkwkwk', 'sampe', 'tr', 'nih', 'yuk', 'yaudah', 'lupa', 'kek', 'tuh', 'jd', 'orang',
           'kau', 'coba', 'kali', 'pake', 'udh', 'biar', 'ih', 'tpi', 'nak', 'ayo', 'udah', 'gak', 'langsung',
           'tu', 'gw', 'li', 'trs', 'skrg', 'ngga', 'pas', 'ku', 'km', 'nggak', 'bp', 'udah', 'gitu', 'mani',
           'gimana', 'tru', 'bilang', 'banget', 'nder', 'bener', 'g', 'zhiming', 'usir', 'karna', 'cina',
           'cina usir', 'ni', 'btw', 'trus', 'mulu', 'dapet', 'gini', 'ntar', 'inget', 'mah', 'ambil', 'dah',
           'masuk', 'je', 'ng', 'haha', 'hahaha', 'liat', 'muk', 'mas', 'hyung', 'besok', 'ko', 'amp', 'salah',
           'd', 'loh', 'yah', 'anjir', 'habi', 'allah', 'ka', 'cari', 'bang', 'la', 'e', 'sumpah', 'hehe', 'gatau',
           'dr', 'na', 'dgn', 'wkwkw', 'ye', 'ama', 'bagu', 'tukang', 'knp', 'bawa', 'beneran', 'jdi', 'mv', 'kyk',
           'mo', 'oh', 'jgn', 'kang', 'pokoknya', 'pergi', 'mending', 'gt', 'bagus', 'b', 'hm', 'engga', 'org',
           'maunya', 'nyari', 'dek', 'krn', 'lt', 'hai', 'kl', 'gamau', 'oke', 'gapapa', 'gaada', 'takut', 'u', 
           'ayam', 'goreng', 'nasi', 'you', 'me', 'lisa', 'x', 'and', '5', 'in', 'the', 'to', 'nan', 'she/her',
           'none', 'her', 'she', 's', 'of', 'my', 'heart', 'carrd', 'byf', 't', 'read', 'nsfw', 'on', 'your', 'only',
           'n', 'h', 'no', 'part', 'he', 'we', 'with', 'non', 'him', 'exo', 'nsa', 'l', 'ca', 'm', 'they', 'is', 'for']

df = pd.read_csv('Giska-2.csv')
print(df)

tweets = []
for word in df.tweet:
#     text = str(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
#                            " ", word.lower()))
    tweets.append(word_tokenize(text))
    

words = ''
for t in tweets:
    for word in t:
        if word not in stopwot and word not in listStopword:
            words += " "
            words += word

plt.close()

x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
circle = np.array(Image.open('circle.jpeg'))
black = '#000000'
yellow = '#FFFF00'
orange = '#FFA500'
green = '#00FF00'
blue = '#0000FF'
red = '#FF0000'

color_list= blue

#transfer
colormap=colors.ListedColormap(color_list)

wordcloud = WordCloud(background_color="white",
 mask=circle, width=mask.shape[1], height=mask.shape[0], colormap=colormap, max_words=1000).generate(words)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
print('Showing graph..')
plt.show()
print('Graph closed')
