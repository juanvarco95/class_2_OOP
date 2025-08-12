class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Cannot overdraft a savings account")
        else:
            super().withdraw(amount)

acc = SavingsAccount("Juan", 1000, 0.03)
acc.withdraw(1200)  # Cannot overdraft...
