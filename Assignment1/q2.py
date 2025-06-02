Create a custom Python class for managing a bank account with basic functionalities like deposit and
withdrawal?

  Ans- class BankAccount:
          def __init__(self,owner,balance=0):
            self.owner=owner
            self.balance=balance

          def deposit(self,amount):
            self.balance +=amount

          def withdraw(self,amount):
            if amount>self.balance:
              print("insufficient funds.")
            else:
              self.balance -=amount

          def display(self):
            print(f"{self.owner}'s balance: rs{self.balance}")
