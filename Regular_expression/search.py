import re

xfile = open('1.txt')
for line in xfile:
    line = line.rstrip()
    if re.search(r'Hello', line):
        print(line)