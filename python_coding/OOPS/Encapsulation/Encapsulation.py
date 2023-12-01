class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  # Encapsulation: Attribute is private with a single leading underscore
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance

    def get_account_holder(self):
        return self._account_holder

# Create an instance of the BankAccount class
account = BankAccount("John Doe", 1000)

# Accessing attributes directly (not recommended, violates encapsulation)
# print(account._account_holder)  # Avoid doing this, it's not encapsulated

# Accessing attributes through methods (encapsulated)
print(f"Account holder: {account.get_account_holder()}")
print(f"Initial balance: ${account.get_balance()}")

# Perform transactions using methods
account.deposit(500)
account.withdraw(200)

# Accessing attributes through methods (encapsulated)
print(f"Current balance: ${account.get_balance()}")
