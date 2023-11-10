# exception handling
try:
    age = int(input('Age : '))
    income =20000
    risk = income / age
    print(age)
except ValueError:
    print('Error : Invalid value')
except ZeroDivisionError: 
    print('Error : ZeroDivisionError - cannot devide by zero, age input 0cannot be zero')