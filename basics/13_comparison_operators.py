temperature = 19

if temperature >= 30:
    print("Hot day")
elif temperature <= 10:
    print("Cold day")
else:
    print("Neiter hot or cold")

if temperature == 19:
    print("It is 19")

if temperature != 20:
    print("It is not 20")

# another one
name = 'James'

if len(name) < 3:
    print("name must be atleast 3 characters")
elif len(name) > 50:
    print("name must be less than 50 characters")
else:
    print("name looks good")