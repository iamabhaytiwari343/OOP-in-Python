# Encapsulation is the concept of hiding the internal implementation details of a class and providing a public interface for interacting with the object. In Python, this is achieved through private (name mangling) and protected attributes. For example, you can use a single underscore _ to indicate a protected attribute and double underscores __ to indicate a private attribute.
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Creating a bank account
account = BankAccount("12345", 1000)

# Accessing attributes via methods
print("Account Number:", account.get_account_number())
print("Initial Balance:", account.get_balance())

# Depositing and withdrawing funds
account.deposit(500)
account.withdraw(200)

# Getting the updated balance
print("Updated Balance:", account.get_balance())

# Private: Private members are only accessible within the class. They are not directly accessible from outside the class.

# Protected: Protected members are accessible within the class and its subclasses (inheritance). They are not accessible from outside the class hierarchy.

# Public: Public members are accessible from anywhere, including outside the class.