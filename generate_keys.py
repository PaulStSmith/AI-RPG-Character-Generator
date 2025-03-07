from cryptography.fernet import Fernet
from file_utils import open_file

def generate_keys():
    # Generate and save the encryption key
    encryption_key = Fernet.generate_key()
    with open_file('key.key', 'wb') as key_file:
        key_file.write(encryption_key)

    # Read the API key from an external file
    with open_file('api_key.txt', 'r') as api_key_file:
        api_key = api_key_file.read().strip()

    # Encrypt the API key
    cipher_suite = Fernet(encryption_key)
    encrypted_api_key = cipher_suite.encrypt(api_key.encode('utf-8'))

    # Save the encrypted API key
    with open_file('api_key.enc', 'wb') as enc_file:
        enc_file.write(encrypted_api_key)
