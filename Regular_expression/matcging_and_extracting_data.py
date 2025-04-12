import re

x = 'My favorite 2 numbers are 19 and 20 and AEI-chars'
y = re.findall('[0-9]+', x)
y1 = re.findall('[0-9]', x)
y2 = re.findall('[a-z]+', x)
y3 = re.findall('[AEIOU]+', x)
y4 = re.findall('^M.+', x)
y5 = re.findall('^M.+?e', x)
print(y, y1,'\n',y2, y3,'\n',y4,'\n',y5,'\n')