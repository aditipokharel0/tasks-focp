import random
import string

def random_interval():
    return random.randint(2, 20)

def random_letter():
    return random.choice(string.ascii_uppercase)

def random_encrypt(message):
    interval = random_interval()

    encrypted_message = ''
    index = 0

    for char in message:
        if char.isalpha():
            encrypted_message += char
        else:
            for _ in range(interval - 1):
                encrypted_message += random_letter()
            encrypted_message += char

    return encrypted_message, interval
original_message = "send cheese"
encrypted_message, interval = random_encrypt(original_message)

print(f"Original message: {original_message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval}")
