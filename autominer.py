import requests
import json
import time


endpoint = "https://api.twitter.com/1.1/tweets/search/30dayORfullarchive/YOURDEVLABEL.json"

headers = {"Authorization": "Bearer YOURBEARERTOKEN",
           "Content-Type": "application/json"}

nexts = []
for num in range(1, 1000000):
    with open("YOURFILENAME"+str(num)+".json") as infile:
        json_data = json.load(infile)
        nexts.append(json_data['next'])
        print(nexts[-1])
        data = '{"query":"YOURQUERY", "fromDate": "YOURSTARTTIME", \
            "toDate": "YOURENDTIME", "next": "%s"}' % nexts[-1]
        print(data)
        response = requests.post(
            endpoint, data=data, headers=headers).json()
        # for num in range(182, 184):
        with open("YOURFILENAME"+str(num+1)+".json", "w") as new_file:
            json.dump(response, new_file)
            print("a sec break")
        time.sleep(1.2)
