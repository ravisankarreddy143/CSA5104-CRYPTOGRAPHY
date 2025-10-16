def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetic characters stay same
    return result


# Input from user
text = input("Enter the message: ")

print("\nEncrypted messages for all key values (k = 1 to 25):\n")
for k in range(1, 26):
    encrypted = caesar_cipher(text, k)
    print(f"k = {k:2d} → {encrypted}")
