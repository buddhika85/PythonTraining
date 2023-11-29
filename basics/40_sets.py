# do not allow duplicates
grades = {"F", "P", "C", "D", "HD", "HD"}      
print(grades)

# create empty set
my_set = set()      # {}
if len(my_set) == 0:
    print("my_set is empty")
my_set.add(1)       # {1}
my_set.add(2)       # {1, 2}
my_set.add(1)       # will not be added - duplicate
my_set.discard(1)   # remove => {1}
print(my_set)



# creating a set from a list using set() function
list = ["Banana", "Pineapple", "Pineapple", "Orange"]
fruitsSet = set(list)
print(fruitsSet)

# iterating
for fruit in fruitsSet:
    print(fruit)

letters = set()
letters.add("A")
letters.add("B")
letters.add("C")

# check if B is there in set
if "B" in letters:
    print("B is there")
if "b" not in letters:
    print("b is not there")