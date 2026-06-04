import random
name = ['rock', 'paper', 'scissor']
signs = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
         '''
,
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
print("Welcome let's play rock paper scisors")
cc = random.randint(0, 2)
hu = int(input("Please enter 0 for rock, 1 for paper and 2 for scissors: "))
if 0<= hu <=2:
    print(f"You chose {name[hu]}.\n{signs[hu]}")
    print(f"Computer chose {name[cc]}.\n{signs[cc]}")
    if hu == cc:
        print("It's a Tie.")
    elif hu ==0 and cc ==2:
        print("YOU WON!!")
    elif hu == 2 and cc == 0:
        print("YOU LOSE!!")
    elif cc>hu:
        print("YOU LOSE!")
    elif hu>cc:
        print("YOU WON!!!!")
else:
    print('INVALID Input!!!!!!')