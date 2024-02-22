import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        return

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Triangle Perimeter:", perim)
        return perim
    
class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Rectangle Perimeter:", perim)
        return perim
    
class Square(Rectangle):
    
    def __init__(self, a):
        self.a = a
    
    def calc_perimeter(self):
        perim = 4 * self.a
        print("Square Perimeter:", perim)
        return perim

### Examples for both new classes

# Rectangle
rect1 = Rectangle(5, 10)
rect1.calc_perimeter()

rect2 = Rectangle(7, 12)
rect2.calc_perimeter()

#Square
sq1 = Square(10)
sq1.calc_perimeter()

sq2 = Square(7)
sq2.calc_perimeter()
