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




