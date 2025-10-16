def generate_key(plaintext, key):
    key = key.upper()
    key_extended = ""
    i = 0
    for char in plaintext:
        if char.isalpha():
            key_extended += key[i % len(key)]
            i += 1
        else:
            key_extended += char
    return key_extended


def encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)

    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = (ord(k) - ord('A'))  # Shift based on key letter
            ciphertext += chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += p
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)

    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = (ord(k) - ord('A'))
            plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += c
    return plaintext


# --- MAIN PROGRAM ---
plaintext = input("Enter the plaintext message: ")
key = input("Enter the keyword: ")

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("\nGenerated Key: ", generate_key(plaintext, key))
print("Encrypted Message:", ciphertext)
print("Decrypted Message:", decrypted)
