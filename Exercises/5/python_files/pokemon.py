class Pokemon:
    def __init__(self, name, level, pokemon_type):
        self.name = name
        self.level = level
        self.pokemon_type = pokemon_type
        self.health = 10 * self.level
    
    def take_damage(self, damage):
        self.health -= damage
    
    def attack(self, target):
        target.take_damage(self.level)
    
    def __str__(self) -> str:
        return f'{self.name} type {self.pokemon_type} of level {self.level} has health {self.health}'
    
# testing
pokemon_obj_one = Pokemon('Pikachu', 1, 'electric')
pokemon_obj_two = Pokemon('Black', 2, 'dragon')

print(pokemon_obj_one)
print(pokemon_obj_two)

pokemon_obj_one.attack(pokemon_obj_two)
pokemon_obj_two.attack(pokemon_obj_one)
print(f'\nAfter one round of attacking: ')
print(pokemon_obj_one)
print(pokemon_obj_two)