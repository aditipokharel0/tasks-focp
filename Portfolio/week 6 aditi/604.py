def simple_encrypt(message):
    encrypted_message = message.replace(" ", "")[::-1]
    return encrypted_message

originalmessage = "Hello, world! This is a simple encryption example."
encryptedmessage = simple_encrypt(original_message)

print(f"Original message: {originalmessage}")
print(f"Encrypted message: {encryptedmessage}")
