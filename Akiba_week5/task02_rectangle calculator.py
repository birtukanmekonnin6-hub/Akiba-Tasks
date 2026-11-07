class Rectangle:
  def __init__(self,length,width):
    self.length= length
    self.width=width
  def area(self):
     return (self.length * self.width)
  def perimeter(self):
    return (2*(self.length+self.width))

r1=Rectangle(4,5)
r2=Rectangle(6,7)
print(f"the area of rectangle 1 is:{r1.area()}")
print(f"the area of rectangle 2 is: {r2.area()}")
print(f"the perimeter of the rectangle 1 is :{r1.perimeter()}")
print(f"the perimeter of the rectangle 2 is :{r2.perimeter()}")