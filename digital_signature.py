# *** Write a Python code to implement Digital Signature ***

import hashlib

def sign(message, key):
    hash_val = hashlib.sha256(message.encode()).hexdigest()
    return hash_val + key

def verify(message, signature, key):
    hash_val = hashlib.sha256(message.encode()).hexdigest()
    return signature == hash_val + key

msg = "HELLO"
key = "secret"

sig = sign(msg, key)

print("Original Message:", msg)
print("Key:", key)
print("Generated Signature:", sig)
print("Verification Result:", verify(msg, sig, key))




# 8. Write a Python code to implement Digital Signature 

# import hashlib
# def sign(message, key):
#     hash_val = hashlib.sha256(message.encode()).hexdigest()
#     return hash_val + key

# def verify(message, signature, key):
#     hash_val = hashlib.sha256(message.encode()).hexdigest()
#     return signature == hash_val + key

# msg = "HELLO"
# key = "secret"
# sig = sign(msg, key)

# print("Original Message:", msg)
# print("Key:", key)
# print("Generated Signature:", sig)
# print("Verification Result:", verify(msg, sig, key))

# Output:-
# Original Message: HELLO
# Key: secret
# Generated Signature: 3733cd977ff8eb18b987357e22ced99f46097f31ecb239e878ae63760e83e4d5secret
# Verification Result: True
