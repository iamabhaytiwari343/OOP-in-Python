class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} - Holder: {self.account_holder}, Balance: ${self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Interest applied. New balance: ${self.balance}")


# Creating a regular account
account1 = Account("123456", "Alice", 1000)
print(account1)
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())

# Creating a savings account
savings_account = SavingsAccount("789012", "Bob", 2000, 2)
print(savings_account)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account.get_balance())
