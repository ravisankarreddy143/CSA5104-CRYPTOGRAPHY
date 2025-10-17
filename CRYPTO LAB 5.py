import math
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            c = (a * p + b) % 26
            result += chr(c + base)
        else:
            result += char
    return result
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  
def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Decryption not possible — 'a' and 26 are not coprime."
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            c = ord(char) - base
            p = (a_inv * (c - b)) % 26
            result += chr(p + base)
        else:
            result += char
    return result
text = "HELLO"
a = 5
b = 8

cipher = affine_encrypt(text, a, b)
print("Encrypted:", cipher)

plain = affine_decrypt(cipher, a, b)
print("Decrypted:", plain)
