from pydantic import BaseModel, Field, field_validator
from typing import List, Union, Dict, Any
from enum import Enum

class Ability(BaseModel):
    """Represents an ability score with validation for range."""
    score: int

    @field_validator('score')
    def check_score_range(cls, v):
        """Validates that the ability score is between 1 and 30."""
        if v < 1 or v > 30:
            raise ValueError('Score must be between 1 and 30')
        return v

class Abilities(BaseModel):
    """Represents a collection of ability scores."""
    Strength: Ability
    Dexterity: Ability
    Constitution: Ability
    Intelligence: Ability
    Wisdom: Ability
    Charisma: Ability

class SavingThrows(BaseModel):
    """Represents saving throw values."""
    Fortitude: int
    Reflex: int
    Will: int

class ProficiencyLevel(str, Enum):
    """Enumeration of proficiency levels."""
    untrained = "untrained"
    trained = "trained"
    expert = "expert"
    master = "master"
    legendary = "legendary"

class Skill(BaseModel):
    """Represents a skill with a name, proficiency level, and modifier."""
    name: str
    proficiency: ProficiencyLevel
    modifier: int

class CharacterClass(BaseModel):
    """Represents a character class with a name and level."""
    name: str
    level: int

    @field_validator('level')
    def check_level_range(cls, v):
        """Validates that the character level is between 1 and 20."""
        if v < 1 or v > 20:
            raise ValueError('Level must be between 1 and 20')
        return v

class Alignment(str, Enum):
    """Enumeration of character alignments."""
    LG = "Lawful Good"
    NG = "Neutral Good"
    CG = "Chaotic Good"
    LN = "Lawful Neutral"
    TN = "True Neutral"
    CN = "Chaotic Neutral"
    LE = "Lawful Evil"
    NE = "Neutral Evil"
    CE = "Chaotic Evil"

class CharacterSheet(BaseModel):
    """Represents a complete character sheet."""
    name: str
    ancestry: str
    background: str
    character_class: CharacterClass
    alignment: Alignment
    level: int
    abilities: Abilities
    skills: List[Skill]
    languages: List[str]
    hit_points: int
    armor_class: int
    saving_throws: SavingThrows
    feats: List[str]
    equipment: List[str]
    description: Union[str, None]
    look: str
    way_of_speaking: str
    loves: str
    hates: str

    @field_validator('level')
    def check_level_range(cls, v):
        """Validates that the character level is between 1 and 20."""
        if v < 1 or v > 20:
            raise ValueError('Level must be between 1 and 20')
        return v

    class Config:
        """Configuration for the CharacterSheet model."""
        extra = 'forbid'

def set_all_required(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively sets all properties in the schema as required."""
    if 'type' in schema and schema['type'] == 'object' and 'properties' in schema:
        schema['required'] = list(schema['properties'].keys())
        for prop in schema['properties'].values():
            set_all_required(prop)
    elif 'type' in schema and schema['type'] == 'array' and 'items' in schema:
        set_all_required(schema['items'])
    return schema

def get_character_sheet_schema():
    """Generates the schema for the CharacterSheet model with all properties set as required."""
    schema = CharacterSheet.schema()
    return set_all_required(schema)