counts = {}
names = ['Joseph', 'Gwen', 'Sally', 'Joseph']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(f'Name Dictionary: {counts}')
print("Get Sally:", counts.get('Sally'))