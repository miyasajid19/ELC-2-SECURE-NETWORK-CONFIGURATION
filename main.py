import time
import numpy as np
import matplotlib.pyplot as plt
from playfairCipher import encrypt as playfair_encrypt, decrypt as playfair_decrypt
from hillCipher import hill_encrypt, hill_decrypt,generate_key_matrix
from ceaserCipher import caesar_encrypt, caesar_decrypt

# Function to measure encryption/decryption time
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# Main Function
if __name__ == "__main__":
    try:
        # Read the text file
        with open("Text_To_Be_Encrypted.txt", "r") as file:
            text = file.read().strip()

        caesar_shift = 3
        playfair_key = "SMPK"
        hill_key="GYBNQKURP"
        hill_key_matrix = generate_key_matrix(hill_key,3)
        # Encrypt and Decrypt with Caesar Cipher
        caesar_encrypted, caesar_enc_time = measure_time(caesar_encrypt, text, caesar_shift)
        caesar_decrypted, caesar_dec_time = measure_time(caesar_decrypt, caesar_encrypted, caesar_shift)

        # Encrypt and Decrypt with Playfair Cipher
        playfair_encrypted, playfair_enc_time = measure_time(playfair_encrypt, text, playfair_key)
        playfair_decrypted, playfair_dec_time = measure_time(playfair_decrypt, playfair_encrypted, playfair_key)

        # Encrypt and Decrypt with Hill Cipher
        hill_encrypted, hill_enc_time = measure_time(hill_encrypt, text, hill_key_matrix)
        hill_decrypted, hill_dec_time = measure_time(hill_decrypt, hill_encrypted, hill_key_matrix)

        # Write the decrypted texts to files
        with open("DecryptedText/caesar_decrypted.txt", "w") as file:
            file.write(caesar_decrypted.upper())
        with open("DecryptedText/playfair_decrypted.txt", "w") as file:
            file.write(playfair_decrypted.upper())
        with open("DecryptedText/hill_decrypted.txt", "w") as file:
            file.write(hill_decrypted.upper())

        # Write the Encrypted texts to files
        with open("EncryptedText/caesar_encrypted.txt", "w") as file:
            file.write(caesar_encrypted.upper())
        with open("EncryptedText/playfair_encrypted.txt", "w") as file:
            file.write(playfair_encrypted.upper())
        with open("EncryptedText/hill_encrypted.txt", "w") as file:
            file.write(hill_encrypted.upper())

        # Verification (Match Texts)
        print("Verification Results:")
        print(f"Caesar Cipher Match: {text == caesar_decrypted}")
        print(f"Playfair Cipher Match: {text.replace(' ', '').lower() == playfair_decrypted}")
        print(f"Hill Cipher Match: {text.upper() == hill_decrypted}")

        # Plot encryption/decryption times
        algorithms = ["Caesar Cipher", "Playfair Cipher", "Hill Cipher"]
        encryption_times = [caesar_enc_time, playfair_enc_time, hill_enc_time]
        decryption_times = [caesar_dec_time, playfair_dec_time, hill_dec_time]

        x = np.arange(len(algorithms))
        plt.figure(figsize=(10, 6))

        # Plot bars for encryption/decryption times
        bars1 = plt.bar(x - 0.2, encryption_times, width=0.4, label="Encryption Time", color="skyblue")
        bars2 = plt.bar(x + 0.2, decryption_times, width=0.4, label="Decryption Time", color="salmon")

        # Add the time taken on top of each bar
        for bar in bars1:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     f"{bar.get_height():.7f}s", ha="center", va="bottom", fontsize=10)

        for bar in bars2:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     f"{bar.get_height():.7f}s", ha="center", va="bottom", fontsize=10)

        # Add labels and grid
        plt.xticks(x, algorithms)
        plt.ylabel("Time (seconds)")
        plt.title("Comparison of Encryption and Decryption Times")
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("The file 'Text_To_Be_Encrypted.txt' was not found. Please ensure it exists in the script's directory.")
