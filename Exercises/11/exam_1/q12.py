class App:
	def __init__(self, name, minimum_age):
		self.name = name
		self.minimum_age = minimum_age
	
class SubscriptionApp(App):
	def __init__(self, name, minimum_age, monthly_price):
		super().__init__(name, minimum_age)
		self.monthly_price = monthly_price
	
	def annual_cost(self):
		return self.monthly_price * 12
		
	def weekly_cost(self):
		return self.monthly_price / 4