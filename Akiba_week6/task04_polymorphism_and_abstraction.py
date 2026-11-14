#part A: polymorphism
class Dog:
  def make_sound(self):
    print("woof!")
class Cat:
  def make_sound(self):
    print("meow")
class Cow:
  def make_sound(self):
    print("moo")

dog=Dog()
cat=Cat()
cow=Cow()
dog.make_sound()
cat.make_sound()
cow.make_sound()
#part B:Abstraction
from abc import ABC,abstractmethod
class Shape(ABC):
  @abstractmethod
  def calculate_area(self):
    pass

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def calculate_area(self):
    return self.length * self.width

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
    self.pay=3.14
  def calculate_area(self):
    return self.pay *(self.radius**2)
  
  
rectangle=Rectangle(3,4)
circle=Circle(4)
print(rectangle.calculate_area())
print(circle.calculate_area())