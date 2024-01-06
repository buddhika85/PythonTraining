# printing list of lists
list_of_lists = [[1,2,3], [4,5,6,7]]
# for list in list_of_lists:
#     for i in list:
#         print(i)

# do the same with a while loop
i = 0
# while i < len(list_of_lists):
#     j = 0
#     while j < len(list_of_lists[i]):
#         print(list_of_lists[i][j])
#         j += 1
#     i += 1

# 30,40,50,...,80 using range function
# for num in range(30, 81, 10):           # inclusive start, exclusive stop, step
#     print(num)

# print("\n")
# # 20,18,16....-2
# for num in range(20, -3, -2):
#     print(num)

# def add(x, y):
#     return x + y

# print(add(10, 15))              # numeric addition
# print(add('A', 'b'))            # string concatenation
# print(add(True, False))         # for bools + acts like or operator
# print(add(False, False))

list = [1]
list.append("a")
list.append("b")
list.remove(1)
print(list)
list.pop(1)
print(list)