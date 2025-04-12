import json

data = '''
{
    "name": "John",
    "phone": {
        "type": "intl",
        "number": "+91 70990 50919"
    },
    "email": {
        "hide": "yes"
    }
}
'''

info = json.loads(data)
print('Name: ', info["name"])
print("Hide: ", info["email"]["hide"])