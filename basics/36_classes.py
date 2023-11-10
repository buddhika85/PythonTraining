class Point:            # start with capitilize - upper camel class

    # constructor
    def __init__(self, x, y):               # self - references current object
        self.x = x
        self.y = y

    def move(self):
        print('Move')
    
    def draw(self):
        print('draw')




# usinng the class
point_one = Point(1, 2)

point_one.draw()
point_one.move()

point_one.x =10

print(f'{point_one.x + point_one.y}')
