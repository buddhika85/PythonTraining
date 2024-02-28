first_name = 'Elon'
last_name = 'Musk'
date = '12 April 2023'
starting_balance  = 1000
transaction_0 = 100.0
transaction_0_description = "Small deposit"
transaction_1 = -75.0
transaction_1_description = "Small withdraw"

print(" --------------------------------- ")
print("|        COMMONWEALTH BANK        |")
print(" --------------------------------- \n")
print(f"Date: {date}\n")
print(f"Welcome back, {first_name} {last_name}!")
print(f"Starting balance: {starting_balance}")
print(f"{transaction_0_description} : {transaction_0}")
print(f"{transaction_1_description} : {transaction_1}")
print(f"Ending balance: {starting_balance + transaction_0 + transaction_1}")