import random

from strands_of_time import RAINBOW_ORDER
from strands_of_time.utils import colourize


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

    >>> character_with_strands = create_character(3)
    >>> has_strands(character_with_strands)
    True
    >>> character_without_strands = create_character(0)
    >>> has_strands(character_without_strands)
    False
    """
    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "Strands" not in character:
        raise KeyError("character must have 'Strands' key")

    if not isinstance(character["Strands"], dict):
        raise TypeError("character['Strands'] must be an dictionary")

    for value in character["Strands"].values():
        if not (isinstance(value, int) or isinstance(value, float)):
            raise ValueError("character['Strands'] must have number values")

    return max(list(character["Strands"].values())) > 0


def print_strands(character: dict):
    """
    Print the character's current Strand amounts in their colours, enumerated with a label.

    Results are formated as: Strands: 1. Red: #, 2. Orange: #, 3. Yellow: #, 4. Green: #,
    5. Blue: #, 6. Violet: #

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Strands" key
    :postcondition: prints the character's current Strand amounts in their colours, enumerated
    with a label.
    :raises KeyError: if character does not have a "Strands" key
    :raises TypeError: if character is not a dictionary
    :raises TypeError: if "Strands" is not a dictionary
    """
    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "Strands" not in character:
        raise KeyError("character must have 'Strands' key")

    if not isinstance(character["Strands"], dict):
        raise TypeError("character['Strands'] must be an dictionary")

    print("Strands:", end=" ")
    for colour_ordinal, strand_record in enumerate(character["Strands"].items(), start=1):
        strand_listing = f"{colour_ordinal}. {strand_record[0]}: {strand_record[1]}"

        if colour_ordinal != len(character["Strands"]):
            strand_listing += ","

        print(colourize(strand_listing, strand_record[0]), end=" ")


def get_character_location_as_tuple(character: dict) -> tuple:
    """
    Return the character's location as a tuple of (X, Y) coordinates.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    with number values
    :postcondition: returns character's location as a tuple of (X, Y) coordinates
    :return: a tuple with the character's location as (X, Y) coordinates
    :raises KeyError: if character does not have an "X-coordinate" key
    :raises KeyError: if character does not have an "Y-coordinate" key
    :raises TypeError: if character is not a dictionary

    >>> character_at_initial_position = create_character(3)
    >>> get_character_location_as_tuple(character_at_initial_position)
    (-1, -1)
    >>> character_x_3_y_2 = create_character(3)
    >>> character_x_3_y_2["X-coordinate"] = 3
    >>> character_x_3_y_2["Y-coordinate"] = 2
    >>> get_character_location_as_tuple(character_x_3_y_2)
    (3, 2)
    """
    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "X-coordinate" not in character:
        raise KeyError("character must have 'X-coordinate' key")

    if "Y-coordinate" not in character:
        raise KeyError("character must have 'Y-coordinate' key")

    return character["X-coordinate"], character["Y-coordinate"]


def remove_random_strand(character):
    """
    Remove a random Strand from the character's current Strands.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary
    :precondition: character must have a "Strands" key that is a dictionary with the rainbow
    colours as keys and number values
    :precondition: character must have at least one Strand colour with more than 0 Strands
    :postcondition: reduces the value of a randomly selected one of character["Strands"] Strand
    colours by 1
    :raises KeyError: if character does not have a "Strands" key
    :raises TypeError: if character is not a dictionary
    :raises TypeError: if "Strands" is not a dictionary
    :raises TypeError: if values in "Strands" are not ints or floats
    :raises ValueError: if values of all "Strands" are less than 1

    >>> new_character = create_character(3)
    >>> remove_random_strand(new_character)
    >>> new_character['Strands'] # doctest: +SKIP
    {'Red': 3, 'Orange': 2, 'Yellow': 3, 'Green': 3, 'Blue': 3, 'Violet': 3}
    >>> dying_character = create_character(0)
    >>> dying_character['Strands']['Red'] = 1
    >>> remove_random_strand(dying_character)
    >>> dying_character['Strands']
    {'Red': 0, 'Orange': 0, 'Yellow': 0, 'Green': 0, 'Blue': 0, 'Violet': 0}
    """
    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "Strands" not in character:
        raise KeyError("character must have 'Strands' key")

    if not isinstance(character["Strands"], dict):
        raise TypeError("character['Strands'] must be an dictionary")

    for value in character["Strands"].values():
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("character['Strands'] must have number values")

    available_strands = [colour for colour, number in character["Strands"].items() if number > 0]

    if len(available_strands) == 0:
        raise ValueError("Character must have at least 1 Strand of at least 1 colour")

    strand_to_remove = random.choice(available_strands)
    character["Strands"][strand_to_remove] -= 1
