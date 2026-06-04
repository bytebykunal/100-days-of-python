import random
from art import logo, vs
from game_data import data

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(userguess, a_followers, b_followers):
    if a_followers > b_followers:
        return userguess == 'A'
    else:
        return userguess == 'B'
    

print(logo)

score = 0

account_a = random.choice(data)
account_b = random.choice(data)

while account_a == account_b:
    account_b = random.choice(data)

game_should_continue = True

while game_should_continue:
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    is_correct = check_answer(guess, account_a["follower_count"],account_b["follower_count"])
    if is_correct:
        score += 1
        print('\n'*20)
        print(logo)
        print(f"You're right! current score: {score}")
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

    else :
        print(f"Sorry, that's wrong final score: {score}")
        game_should_continue = False