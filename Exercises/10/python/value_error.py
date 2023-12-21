# while True:
#     try:
#         number = int(input("Number : "))
#         print(f"You entered: {number}")
#         break
#     except ValueError:
#         print("\tInvalid input, Please input an integer")

max_attempts = 3
used_count = 0
provided = False
while used_count < max_attempts and not provided:
    try:
        used_count += 1
        number = int(input(f"Attempt {used_count}: Number : "))
        print(f"You entered: {number}")
        provided = True
    except ValueError as e:
        print(f"\tInvalid input: {e}, Please input an integer")

if not provided:
    print("You've failed to input an integer! I'm giving up...")