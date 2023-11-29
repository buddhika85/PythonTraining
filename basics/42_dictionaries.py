# create empty diactionary
empty_dictionary = {}
# length of dictionary
print(len(empty_dictionary))                # 0
print(empty_dictionary)

class City:
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"

# create a dictionary with key value pairs
dict = {
    "Sydney": City("Sydney", "Australia"),
    "New York": City("New York", "USA"),
    "Rome": City("Rome", "Italy")
};
print(len(dict))                # 3




# accessing dictionary element using unique key
print(dict["Sydney"])
print(dict["Sydney"].country)

# checking exitance of a key
if "New York" in dict:
    print(dict["New York"])

if "new york" not in dict:
    print("new york not in")

# adding
dict["Shanghai"] = City("Shanghai", "China")
print(len(dict))                # 4

# edit
if "New York" in dict:
    dict["New York"].country = "United States of America"
    print(dict["New York"])

# deleting
removed = dict.pop("Shanghai")
print(f"Removed: {removed}")

# display all keys
for key in dict.keys():
    print(key)

# display all values
for value in dict.values():
    print(value)