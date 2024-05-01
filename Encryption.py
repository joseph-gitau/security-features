from nacl import secret, utils
from base64 import b64encode, b64decode

# Generate a random key for encryption
key = utils.random(secret.SecretBox.KEY_SIZE)
box = secret.SecretBox(key)

# sensitive data that needs to be encrypted
message = b"Hola, mundo!"

# Encrypt the message
encrypted = box.encrypt(message)
encrypted_text = b64encode(encrypted).decode('utf-8')

print(f"Encrypted: {encrypted_text}")
