# AI-RPG-Character-Generator

<div style="display: flex; align-items: flex-start;">
<div style="flex: 1; padding-right: 20px;">

This project is a web-based application that generates character sheets for the Pathfinder 2nd Edition role-playing game. It uses OpenAI's GPT model to create detailed and creative character backgrounds, personalities, and statistics based on user prompts.

## Features

- Generate complete Pathfinder 2e character sheets from simple text prompts
- Web-based user interface for easy access and use
- Detailed character information including:
  - Basic details (name, ancestry, background, class, alignment)
  - Ability scores
  - Skills and proficiencies
  - Saving throws
  - Hit points and armor class
  - Feats and equipment
  - Character description, appearance, and personality traits
- Automatic calculation of ability modifiers
- Responsive design for use on various devices

</div>
<div style="flex: 1;">
<img src="Screenshot.png" alt="AI-RPG-Character-Generator Screenshot" style="max-width: 100%; height: auto;">
</div>
</div>

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/PaulStSmith/AI-RPG-Character-Generator
   cd AI-RPG-Character-Generator
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Place your OpenAI API key in a file named `api_key.txt` in the project root directory.

5. Generate the encryption keys and encrypt your OpenAI API key:
   ```
   python generate_keys.py
   ```

6. Run the Flask application:
   ```
   python app.py
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter a character description in the text area and click "Generate Character"

    For instance, try:
    > Joe Under-Average. A level 3 fighter with big muscles and a small brain. He’s kind and friendly but has a low frustration tolerance. He always wears an amulet, which is actually just a small stick bound to a piece of rope.

4. Wait for the character generation process to complete

5. View your generated character sheet

6. You can use the buttons under the character sheet to copy it as JSON or HTML

## Project Structure

```
src/
│
├── static/
│   ├── pathfinder.png       # Pathfinder Compatible logo
│   ├── pathfinder.ttf       # Pathfinder font (From the Compatibility package)
│   ├── script.js            # JavaScript file for client-side functionality
│   └── styles.css           # CSS file for styling the web interface
│
├── templates/
│   └── index.html           # HTML template for the web interface
│
├── .gitignore               # Git ignore file to exclude certain files from version control
├── api_key.enc              # Encrypted OpenAI API key
├── api_key.txt              # Plain text OpenAI API key (to be encrypted)
├── app.py                   # Flask application entry point
├── character_schema.py      # Pydantic models for character data
├── file_utils.py            # Utility functions for file operations
├── generate_keys.py         # Script to generate encryption keys and encrypt the API key
├── key.key                  # Encryption key file
├── LICENSE                  # License file for the project
├── openai_client.py         # OpenAI API client for interacting with the GPT model
├── README.md                # This file
├── requirements.txt         # Project dependencies
└── Screenshot.png           # Application screenshot
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT model used in character generation
- The Pathfinder 2e community for inspiration and game mechanics

## Disclaimer

This project is not affiliated with or endorsed by Paizo Inc., the creators of Pathfinder. It is a fan-made tool intended for personal use and should not be used for commercial purposes.
