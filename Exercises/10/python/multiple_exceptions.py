try:
    my_list = [10, 20, 30, 40, 50]    
    index = int(input("Enter an index for array indexing: "))   # ValueError may occur
    value = my_list[index]                                      # IndexError may occur
    print("Value at index", index, "is:", value)
except ValueError as e:
    print(f"Invalid input - {e}. Please enter a valid integer.")
except IndexError as e:
    print(f"Index out of range - {e}. Please enter a valid index within the range of the array.")