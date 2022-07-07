class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"New balance is {self.balance}")
        return self
    def withdraw(self, amount):
        self.amount = amount
        if amount <= self.balance:
            self.balance-=amount
            print(f"New balance is {self.balance}")
            return self
        else:
            self.balance-=5
            print(f"Insufficient funds new balance is {self.balance}")
            return self
        
    def display_account_info(self):
        print(f"balance is: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance= (self.int_rate * self.balance) + self.balance
            print(f"new balance is {self.balance}")
            return self
        else :
            print("no changes")
            return self

my_account = BankAccount(0.01, 100)
your_account = BankAccount(0.01, 60)

# my_account.deposit(100).deposit(50).deposit(300).withdraw(200).yield_interest()

your_account.deposit(500).deposit(200).withdraw(20).withdraw(200).withdraw(100).withdraw(100).yield_interest().display_account_info()