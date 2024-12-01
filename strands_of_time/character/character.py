from logging import raiseExceptions

from strands_of_time import RAINBOW_ORDER


def create_character(initial_strands: int) -> dict[str, int or None or dict[str, int]]:
    """
    Create a character with X and Y coordinates, level, last distance to goal, and Strands.

    :param initial_strands: a positive interger number of Strands of each colour the character
    starts with
    :precondition: initial_strands must be greater than or equal to 0
    :postcondition: creates a character dictionary with the key-value pairs "X-coordinate": -1,
    "Y-coordinate": -1, "level": 1, "last distance to goal": None, "Strands": a dictionary with
    keys for each rainbow colour with values set to initial_strands
    :return: a character dictionary with the key-value pairs "X-coordinate": -1,
    "Y-coordinate": -1, "level": 1, "last distance to goal": None, "Strands": a dictionary with
    keys for each rainbow colour with values set to initial_strands
    :raises ValueError: if initial_strands is negative
    :raises TypeError: if initial_strands is not an integer

    >>> create_character(3)
    {'X-coordinate': -1, 'Y-coordinate': -1, 'level': 1, 'last distance to goal': None,\
 'Strands': {'Red': 3, 'Orange': 3, 'Yellow': 3, 'Green': 3, 'Blue': 3, 'Violet': 3}}
    >>> create_character(0)
    {'X-coordinate': -1, 'Y-coordinate': -1, 'level': 1, 'last distance to goal': None,\
 'Strands': {'Red': 0, 'Orange': 0, 'Yellow': 0, 'Green': 0, 'Blue': 0, 'Violet': 0}}
    """
    if not isinstance(initial_strands, int):
        raise TypeError("initial_strands must be an integer")

    if initial_strands < 0:
        raise ValueError("Character cannot start with negative Strands")

    strands = {colour: initial_strands for colour in RAINBOW_ORDER}
    return {"X-coordinate": -1, "Y-coordinate": -1, "level": 1,
            "last distance to goal": None, "Strands": strands}


def has_strands(character: dict) -> bool:
    """
    Determine if the character has any Strands remaining.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Strands" key that is a dictionary with
    number values
    :postcondition: determines as a Boolean if character has at least one Strand colour greater
    than 0
    :return: a boolean that is True if character has at least one Strand colour greater
    than 0
    :raises KeyError: if character does not have a "Strands" key
    :raises TypeError: if character is not a dictionary
    :raises TypeError: if "Strands" is not a dictionary
    :raises ValueError: if values in "Strands" are not ints or floats

    >>> character_with_strands = create_character()
    >>> has_strands(character_with_strands)
    True
    >>> character_without_strands = create_character()
    >>> character_without_strands["Strands"] = {"Red": 0, "Orange": 0, "Yellow": 0}
    >>> has_strands(character_without_strands)
    False
    """
    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "Strands" not in character:
        raise ValueError("character must have 'Strands' key")

    if not isinstance(character["Strands"], dict):
        raise TypeError("character['Strands'] must be an dictionary")

    for value in character["Strands"].values():
        if not isinstance(value, int or float):
            raise ValueError("character['Strands'] must have number values")

    return max(list(character["Strands"].values())) > 0


def prep_current_hp_for_printing(character):
    """
    Return the character's current HP with a label as a string for printing.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: returns character's current HP with label as a string
    :return: character's current HP with label a string

    >>> new_character = create_character()
    >>> prep_current_hp_for_printing(new_character)
    'Current HP: 5'
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> prep_current_hp_for_printing(mid_game_character)
    'Current HP: 3'
    """
    return f"Current HP: {character["Current HP"]}"


def get_character_location_as_tuple(character):
    """
    Return the character's location as a tuple of (X, Y) coordinates.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: returns character's location as a tuple of (X, Y) coordinates
    :return: a tuple with the character's location as (X, Y) coordinates

    >>> character_at_initial_position = create_character()
    >>> get_character_location_as_tuple(character_at_initial_position)
    (0, 0)
    >>> character_x_3_y_2 = create_character()
    >>> character_x_3_y_2["X-coordinate"] = 3
    >>> character_x_3_y_2["Y-coordinate"] = 2
    >>> get_character_location_as_tuple(character_x_3_y_2)
    (3, 2)
    """
    return character["X-coordinate"], character["Y-coordinate"]


def damage_character(character):
    """
    Reduce the current HP of the character by 1.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: reduces the value of character["Current HP"] by 1

    >>> new_character = create_character()
    >>> damage_character(new_character)
    >>> new_character
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4}
    >>> dying_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 1}
    >>> damage_character(dying_character)
    >>> dying_character
    {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 0}
    """
    character["Current HP"] -= 1
