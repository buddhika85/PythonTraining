try:
    # Creating a list
    my_list = [10, 20, 30, 40, 50]
    
    # Trying to access an out-of-range index
    value = my_list[10]
except IndexError as e:
    # Handling the IndexError exception
    print(f"IndexError: {e}: The specified index is out of range.")