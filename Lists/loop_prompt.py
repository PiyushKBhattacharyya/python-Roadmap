numlist = list()
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp.lower() == 'done': break
    try:
        val = float(inp)
        total += val
        count += 1
    except:
        print('Invalid input')
print(f'Average: {total / count}')