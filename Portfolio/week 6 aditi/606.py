import random

def random_encrypt(message):
    interval = random.randint(2, 20)
    encrypted_message = ''
    index = 0

    for char in message:
        if char.isalpha():
            encrypted_message += char
            index += 1
        else:

            random_letter = chr(random.randint(65, 90))  
            encrypted_message += random_letter
            index += 1

        if index % interval == 0:
            encrypted_message += ' '

    return encrypted_message, interval

def random_decrypt(encrypted_message, interval):
    decrypted_message = ''
    index = 0

    for char in encrypted_message:
        if char.isalpha():
            decrypted_message += char
            index += 1

    return decrypted_message

message = "send cheese"
encrypted_message, interval = random_encrypt(message)

decrypted_message = random_decrypt(encrypted_message, interval)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
