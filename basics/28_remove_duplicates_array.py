array = [1,1,2,1,3,3,4,1,3,5,6,4]
uniques = []

for num in array:
    if num not in uniques:
        uniques.append(num)

print(uniques)