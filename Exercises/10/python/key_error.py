try:
    dictionary = {"banana": 20, "apple": 10}
    print(f"Apples Count: {dictionary["apple"]}")       # key exists
    print(f"Oranges Count: {dictionary["orange"]}")     # key unavailable
except KeyError as e:
    print(f"Key Error - {e}")
