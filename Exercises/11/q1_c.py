# Write a Python loop that uses the range function to add up all numbers from 34 up to and including 57.
total = 0
for num in range(34, 58):
    #print(num)
    total += num
print(f"Total => {total}")

# testing with a while loop
total = 0
num = 34
while(num <= 57):
    total += num
    num += 1
print(f"Total from while => {total}")