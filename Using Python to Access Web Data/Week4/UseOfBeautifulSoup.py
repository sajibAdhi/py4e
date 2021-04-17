import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

url = input('Enter - ')
rawHtml = urllib.request.urlopen(url).read()
soup = BeautifulSoup(rawHtml, 'html.parser')

# Retriving all Anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))
