import pandas as pd
from csv import DictWriter, writer
import re

data = pd.read_json('diindonesiaaja.json')

insta_properties = {}
with open('diindonesiaaja.csv', 'w') as f:
    csv_writer = DictWriter(f, fieldnames=[
                            'user_id', 'date', 'caption'])
    csv_writer.writeheader()
    for d in data.GraphImages:
        
        # print(d)
        insta_properties['caption'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", d['edge_media_to_caption']['edges'][0]['node']['text'].lower())
        csv_writer.writerow({
            'user_id': d['id'],
            'date': d['taken_at_timestamp'],
            'caption': insta_properties['caption']
#             'comments': d['edge_media_to_comment']['count'],
#             'height': d['dimensions']['height'],
#             'width': d['dimensions']['width']
        })

#, 'comments', 'height', 'width'
