fname = input('Enter file name: ')
try:
    xfile = open(fname)
    count = 0
    for line in xfile:
        count = count + 1
    print(f'There are {count} lines in {fname}')
except:
    print('File not found')