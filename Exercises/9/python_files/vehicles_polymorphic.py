class Vehicle:
    def __init__(self, wheel_size, tyre_thickness, name):
        self.wheel_size = wheel_size
        self.tyre_thickness = tyre_thickness
        self.name = name

    def show_details(self):
        print(f"Vehicle: {self.name}")
        print(f"Wheel Size: {self.wheel_size}")
        print(f"Tyre Thickness: {self.tyre_thickness}")


class Truck(Vehicle): # Truck INHERITS from Vehicle
    def __init__(self, wheel_size, tyre_thickness, name, cargo_capacity):
        # The following line calls the Vechicle constructor
        super().__init__(wheel_size, tyre_thickness, name)

		# Set the truck-specific attribute here
        self.cargo_capacity = cargo_capacity

    def show_details(self):
        super().show_details()
        print(f"Cargo Capacity: {self.cargo_capacity}kg")


class Car(Vehicle): # Car inherits from Vehicle
    def __init__(self, wheel_size, tyre_thickness, name, seating_capacity):
        # The following line calls the Vechicle constructor
        super().__init__(wheel_size, tyre_thickness, name)

		# Set the car-specific attribute here
        self.seating_capacity = seating_capacity

    def show_details(self):
        super().show_details()
        print(f"Seating Capacity: {self.seating_capacity}")

# Testing code
def display_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.show_details()          # this line is polymorphic
        print()

truck = Truck(34, 22, "Izuzu", 3435.0)
car = Car(80, 30, "Toyota", 5)
vehicles = [truck, car]

display_vehicles(vehicles)