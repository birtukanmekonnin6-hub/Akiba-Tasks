def is_prime(number):
   count=0
   for i in range (1,number +1):
      if number%i==0:
         count +=1
   if count == 2:
      return "prime"
   elif count >2:
      return "composite"
def get_divisors(number):
   divisor=[]
   for i in range(1,number):
      if number%i ==0:
         divisor.append(i)
   return divisor
def sum_of_digits(number):
    total=0
    while number >0:
       digit=number %10
       total=total+digit
       number=number//10
    return total

def reverse_number(number):
    reversednumber = ""

    for i in str(number):
        reversednumber = i + reversednumber

    return reversednumber


def analyze_number(number):
    print("=============number analysis============")
    if number<=0:
       print("choose number greater than 0")
    if number%2==0:
       print("even")
    else:
       print("odd")
    prime=is_prime(number)
    overall=sum_of_digits(number)
    rev=reverse_number(number)
    div=get_divisors(number)

    print(f"The number is :{prime}")
    print(f"The sum of the digit is:{overall}")
    print(f"The reversed number is: {rev}")
    print(f"It divisors are : {div}")
    print("==========================================")
analyze_number(12345)
    
  
   
      
      