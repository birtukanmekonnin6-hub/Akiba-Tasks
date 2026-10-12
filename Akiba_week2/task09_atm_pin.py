PIN="1234"
userpin=input("enter the password :  ")
count=0
while userpin!=PIN:
    if 0<=count<3:
        print("Incorrect PIN")
        print(f"Attemps remaining : {3-count}")
        userpin=input("enter the password again: ")
        count+=1
    elif count>=3:
        print("you reached the maximum limit") 
        break
if userpin==PIN:
    print("correct PIN")
    print(f"Attempts remainig: {(2-count)}")