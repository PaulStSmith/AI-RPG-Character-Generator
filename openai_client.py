from openai import OpenAI
from character_schema import CharacterSheet, get_character_sheet_schema
import logging
from pydantic import ValidationError
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenAIClient:
    def __init__(self, api_key):
        """
        Initialize the OpenAI client with the provided API key.
        
        :param api_key: The API key for authenticating with the OpenAI service.
        """
        self.client = OpenAI(api_key=api_key)

    def generate_character_sheet(self, prompt):
        """
        Generate a Pathfinder 2e character sheet based on the provided prompt.
        
        :param prompt: The user's prompt describing the character.
        :return: A validated CharacterSheet object or None if an error occurs.
        """
        try:
            # Create a completion request to the OpenAI API
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a Pathfinder 2e character generator. Create a complete character sheet based on the user's prompt. Fill in any missing details creatively. Make sure to fill in ALL fields. If you're missing information to fill in a field, come up with something creative."},
                    {"role": "user", "content": prompt}
                ],
                functions=[
                    {
                        "name": "create_character_sheet",
                        "description": "Generate a complete Pathfinder 2e character sheet",
                        "parameters": get_character_sheet_schema()
                    }
                ],
                function_call={"name": "create_character_sheet"}
            )

            # Extract the function call from the completion response
            function_call = completion.choices[0].message.function_call
            if function_call and function_call.name == "create_character_sheet":
                # Parse the character data from the function call arguments
                character_data = json.loads(function_call.arguments)
                try:
                    # Validate and return the character sheet
                    return CharacterSheet(**character_data)
                except ValidationError as e:
                    # Log validation errors
                    logger.error(f"Validation error: {e}")
                    return None
            else:
                # Log a warning if no valid function call is found
                logger.warning("No valid function call found in the API response")
                return None
        except Exception as e:
            # Log any unexpected errors
            logger.error(f"Unexpected error: {e}")
            return None