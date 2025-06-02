Write a Python program that uses private attributes for creating a BankAccount class. Implement
methods to deposit, withdraw, and display the balance, ensuring direct access to the balance attribute is
restricted. Explain why using private attributes can help improve data security and prevent accidental
modifications.

Ans:
    class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def display_balance(self):
        print("Balance:", self.__balance)
