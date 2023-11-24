class Savings_Account:
    def __init__(self, acc_num, owner_national_id):
        self.acc_num = acc_num
        self.owner_national_id = owner_national_id
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            return True
        else:
            return False

    def can_withdraw(self, amount):
        return self.balance >= amount

    def __str__(self):
        return f"Savings Account: {self.acc_num} with balance: {self.balance}"

class Customer:
    def __init__(self, name, national_id):
        self.name = name
        self.national_id = national_id
        self.savings_accounts = []
    
    def deposit(self, amount, account):
        account.deposit(amount)

    def withdraw(self, amount, account):
        return account.withdraw(amount)

    def has_account(self, account):
        return account in self.savings_accounts

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.savings_accounts = []

    def calc_deposit_base(self):
        total = 0.0
        for acc in self.savings_accounts:
            total += acc.balance
        return total

    def find_largest_balance_acccount(self):
        if len(self.savings_accounts) == 0:
            return None
        else:
            largest_balance_acccount = self.savings_accounts[0]
            for acc in self.savings_accounts:
                if acc.balance > largest_balance_acccount.balance:
                    largest_balance_acccount = acc
            return largest_balance_acccount

    def find_negative_balanced_accounts(self):        
        negative_balanced_accounts = []
        for acc in self.savings_accounts:
            if acc.balance < 0.0:
                negative_balanced_accounts.append(acc)
        return negative_balanced_accounts

    def open_account(self, account, customer):
        if customer not in self.customers: 
            self.customers.append(customer)
        self.savings_accounts.append(account)
        customer.savings_accounts.append(account)

    def close_account(self, account, customer):
        if customer.has_account(account):
            customer.savings_accounts.remove(account)
            self.savings_accounts.remove(account)
            return True
        else:
            return False            # customer does not owns this account
    
    def __str__(self):
        return f"{self.name}, total funds: {self.calc_deposit_base()}, customers: {len(self.customers)}, savings accounts: {len(self.savings_accounts)}"
    
# test code
bank = Bank("West Bank")

customer_one = Customer("John Smith", "12345V")
customer_two = Customer("Bruce Wayne", "54321V")
account_one = Savings_Account(12345, customer_one.national_id)
account_two = Savings_Account(45678, customer_two.national_id)
bank.open_account(account_one, customer_one)
bank.open_account(account_two, customer_two)

customer_one.deposit(1000, account_one)
customer_two.deposit(2000, account_two)
result = customer_one.withdraw(500, account_one)
print(f"Withdraw success:{result}")
print(bank)

print(bank.find_largest_balance_acccount())
negative_accs = bank.find_negative_balanced_accounts()
print(f"Negative balanced accounts")
for acc in negative_accs:
    print(acc)