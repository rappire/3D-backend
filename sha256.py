import hashlib

key = "@*&an10^"


def encrypt_sha(password):
    password = key + password
    print(hashlib.sha256(password.encode()).hexdigest())
    return hashlib.sha256(password.encode()).hexdigest()
