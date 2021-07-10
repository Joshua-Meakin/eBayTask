import json
import urllib.request

res1 = urllib.request.urlopen("http://api.postcodes.io/postcodes/SE16/validate").read()
data1 = json.loads(res1)
print(data1)
print(data1['result'] == False)