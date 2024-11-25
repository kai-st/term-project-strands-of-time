def create_character():
    """
    Create a character with X and Y coordinates, level, last distance to goal, and Strands.

    :postcondition: creates a character dictionary with the key-value pairs "X-coordinate": -1,
    "Y-coordinate": -1, "level": 1, "last distance to goal": None, "Strands": {"Red": 3,
    "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3}
    :return: a character dictionary with the key-value pairs key-value pairs "X-coordinate": -1,
    "Y-coordinate": -1, "level": 1, "last distance to goal": None, "Strands": {"Red": 3,
    "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3}

    >>> create_character()
    {"X-coordinate": -1, "Y-coordinate": -1, "level": 1, "last distance to goal": None,
    "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3}}
    """
    return {"X-coordinate": -1, "Y-coordinate": -1, "level": 1,
            "last distance to goal": None, "Strands": {"Red": 3, "Orange": 3, "Yellow": 3,
                                                       "Green": 3, "Blue": 3, "Violet": 3}}


def has_strands(character):
    """
    Determine if the character is still alive.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: determines as a Boolean if character is alive based on if
    character["Current HP"] is greater than 0
    :return: a boolean that is True if character["Current HP"] is greater than 0

    >>> alive_character = create_character()
    >>> has_strands(alive_character)
    True
    >>> dead_character = create_character()
    >>> dead_character["Current HP"] = 0
    >>> has_strands(dead_character)
    False
    """
    return character["Current HP"] > 0


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
