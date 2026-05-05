# *** Write a Python code to implement RSA Algorithm ***

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

p = 3
q = 11
n = p * q
phi = (p-1)*(q-1)

e = 3
d = modinv(e, phi)

msg = 7

enc = pow(msg, e, n)
dec = pow(enc, d, n)

print("Original Message:", msg)
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
print("Encrypted Message:", enc)
print("Decrypted Message:", dec)