price_of_house = 1000000
is_good_credit = True
if is_good_credit:
    down_payment = (price_of_house / 100) * 10
else:
    down_payment = (price_of_house / 100) * 20
print(f'Down payment: ${down_payment}')