class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def display_info(self):
    return("....")
class Manager(Employee):
  def __init__(self,name,salary,department):
    super().__init__(name,salary)
    self.department=department
  def display_info(self):
    print(f"name:{self.name},salary:{self.salary}")

class Developer(Employee):
  def __init__(self,name,salary,programming_language):
    super().__init__(name,salary)
    self.programming_langauge= programming_language

  def display_info(self):
    print(f"name:{self.name},salary:{self.salary}")

m1=Manager("Abel",80000,"computer science")
d1=Developer("Birtukan",100000,"python")
m1.display_info()
d1.display_info()


### 1, what is inheritance? 
#oop concept thet allaow one class (child)to acquire the attributes  and methods
# of another class(parent).
##2,What is the difference between a parent class and a child class?
#parent class is class whose attributes and methods are inherited
#child class  is class that inherit from another class
#3,What is method overriding?
# happen when a child class define a method that already exists in its parent class
#4,What is the purpose of super()?
# used to access methods of the next class in the method resolution order
## What is the difference between single and multiple inheritance?
# in single inheritance one child inherit from one parent 
# in multiple inheritance one child inherit from more than one parents.#