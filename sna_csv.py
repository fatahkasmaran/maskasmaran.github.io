import pandas as pd
import json
import re
from csv import DictWriter, writer
from datetime import date, time, datetime

tweet_properties = {}

with open("aaa3357.json", "r") as data_read:
    json_data = json.load(data_read)

with open('NEWFILE.csv', 'w') as f:
    csv_writer = DictWriter(f, fieldnames=[
                            'tweet_date', 'username', 'user_id', 'account_creation', 'tweet', 
                            'followers', 'following', 'location'])
    csv_writer.writeheader()
    for data in json_data:
        if 'extended_tweet' in data:
            tweet_properties['tweet'] = re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data['extended_tweet']['full_text'].lower())
        else:
            tweet_properties['tweet'] = re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data['text'].lower())
        tweet_properties['location'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                                                  " ", str(data['user']['location']).lower())
        csv_writer.writerow({
                'tweet_date': datetime.strptime(
                    data['created_at'], "%a %b %d %X %z %Y").strftime("%Y-%m-%d %X"),
                'username': data['user']['screen_name'],
                'user_id': data['user']['id_str'], 
                'account_creation': data['user']['created_at'],
                'tweet': tweet_properties['tweet'],
                'followers': data['user']['followers_count'],
                'following': data['user']['friends_count'],
                'location': tweet_properties['location']

            })


print('DONE!')
