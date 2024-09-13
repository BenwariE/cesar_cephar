def input():
    shift = 0
    print("welcome")
    text = str(input("enter a value: "))
    if int:  
        shift = input('enter your value') 
    elif str: 
        
        shift+= char(input("enter your shift here: ")) 
    else:
        shift = int(input('enert your shift: '))
    return caesar_cipher(text,shift)

def caesar_cipher(text, shift):
    # Encrypt or decrypt the text using Caesar cipher
    result = ""

    # Traverse through each character in the text
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Get the base ASCII value (65 for uppercase, 97 for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            
            # Perform the shift using modular arithmetic
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # If it's not a letter (e.g., a space or punctuation), keep it as is
            result += char

    return print_result(result)

def input_encrypted_text():
    text = str(input('eter your text: '))
    shift = input('enter your shift: ')
def decrypt_caesar_cipher(text, shift):
    # Decrypt the text using Caesar cipher
    result = ""

    # Traverse through each character in the text
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Get the base ASCII value (65 for uppercase, 97 for lowercase)
            base = ord('A') if char.isupper() else ord('a')

            # Perform the reverse shift using modular arithmetic
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            # If it's not a letter (e.g., a space or punctuation), keep it as is
            result += char

    return print_result(result)

def print_result(result):
    print(result)

