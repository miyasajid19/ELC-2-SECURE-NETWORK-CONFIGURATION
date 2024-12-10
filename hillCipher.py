import numpy as np

def generate_key_matrix(key, n):
    """
    Generates a key matrix of size n x n from the given key text.
    """
    key = ''.join(filter(str.isalpha, key.upper()))  # Ensure only alphabet characters
    while len(key) < n * n:
        key += 'A'  # Pad with 'A' if key is too short
    key_vector = [ord(char) - 65 for char in key[:n * n]]  # Convert to numbers
    key_matrix = np.array(key_vector).reshape(n, n)
    return key_matrix

def hill_encrypt(text, key_matrix):
    """
    Encrypts the text using the Hill cipher.
    """
    text = ''.join(filter(str.isalpha, text.upper()))  # Ensure only alphabet characters
    n = len(key_matrix)
    while len(text) % n != 0:
        text += 'A'  # Pad with 'A' if text length is not a multiple of n
    text_vector = [ord(char) - 65 for char in text]
    text_matrix = np.array(text_vector).reshape(-1, n).T
    cipher_matrix = np.dot(key_matrix, text_matrix) % 26
    return ''.join(chr(num + 65) for num in cipher_matrix.T.flatten())

def hill_decrypt(ciphertext, key_matrix):
    """
    Decrypts the ciphertext using the Hill cipher.
    """
    det = round(np.linalg.det(key_matrix))
    if det == 0 or np.gcd(det, 26) != 1:
        raise ValueError("The key matrix is not invertible under mod 26. Please use a different key.")
    inv_det = pow(int(det), -1, 26)  # Modular multiplicative inverse of the determinant
    adj_matrix = np.round(np.linalg.inv(key_matrix) * det).astype(int) % 26
    inv_key_matrix = (inv_det * adj_matrix) % 26
    ciphertext_vector = [ord(char) - 65 for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, key_matrix.shape[0]).T
    plain_matrix = np.dot(inv_key_matrix, ciphertext_matrix).round().astype(int) % 26
    return ''.join(chr(num + 65) for num in plain_matrix.T.flatten())

# Main Function
if __name__ == "__main__":
    try:
        # Input from the user
        text = input("Enter the text to encrypt: ").strip()
        key = input("Enter the key for the cipher (alphabetic characters only): ").strip()
        n = int(input("Enter the size of the key matrix (e.g., 2 for 2x2, 3 for 3x3): "))

        # Generate key matrix
        hill_key_matrix = generate_key_matrix(key, n)
        print(f"Generated Key Matrix:\n{hill_key_matrix}")

        # Encrypt and Decrypt with Hill Cipher
        hill_encrypted = hill_encrypt(text, hill_key_matrix)
        hill_decrypted = hill_decrypt(hill_encrypted, hill_key_matrix)

        print(f"Encrypted Text: {hill_encrypted}")
        print(f"Decrypted Text: {hill_decrypted}")
        print(f"Hill Cipher Match: {text.upper() == hill_decrypted}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    """
    ACT
    GYBNQKURP
    POH
    """