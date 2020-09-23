"""******************** 

Caesar Cipher Program

********************""" 
#ASCII encoder
def ascii_code(message):
    print("Decryption with ASCII-output")
    for letter in message:
        print(ord(letter), end = " ")

    print("\n")

    ascii_code(enter)

#ceasar encoder
def caesar(message): 

    print("Caesar Cipher:") 

    letter_shift = 1 

    for letter in message: 

        if letter.isupper(): 

            print(chr((ord(letter)+ letter_shift - 65) % 26 + 65), end = " ") 

        else: 

            print(chr((ord(letter)+ letter_shift - 97) % 26 + 97), end = " ") 

        letter_shift = letter_shift + 1 

    print("\n") 

enter = input("Please enter the your message here: ") 

caesar(enter) 
