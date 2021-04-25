import urllib.request
import urllib.parse
import urllib.error
import json


url = input("Enter Url - ")
data = urllib.request.urlopen(url).read()

jsonData = json.loads(data)

count = 0
for sJSData in jsonData['comments']:
    count = count + int(sJSData['count'])

print(count)