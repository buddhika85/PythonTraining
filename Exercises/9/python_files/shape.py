import math

class Shape:
    def __init__(self, name):
        self.name = name
    
    def perimeter(self):
        pass
    
    def area(self):
        pass
    
    def __str__(self) -> str:
        return self.name

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
    def area(self):
        return self.height * self.width
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n\tWidth: {self.width}\n\tHeight: {self.height}\n\tArea: {self.area()}\n\tPerimeter: {self.perimeter()}"

class Hexagon(Shape):
    def __init__(self, side):
        super().__init__("Hexagon")
        self.side = side
    
    def perimeter(self):
        return 6 * self.side
    
    def area(self):
        return (3 * math.sqrt(3)) / 2 * self.side * self.side
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n\tSide: {self.side}\n\tArea: {self.area()}\n\tPerimeter: {self.perimeter()}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        self.name = "Square"
    
    def __str__(self) -> str:
        return f"{self.name}\n\tSide: {self.side}\n\tArea: {self.area()}\n\tPerimeter: {self.perimeter()}"

class Shapes:
    def __init__(self) -> None:
        self.shapes = []
    
    def add_shape(self, shape):
        self.shapes.append(shape)
    
    def __str__(self):
        str = ""
        for shape in self.shapes:
            str += f"{shape}\n"
        return str

# test code
rectangle = Rectangle(10, 5)
hexagon = Hexagon(10)
square = Square(4)
shapes = Shapes()

shapes.add_shape(rectangle)
shapes.add_shape(hexagon)
shapes.add_shape(square)

# Rectangle
#         Width: 10
#         Height: 5
#         Area: 50
#         Perimeter: 30
# Hexagon
#         Side: 10
#         Area: 259.8076211353316
#         Perimeter: 60
# Square
#         Side: 4
#         Area: 16
#         Perimeter: 16
print(shapes)

