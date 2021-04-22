import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Sajib Adhikary</name>
    <phone type="intl">
        +8801000000000
    </phone>
    <email hide="yes" />
</person>
'''

xmlTree = ET.fromstring(data)

print("Person Name:", xmlTree.find('name').text)
print("Person Phone:", xmlTree.find('phone').text)
print("Person Email:", xmlTree.find('email').text)
print("Person Email Is Hidden:", xmlTree.find('email').get('hide'))
