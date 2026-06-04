import random
easy_words = [
    "cat", "dog", "sun", "hat", "pen", "cup", "book", "tree",
    "fish", "milk", "ring", "ball", "star", "moon", "duck"
]
medium_words = [
    "apple", "chair", "table", "bread", "water", "light",
    "plant", "train", "clock", "brush", "smile", "house",
    "river", "stone", "paper"
]
hard_words = [
    "python", "jumble", "oxygen", "wizard", "galaxy",
    "puzzle", "rhythm", "crypt", "knight", "xylophone",
    "zombie", "awkward", "blizzard", "jigsaw"
]


all_words = easy_words + medium_words + hard_words

chosen_word = random.choice(all_words)
hangman_logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                      
                   |___/                       

        H A N G M A N
"""

hangman_stages = [
"""
   +--------+
   |        |
            |
            |
            |
            |
===============
""",
"""
   +--------+
   |        |
   O        |
            |
            |
            |
===============
""",
"""
   +--------+
   |        |
   O        |
   |        |
            |
            |
===============
""",
"""
   +--------+
   |        |
   O        |
  /|        |
            |
            |
===============
""",
"""
   +--------+
   |        |
   O        |
  /|\       |
            |
            |
===============
""",
"""
   +--------+
   |        |
   O        |
  /|\       |
  /         |
            |
===============
""",
"""
   +--------+
   |        |
   X        |
  /|\       |
  / \       |
  RIP       |
===============
"""
]

print(hangman_logo)
# print(chosen_word)

placeholder =""
for i in range(0, len(chosen_word)):
    placeholder += "_"
print("Word to Guess: "+ placeholder + " and have " + str(len(chosen_word)) + " letters.")

lives = 0
allguess = []
correct_letters = []
display = placeholder
while lives<7:
    print(f"********************************{7-lives}/7 lives left*****************************")
    guess = input("Guess a letter: ").lower()
    # display = ""
    if guess in correct_letters:
        print(f"You'hv already guessed {guess}.")
        print(display)
        continue
    if guess not in chosen_word:
        print("Incorrect!!!")
        if guess in allguess:
            print(f"You have already guessed {guess}, which is incorrect.")
            print(display)
            continue
        allguess.append(guess)
        print(f"You guessed {guess}, that's  not in the word.")
        print(display)
        print(hangman_stages[lives])
        lives += 1
        if lives == 7:
            print(f"YOU LOSE, the word was {chosen_word}")
        continue
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display+= letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+= letter
        else:
            display+="_"
    print(display)
    if "_" not in display:
        print("YOU WIN")
        break