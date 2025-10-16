import string

# Function to generate the 5x5 key matrix
def generate_key_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    matrix = []
    used = set()

    # Add keyword letters to matrix
    for char in keyword:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    # Add remaining letters A–Z (excluding J)
    for char in string.ascii_uppercase:
        if char != "J" and char not in used:
            used.add(char)
            matrix.append(char)

    # Create 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]


# Function to locate letter positions in matrix
def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == letter:
                return i, j
    return None


# Function to prepare plaintext (split into digraphs)
def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join([c for c in plaintext if c.isalpha()])

    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs


# Encrypt digraphs using Playfair rules
def encrypt(pairs, matrix):
    ciphertext = ""
    for pair in pairs:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle case
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext


# MAIN PROGRAM
keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext message: ")

matrix = generate_key_matrix(keyword)
print("\nPlayfair Key Matrix (5x5):")
for row in matrix:
    print(" ".join(row))

pairs = prepare_text(plaintext)
ciphertext = encrypt(pairs, matrix)

print("\nPrepared Digraphs:", pairs)
print("Encrypted Ciphertext:", ciphertext)
