# encryption/encryption.py
from cryptography.fernet import Fernet

class AESEncryption:
    def __init__(self, key):
        self.cipher_suite = Fernet(key)

    def encrypt(self, plaintext):
        encrypted_text = self.cipher_suite.encrypt(plaintext.encode())
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = self.cipher_suite.decrypt(ciphertext).decode()
        return decrypted_text