class Student:
  def __init__(self,name,student_id,department):
    self.name=name
    self.student_id=student_id
    self.department=department
  def display_info(self):
    print("Student Name:", self.name)
    print("Student ID:", self.student_id)
    print("Department:", self.department)
  def introduce(self):
    print(f"Hello! My name is {self.name}. "
          f"I am a student in the {self.department} department.")

student1 = Student("Abebe", "SE001", "Software Engineering")
student2 = Student("Hana", "SE002", "Computer Science")
student3 = Student("Mekdes", "SE003", "Information Technology")

print("Student 1 Information:")
student1.display_info()
student1.introduce()

print("\nStudent 2 Information:")
student2.display_info()
student2.introduce()

print("\nStudent 3 Information:")
student3.display_info()
student3.introduce()
# 1. What is a class in Python?

#A class is a blueprint or template used to create objects. It defines the attributes (data) and methods (functions) that its objects will have. 
#2. What is an object?

 #An object is an instance of a class. It has its own data (attributes) and can use the methods defined in its class.

#3. What is the purpose of the __init__() method?

 #The __init__() method is a special method called a constructor in Python. Its purpose is to initialize an object's attributes when the object is created.