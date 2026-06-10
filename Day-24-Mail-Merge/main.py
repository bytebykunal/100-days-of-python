#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

# print(letter)

#for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

for name in name_list:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(f"./Output\\ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
# print(letter)
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

