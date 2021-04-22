import xml.etree.ElementTree as ET
data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chunck</name>
        </user>
        <user x="6">
            <id>009</id>
            <name>Sajib</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(data)
userList = stuff.findall('users/user')

print('Total Users: ', len(userList))

for user in userList:
    print('User ID :', user.find('id').text)
    print('User Name :', user.find('name').text)
    print('User Attribute :', user.get('x'))
