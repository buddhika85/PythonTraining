has_high_income = True;
has_good_credit = True;
has_criminal_record = True;

if has_high_income and not has_criminal_record:          # or and not
    print("Eligible for loan")
elif has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
     print("Not Eligible for loan")