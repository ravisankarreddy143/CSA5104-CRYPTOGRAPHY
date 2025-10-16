import string
import random

# Generate random cipher alphabet (unique substitution for each letter)
def generate_cipher_alphabet():
    letters = list(string.ascii_uppercase)
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

# Encrypt plaintext using substitution cipher
def encrypt(plaintext, cipher_alphabet):
    ciphertext = ""
    for char in plaintext.upper():
        if char in cipher_alphabet:
            ciphertext += cipher_alphabet[char]
        else:
            ciphertext += char  # Non-alphabet characters remain same
    return ciphertext

# Decrypt ciphertext using substitution cipher
def decrypt(ciphertext, cipher_alphabet):
    reverse_alphabet = {v: k for k, v in cipher_alphabet.items()}
    plaintext = ""
    for char in ciphertext.upper():
        if char in reverse_alphabet:
            plaintext += reverse_alphabet[char]
        else:
            plaintext += char
    return plaintext


# --- MAIN PROGRAM ---
plaintext = input("Enter the plaintext message: ")

# Generate cipher alphabet (key)
cipher_key = generate_cipher_alphabet()

print("\nCipher Alphabet Mapping:")
for k, v in cipher_key.items():
    print(f"{k} → {v}")

# Encryption
ciphertext = encrypt(plaintext, cipher_key)
print("\nEncrypted Message:", ciphertext)

# Decryption
decrypted_text = decrypt(ciphertext, cipher_key)
print("Decrypted Message:", decrypted_text)
