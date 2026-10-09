number=int(input("enter postive number: "))
even=0
odd=0
total=0
for i in range(1,number+1):
  if i %2==0:
    even += 1
  elif i %2 !=0:
    odd +=1
  total += i
print (f"There are {even} even  numbers")
print(f"There are {odd} odd numbers")
print(f"The sum of the numbers is {total}")
 