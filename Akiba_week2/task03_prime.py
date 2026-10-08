num=int(input("enter the number: "))
count=0
if num == 0:
    print("Not prime")
elif num == 1:
    print("Not prime")
elif num ==2:
    print("Prime")
elif num >2:
    for i in range (1,num+1):
        if num % i ==0:
            count += 1
    if count == 2:
        print("Prime")
    elif count > 2:
        print("composite")