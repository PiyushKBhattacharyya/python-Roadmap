line = 'A lot                 of spaces'
etc = line.split()
print(etc)
line = 'first;second;third'
thing = line.split()
print(f'Length of String without split: {len(thing)}')
thing = line.split(';')
print(f'Length of Strings with delimiter: {len(thing)}')
words = 'His e-mail is email-abc@example.com'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(parts)
print(n)