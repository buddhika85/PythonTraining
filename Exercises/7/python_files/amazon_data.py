# this looks like a list of dictionaries
# list - because you have [...]
# list contains dictionaries with key: value pairs
amazon_data = [
    {"id": 100, "is_prime": False, "monthly_spend": 800.0},
    {"id": 101, "is_prime": True, "monthly_spend": 1500.0},
    {"id": 102, "is_prime": False, "monthly_spend": 1000.0},
    {"id": 103, "is_prime": True, "monthly_spend": 2350.0},
    {"id": 104, "is_prime": False, "monthly_spend": 1100.0},
    {"id": 105, "is_prime": True, "monthly_spend": 900.0},
    {"id": 106, "is_prime": False, "monthly_spend": 2300.0},
    {"id": 107, "is_prime": True, "monthly_spend": 1050.0},
    {"id": 108, "is_prime": False, "monthly_spend": 950.0},
    {"id": 109, "is_prime": True, "monthly_spend": 1250.0},
    {"id": 110, "is_prime": False, "monthly_spend": 1150.0},
    {"id": 111, "is_prime": True, "monthly_spend": 1400.0},
    {"id": 112, "is_prime": False, "monthly_spend": 1000.0},
    {"id": 113, "is_prime": True, "monthly_spend": 1100.0},
    {"id": 114, "is_prime": False, "monthly_spend": 950.0},
    {"id": 115, "is_prime": True, "monthly_spend": 1200.0},
    {"id": 116, "is_prime": False, "monthly_spend": 4444.0},
    {"id": 117, "is_prime": True, "monthly_spend": 4300.0},
    {"id": 118, "is_prime": False, "monthly_spend": 1400.0},
    {"id": 119, "is_prime": True, "monthly_spend": 900.0}
]

prime_members = set()
non_prime_members = set()
greater_than_2000 = set()
between_1000_and_2000 = set()
less_than_1000 = set()

# populating sets
for member in amazon_data:
    if member["is_prime"]:
        prime_members.add(member["id"])
    if not member["is_prime"]:
        non_prime_members.add(member["id"])
    if member["monthly_spend"] > 2000:
        greater_than_2000.add(member["id"])
    if member["monthly_spend"] >= 1000 and member["monthly_spend"] <= 2000:
        between_1000_and_2000.add(member["id"])
    if member["monthly_spend"] < 1000:
        less_than_1000.add(member["id"])

# set operations 
print(f"There are {len(prime_members & greater_than_2000)} Prime members who spend > $2000")
print(f"There are {len(prime_members & between_1000_and_2000)} Prime members who spend between $1000 and $2000")
print(f"There are {len(prime_members & less_than_1000)} Prime members who spend less than $1000")
print(f"There are {len(non_prime_members & greater_than_2000)} non-Prime members who spend > $2000")
print(f"There are {len(non_prime_members & between_1000_and_2000)} non-Prime members who spend between $1000 and $2000")
print(f"There are {len(non_prime_members & less_than_1000)}  non-Prime members who spend less than $1000")