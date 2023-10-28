list = [1,1,2,1,3,3,4,1,3,5,6,4]
print(f'\nOriginal: {list}')

list.sort()
print(f'\nSorted: {list}')
i = 1
while i < len(list):
    if list[i] == list[i - 1]:
        list.remove(list[i])
    else:
        i += 1

print(f'\nRemoved Duplicates: {list}')