from nacl import secret, utils
from base64 import b64encode, b64decode

# Generate a random key for encryption
key = utils.random(secret.SecretBox.KEY_SIZE)
box = secret.SecretBox(key)

# sensitive data to be decrypted
message = b"This is a secret message!"

# Encrypt the message
encrypted = box.encrypt(message)
encrypted_text = b64encode(encrypted).decode('utf-8')

print(f"Encrypted: {encrypted_text}")

# Decode the encrypted message
encrypted = b64decode(encrypted_text)

# Decrypt the message
decrypted = box.decrypt(encrypted)
print(f"Decrypted: {decrypted.decode('utf-8')}")
