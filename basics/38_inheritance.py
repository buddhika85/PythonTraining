# dry - dont repeat yourself

class Mammal:
    
    def walk(self):
        print('walk')


class Dog(Mammal):      # Dog's Parent class is Mammal class
     
     def bark(self):
         print('bark')


class Cat(Mammal):
    
    def miaow(self):
        print('miaaw')


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.miaow()



