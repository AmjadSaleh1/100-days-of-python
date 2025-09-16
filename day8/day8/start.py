from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def run():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text=text, shift=shift, direction=direction)
def caesar(text , shift , direction):
        end_text = ""
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(f"The encoded text is {end_text}")

flag = True
while flag:
    run()
    answer = input("Type yes if you want to go again , otherwise type no\n")
    if answer == "no":
        flag = False
        print("goodbye!")