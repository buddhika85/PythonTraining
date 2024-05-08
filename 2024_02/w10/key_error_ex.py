try:
    # Creating a dictionary
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
    
    # Trying to access a non-existent key
    favorite_color = my_dict['favorite_color']
except KeyError as e:
    # Handling the KeyError exception
    print(f"KeyError: {e}: The specified key does not exist in the dictionary.")