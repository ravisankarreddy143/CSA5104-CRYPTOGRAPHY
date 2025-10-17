def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Decryption not possible — invalid key"
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            c = ord(char) - base
            p = (a_inv * (c - b)) % 26
            result += chr(p + base)
        else:
            result += char
    return result
a = 3
b = 15
ciphertext = "BUUBBUBBUUBB"
plaintext = affine_decrypt(ciphertext, a, b)
print("a =", a, ", b =", b)
print("Decrypted text:", plaintext)
