def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def convert():
    try:
        input_temp = float(input("Enter the temperature value: "))
        input_unit = input("Enter the input unit (C/F): ").upper()
        if input_unit != "C" and input_unit != "F":
            raise ValueError("Invalid input unit. Enter C for celsius or F for Fahrenheit.")
        
        output_unit = input("Enter the output unit (C/F): ").upper()
        if output_unit != "F" and output_unit != "C":
            raise ValueError("Invalid output unit. Enter C for celsius or F for Fahrenheit.")
        elif input_unit == output_unit:
            print(f"{input_temp}{input_unit} is {input_temp}{input_unit}, duh")
            return

        output_temp = 0.0
        if input_unit == "C" and output_unit == "F":
            output_temp = celsius_to_fahrenheit(input_temp)
        elif input_unit == "F" and output_unit == "C":
            output_temp = fahrenheit_to_celsius(input_temp)
        
        print(f"{input_temp}{input_unit} is {output_temp}{output_unit}")
    except ValueError as e:
        print(f"An error occurred: {e}")

convert()