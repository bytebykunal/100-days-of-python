import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, lives):
    if user_guess == actual_answer:
        print(f"You got it! The answer was {user_guess}.")
    elif user_guess>actual_answer:
        print("Too high.")
        print("Guess again.")
        return lives - 1
    else:
        print("Too low")
        print("Guess again.")
        return lives -1

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

    

# print(num)
logo = r'''                                                                                                        
 ▄▄▄▄▄▄▄                            ▄▄▄▄▄▄▄▄▄ ▄▄            ▄▄▄    ▄▄▄                ▄▄                
███▀▀▀▀▀                            ▀▀▀███▀▀▀ ██            ████▄  ███                ██                
███       ██ ██ ▄█▀█▄ ▄█▀▀▀ ▄█▀▀▀      ███    ████▄ ▄█▀█▄   ███▀██▄███ ██ ██ ███▄███▄ ████▄ ▄█▀█▄ ████▄ 
███  ███▀ ██ ██ ██▄█▀ ▀███▄ ▀███▄      ███    ██ ██ ██▄█▀   ███  ▀████ ██ ██ ██ ██ ██ ██ ██ ██▄█▀ ██ ▀▀ 
▀██████▀  ▀██▀█ ▀█▄▄▄ ▄▄▄█▀ ▄▄▄█▀      ███    ██ ██ ▀█▄▄▄   ███    ███ ▀██▀█ ██ ██ ██ ████▀ ▀█▄▄▄ ██    
                                                                                                        
                                                                                                        '''

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    lives = set_difficulty()
    guess = 0
    while lives!= 0 and guess!= num:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess ,num, lives)

    if lives == 0:
        print(f"You've run out of guesses. The number was {num}.")

game()