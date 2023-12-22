# print(f"{1/0}")         # ZeroDivisionError: division by zero

def divide(x, y):
    return x/y


max_count = 5
used_count = 0
while(used_count < max_count):
    try:
        num_one = float(input("Number 1 : "))
        num_two = float(input("Number 2 : "))
        print(f"Division : {divide(num_one, num_two)}")
        used_count += 1
    except ValueError as e:
        print(f"Error - {e}")
    except ZeroDivisionError as e:
        print(f"Error - {e}")