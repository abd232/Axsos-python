class User:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def make_withdrawal(self, amount):
        if(self.balance < amount):
            print("there is not enough balance to make this withdrawal")
            return self
        self.balance -= amount
        return self
        
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def display_user_balance(self):
        print(f"{self.name} current balance is {self.balance}")
        return self;

    def transfer_money(self,amount,user):
        if(self.balance < amount):
            print("there is not enough balance to make this transfer")
            return self
        self.balance -= amount
        user.balance += amount
        return self

    
user1 = User("user1")
user2 = User("user2")
user3 = User("user3")

user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200).display_user_balance()

user2.make_deposit(100).make_deposit(150).make_withdrawal(170).make_withdrawal(50).display_user_balance()


user3.make_deposit(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(200).display_user_balance()

user1.transfer_money(50,user3).display_user_balance()

user3.display_user_balance()