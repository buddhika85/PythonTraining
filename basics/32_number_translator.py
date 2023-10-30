# numberText dictionary
numberTexts = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
};

# read the number
phoneNum = input('Phone: ')

phoneStr = ''

# iterate and find word from it from numberText dictionary
for item in phoneNum:
    phoneStr += f'{numberTexts[item]} '

# display
print(f'{phoneNum} => {phoneStr}')