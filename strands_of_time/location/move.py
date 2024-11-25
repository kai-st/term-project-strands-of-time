import copy


def get_move_from_player():
    """
    Gets the player's choice of which cardinal direction they want to move.

    :postcondition: gets the player's choice of which cardinal direction they want to move
    :return: the player's choice of cardinal direction as a string
    """
    numbers_to_direction_map = {"1": "north", "2": "south", "3": "west", "4": "east"}

    user_choice = input("Which way do you want to go?\n(Enter 1. North, 2. South, 3. West, "
                        "4. East)\n")

    while user_choice not in numbers_to_direction_map:
        print("\nSorry, that is not a valid direction. Please try again.", end="\n\n")
        user_choice = input("Which way do you want to go?\n(Enter 1. North, 2. South, 3. West, "
                            "4. East)\n")

    return numbers_to_direction_map[user_choice]


def move_character(character, direction):
    """
    Move the character in the direction the player chose.

    :param character: A well-formed character dictionary
    :param direction: north, south, east, or west as a string
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :precondition: direction must be a string equal to one of north, south, east, or west
    :postcondition: updates the correct coordinate key in character to reflect the new location

    >>> new_character = create_character()
    >>> move_character(new_character, "south")
    >>> new_character
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> move_character(mid_game_character, "east")
    >>> mid_game_character
    {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 3}
    """
    if direction == "north":
        character["Y-coordinate"] -= 1
    elif direction == "south":
        character["Y-coordinate"] += 1
    elif direction == "west":
        character["X-coordinate"] -= 1
    elif direction == "east":
        character["X-coordinate"] += 1


def validate_move(board, character, direction):
    """
    Check that the player's choice of direction is in the bounds of the board.

    :param board: A well-formed board dictionary
    :param character: A well-formed character dictionary
    :param direction: north, south, east, or west as a string
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :precondition: direction must be a string equal to one of north, south, east, or west
    :postcondition: checks that the player's choice of direction is in the bounds of the board
    :return: A boolean that is True if the player's choice of direction is in the bounds of the
    board

    >>> character_at_x_0_y_0 = create_character()
    >>> board_5_by_5 = create_game_board(5, 5)
    >>> validate_move(board_5_by_5, character_at_x_0_y_0, "south")
    True
    >>> validate_move(board_5_by_5, character_at_x_0_y_0, "north")
    False
    >>> character_in_last_column = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 3}
    >>> validate_move(board_5_by_5, character_in_last_column, "east")
    False
    """
    max_coordinates = get_goal_location(board)

    character_copy = copy.deepcopy(character)

    move_character(character_copy, direction)

    return (character_copy["X-coordinate"] in range(max_coordinates[0] + 1)
            and character_copy["Y-coordinate"] in range(max_coordinates[1] + 1))
