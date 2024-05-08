max_retry_count = 3
current = 0
input_read = False
while current < max_retry_count and not input_read:
    current += 1
    try:
        number = int(input(f'Attempt {current} - Please enter a number: '))
        input_read = True
    except ValueError:
        print('\tError - Please provide a valid number')
if input_read:
    print(f'\nYour input {number}')   
else:
    print(f'\nYou were unable to give a valid number with in {max_retry_count} attempts, Im giving up.')     