largest = -1
print(f'Before: {largest}')
for num in [9, 12433, 6, 67]:
    if num > largest:
        largest = num
    print(f'num: {num}')
print(f'After: {largest}')