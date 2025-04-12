xfile = open('1.txt')
for line in xfile:
    line = line.rstrip()
    if not 'Revising' in line:
        continue
    print(line)