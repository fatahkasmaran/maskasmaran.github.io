import sys
import json
import re
import numpy as np
from datetime import datetime
import pandas as pd

with open("c1.json", "r") as data_read:
    json_data = json.load(data_read)

userdata = pd.DataFrame(columns=('Id', 'Label', 'user_created_at',
                                 'profile_image', 'followers_count', 'friends_count'))
edges = pd.DataFrame(columns=('Source', 'Target', 'Weight'))


for tweet in json_data:
    
    if 'retweeted_status' in tweet:
        userdata = userdata.append(pd.DataFrame([[tweet['user']['id_str'],
                                                tweet['user']['screen_name'],
                                                tweet['user']['created_at'],
                                                tweet['user']['profile_image_url_https'],
                                                tweet['user']['followers_count'],
                                                tweet['user']['friends_count']]], columns=('Id', 'Label', 'user_created_at', 'profile_image', 'followers_count', 'friends_count')), ignore_index=True)
        userdata = userdata.append(pd.DataFrame([[tweet['retweeted_status']['user']['id_str'],
                                                tweet['retweeted_status']['user']['screen_name'],
                                                tweet['retweeted_status']['user']['created_at'],
                                                tweet['retweeted_status']['user']['profile_image_url_https'],
                                                tweet['retweeted_status']['user']['followers_count'],
                                                tweet['retweeted_status']['user']['friends_count']]], columns=('Id', 'Label', 'user_created_at', 'profile_image', 'followers_count', 'friends_count')), ignore_index=True)
        edges = edges.append(pd.DataFrame([[tweet['user']['id_str'],
                                            tweet['retweeted_status']['user']['id_str'],
                                            str(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))]], columns=('Source', 'Target', 'Weight')), ignore_index=True)
                
# Network connection strength level: the number of times in total each of the tweeters responded to or mentioned the other.
weightlevel = 1
# If you have 1 as the level, then all tweeters who mentioned or replied to another at least once will be displayed. But if you have 5, only those who have mentioned or responded to a particular tweeter at least 5 times will be displayed, which means that only the strongest bonds are shown.

edges2 = edges.groupby(['Source', 'Target'])['Weight'].count()
edges2 = edges2.reset_index()
edges2 = edges2[edges2['Weight'] >= weightlevel]


# Export nodes from the edges and add node attributes for both Sources and Targets.
userdata = userdata.sort_values(
    ['Id', 'followers_count'], ascending=[True, False])
userdata = userdata.drop_duplicates(['Id'], keep='first')

ids = edges2['Source'].append(edges2['Target']).to_frame()
ids.columns = ['Id']
ids = ids.drop_duplicates()

nodes = pd.merge(ids, userdata, on='Id', how='left')
# print(nodes.head(3))


# change column names for Kumu import (Run this when using Kumu)
nodes.columns = ['Id', 'Label', 'Date',
                 'Image', 'followers_count', 'friends_count']
# print(edges2.head(5))
edges2.columns = ['Source', 'Target', 'Weight']

nodes.to_csv('nodes1.csv', encoding='utf-8', index=False)
edges2.to_csv('edges1.csv', encoding='utf-8', index=False)

print('DONE!!!')
