def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_seq = ""
    for char in keyword:
        if char not in cipher_seq:
            cipher_seq += char
    for char in alphabet:
        if char not in cipher_seq:
            cipher_seq += char
    return cipher_seq
def monoalphabetic_encrypt(plaintext, cipher_alphabet):
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in plaintext:
        if char.isalpha():
            index = alphabet.index(char)
            result += cipher_alphabet[index]
        else:
            result += char
    return result
def monoalphabetic_decrypt(ciphertext, cipher_alphabet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in ciphertext:
        if char.isalpha():
            index = cipher_alphabet.index(char)
            result += alphabet[index]
        else:
            result += char
    return result


keyword = "CIPHER"
cipher_alphabet = generate_cipher_alphabet(keyword)
print("Generated Cipher Alphabet:")
print(cipher_alphabet)

plaintext = "HELLO WORLD"
ciphertext = monoalphabetic_encrypt(plaintext, cipher_alphabet)
print("\nEncrypted Text:", ciphertext)

decrypted = monoalphabetic_decrypt(ciphertext, cipher_alphabet)
print("Decrypted Text:", decrypted)
