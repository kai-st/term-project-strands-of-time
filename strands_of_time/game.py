"""
Kai Steingarten
A01435070
"""
from strands_of_time import RAINBOW_ORDER
from strands_of_time.character.character import print_strands, create_character
from strands_of_time.location.board import prep_current_location_for_printing


def colourize(message: str, colour: str) -> str:
    """
    Wrap a string in ANSI escape sequences to print it in a given colour and then reset to default.

    Available colours are Red, Orange, Yellow, Green, Blue, Violet, Pink.

    :param message: a string to wrap in color sequences
    :param colour: the colour to make the message as a string matching an available colour
    :precondition: message must be a string
    :precondition: colour must be a string
    :precondition: colour must be aan available colour
    :postcondition: wraps a string in ANSI escape sequences to print it in colour and then
    reset the colour
    :return: a string beginning with the colour escape sequence, then the message, then the
    reset escape sequence
    :raises TypeError: if message is not a string
    :raises TypeError: if colour is not a string
    :raises ValueError: if colour does not match an available colour

    >>> colourize("My message", "Red") # doctest: +SKIP
    '\033[38;5;160mMy message\033[0m'
    >>> print(colourize("My red message", "Red"))
    \033[38;5;160mMy red message\033[0m
    >>> print(colourize("My pink message", "Pink"))
    \033[38;5;207mMy pink message\033[0m
    """
    reset_sequence = "\033[0m"
    rainbow_printing_sequences = ("\033[38;5;160m", "\033[38;5;208m", "\033[38;5;220m",
                                  "\033[38;5;41m", "\033[38;5;33m", "\033[38;5;135m")

    colour_printing_sequences = {rainbow_colour: rainbow_sequence for rainbow_colour,
                                 rainbow_sequence in zip(RAINBOW_ORDER, rainbow_printing_sequences)}

    colour_printing_sequences["Pink"] = "\033[38;5;207m"

    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    if not isinstance(colour, str):
        raise TypeError("Colour must be a string")

    if colour not in colour_printing_sequences:
        raise TypeError("Colour must be Red, Orange, Yellow, Green, Blue, Violet, or Pink")

    return f"{colour_printing_sequences[colour]}{message}{reset_sequence}"


def show_game_state(board, character):
    """
    Print the character's current HP, current location, and goal location.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate", "Y-coordinate",
    and "Current HP" keys
    :postcondition: prints the character's current HP, current location, and goal location

    >>> new_character = create_character()
    >>> board_5_by_5 = create_game_board(5, 5)
    >>> show_game_state(board_5_by_5, new_character)
    <BLANKLINE>
    --- Current HP: 5 --- Current location: Row 1, Column 1 --- Goal: Row 5, Column 5 ---
    <BLANKLINE>
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> board_5_rows_4_cols = create_game_board(5, 4)
    >>> show_game_state(board_5_rows_4_cols, mid_game_character)
    <BLANKLINE>
    --- Current HP: 3 --- Current location: Row 4, Column 3 --- Goal: Row 5, Column 4 ---
    <BLANKLINE>
    """
    print_strands(character)

    location_to_print = prep_current_location_for_printing(character)

    # goal_to_print = prep_goal_for_printing(board)

    # print("\n---", hp_to_print, "---", location_to_print, "---", goal_to_print, "---", end="\n\n")


def game():
    """
    Drive the game.
    """
    rows = 3
    columns = 9
    epoch_boundaries = [3, 6]
    initial_number_of_strands = 3
    # board = create_game_board(rows, columns, epoch_boundaries)
    #
    # print_intro()
    #
    character = create_character(initial_number_of_strands)
    #
    # set_starting_location(board, character)
    #
    # describe_current_location(board, character)
    # show_game_state(board, character)
    #
    # print_combat_instructions()
    # handle_regular_combat(board, character)
    #
    # while has_strands(character) and character["level"] <= 3:
    #     set_level_goal(board, character)
    #
    #     while has_strands(character):
    #         handle_movement(board, character)
    #         # Tell the user where they are
    #         describe_current_location(board, character)
    #         # Tell the user their status
    #         show_game_state(board, character)
    #
    #         if board["level goal"] != get_character_location_as_tuple(character):
    #             there_is_a_challenger = check_for_foes()
    #             if there_is_a_challenger:
    #                 handle_regular_combat(board, character)
    #
    #             check_for_restore(board, character)
    #         else:
    #             describe_level_goal(character)
    #             handle_boss_combat(board, character)
    #             break
    #
    # if character["level"] > 3:
    #     print("winning scenario")
    # else:
    #     show_game_state(board, character)
    #     print("losing scenario")
    #     print("Game Over")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
