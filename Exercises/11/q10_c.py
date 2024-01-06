class BankAccount:
	def __init__(self, customer_name , balance, annual_interest_rate):
		self.customer_name = customer_name
		self.balance = balance
		self.annual_interest_rate = annual_interest_rate
	
	def deposit(self, amount):
		if amount > 0:	
			self.balance  += amount
		else:
			print("Invalid deposit")

	def withdraw(self, amount):
		if amount > 0:	
			if self.balance  >= amount:
				self.balance -= amount
			else:
				print("not enough credit")
		else:
			print("Invalid amount")

	def monthly_interest(self):
		self.balance += self.balance * (self.annual_interest_rate / 12)


# test code
bankAccount = BankAccount("John", 100, 12)
print(bankAccount.balance)		# 100
bankAccount.monthly_interest()		
print(bankAccount.balance)		# 200
bankAccount.deposit(20)	
print(bankAccount.balance)		# 220
bankAccount.withdraw(21)
print(bankAccount.balance)		# 199
bankAccount.withdraw(-1)		# Invalid deposit
bankAccount.withdraw(200)		# not enough credit