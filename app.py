from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai_client import OpenAIClient
import os

app = Flask(__name__)
CORS(app)

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

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