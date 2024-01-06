# key_management/key_management.py
from cryptography.fernet import Fernet

class KeyManagement:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()