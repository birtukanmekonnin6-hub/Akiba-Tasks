def validate_student_score(score):
     if   score < 0 or score >100:
          print("invalid score")
          return False

     else:
          print("valid score")  
          return True
def calculate_grade(score):
     if score >=90:
          return "A" 
     elif score >=80:
          return "B"
     elif score >=70:
          return "C"
     elif score >=60:
          return "D"
     else:
          return "F"

def calculate_the_average_score(students):
     total=0
     for student in students:
          total +=student["score"]   
     average= total/ len(students)
     return average
def highest_score(students):
     highest=students[0]["score"]
     for i in students:
          if students[i]["score"] > highest:
               highest=students[i]["score"]
     return highest
def lowest_score(students):
     lowest=students[0]["score"]
     for i in students:
          if students[i]["score"]<lowest:
               lowest= students[i]["score"]
     return lowest
def count_passed_and_failed(students):
     passed=0
     failed=0
     for student in students:
          if student["score"] >= 50:
               passed+=1
          else:
               failed += 1
     return passed, failed
def count_student_above_average(students):
     average=calculate_the_average_score(students)
     above=[]
     for student in students:
          if student["score"] > average:
             above.append (student["name"])
     return above
     
     
def generate_report_for_class(students):
     passed,failed=count_passed_and_failed(students)
     average=calculate_the_average_score(students)
     above=count_student_above_average(students)
     print("=====================CLASS REPORT===============")
     print("name        score        grade")
     for student in students:
          name =student["name"]
          score=student["score"]
          grade=calculate_grade(student["score"])
          print(f'{name}           {score}           {grade}')
     print(f"number of student passed: {passed}")
     print(f"number of student failed: {failed}")
     print(f"the average score is: {average}")
     print("students which score above the average")
     print(above)
     print("=================================================")
students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]
generate_report_for_class(students)

