import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('https://www.py4e.com/code/urllinks.py')

for line in fhand:
    print(line.decode().strip())
