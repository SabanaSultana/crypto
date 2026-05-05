# *** Write a Python code to implement Transposition Cipher ***

def encrypt(message, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key
    return ''.join(cipher)

def decrypt(cipher, key):
    num_cols = len(cipher) // key + (len(cipher) % key != 0)
    num_rows = key
    num_shaded = num_cols * num_rows - len(cipher)

    plain = [''] * num_cols
    col = row = 0

    for symbol in cipher:
        plain[col] += symbol
        col += 1
        if col == num_cols or (col == num_cols - 1 and row >= num_rows - num_shaded):
            col = 0
            row += 1

    return ''.join(plain)

msg = "HELLO WORLD"
key = 4

enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Original Text:", msg)
print("Key:", key)
print("Encrypted Text:", enc)
print("Decrypted Text:", dec)