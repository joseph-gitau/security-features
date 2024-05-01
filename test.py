import unittest
from nacl import secret, utils

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = utils.random(secret.SecretBox.KEY_SIZE)
        box = secret.SecretBox(key)
        message = b"Test Message"
        encrypted = box.encrypt(message)
        decrypted = box.decrypt(encrypted)
        self.assertEqual(message, decrypted)
        
    def test_decrypt(self):
        key = utils.random(secret.SecretBox.KEY_SIZE)
        box = secret.SecretBox(key)
        message = b"Test Message"
        encrypted = box.encrypt(message)
        decrypted = box.decrypt(encrypted)
        self.assertEqual(message, decrypted)

if __name__ == '__main__':
    unittest.main()
