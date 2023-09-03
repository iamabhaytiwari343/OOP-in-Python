# Initialization of Object Attributes
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize the 'name' attribute
        self.age = age    # Initialize the 'age' attribute
# Initialization Logic
class BankAccount:
    def __init__(self, account_number, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.account_number = account_number
        self.balance = balance
p1=Person("Ajay",30)
p2=Person("sarthak",25)

b1=BankAccount("2a56",2500)

