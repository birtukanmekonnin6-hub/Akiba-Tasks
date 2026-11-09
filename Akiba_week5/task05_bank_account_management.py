class BankAccount:
  def __init__(self,owner,balance):
    self.owner=owner
    self.balance=balance
  def deposit(self,amount):
    self.balance += amount
  def withdraw(self,amount):
    self.balance -= amount
  def display_balance(self):
    return f" THE current balance is {self.balance}"
    
