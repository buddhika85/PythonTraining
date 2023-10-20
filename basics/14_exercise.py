weight = float(input("Weight: "))
unit = input('(L)bs or (K)g:')[0].upper()
if unit == 'L':
    result = weight * 0.45
    print(f'Weight in Kg is {result}')
else:
    result = weight / 0.45
    print(f'Weight in Lbs is {result}')

