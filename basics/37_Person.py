class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, msg):
        print(f'{self.name} says - {msg}')

john = Person('John')
john.talk('Hello')

bob = Person('Bob')
bob.talk('Hii')