import random
# Letters (a-z and A-Z)
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Numbers (0-9)
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Symbols (common ones)
symbols = ['!','#','$','%','&', '(', ')','*','+']

print("Welcome to Password generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_symbols = int(input("How many symbols?\n"))
passw = []
for i in range(0, nr_letters):
    passw.append(random.choice(letters))
for i in range(0, nr_numbers):
    passw.append(random.choice(numbers))
for i in range(0, nr_symbols):
    passw.append(random.choice(symbols))

# print(passw)
random.shuffle(passw)
# print(passw)
password = "".join(passw)
print(password)