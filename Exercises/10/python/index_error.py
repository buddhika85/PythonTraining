try:
    list = [1,2,3]
    index_3_element = list[3]
except IndexError as e:
    print(f"Error- {e}")
