from collections import Counter
ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""
freq = Counter(ciphertext)
print("Character frequencies:")
for char, count in freq.most_common():
    if char.isalnum() or not char.isspace():
        print(f"{char} : {count}")
mapping = {
    '8': 'E', '†': 'T', '‡': 'H', '(': 'I', ')': 'N', ';': 'S', 
    '*': 'A', '5': 'A', '6': 'R', '4': 'O', '3': 'G', 
    '0': 'D', '9': 'Y', '1': 'B', '2': 'C', '¶': 'L',
    ']': 'F', ':': 'U', '?': 'M', '—': 'W'
}
plaintext = ""
for ch in ciphertext:
    plaintext += mapping.get(ch, ch)

print("\nDecrypted text:")
print(plaintext)
