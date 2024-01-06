# main.py
import argparse
from encryption.encryption import AESEncryption
from decryption.decryption import AESDecryption
from key_management.key_management import KeyManagement

def main():
    parser = argparse.ArgumentParser(description="AES Encryption and Decryption CLI")
    parser.add_argument("--generate-key", action="store_true", help="Generate a new AES encryption key")
    parser.add_argument("--encrypt", help="Encrypt a message")
    parser.add_argument("--decrypt", help="Decrypt a message")

    args = parser.parse_args()

    if args.generate_key:
        key = KeyManagement.generate_key()
        print("Generated AES encryption key:", key.decode())
        
       
    elif args.encrypt:
        key = KeyManagement.generate_key()
        print(f"\n\nYour Decrption key is {key}")
        aes = AESEncryption(key)
        encrypted_message = aes.encrypt(args.encrypt)
        print("\n\nEncrypted message:", encrypted_message.decode())

    elif args.decrypt:
        key = input("Enter the AES encryption key: ").encode()
        aes = AESDecryption(key)
        decrypted_message = aes.decrypt(args.decrypt.encode())
        print("Decrypted message:", decrypted_message)


main()