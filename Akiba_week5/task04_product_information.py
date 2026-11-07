class Product:
  def __init__(self,name,price,quantity):
    self.name=name
    self.price=price
    self.quantity=quantity
  def __str__(self):
    return f"product name:{self.name}, product price:{self.price}, quantity:{self.quantity}"
  def total_value(self):
    return self.price * self.quantity
p1=Product("Phone",20000,10)
p2=Product("Earphone",4000,6)
p3=Product("laptop",100000,7)
print(p1)
print(p2)
print(p3)
print(f"the total value of product1: {p1.total_value()}")
print(f"the total value of product2: {p2.total_value()}")
print(f"the total value pf product3: {p3.total_value()}")
# What is the purpose of the __str__() method?
# define how  an object should look when we want a readable user friendly representation