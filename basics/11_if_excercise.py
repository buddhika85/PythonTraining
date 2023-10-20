price_of_house = 1000000
is_good_credit = False
if is_good_credit:
    price_of_house = (price_of_house / 100) * 90
else:
    price_of_house = (price_of_house / 100) * 80
print(price_of_house)