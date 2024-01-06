class BankAccount:
    def __init__(self, cusomter_name, balance, annual_interest_rate):
        self.customer_name = cusomter_name
        self.balance = balance
        self.annual_interest_rate = annual_interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Not enough credit")
        else:
            print("Invalid Amount")

    def monthly_interest(self):
        self.balance += self.balance * self.annual_interest_rate / 12

    def __str__(self):
        return f"{self.customer_name} - {self.balance} - {self.annual_interest_rate}";

bank_account = BankAccount("Jack", 100, 12)
print(bank_account)
bank_account.withdraw(101)
bank_account.withdraw(50)
print(bank_account)
bank_account.deposit(50)
bank_account.monthly_interest()
print(bank_account)