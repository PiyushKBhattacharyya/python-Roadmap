import re
data = 'From abc@example.com SAT APR 13'
atpos = data.find('@')
print(atpos)
spos = data.find(' ', atpos)
print(spos)
host = data[atpos + 1 : spos]
print(host)
words = data.split()
wmail = words[1]
pieces = data.split('@')
print(pieces[1])