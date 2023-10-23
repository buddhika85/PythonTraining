numbers = [10,3,11,2,0,1,5,7,6,8,4,3,7,12,11,12]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f'Largest is : {largest}')