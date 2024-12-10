import numpy as np
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Main Function
if __name__ == "__main__":
    try:
        text="HELLO"
        caesar_shift=3
s
        # Encrypt and Decrypt with Caesar Cipher
        caesar_encrypted =caesar_encrypt( text, caesar_shift)
        caesar_decrypted = caesar_decrypt( caesar_encrypted, caesar_shift)
        print("Original Text ::",text)
        print("Caeser Shift ::",caesar_shift)
        print("Encrypted Text ::",caesar_encrypted)
        print("Decrypted Text ::",caesar_decrypted)
        # Verification (Match Texts)
        print("Verification Results:")
        print(f"Caesar Cipher Match: {text == caesar_decrypted}")

    except FileNotFoundError:
        print("The file 'Text_To_Be_Encrypted.txt' was not found. Please ensure it exists in the script's directory.")
