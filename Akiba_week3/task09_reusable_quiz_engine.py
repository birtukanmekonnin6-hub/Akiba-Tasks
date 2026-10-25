def display_a_question(questions,options):
   question1=questions
   A=options[0]
   B=options[1]
   C=options[2]
   D=options[3]
   return (f'{question1} \n A,{A}  B, {B}, C,{C} D,{D}')
def validate_an_answer(answer):
    valid = ("A", "B", "C", "D")

    answer = answer.upper()

    while answer not in valid:
        print("Invalid input!")
        answer = input("Enter a valid option (A, B, C, or D): ")
        answer = answer.upper()

    return answer
def check_whether_the_answer_is_correct(correct,useranswer):
     correct_answer=correct
     user=validate_an_answer(useranswer)
     if user==correct_answer:
         return "Correct!"
     else:
         return "Incorrect"
     
def update_the_score(score,result):
    if result == "Correct!":
        score += 1
    return score

def categorize_the_result(percentage):
    if percentage >= 80:
        return "Excellent!"
    elif percentage >= 60:
        return "Good job!"
    else:
        return "Keep practicing!"

def display_final_results(score, total_questions):
    percentage = (score / total_questions) * 100
    incorrect = total_questions - score

    print("\n--- QUIZ RESULTS ---")
    print("Total questions:", total_questions)
    print("Correct answers:", score)
    print("Incorrect answers:", incorrect)
    print("Final score:", str(score) + "/" + str(total_questions))
    print("Percentage:", round(percentage, 2), "%")
    category = categorize_the_result(percentage)
    print("Result category:", category)
  
def ask_to_play_again():
    answer = input("Do you want to play again? (yes/no): ")
    answer = answer.lower()

    while answer not in ("yes", "no"):
        print("Please enter yes or no.")
        answer = input("Do you want to play again? (yes/no): ")
        answer = answer.lower()

    return answer == "yes"

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["Java", "Python", "C++", "HTML"],
        "correct_answer": "B"
    },
    {
        "question": "Which function displays output?",
        "options": ["input()", "len()", "print()", "type()"],
        "correct_answer": "C"
    },
    {
        "question": "Which keyword returns a value?",
        "options": ["print", "return", "input", "while"],
        "correct_answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "list", "bool"],
        "correct_answer": "D"
    },
    {
        "question": "Which operator checks equality?",
        "options": ["=", "==", "!=", "+"],
        "correct_answer": "B"
    }
]

play_again = True

while play_again:
    score = 0

    for item in questions:
        print(display_a_question(
            item["question"],
            item["options"],
        ))

        answer = input("Enter your answer (A/B/C/D): ")

        result = check_whether_the_answer_is_correct(
            item["correct_answer"], answer
        )

        print(result)
        score = update_the_score(score, result)

    display_final_results(score, len(questions))
    play_again = ask_to_play_again()

print("Thank you for playing!")

