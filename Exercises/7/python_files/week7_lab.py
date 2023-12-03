class ClothingStore :
    def __init__(self) -> None:
        self.inventory = {}
        self.inventory["P001"] = {
            "name": "T-Shirt",
            "quantity": 10,
            "price": 15.99,
            "categories": "Shirts"
        }
        self.inventory["P002"] = {
            "name": "Jeans",
            "quantity": 5,
            "price": 29.99,
            "categories": "Pants"
        }
        self.inventory["P003"] = {
            "name": "Sneakers",
            "quantity": 8,
            "price": 49.99,
            "categories": "Shoes"
        }
        self.categories = {"Shirts", "Pants", "Shoes"}


    def add_product(self, product_code, name, quantity, price, categories):
        if product_code in self.inventory:
            print(f"-------Added Product code = {product_code} already exists")
        else:
            self.inventory[product_code] = {
                "name": name,
                "quantity": quantity,
                "price": price,
                "categories": categories
            }
            self.categories.add(categories)
            print(f"-------Product code = {product_code} added")


    def remove_product(self, product_code):
        if product_code in self.inventory:
            product = self.inventory.pop(product_code)
            print(f"-------Removed {product}")
        else:
            print(f"-------Product code = {product_code} does not exist")
    
    def update_quantity(self, product_code, quantity):
        if product_code in self.inventory:
           self.inventory[product_code]["quantity"] = quantity
           print(f"-------Product code = {product_code} quantity updated to {quantity}")
        else:
            print(f"-------Product code = {product_code} does not exist")
    
    def calculate_total_value(self):
        total = 0.0
        for product in self.inventory.values():
            total += product["price"] * product["quantity"]
        return total

# Test code
clothing_store = ClothingStore()
# for product in clothing_store.inventory.values():
#     print(product)
# print(clothing_store.categories)

# adding
# clothing_store.add_product("p1", "Test Prod", 10, 10.5, "Test")
# clothing_store.add_product("p2", "Test Shirts", 10, 10.5, "Shirts")
for product in clothing_store.inventory.values():
    print(product)
# print(clothing_store.categories)

# removing
# clothing_store.remove_product("p2")
# print("After removing 1 product")
# for product in clothing_store.inventory.values():
#     print(product)

# updating
# clothing_store.update_quantity("p1", 100)
# for product in clothing_store.inventory.values():
#     print(product)

# total
print(f"{clothing_store.calculate_total_value()}")