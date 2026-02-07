class BankAccount:
    def __init__(self, int_rate = 1, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def make_withdrawal(self, amount):
        if(self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        self.balance -= amount
        return self
        
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def display_account_balance(self):
        print(f"balance: {self.balance}")
        return self

    def get_account_balance(self):
        return self.balance

    def yield_interest(self):
        if(self.balance >= 0):
            self.balance += (self.int_rate * self.balance) / 100
        return self


    
class User:
    def __init__(self, int_rate = 1, balance = 0):
        self.bankAccount = []
        self.bankAccount.append(BankAccount(int_rate, balance))
    
    def create_new_account(int_rate = 1, balance = 0):
        self.bankAccount.append(BankAccount(int_rate, balance))

    def make_withdrawal(self, amount, acountIndex = 0):
        self.bankAccount[acountIndex].make_withdrawal(amount)
        return self
        
    def make_deposit(self, amount, acountIndex = 0):
        self.bankAccount[acountIndex].make_deposit(amount)
        return self
    
    def display_user_balance(self):
        total_user_balance = 0
        for account in self.BankAccount:
            total_user_balance += account.get_account_balance()
        
        print(f"total balance: {total_user_balance}")
        return self;

    
    def display_user_balance(self, acountIndex):
        self.bankAccount[acountIndex].display_account_balance()
        return self;
