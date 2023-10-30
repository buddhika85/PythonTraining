# def keyword is used
#define function before you call them
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abroad\n')

print('Start----')
greet_user('John', 'Smith')

greet_user(first_name='Gill', last_name='Smith')    # keyword arguments improve readability 
greet_user(last_name='Ponting', first_name='Ricky')    # keyword arguments change order of arguments

print('End----')