# *** Write a Python code to implement Diffie-Hellman Key Exchange ***

p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Public Values: p =", p, "g =", g)
print("Private Keys: a =", a, "b =", b)
print("Shared Key User1:", key1)
print("Shared Key User2:", key2)


// proper------------------------------------------

import random

# Step 1: Public values (prime and generator)
p = 23   # prime number
g = 5    # primitive root modulo p

# Step 2: Private keys (chosen secretly)
alice_private = random.randint(1, p-1)
bob_private = random.randint(1, p-1)

# Step 3: Compute public values
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("Public values:")
print("p =", p, "g =", g)
print("Alice public key:", alice_public)
print("Bob public key:", bob_public)

# Step 4: Exchange and compute shared secret
alice_shared_secret = pow(bob_public, alice_private, p)
bob_shared_secret = pow(alice_public, bob_private, p)

print("\nShared secrets:")
print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)

# Check if both secrets match
if alice_shared_secret == bob_shared_secret:
    print("\n✅ Key exchange successful!")
else:
    print("\n❌ Key exchange failed!")
