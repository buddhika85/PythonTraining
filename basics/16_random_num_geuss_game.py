import random

random_number = random.randrange(1, 5)      # it can be 1,2,3,4
#print(f'Testing: Random number is {random_number}')
max_guess_count = 3
i = 0
is_won = False;
while not is_won and  i < max_guess_count:
    guess = int(input(f'Guess {i + 1}: '))
    if guess == random_number:
        print('You win !')
        is_won = True
    i += 1

if not is_won:
    print(f'You lost. Random number was {random_number}. Better luck next time !')