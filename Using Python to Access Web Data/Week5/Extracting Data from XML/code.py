import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET


url = input("Enter Url - ")
data = urllib.request.urlopen(url).read()

xmlTree = ET.fromstring(data)

comments = xmlTree.findall('comments/comment')

totalCount = 0
for comment in comments:
    totalCount = totalCount + int(comment.find('count').text)
print(totalCount)
