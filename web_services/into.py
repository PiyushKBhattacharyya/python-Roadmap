import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chunk</name>
    <phone type="intl">
        +91 70990 50919
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))