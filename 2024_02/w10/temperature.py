def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def convert():
    print('\nTemperature Conversion')
    while True:
        try:
            
            input_temp = float(input('\nEnter the temperature value: '))
            input_unit = input('Enter the input unit (C/F): ').upper()
            
            # raise exception if input unit is invalid
            if input_unit != 'C' and input_unit != 'F':
                raise ValueError('Invalid input unit. Enter C for celsius or F for Fahrenheit.')
            
            # raise exception if output unit is invalid
            output_unit = input('Enter the output unit (C/F): ').upper()
            
            # if it reaches here it means input and output units are C or F
            if output_unit != 'C' and output_unit != 'F':
                raise ValueError('Invalid output unit. Enter C for celsius or F for Fahrenheit.')
            
            if input_unit == output_unit:
                print(f'{input_temp}{input_unit} is {input_temp}{output_unit}, duh')
            elif output_unit == 'C':
                print(f'{input_temp}{input_unit} is {fahrenheit_to_celsius(input_temp)}{output_unit}')
            elif output_unit == 'F':
                print(f'{input_temp}{input_unit} is {celsius_to_fahrenheit(input_temp)}{output_unit}')
            break
        
        except ValueError as error:
            print(f'An error occurred: {error}')
    
# test code
convert()