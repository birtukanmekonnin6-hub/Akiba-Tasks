class Student:
  school_name="Akiba Academy"
  def __init__(self,name,score,department):
    self.name=name
    self.score=score
    self.department=department
  def display(self):
    return (f"school name:{Student.school_name}, student name:{self.name}, student score:{self.score},student department:{self.department}")

s1= Student( "Abel",90,"computer science")
s2=Student("Robel",65,"chemical engineering")
s2.score=85
print(s1.display())
print(s2.display())