alphabet = [chr(i) for i in range(97, 123)]
caesar_logo = r"""
   ____                                  ____ _               
  / ___| __ _ _ __ ___   ___  ___  ___  / ___| |__   ___  ___ 
 | |    / _` | '_ ` _ \ / _ \/ __|/ _ \| |   | '_ \ / _ \/ __|
 | |___| (_| | | | | | |  __/\__ \  __/| |___| | | |  __/\__ \\
  \____|\__,_|_| |_| |_|\___||___/\___| \____|_| |_|\___||___/
                                                              
              C A E S A R   C I P H E R
"""
print(caesar_logo)
def ceaser(original_text, shift_amount, encode_or_decode):
    output_text= ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            output_text+= char
            continue
        shifted_position = (alphabet.index(char) + shift_amount)%len(alphabet)
        output_text+= alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    ceaser(text, shift, direction)
    again = input("Type 'yes' if you want to go again.\nOtherwise, type 'no': ").lower()
    if again == "no":
        should_continue = False
        print("Good Bye")