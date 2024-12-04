import copy

from strands_of_time.location.board import create_game_board


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


def move_character(character: dict, player_input: str):
    """
    Move the character to the location the player chose.

    The character can move one space with wasd or jump with the format:
    "[number of columns][a or d][number of rows][w or s]".

    :param character: A well-formed character dictionary
    :param player_input: a string beginning with "[number of columns][a or d][number of rows][w or
    s]" or w, a, s, or d
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :precondition: direction must be a string beginnng with "[number of columns][a or d][number
    of rows][w or s]" or w, a, s, or d
    :postcondition: updates the coordinate keys in character to reflect the new location
    :raises TypeError: if character is not a dictionary
    :raises TypeError: if player_input is not a string
    :raises KeyError: if character does not have an "X-coordinate" key
    :raises KeyError: if character does not have an "Y-coordinate" key

    >>> moving_character = {"X-coordinate": 3, "Y-coordinate": 2}
    >>> move_character(moving_character, "w")
    >>> moving_character
    {'X-coordinate': 3, 'Y-coordinate': 1}
    >>> jumping_character = {"X-coordinate": 3, "Y-coordinate": 1}
    >>> move_character(jumping_character, "4d1s Yellow")
    >>> jumping_character
    {'X-coordinate': 7, 'Y-coordinate': 2}
    """
    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if not isinstance(player_input, str):
        raise TypeError("player_input must be a string")

    if "X-coordinate" not in character:
        raise KeyError("character must have 'X-coordinate' key")

    if "Y-coordinate" not in character:
        raise KeyError("character must have 'Y-coordinate' key")

    rows_to_move = 1
    columns_to_move = 1

    index_s = player_input.find("s")
    if index_s != -1 and index_s < 4:
        if index_s != 0:
            rows_to_move = int(player_input[index_s - 1])
        character["Y-coordinate"] += rows_to_move

    index_w = player_input.find("w")
    if index_w != -1 and index_w < 4:
        if index_w != 0:
            rows_to_move = int(player_input[index_w - 1])
        character["Y-coordinate"] -= rows_to_move

    index_d = player_input.find("d")
    if index_d != -1 and index_d < 4:
        if index_d != 0:
            columns_to_move = int(player_input[index_d - 1])
        character["X-coordinate"] += columns_to_move

    index_a = player_input.find("a")
    if index_a != -1 and index_a < 4:
        if index_a != 0:
            columns_to_move = int(player_input[index_a - 1])
        character["X-coordinate"] -= columns_to_move


def get_max_board_coordinates(board):
    """
    Return the largest coordinates for the board as a tuple of (X, Y) coordinates.

    :param board: a well-formed board dictionary
    :precondition: board must be a dictionary with (X, Y) coordinate keys
    :postcondition: returns the largest coordinates for board as a tuple of (X, Y) coordinates
    :return: a tuple with the largest coordinates as (X, Y) coordinates
    :raises TypeError: if board is not a dictionary
    :raises KeyError: if board does not have tuple keys containing pairs of integers
    :raises KeyError: if board tuple keys do not contain pairs of integers

    >>> board_5_by_5, _ = create_game_board(5, 5, [2, 4])
    >>> get_max_board_coordinates(board_5_by_5)
    (4, 4)
    >>> board_not_square, _ = create_game_board(6, 3, [2, 4])
    >>> get_max_board_coordinates(board_not_square)
    (5, 2)
    >>> smallest_board, _ = create_game_board(3, 2, [1, 2])
    >>> get_max_board_coordinates(smallest_board)
    (2, 1)
    """
    if not isinstance(board, dict):
        raise TypeError("board must be a dictionary")

    tuple_keys = []
    for key in board:
        if isinstance(key, tuple):
            tuple_keys.append(key)
            if len(key) != 2 or not isinstance(key[0], int) or not isinstance(key[1], int):
                raise KeyError('board locations must have "description" keys')
    if len(tuple_keys) < 1:
        raise KeyError("board must have tuple keys")

    max_x_coordinate = max(key[0] for key in board.keys() if isinstance(key, tuple))
    max_y_coordinate = max(key[1] for key in board.keys() if isinstance(key, tuple))

    return max_x_coordinate, max_y_coordinate


def validate_move(board, character, player_input):
    """
    Check that the player's choice of movement is in the bounds of the board.

    :param board: A well-formed board dictionary
    :param character: A well-formed character dictionary
    :param player_input: a string beginning with "[number of columns][a or d][number of rows][w or
    s]" or w, a, s, or d
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :precondition: player_input must be a string beginnng with "[number of columns][a or d][number
    of rows][w or s]" or w, a, s, or d
    :postcondition: checks that the player's choice of player_input is in the bounds of the board
    :return: A boolean that is True if the player's choice of player_input is in the bounds of the
    board
    :raises TypeError: if character is not a dictionary
    :raises TypeError: if player_input is not a string
    :raises TypeError: if board is not a dictionary
    :raises KeyError: if board does not have tuple keys containing pairs of integers
    :raises KeyError: if board tuple keys do not contain pairs of integers
    :raises KeyError: if character does not have an "X-coordinate" key
    :raises KeyError: if character does not have an "Y-coordinate" key

    >>> character_at_x_0_y_0 = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> board_5_by_5, _ = create_game_board(5, 5, [2, 4])
    >>> validate_move(board_5_by_5, character_at_x_0_y_0, "3s3d Blue")
    True
    >>> validate_move(board_5_by_5, character_at_x_0_y_0, "w")
    False
    >>> character_in_last_column = {"X-coordinate": 4, "Y-coordinate": 3}
    >>> validate_move(board_5_by_5, character_in_last_column, "d")
    False
    """
    if not isinstance(board, dict):
        raise TypeError("board must be a dictionary")

    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if not isinstance(player_input, str):
        raise TypeError("character must be an dictionary")

    if "X-coordinate" not in character:
        raise KeyError("character must have 'X-coordinate' key")

    if "Y-coordinate" not in character:
        raise KeyError("character must have 'Y-coordinate' key")

    tuple_keys = []
    for key in board:
        if isinstance(key, tuple):
            tuple_keys.append(key)
            if len(key) != 2 or not isinstance(key[0], int) or not isinstance(key[1], int):
                raise KeyError('board locations must have "description" keys')
    if len(tuple_keys) < 1:
        raise KeyError("board must have tuple keys")

    max_coordinates = get_max_board_coordinates(board)

    character_copy = copy.deepcopy(character)

    move_character(character_copy, player_input)

    return (character_copy["X-coordinate"] in range(max_coordinates[0] + 1)
            and character_copy["Y-coordinate"] in range(max_coordinates[1] + 1))
