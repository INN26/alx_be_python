# base class
class Shape:
    def area(self):
        raise NotImplementedError(" this method is expected to be overridden in any subclass of Shape")
#derived class
class Rectangle(Shape):
      def __init__(self, length, width):
          self.length = length
          self.width = width
      def area(self):
           return self.length * self.width
      
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2