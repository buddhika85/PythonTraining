try:
    amount_to_withdraw = float(input("How much do you want to withdraw? "))
    if amount_to_withdraw <= 0:
        raise ValueError("You must withdraw a positive amount!")
except ValueError as error: 
     print("An error occurred:", error)