from cryptography.fernet import Fernet

class AESDecryption:
    def __init__(self, key):
        self.cipher_suite = Fernet(key)

    def decrypt(self, ciphertext):
        try:
            decrypted_text = self.cipher_suite.decrypt(ciphertext)
            return decrypted_text.decode()
        except Exception as e:
            return f"Decryption error: {str(e)}"