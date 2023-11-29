a = { 10, 20, 30, 40}
b = { 20, 40}

print(a & b) # intersection (AND)
print(a | b) # union (OR)


top_performers = {
    "HD": 10,
    "D": 13
}

remaining = {
    "C": 23,
    "P": 40,
    "F": 9
}

combined = {}

for key in top_performers.keys():
    combined[key] = top_performers[key]

for key in remaining.keys():
    combined[key] = remaining[key]

print(combined)

combined["HD"] = combined["HD"] - 3
combined["D"] = combined["D"] + 3

print(combined)