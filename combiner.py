import json

result = []
for num in range(1, 1000000):
    with open("YOURFILENAME"+str(num)+".json") as infile:
        json_data = json.load(infile)
        for data in json_data.get('results'):
            result.append(data)
with open("NEWFILENAME.json", "w") as outfile:
    json.dump(result, outfile)  

print('done!')
