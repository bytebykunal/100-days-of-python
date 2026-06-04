MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resources_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if resources[item]<drink_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def is_transaction_successful(inserted_amount, drink_cost):
    if inserted_amount > drink_cost:
        print(f"Here is ${round(inserted_amount - drink_cost,2)} in change")
        return True
    elif inserted_amount == drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def process_coins(drink_cost):
    print("Please insert coins.")

    quarter_count = int(input("How many quarters?: "))
    dime_count = int(input("How many dimes?: "))
    nickel_count = int(input("How many nickels?: "))
    penny_count = int(input("How many pennies?: "))

    inserted_amount = (
        quarter_count * 0.25
        + dime_count * 0.1
        + nickel_count * 0.05
        + penny_count * 0.01
    )
    return is_transaction_successful(inserted_amount, drink_cost)





def make_coffee(choice, drink):
    if is_resources_sufficient(drink["ingredients"]):
        if process_coins(drink["cost"]):
            for item in drink["ingredients"]:
                resources[item] -= drink["ingredients"][item]

            print(f"Here is your {choice} ☕ Enjoy!")
            return drink["cost"]
        else:
            return 0
    else:
        return 0


def report():
    print(
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${Money}"
    )

def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Machine Refilled Successfully.")

def handle_order(choice):
    if choice == "report":
        report()
        return 0
    elif choice == "refill":
        refill()
        return 0
    else:
        drink = MENU[choice]
        return make_coffee(choice, drink)


Money = 0

machine_running = True

while machine_running:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_running = False
    elif choice!= "report" and choice not in MENU and choice!= "refill":
        print("This item is not in menu.")
    else:
        Money += handle_order(choice)