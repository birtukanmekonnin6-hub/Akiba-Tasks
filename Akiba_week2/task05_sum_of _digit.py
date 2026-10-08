num=input("enter the number: ")
sum=0
for i in num:
   sum=sum+int(i)
print(sum) 

number=int(input("enter the number: "))
total=0
while number >0:
    digit=number %10
    total=total+digit
    number=number//10
print (total)