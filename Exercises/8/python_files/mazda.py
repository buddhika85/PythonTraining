class CX9Sport:
    def __init__(self) -> None:
        self.features = ["Anroid Auto", "Apple Car Play", 
                         "Mazda Radar Cruise Control with Stop and Go",
                         "Reverse Camera"]
    
    def __str__(self) -> str:
        str = ""
        for feature in self.features:
            str += f"{feature}\n"
        return str

class CX9Touring(CX9Sport):
    def __init__(self) -> None:
        super().__init__()
        self.features += ["Leather seats", 
                         "Front parking sensors",
                         "Paddle shift gear control"]
    
class CX9GT(CX9Touring):
    def __init__(self) -> None:
        super().__init__()
        self.features += ["Sunroof", 
                         "Bose Audio",
                         "Mazda connect system"]

print(CX9Sport())
print(CX9Touring())
print(CX9GT())