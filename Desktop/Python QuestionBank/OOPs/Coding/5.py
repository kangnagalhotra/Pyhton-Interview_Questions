# Use abc module to create an abstract class.

from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius =  radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2*3.14*self.radius
    
class Rectangle(Shape):
    def __init__(self,length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

Circ = Circle(5)
print("Circle Area : ", Circ.area())
print("Perimeter of Circle: ",Circ.perimeter())

rect = Rectangle(4, 6)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())
    
    