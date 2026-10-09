number=9
guess=int(input("enter the number between 1 and 10: "))
count=0
while guess!= number:
    if count== 4:
        print("Game over")
    count +=1
    guess= int(input("try again! enter the number between 1 and 10: "))

print("congratulation")
print(f"you guessed the number in {count} attempts.")