from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai_client import OpenAIClient
import os
from cryptography.fernet import Fernet
from generate_keys import generate_keys
from file_utils import file_exists, open_file

app = Flask(__name__)
CORS(app)

# Check for the existence of key.key
if not file_exists('key.key'):
    # If key.key does not exist, check for api_key.txt
    if not file_exists('api_key.txt'):
        print("Error: Both key.key and api_key.txt are missing. Aborting.")
        exit(1)
    else:
        # If api_key.txt exists, generate the keys
        generate_keys()

# Load the encryption key and API key
with open_file('key.key', 'rb') as key_file:
    encryption_key = key_file.read()

cipher_suite = Fernet(encryption_key)

with open_file('api_key.enc', 'rb') as enc_file:
    encrypted_api_key = enc_file.read()

api_key = cipher_suite.decrypt(encrypted_api_key).decode('utf-8')

client = OpenAIClient(api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_character():
    prompt = request.json['prompt']
    character_sheet = client.generate_character_sheet(prompt)
    if character_sheet:
        return jsonify(character_sheet.dict())
    else:
        return jsonify({"error": "Failed to generate character sheet"}), 400

if __name__ == '__main__':
    app.run(debug=True)