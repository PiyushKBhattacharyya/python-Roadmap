import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chunk</name>
        </user>
        <user x="3">
            <id>001</id>
            <name>Chunk</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(f'User Count: {len(lst)}')
for items in lst:
    print(f'User ID: {items.find("id").text}')
    print(f'Name: {items.find("name").text}')
    print(f'Attributes: {items.get("x")}')