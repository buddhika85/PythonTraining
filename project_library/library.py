class Library:
    pass

class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.availability = True
    
    def __str__(self):
        availability_str = 'Yes' if self.availability else 'No'     # ternary operator
        return f'Book {self.id} {self.name} availability: {availability_str}';