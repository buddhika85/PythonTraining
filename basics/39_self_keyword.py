class VideoGame:
    genre = 'Normal'
    # constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # a method
    def apply_discount(self, discount):
        self.price -= discount
    
    # another method
    def display(self):
        print(f'{self}')

    # to provide a string about object
    def __str__(self):
        return f'{self.name} - {self.price}'
    
videoGame = VideoGame("Zelda", 100)
videoGame.display()

videoGame.apply_discount(10)
videoGame.display()

videoGame.price = 110
videoGame.display()

print(f'{videoGame.genre}')
print(f'__str__ = {videoGame}')