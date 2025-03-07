from openai import OpenAI
from character_schema import CharacterSheet, get_character_sheet_schema
import logging
from pydantic import ValidationError
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenAIClient:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_character_sheet(self, prompt):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a Pathfinder 1e character generator. Create a complete character sheet based on the user's prompt. Fill in any missing details creatively. Make sure to fill in ALL fields. If you're missing information to fill in a field, come up with something creative."},
                    {"role": "user", "content": prompt}
                ],
                functions=[
                    {
                        "name": "create_character_sheet",
                        "description": "Generate a complete Pathfinder 1e character sheet",
                        "parameters": get_character_sheet_schema()
                    }
                ],
                function_call={"name": "create_character_sheet"}
            )

            function_call = completion.choices[0].message.function_call
            if function_call and function_call.name == "create_character_sheet":
                character_data = json.loads(function_call.arguments)
                try:
                    return CharacterSheet(**character_data)
                except ValidationError as e:
                    logger.error(f"Validation error: {e}")
                    return None
            else:
                logger.warning("No valid function call found in the API response")
                return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None