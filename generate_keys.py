from cryptography.fernet import Fernet
from file_utils import open_file, file_exists
import os

def generate_keys():
    # Generate and save the encryption key
    encryption_key = Fernet.generate_key()
    with open_file('key.key', 'wb') as key_file:
        key_file.write(encryption_key)

    # Check if the API key file exists
    if not file_exists('api_key.txt'):
        print("Error: api_key.txt file is missing.")
        return False

    # Read the API key from an external file
    with open_file('api_key.txt', 'r') as api_key_file:
        api_key = api_key_file.read().strip()

    # Encrypt the API key
    cipher_suite = Fernet(encryption_key)
    encrypted_api_key = cipher_suite.encrypt(api_key.encode('utf-8'))

    # Save the encrypted API key
    with open_file('api_key.enc', 'wb') as enc_file:
        enc_file.write(encrypted_api_key)

    return True

if __name__ == "__main__":
    if generate_keys():
        print("Encryption keys generated and API key encrypted successfully.")
        delete_option = input("Do you want to delete the clean-text API key file (api_key.txt)? (yes/no): ").strip().lower()
        if delete_option == 'yes':
            os.remove('api_key.txt')
            print("Clean-text API key file deleted.")
    else:
        print("Failed to generate encryption keys and encrypt API key.")
