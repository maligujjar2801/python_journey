class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance      


    def deposit(self, amount):
        self.balance += amount
        deposit_message = f"Deposited: ${amount:.2f}"
        return deposit_message

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds"

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
account_1 = Account("John Doe", 1000)
print(account_1.deposit(500))
account_1.withdraw(200) 
account_1.display_balance()