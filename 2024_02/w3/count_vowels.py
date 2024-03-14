str = "Timee"
vowels = ['a', 'e', 'i', 'o', 'u']

# This loop iterates over every character in a string.
count = 0
for c in str:
    if c in vowels:
        print(c)
        count += 1
print(count)