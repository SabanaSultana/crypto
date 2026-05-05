# *** Write a Python code to implement Vigenere Cipher ***

def generate_key(text, key):
    key = list(key)
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    result = ""
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = 65 if text[i].isupper() else 97
            result += chr((ord(text[i]) + ord(key[i]) - 2*shift) % 26 + shift)
        else:
            result += text[i]
    return result

def decrypt(text, key):
    result = ""
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = 65 if text[i].isupper() else 97
            result += chr((ord(text[i]) - ord(key[i])) % 26 + shift)
        else:
            result += text[i]
    return result

msg = "HELLO WORLD"
key = "KEY"

enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Original Text:", msg)
print("Key:", key)
print("Encrypted Text:", enc)
print("Decrypted Text:", dec)