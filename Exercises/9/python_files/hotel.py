class Room:
    def __init__(self, id, bed_type, head_count, price_per_day):
        self.id = id
        self.status = "Available"
        self.bed_type = bed_type
        self.head_count = head_count
        self.price_per_day = price_per_day
    
    def book(self):
        if self.status == "Available":
            self.status = "Booked"
            print("Room booked")
        else:
            print("Error - Room is unavailable for booking")
    
    def unbook(self):
        if self.status == "Booked":
            self.status = "Available"
            print("Room unbooked. - now available")
        else:
            print("Error - Room not booked to cancel the booking")
    
    def check_in(self):
        if self.status == "Booked":
            self.status = "Checked-In"
            print("Room checked in")
        else:
            print("Error - Room not booked to check in")
    
    def check_out(self):
        if self.status == "Checked-In":
            self.status = "Available"
            print("Room checked out. - now available")
        else:
            print("Error - Room not checked in to check out")
    
    def calc_price(self, day_count):
        return self.price_per_day * day_count
    
    def __str__(self):
        return f"ID: {self.id}, Status: {self.status}, bed-type: {self.bed_type}, head-count: {self.head_count}, price per day: {self.price_per_day}"

# sub classes
class StandardRoom(Room):
    def __init__(self, id):
        super().__init__(id, "Double", 2, 10000)
    
    def __str__(self):
        return f"Standard Room: {super().__str__()}"
    
class DeluxRoom(Room):
    def __init__(self, id, view):
        super().__init__(id, "King", 4, 20000)
        self.view = view
        self.additional_amenities = ["bath tub", "minibar", "smartTV", "electronic SafeBox"]
        self.additional_meal_price = 1000
        self.additional_meal_count = 0
    
    def request_meal(self):
        self.additional_meal_count += 1
    
    def calc_price(self, day_count):
        return super().calc_price(day_count) + (self.additional_meal_count * self.additional_meal_price)
    
    def __str__(self):
        return f"Delux Room: {super().__str__()}, view: {self.view}, features: {self.additional_amenities}, meal count: {self.additional_meal_count}, meal price: {self.additional_meal_price}"

class Hotel:
    def __init__(self) -> None:
        self.romms = []
    
    def add_room(self, room):
        self.romms.append(room)
    
    def __str__(self) -> str:
        str = "All Rooms\n"
        for room in self.romms:
            str += f"{room}\n"
        return str

# testing
hotel = Hotel()
hotel.add_room(StandardRoom(1))
hotel.add_room(DeluxRoom(2, "River View"))
hotel.add_room(DeluxRoom(3, "Mountain View"))
hotel.add_room(StandardRoom(4))
print(hotel)

# testing
# standard_room = StandardRoom(1);
# standard_room.book()
# standard_room.check_in()
# print(standard_room)
# standard_room.check_out()
# print(f"Price for 2 days = {standard_room.calc_price(2)}")
# print()

# delux_room = DeluxRoom(2, "River View");
# delux_room.book()
# delux_room.check_in()
# delux_room.request_meal()
# delux_room.request_meal()
# print(delux_room)
# delux_room.check_out()
# print(f"Price for 2 days = {delux_room.calc_price(2)}")