class SavingsAccount:
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