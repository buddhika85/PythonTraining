class Bank:
   def __init__(self,name):
      self.name=name
      self.customers=[]
      self.savings_accs=[]

   def calc_deposit_base(self):
      total =0.0
      for account in self.savings_accs:
         total+=account.balance
      return total

   def largest_balance_acc(self):
      largest_account=self.savings_accs[0]
      for account in self.savings_accs:
         if account.balance >largest_account.balance:
            largest_account=account
      return largest_account

   def get_negative_balance_accounts(self):
      negative_balance_accounts=[]
      for account in self.savings_accs:
         if account.balance < 0.0:
            negative_balance_accounts.append(account)
      return negative_balance_accounts

   def open(self, customer, saving_acc):
      if customer not in self.customers:
         self.customers.append(customer)
      self.savings_accs.append(saving_acc)
      customer.accounts.append(saving_acc)

   def close(self, customer, saving_acc):
      self.savings_accs.remove(saving_acc)
      customer.accounts.remove(saving_acc)

   def __str__(self):
      return f"Bank: {self.name}, Total funds: {self.calc_deposit_base()}, Customer count: {len(self.customers)}, Accounts count: {len(self.savings_accs)}"


class Customer:
   def __init__(self,name,nic):
      self.name=name
      self.accounts=[]
      self.nic=nic

   def withdraw(self,amount,acc):
      return acc.withdraw(amount)

   def deposit(self, amount,acc):
      return acc.deposit(amount)

   def __str__(self):
      str=f"Customer: {self.name}, NIC No: {self.nic}, Accounts:\n"
      for account in self.accounts:
         str+=f"{account}\n"
      return str

class Savings_acc:
   def __init__(self,acc_no,nic):
      self.acc_no=acc_no
      self.nic=nic
      self.balance=0.0

   def withdraw(self,amount):
      #if self.balance>=amount:
      self.balance-=amount
      return True
      #else:
         #return False #not enough credit

   def deposit(self, amount):
      self.balance+=amount

   def __str__(self):
      return f"Savongs account: {self.acc_no}, owner: {self.nic}, balance: {self.balance}"

#Test
bank=Bank("HNB")
customer=Customer("123V", "Tom Grey")
customer_two=Customer("567V", "Tylor Smith")
savings_acc=Savings_acc("12345", "123V")
savings_acc_two=Savings_acc("34567", "567V")

bank.open(customer,savings_acc)
#bank.open(customer_two,savings_acc)    # here is the issue - should be savings_acc_two
bank.open(customer_two,savings_acc_two)

customer.deposit(1000,savings_acc)
customer.withdraw(900,savings_acc)
# print(savings_acc)

customer_two.deposit(1000,savings_acc_two)
customer_two.withdraw(2100,savings_acc_two)
# print(savings_acc_two)
print(bank)

print("Negative Accounts")
negatives= bank.get_negative_balance_accounts()
if len(negatives) == 0:
   print("\tNo negative accounts")
else:
   for acc in negatives:
      print(f"\t{acc}")