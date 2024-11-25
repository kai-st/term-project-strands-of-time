import random

from strands_of_time.character.character import get_character_location_as_tuple


def create_game_board(rows, columns):
    """
    Construct a 2D gameboard with rooms laid out in a given numbers of rows and columns.

    The gameboard will be represented by a dictionary with keys of tuples representing the
    (x,y) coordinates of each room, and values containing descriptions for each room.

    :param rows: a positive non-zero integer number of rows to create
    :param columns: a positive non-zero integer number of columns to create
    :precondition: rows must be an integer greater than 0
    :precondition: columns must be an integer greater than 0
    :postcondition: constructs a dictionary representing a game board with rows * column number
    of rooms
    :postcondition: stores each room in the dictionary with a tuple containing the room's
    coordinates as the key and a string containing the room's description as the value
    :return: a dictionary representing the gameboard with keys (x-coordinate, y-coordinate) for
    each room and string values containing descriptions for each room

    >>> create_game_board(2, 2) # doctest: +SKIP
    {
    (0, 0): 'a dark cavern at the northwest end of a tangled cave system deep in the Underdark
    with only the dim glow of your trusty magic blade to lead you to the surface.',
    (0, 1): 'a cramped cave, its walls thick with jagged crystalline outcroppings. It's beautiful,
    like walking through a geode, but the edges look razor sharp',
    (1, 0): 'an immense cavern. A narrow rock bridge crosses a deep chasm running though the
    centre. You can't see the bottom.',
    (1, 1): 'a long narrow tunnel. Finally, you can see the glimmer of surface sunlight filtering
    into he mouth of the cave ahead of you.',
    }
    >>> create_game_board(1, 1) # doctest: +SKIP
    {(0, 0): 'a dark cavern at the northwest end of a tangled cave system deep in the Underdark
    with only the dim glow of your trusty magic blade to lead you to the surface.'}
    """
    first_room_description = ("a dark cavern at the northwest end of a tangled cave system deep "
                              "in the Underdark with\nonly the dim glow of your trusty magic "
                              "blade to lead you to the surface.")

    last_room_description = ("a narrow tunnel. Finally, you can see the glimmer of surface "
                             "sunlight filtering into\nthe mouth of the cave ahead of you.")

    random_room_descriptions = ["a cramped cave, its walls thick with jagged crystalline "
                                "outcroppings.\nIt's beautiful, like walking through a geode, "
                                "but the edges look razor sharp.",
                                "an immense cavern. A narrow rock bridge crosses a deep chasm "
                                "running though\nthe centre. You can't see the bottom.",
                                "a damp cave with small hot spring bubbling in the centre. A "
                                "strange mold coats\nthe rock surfaces around the spring, "
                                "emitting an eerie glow.",
                                "a large cave filled with giant fungi. You can easily stand "
                                "under the cap of\nthe tallest mushroom.",
                                "pitch black space. Even the glow of your sword suppressed here. "
                                "You hear faint skittering\nsounds around you in the dark.",
                                ]

    board = {}
    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0:
                board[(column, row)] = first_room_description
            elif row == rows - 1 and column == columns - 1:
                board[(column, row)] = last_room_description
            else:
                board[(column, row)] = random.choice(random_room_descriptions)

    return board


def prep_current_location_for_printing(character):
    """
    Return the character's current location with a label as a string for printing.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: returns character's current location with label as a string
    :return: character's current location with label as a string

    >>> new_character = create_character()
    >>> prep_current_location_for_printing(new_character)
    'Current location: Row 1, Column 1'
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> prep_current_location_for_printing(mid_game_character)
    'Current location: Row 4, Column 3'
    """
    current_row = character["Y-coordinate"] + 1
    current_col = character["X-coordinate"] + 1
    return f"Current location: Row {current_row}, Column {current_col}"


def describe_current_location(board, character):
    """
    Print the description of the character's current location.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate", "Y-coordinate",
    and "Current HP" keys
    :postcondition: prints the description of the character's current location.

    >>> new_character = create_character()
    >>> board_5_by_5 = create_game_board(5, 5)
    >>> describe_current_location(board_5_by_5, new_character)
    You're in a dark cavern at the northwest end of a tangled cave system deep in the Underdark with
    only the dim glow of your trusty magic blade to lead you to the surface.
    <BLANKLINE>
    >>> end_game_character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 3}
    >>> describe_current_location(board_5_by_5, end_game_character)
    You're in a narrow tunnel. Finally, you can see the glimmer of surface sunlight filtering into
    the mouth of the cave ahead of you.
    <BLANKLINE>
    """
    current_location = get_character_location_as_tuple(character)

    print("You're in", board[current_location], end="\n\n")
