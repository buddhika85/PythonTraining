# dictionary - key value pairs

customer = {
    "id": 1,
    "name": "John Smith",
    "is_verified": True
}

print(customer)
print(customer["name"])     # access a key's value

print(customer.get('name'))

customer["name"] = "abcd"                   # update value of key
print(customer['name'])

customer['birth_date'] = '1st Feb 2011'     # add a new key
print(customer)