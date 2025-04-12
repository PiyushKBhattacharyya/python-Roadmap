friends = ['Joseph', 'Glenn', 'Sally']
print(f'Length: {len(friends)}')
print(f'Range: {range(len(friends))}')
print(friends[0])
print(friends[-1])
print(friends[0:-1:2])

for i in friends:
    print(i)

for i in friends:
    print(f'Lower Case: {i.lower()}\nUpper Case: {i.upper()}')