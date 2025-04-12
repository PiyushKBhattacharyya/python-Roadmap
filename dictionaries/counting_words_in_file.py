name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
print(f'Words: {words}')
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f'Word Count: {counts}')