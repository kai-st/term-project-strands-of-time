import random

from strands_of_time.character.character import get_character_location_as_tuple


def create_game_board(columns: int, rows: int, epoch_boundaries: list[int]) -> dict:
    """
    Construct a 2D gameboard with locations laid out in a given numbers of rows and columns.

    The gameboard will be represented by a dictionary with keys of tuples representing the
    (x,y) coordinates of each location, and values containing dictionaries with descriptions for
    each location and what colour of Strand can be restored there, if any. It will also contain
    a key "epoch_boundaries" with a list of column numbers before which the time period changes.

    :param columns: a positive non-zero integer number of columns to create
    :param rows: a positive non-zero integer number of rows to create
    :param epoch_boundaries: a list containing positive non-zero integer column numbers before
    which the time period changes
    :precondition: rows must be an integer greater than 0
    :precondition: columns must be an integer greater than 0
    :precondition: epoch_boundaries must be a list of ints greater than 0 and less than columns
    :postcondition: constructs a dictionary representing a game board with rows * column number
    of locations
    :postcondition: stores each location in the dictionary with a tuple containing the location's
    coordinates as the key and dictionary as the value containing the key "description" with a
    string containing the location's description
    :postcondition: marks which locations restore Strands with a key "gives Strand" and a colour
    value
    :postcondition: stores the epoch_boundaries in a key "epoch_boundaries"
    :return: a dictionary representing the gameboard with the key "epoch_boundaries" with
    epoch_boundaries as a value and keys (x-coordinate, y-coordinate) for each location and
    dictionary values containing "description" keys with string values for each location and a
    "gives Stand" key with a colour string value if the location gives a stand
    :raises TypeError: if columns is not an integer
    :raises TypeError: if rows is not an integer
    :raises TypeError: if epoch_boundaries is not a list
    :raises TypeError: if epoch_boundaries contains items that are not integers
    :raises ValueError: if columns is not greater than 0
    :raises ValueError: if rows is not greater than 0
    :raises ValueError: if epoch_boundaries contains numbers less than 0
    :raises ValueError: if epoch_boundaries contains numbers not less than columns

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
