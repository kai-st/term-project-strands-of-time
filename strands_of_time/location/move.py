import copy
from os import abort

from strands_of_time import RAINBOW_ORDER
from strands_of_time.location.board import create_game_board


def get_move_from_player(board: dict, character: dict) -> str:
    """
    Get the player's choice of where to move using wasd or a jump command.

    A jump command takes the format "[# of columns][a or d][# of rows][w or s] [Strand colour #]".

    :param board: A well-formed board dictionary
    :param character: A well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: gets the player's choice of where to move using wasd or a jump command
    :return: the player's input as a string
    """
    movement_prompt = ('Where do you want to go?\n(Move one space with wasd, or spend a Strand '
                       'to jump using "[# of columns][a or d][# of rows][w or s] ['
                       'Strand colour #]", e.g. 3d2s 4)\n')
    aborted = True
    while aborted:
        aborted = False
        player_input = input(movement_prompt)
        has_error = True
        while has_error:
            try:
                has_error = not check_move_format(player_input)
            except TypeError:
                print("\nSorry, that is not a valid movement command. Please try again.", end="\n\n")
                player_input = input(movement_prompt)
            else:
                if has_error:
                    print("\nSorry, that is not a valid movement command. Please try again.",
                          end="\n\n")
                    player_input = input(movement_prompt)

        while not validate_move(board, character, player_input):
            print("\nYou can't go there. Please try again.", end="\n\n")
            player_input = input(movement_prompt)

        strand_to_spend = None
        split_input = player_input.split()
        needs_strand = False
        if len(player_input) == 1:
            if not (player_input == "a" and character["X-coordinate"] in board["epoch boundaries"]
                    or player_input == "d"
                    and character["X-coordinate"] + 1 in board["epoch boundaries"]):
                return player_input
            else:
                print("This move requires a time jump.")
                needs_strand = True
        elif (len(split_input) == 1
              or not split_input[1].isdigit()
              or int(split_input[1]) not in range(1, 7)):
            print("Sorry, I didn't understand which Strand you entered. Please try again.")
            needs_strand = True
        else:
            strand_to_spend = RAINBOW_ORDER[int(split_input[1]) -1]

        no_strand_of_choice_colour = False
        if character["Strands"][strand_to_spend] < 1:
            no_strand_of_choice_colour = True

        while needs_strand or no_strand_of_choice_colour:
            if no_strand_of_choice_colour:
                print(f"You don't have any {strand_to_spend} Strands to spend.'")
            player_strand = input("What colour Strand do you want to spend?\n(Enter 1-6, "
                                  "or enter 0 to abort this move.\n")
            if player_strand == "0":
                aborted = True
                break
            try:
                strand_to_spend = RAINBOW_ORDER[int(player_strand) - 1]
            except (TypeError, IndexError):
                print("Sorry, entry must be an integer between 0 and 6")
            else:
                needs_strand = False
                if character["Strands"][strand_to_spend] < 1:
                    no_strand_of_choice_colour = True
                else:
                    no_strand_of_choice_colour = False

        if not aborted:
            character["Strands"][strand_to_spend] -= 1
            return split_input[0]


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
    >>> another_jumping_character = {"X-coordinate": 3, "Y-coordinate": 1}
    >>> move_character(another_jumping_character, "4d1s")
    >>> another_jumping_character
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


def get_max_board_coordinates(board: dict) -> tuple[int, int]:
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


def validate_move(board: dict, character: dict, player_input: str) -> bool:
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
        raise TypeError("player_input must be a string")

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


def check_move_format(player_input: str) -> bool:
    """
    Check that the movement input from the player is in a valid format.

    The character can move one space with wasd or jump with the format:
    "[number of columns][a or d][number of rows][w or s] (Colour)".

    :param player_input: a string
    :precondition: player_input is a string
    :postcondition: checks that player_input is in a valid format
    :return: a boolean that is true if player_input is in a valid format
    :raises TypeError: if player_input is not a string

    >>> check_move_format("w")
    True
    >>> check_move_format("3a5s 1")
    True
    >>> check_move_format("3s5a 1")
    False
    """
    wasd = ("w", "s", "a", "d")

    if not isinstance(player_input, str):
        raise TypeError("player_input must be a string")

    if len(player_input) < 1:
        return False

    if len(player_input) == 1:
        return player_input in wasd

    jump_sequence = player_input.split()[0]
    jump_length = len(jump_sequence)

    if jump_length != 2 and jump_length != 4:
        return False

    if not jump_sequence[0].isdigit() or not jump_sequence[1] in wasd[2:4]:
        return False

    if jump_length == 4 and (not jump_sequence[2].isdigit() or not jump_sequence[3] in wasd[:2]):
        return False

    return True
