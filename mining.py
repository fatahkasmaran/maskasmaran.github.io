import requests
import json


endpoint = "https://api.twitter.com/1.1/tweets/search/30day/thesis273.json"
# # endpoint = "https://api.twitter.com/2/tweets/search/stream/rules"

headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAIz%2BJQEAAAAASXxHL6%2FAs16FRA0n5xsrhedvgIc%3D9XkqI0KoTLiICh8xkrnqhpQZeZ6HB1NMudyhdy8WlJ1jkfAmE9",
           "Content-Type": "application/json"}

data = '{"query":"(#MahasiswaBergerak OR #TolakUUCiptaKerja OR #MosiTidakPercaya)", "fromDate": "202010090000", \
    "toDate": "202010100000"}'

response = requests.post(endpoint, data=data, headers=headers).json()


with open("aaa1.json", "w") as data:
    json.dump(response, data)

# '{"query":"(#MahasiswaBergerak OR #TolakUUCiptaKerja OR #MosiTidakPercaya)", "fromDate": "202010050000", "toDate": "202010090000"}'
