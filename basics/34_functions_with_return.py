def square(num, power):
    result = 1
    i = 1
    while i <= power:
        result *= num
        i += 1
    return result

# by default all functions return NONE, its like null in Java

num = int(input('Number to Sqaure:\n'))
power = int(input('Number to Sqaure:\n') )
print(f'{num} ^ {power} = {square(num, power)}')