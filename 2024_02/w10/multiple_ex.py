try:
    my_list = [10, 20, 30, 40, 50]
    
    index = int(input("Enter an index for array indexing: "))
    
    value = my_list[index]
    
    print("Value at index", index, "is:", value)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except IndexError:
    print("Index out of range. Please enter a valid index within the range of the array.")