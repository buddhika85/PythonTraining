class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_patron(self, patron):
        self.patrons.remove(patron)

    def add_book(self, book):
        self.books.append(book)

class Patron:
    def __init__(self, name, is_staff):
        self.name = name
        self.is_staff = is_staff
        self.borrowed_books = []

    def borrow_book(self, book):
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        book.is_borrowed = False
        self.borrowed_books.remove(book)

    def view_borrowed_books(self):
        for book in self.borrowed_books:
            print(book)
    
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self) -> str:
        return f"Book: {self.name}, author: {self.author}, year: {self.year}, Borrowed: {self.is_borrowed}"