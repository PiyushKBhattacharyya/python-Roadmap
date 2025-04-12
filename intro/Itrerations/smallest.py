arr = [1,4,5,6,24,23,232]
large = arr[0]
print(f'Before: {large}')
for num in arr:
    if num < large:
        large = num
    print(f'num: {num}')
print(f'After: {large}')