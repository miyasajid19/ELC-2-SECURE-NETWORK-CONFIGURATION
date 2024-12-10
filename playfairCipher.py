import numpy as np
def to_lower_case(text):
    return text.lower()
def remove_spaces(text):
    return text.replace(" ", "")
def generate_key_table(key):
    key = remove_spaces(to_lower_case(key))
    key = key.replace('j', 'i')  # Treat 'j' as 'i'
    key = ''.join(dict.fromkeys(key))  # Remove duplicate letters
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # 'j' is excluded
    key_table = [c for c in key if c in alphabet]
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
    key_table = np.array(key_table).reshape(5, 5)
    return key_table
def search(key_table, a, b):
    if a == 'j': a = 'i'
    if b == 'j': b = 'i'
    p1 = p2 = None
    for i in range(5):
        for j in range(5):
            if key_table[i, j] == a:
                p1 = (i, j)
            elif key_table[i, j] == b:
                p2 = (i, j)
    return p1, p2
def encrypt(plain_text, key):
    plain_text = remove_spaces(to_lower_case(plain_text))
    plain_text = plain_text.replace('j', 'i')
    i = 0
    while i < len(plain_text) - 1:
        if plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + 'x' + plain_text[i + 1:]
        i += 2
    if len(plain_text) % 2 != 0:
        plain_text += 'z'
    key_table = generate_key_table(key)
    cipher_text = []
    for i in range(0, len(plain_text), 2):
        p1, p2 = search(key_table, plain_text[i], plain_text[i + 1])
        if p1[0] == p2[0]:
            cipher_text.append(key_table[p1[0], (p1[1] + 1) % 5])
            cipher_text.append(key_table[p2[0], (p2[1] + 1) % 5])
        elif p1[1] == p2[1]:
            cipher_text.append(key_table[(p1[0] + 1) % 5, p1[1]])
            cipher_text.append(key_table[(p2[0] + 1) % 5, p2[1]])
        else:
            cipher_text.append(key_table[p1[0], p2[1]])
            cipher_text.append(key_table[p2[0], p1[1]])
    return ''.join(cipher_text)
def decrypt(cipher_text, key):
    key_table = generate_key_table(key)
    deciphered = []
    for i in range(0, len(cipher_text), 2):
        p1, p2 = search(key_table, cipher_text[i], cipher_text[i + 1])
        if p1[0] == p2[0]:
            deciphered.append(key_table[p1[0], (p1[1] - 1) % 5])
            deciphered.append(key_table[p2[0], (p2[1] - 1) % 5])
        elif p1[1] == p2[1]:
            deciphered.append(key_table[(p1[0] - 1) % 5, p1[1]])
            deciphered.append(key_table[(p2[0] - 1) % 5, p2[1]])
        else:
            deciphered.append(key_table[p1[0], p2[1]])
            deciphered.append(key_table[p2[0], p1[1]])
    return ''.join(deciphered)


# Main Function
if __name__ == "__main__":
    try:
        text="ONCEAXAVERIANALWAYSAXAVERIAN"
        playfair_key = "SECTION I"
        # Encrypt and Decrypt with Playfair Cipher
        playfair_encrypted= encrypt( text, playfair_key)
        playfair_decrypted= decrypt( playfair_encrypted, playfair_key)

        # Verification (Match Texts)
        print("Verification Results:")
        print("Original Text  :: ",text)
        print("Playfair Key   :: ",playfair_key)
        print("Encrypted Text :: ",playfair_encrypted)
        print("Decrypted Text :: ",playfair_decrypted)
        print(f"Playfair Cipher Match: {text.replace(' ', '').lower() == playfair_decrypted}")

    except FileNotFoundError:
        print("The file 'Text_To_Be_Encrypted.txt' was not found. Please ensure it exists in the script's directory.")
