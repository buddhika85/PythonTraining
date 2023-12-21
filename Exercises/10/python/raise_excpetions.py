try:
    amount = float(input("Enter amoount to withdraw: "))
    if amount <= 0:
        raise ValueError("Amount to withdraw should be postive number greater than 0")
except ValueError as e:
    print(f"Value Error - {e}")
