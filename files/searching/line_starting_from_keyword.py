xfile = open('1.txt')
for line in xfile:
    line = line.rstrip()
    if line.startswith('Revising'):
        print(line)