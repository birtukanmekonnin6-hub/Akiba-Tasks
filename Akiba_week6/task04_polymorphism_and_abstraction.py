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

#1, what is polymorphism?
# means that different objects can use the same method name,but each object can behave differently
#when that method is called
# 2,what is abstraction ?
# an oop princpile that hides unnecessary internal implementation detail and
# exposes only the essential features that user needs to interact with
# 3,What is an abstract class?
# special parent class that defines methods its child required to implement
# 4 ,What happens if a child class does not implement an inherited abstract method?
# raise error
# 5,What is the difference between abstraction and encapsulation?
# Abstraction: Hides unnecessary implementation details and shows only the essential features of an object. It focuses on what an object does.

# Encapsulation: Bundles data and methods into a single class and controls access to the data to protect it from unauthorized or incorrect modification.