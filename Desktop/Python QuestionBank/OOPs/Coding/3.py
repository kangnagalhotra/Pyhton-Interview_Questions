# Demonstrate polymorphism with a method area() in Circle and Square classes.

# circle , square has same method area , same method call
import math
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius * self.radius
class Square():
    def __init__(self,side):
        self.side =  side
    def area(self):
        return self.side*self.side
shapes = [Circle(5),Square(10)]
for shape in shapes:
    print(f"Area : {shape.area()}")