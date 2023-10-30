class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount"


# Create an ATM instance with an initial balance of $1000
my_atm = ATM(1000)

print("Welcome to the ATM!")
while True:
    print("\nOptions:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        print(my_atm.check_balance())
    elif choice == "2":
        amount = float(input("Enter the deposit amount: $"))
        print(my_atm.deposit(amount))
    elif choice == "3":
        amount = float(input("Enter the withdrawal amount: $"))
        print(my_atm.withdraw(amount))
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
