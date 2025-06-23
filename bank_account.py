# This code defines a simple BankAccount class with methods to deposit, withdraw, and showcase account details.# Bank Account Class
# This program defines a simple BankAccount class with methods to deposit, withdraw, and showcase account details.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ ₹{amount} deposited. New balance is ₹{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn. New balance is ₹{self.balance}")
        else:
            print("❌ Insufficient funds")

    def showcase(self):
        print(f"💳 Account Holder: {self.name}")
        print(f"💰 Current Balance: ₹{self.balance}")

# Sample usage
acc = BankAccount("Nisarg", 1000)
acc.deposit(200)
acc.withdraw(100)
acc.showcase()
