class ClothingStore:
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

    def add_product(self, product_code, name, quantity, price, category):
        if product_code in self.inventory:
            print(f"Error - {product_code} already exists")
        else:
            self.inventory[product_code] = {
                "name": name,
                "quantity": quantity,
                "price": price,
                "categories": category
            }
            self.categories.add(category)
    
    def remove_product(self, product_code):
        if product_code not in self.inventory:
            print(f"Error - {product_code} unavailable")
        else:
            popped = self.inventory.pop(product_code)
            print(f"Deleted: {popped}")
    
    def update_quantity(self, product_code, quantity):
        if product_code not in self.inventory:
            print(f"Error - {product_code} unavailable")
        else:
            self.inventory[product_code]["quantity"] = quantity

    def calculate_total_value(self):
        total = 0.0
        for product in self.inventory.values():
            total += product["quantity"] * product["price"]
        return total

    def __str__(self) -> str:
        return f"Inventory\n{self.inventory}\nCategories\n{self.categories}"

# testing
clothingStore = ClothingStore()
print(f"\n{clothingStore}")

# add
clothingStore.add_product("P001", "Test Product", 10, 1.5, "Test Category")     # error
clothingStore.add_product("P004", "Test Product", 10, 1.5, "Test Category")    
print(f"\n{clothingStore}")

# deletion
# clothingStore.remove_product("P004")
# print(f"\n{clothingStore}")

# update
print(clothingStore.inventory)
clothingStore.update_quantity("P004", 100)
print(f"\n{clothingStore}")

# display total
print(f"Total = {clothingStore.calculate_total_value()}")