# *** Write a Python code to implement DES (simplified) ***

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

text = b'HELLO123'
key = b'8bytekey'

cipher = DES.new(key, DES.MODE_ECB)

enc = cipher.encrypt(pad(text, 8))
dec = unpad(cipher.decrypt(enc), 8)

print("Original Text:", text)
print("Key:", key)
print("Encrypted Text:", enc)
print("Decrypted Text:", dec)



# 5.  Write a Python code to implement DES 
# # pip install pycryptodome
# from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad, unpad

# text = b'HELLO123'
# key = b'8bytekey'

# cipher = DES.new(key, DES.MODE_ECB)

# enc = cipher.encrypt(pad(text, 8))
# dec = unpad(cipher.decrypt(enc), 8)

# print("Original Text:", text)
# print("Key:", key)
# print("Encrypted Text:", enc)
# print("Decrypted Text:", dec)

# Output:-
# Original Text: b'HELLO123'
# Key: b'8bytekey'
# Encrypted Text: b'E\xba\xa1\x11k\x82\xa6\xab\x97F \xab\xef^\xf2J'
# Decrypted Text: b'HELLO123'
