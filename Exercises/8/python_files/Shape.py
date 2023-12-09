from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self) -> str:
        return self.name

class Rectangle(Shape):
    def __init__(self, name, height, width) -> None:
        super().__init__(name)
        self.height = height
        self.width = width
    
    def perimeter(self):
        return (self.height + self.width) * 2
    
    def area(self):
        return self.height * self.width

    def __str__(self) -> str:
        return f"{super().__str__()}:\n\tHeight = {self.height}\n\tWidth = {self.width}"

class Hexagon(Shape):
    def __init__(self, name, side) -> None:
        super().__init__(name)
        self.side = side
        self.num_of_sides = 6

    def area(self):
        return (3 * math.sqrt(3)) / 2 * self.side * self.side
    
    def perimeter(self):
        return self.side * self.num_of_sides
    
    def __str__(self) -> str:
        return f"{super().__str__()}:\n\tSide = {self.side}"

class Square(Rectangle):
    def __init__(self, name, side) -> None:
        super().__init__(name, side, side)
        self.side = side

    def __str__(self) -> str:
        return f"{self.name}:\n\tSide = {self.side}"
    
# test code
# rect = Rectangle("Rectangle 1" , 5, 10)
# print(f"{rect}\n\tArea: {rect.area()}\n\tPerimeter: {rect.perimeter()}")

# hex = Hexagon("Hexagon 1" , 10)
# print(f"{hex}\n\tArea: {hex.area()}\n\tPerimeter: {hex.perimeter()}")

# polymorphic
shapes = [Rectangle("Rectangle 1" , 5, 10), Hexagon("Hexagon 1" , 10), Square("Square 1", 4)]
for shape in shapes:
    print(f"{shape}\n\tArea: {shape.area()}\n\tPerimeter: {shape.perimeter()}")