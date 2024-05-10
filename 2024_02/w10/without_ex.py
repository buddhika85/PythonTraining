while True:
    try:
        number = int(input('Enter an integer: '))
        break  # Exit the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter an integer!")

# Now you can proceed with the 'number' variable containing a valid integer.
print(f"You've entered {number}")