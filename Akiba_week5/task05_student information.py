class Student:
  def __init__(self,name,age,department):
    self.name=name
    self.age=age
    self.department=department
  def display_info(self):
    return (f"Student name:{self.name} AGE: {self.age}  department:{self.department}")

S1=Student("Abel",24,"computer science")
S2=Student("Birtukan",21,"Software engineering")
S3=Student("Kiyya",20,"information system")
print(S1.display_info())
print(S2.display_info())
print(S3.display_info())
