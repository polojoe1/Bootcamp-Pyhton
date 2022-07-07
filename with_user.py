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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_balance(self):
        self.account.display_account_info()
        return self

Joseph = User("Joseph", "CoaJ@codingdojo")
Joseph.make_deposit(500)
Joseph.display_balance()
Joseph.make_withdrawal(250).make_deposit(50)