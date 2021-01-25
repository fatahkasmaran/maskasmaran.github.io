import requests
import json


endpoint = "https://api.twitter.com/1.1/tweets/search/30day/DEVLABEL.json"
# # endpoint = "https://api.twitter.com/2/tweets/search/stream/rules"

headers = {"Authorization": "Bearer YOURBEARERTOKEN",
           "Content-Type": "application/json"}

data = '{"query":"(#MahasiswaBergerak OR #TolakUUCiptaKerja OR #MosiTidakPercaya)", "fromDate": "202010090000", \
    "toDate": "202010100000"}'

response = requests.post(endpoint, data=data, headers=headers).json()


with open("aaa1.json", "w") as data:
    json.dump(response, data)

