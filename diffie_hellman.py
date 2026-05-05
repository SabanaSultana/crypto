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