import random

class Cyclist:
    def __init__(self, name, endurance, sprint_ability, preparation):
        self.name = name
        self.endurance = endurance
        self.sprint_ability = sprint_ability
        self.preparation = preparation

    def race(self):
        #return 0.5 * self.preparation + 0.25 * self.endurance + 0.25 * self.sprint_ability
        return random.uniform(0, 5)     # random number between 0 and 5 inclusive 


class BikeRace:
    def __init__(self, event_name):
        self.event_name = event_name
        self.participants = []              # empty Cyclist list
    
    def register_cyclist(self):
        print('REGISTER CYCLIST')
        print('----------------')
        print("- What is the cyclist's name?")
        name = input()
        print(f"- What is {name}'s endurance level (a number between 1 and 100)?")
        endurance = int(input())
        print(f"- What is {name}'s sprint ability (a number between 1 and 100)?")
        sprint_ability = int(input())
        print(f"- How was {name}'s preparation (a number between 1 and 100)?")
        preparation = int(input())
        cyclist = Cyclist(name, endurance, sprint_ability, preparation)
        self.participants.append(cyclist)
        print(f"{name}is now a registered participant of this race.")

    def conductRace(self):
        for cyclist in self.participants:
            print(f'{cyclist.name} => {cyclist.race()}')
# testing
# cyclist_one = Cyclist('John', 50, 800, 80)
# cyclist_two = Cyclist('Jack', 80, 700, 70)

# print(f'{cyclist_one.name} - {cyclist_one.race()}')
# print(f'{cyclist_two.name} - {cyclist_two.race()}')

bike_race = BikeRace('Race 1')
bike_race.register_cyclist()
bike_race.register_cyclist()
bike_race.conductRace()