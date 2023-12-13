class CX9Sport:
    def __init__(self, price):
        self.features = ["Android Auto & Apple Car Play", "Mazda Radar Cruise Control with Stop & Go", "Reverse Camera"]
        self.price = price
    
    def get_name(self):
        return "\n----CX9Sport----"

    def __str__(self):
        str = f"{self.get_name()}\nPrice: ${self.price} and features list:\n"
        for feature in self.features:
            str += f"\n{feature}"
        return str


class CX9Touring(CX9Sport):
    def __init__(self, price):
        super().__init__(price)
        self.features += ["Leather seats", "Front parking sensors", "Paddle shift gear control"]

    def get_name(self):
        return "\n----CX9Touring----\n"

class CX9GT(CX9Touring):
    def __init__(self, price):
        super().__init__(price)
        self.features += ["Sunroof", "Bose Audio", "Mazda Connect System"]

    def get_name(self):
        return "\n----CX9GT----\n"

class ShowRoom:
    def __init__(self) -> None:
        self.list = []
    
    def add_cx9(self, vehicle):
        self.list.append(vehicle)
    
    def __str__(self) -> str:
        str = f"Show Room Vehicle List - "
        for cx9 in self.list:
            str += f"\n{cx9}"
        return str

# test code
show_room = ShowRoom()
show_room.add_cx9(CX9Sport(52397))
show_room.add_cx9(CX9Touring(60377))
show_room.add_cx9(CX9GT(70352))

print(show_room)