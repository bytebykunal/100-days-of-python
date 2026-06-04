def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
# print(''' 
#  _____________________
# |  _________________  |
# | | JO           0. | |
# | |_________________| |
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | x | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|
# ''')
d = ""
while True:
    if d == "y":
        a = result
    else:
        print('\n'*20)
        print(''' 
             _____________________
            |  _________________  |
            | | JO           0. | |
            | |_________________| |
            |  ___ ___ ___   ___  |
            | | 7 | 8 | 9 | | + | |
            | |___|___|___| |___| |
            | | 4 | 5 | 6 | | - | |
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | |
            | |___|___|___| |___| |
            | | . | 0 | = | | / | |
            | |___|___|___| |___| |
            |_____________________|
            ''')
        a = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    b = float(input("What's the next number?: "))
    result = operations[operation](a, b)
    print(f"{a} {operation} {b} = {result}")
    d = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation: ")