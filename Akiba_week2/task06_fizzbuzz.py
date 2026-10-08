start=int(input("enter the first number: "))
end=int(input("enter the last number: "))
for i in range (start , end):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)