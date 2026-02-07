class User:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def make_withdrawal(self, amount):
        if(self.balance < amount):
            print("there is not enough balance to make this withdrawal")
            return False
        self.balance -= amount
        return True
        
    def make_deposit(self, amount):
        self.balance += amount
        return True
    
    def display_user_balance(self):
        print(f"{self.name} current balance is {self.balance}")
        return True;

    def transfer_money(self,amount,user):
        if(self.balance < amount):
            print("there is not enough balance to make this transfer")
            return False
        self.balance -= amount
        user.balance += amount
        return True

    
user1 = User("user1")
user2 = User("user2")
user3 = User("user3")

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(200)
user1.display_user_balance()

user2.make_deposit(100)
user2.make_deposit(150)
user2.make_withdrawal(170)
user2.make_withdrawal(50)
user2.display_user_balance()

user3.make_deposit(200)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(200)
user3.display_user_balance()

user1.transfer_money(50,user3)
user1.display_user_balance()
user3.display_user_balance()