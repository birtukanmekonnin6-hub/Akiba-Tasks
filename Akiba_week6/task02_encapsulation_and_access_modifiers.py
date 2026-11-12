class BankAccount:
  def __init__(self,balance,account_holder):
    self.__balance=balance
    self.account_holder=account_holder
  
  def deposit(self,amount):
    if amount <0:
      return ValueError("deposit cannot be negative")
    self.__balance +=amount
  
  def withdraw(self,amount):
    if amount < 0:
      return ValueError("Withdraw cannot be negative")
    if amount > self.__balance:
      return ValueError("insufficient balance")
    self.__balance -= amount
  
  def get_balance(self):
    return self.__balance
  
b1=BankAccount(1000,"abel")
b1.deposit(200)
b1.withdraw(500)
print(b1.get_balance())
# 1,What is encapsulation? encapsulation is oop principle that combine data (attribute) and 
# methods into a single unit(class) 
# 2, why do we use private attribut?
# We use private attributes to protect an object's internal data from unintended or invalid direct modification from outside the class.
# 3, what is name mangling in python?
#process python use to change the names of attributes that begin with two underscores in side
# 4,what is the difference between public,protected and private naming convention?
# Public (name) attributes can be accessed and modified from anywhere, protected (_name) attributes are intended for use within the class and its subclasses but can still be accessed outside, while private (__name) attributes are intended for use only within their defining class, with Python using name mangling to discourage direct outside access.
