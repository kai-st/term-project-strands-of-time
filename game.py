"""
Kai Steingarten
A01435070
"""

import random
import copy


def make_board(rows, columns):
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

    >>> make_board(2, 2) # doctest: +SKIP
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
    >>> make_board(1, 1) # doctest: +SKIP
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


def make_character():
    """
    Create a character with an initial state of 5 hp, positioned at x-coordinate 0, y-coordinate 0.

    :postcondition: creates a character dictionary with the key-value pairs "X-coordinate": 0,
    "Y-coordinate": 0, "Current HP": 5
    :return: a character dictionary with the key-value pairs "X-coordinate": 0,
    "Y-coordinate": 0, "Current HP": 5

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}


def is_alive(character):
    """
    Determine if the character is still alive.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: determines as a Boolean if character is alive based on if
    character["Current HP"] is greater than 0
    :return: a boolean that is True if character["Current HP"] is greater than 0

    >>> alive_character = make_character()
    >>> is_alive(alive_character)
    True
    >>> dead_character = make_character()
    >>> dead_character["Current HP"] = 0
    >>> is_alive(dead_character)
    False
    """
    return character["Current HP"] > 0


def get_character_location_as_tuple(character):
    """
    Return the character's location as a tuple of (X, Y) coordinates.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: returns character's location as a tuple of (X, Y) coordinates
    :return: a tuple with the character's location as (X, Y) coordinates

    >>> character_at_initial_position = make_character()
    >>> get_character_location_as_tuple(character_at_initial_position)
    (0, 0)
    >>> character_x_3_y_2 = make_character()
    >>> character_x_3_y_2["X-coordinate"] = 3
    >>> character_x_3_y_2["Y-coordinate"] = 2
    >>> get_character_location_as_tuple(character_x_3_y_2)
    (3, 2)
    """
    return character["X-coordinate"], character["Y-coordinate"]


def get_goal_location(board):
    """
    Return the goal location for the board as a tuple of (X, Y) coordinates.

    :param board: a well-formed board dictionary
    :precondition: board must be a dictionary with (X, Y) coordinate keys
    :postcondition: returns the goal location for board as a tuple of (X, Y) coordinates
    :return: a tuple with the goal location as (X, Y) coordinates

    >>> board_5_by_5 = make_board(5, 5)
    >>> get_goal_location(board_5_by_5)
    (4, 4)
    >>> board_not_square = make_board(3, 4)
    >>> get_goal_location(board_not_square)
    (3, 2)
    >>> smallest_board = make_board(1, 1)
    >>> get_goal_location(smallest_board)
    (0, 0)
    """
    max_x_coordinate = max(key[0] for key in board.keys())
    max_y_coordinate = max(key[1] for key in board.keys())

    return max_x_coordinate, max_y_coordinate


def prep_current_hp_for_printing(character):
    """
    Return the character's current HP with a label as a string for printing.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: returns character's current HP with label as a string
    :return: character's current HP with label a string

    >>> new_character = make_character()
    >>> prep_current_hp_for_printing(new_character)
    'Current HP: 5'
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> prep_current_hp_for_printing(mid_game_character)
    'Current HP: 3'
    """
    return f"Current HP: {character["Current HP"]}"


def prep_current_location_for_printing(character):
    """
    Return the character's current location with a label as a string for printing.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: returns character's current location with label as a string
    :return: character's current location with label as a string

    >>> new_character = make_character()
    >>> prep_current_location_for_printing(new_character)
    'Current location: Row 1, Column 1'
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> prep_current_location_for_printing(mid_game_character)
    'Current location: Row 4, Column 3'
    """
    current_row = character["Y-coordinate"] + 1
    current_col = character["X-coordinate"] + 1
    return f"Current location: Row {current_row}, Column {current_col}"


def prep_goal_for_printing(board):
    """
    Return the goal location with a label as a string for printing.

    :param board: a well-formed board dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :postcondition: returns the goal location for board with label as a string
    :return: board's goal location with label as a string

    >>> board_5_by_5 = make_board(5, 5)
    >>> prep_goal_for_printing(board_5_by_5)
    'Goal: Row 5, Column 5'
    >>> board_5_rows_4_cols = make_board(5, 4)
    >>> prep_goal_for_printing(board_5_rows_4_cols)
    'Goal: Row 5, Column 4'
    """
    goal = get_goal_location(board)
    goal_row = goal[1] + 1
    goal_col = goal[0] + 1
    return f"Goal: Row {goal_row}, Column {goal_col}"


def display_game_state(board, character):
    """
    Print the character's current HP, current location, and goal location.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate", "Y-coordinate",
    and "Current HP" keys
    :postcondition: prints the character's current HP, current location, and goal location

    >>> new_character = make_character()
    >>> board_5_by_5 = make_board(5, 5)
    >>> display_game_state(board_5_by_5, new_character)
    <BLANKLINE>
    --- Current HP: 5 --- Current location: Row 1, Column 1 --- Goal: Row 5, Column 5 ---
    <BLANKLINE>
    >>> mid_game_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 3}
    >>> board_5_rows_4_cols = make_board(5, 4)
    >>> display_game_state(board_5_rows_4_cols, mid_game_character)
    <BLANKLINE>
    --- Current HP: 3 --- Current location: Row 4, Column 3 --- Goal: Row 5, Column 4 ---
    <BLANKLINE>
    """
    hp_to_print = prep_current_hp_for_printing(character)

    location_to_print = prep_current_location_for_printing(character)

    goal_to_print = prep_goal_for_printing(board)

    print("\n---", hp_to_print, "---", location_to_print, "---", goal_to_print, "---", end="\n\n")


def describe_current_location(board, character):
    """
    Print the description of the character's current location.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate", "Y-coordinate",
    and "Current HP" keys
    :postcondition: prints the description of the character's current location.

    >>> new_character = make_character()
    >>> board_5_by_5 = make_board(5, 5)
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


def get_user_choice():
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

    >>> new_character = make_character()
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

    >>> character_at_x_0_y_0 = make_character()
    >>> board_5_by_5 = make_board(5, 5)
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


def check_for_foes():
    """
    Check if the player encounters an enemy, given a 25% chance of an encounter.

    :postcondition: checks if the player encounters an enemy, given a 25% chance of an encounter.
    :return: a boolean that is True the 25% of the time

    >>> check_for_foes() # doctest: +SKIP
    True
    >>> check_for_foes() # doctest: +SKIP
    False
    """
    return random.randint(1, 4) == 4


def pick_type_of_foe():
    """
    Pick a random enemy type from a list of Underdark species.

    :postcondition: returns a random enemy type from a list of Underdark species
    :return: a random enemy type from a list of Underdark species as a string

    >>> pick_type_of_foe() # doctest: +SKIP
    "giant spider"
    >>> pick_type_of_foe() # doctest: +SKIP
    "mind flayer"
    """
    underdark_enemies = ["giant spider", "drow", "drider", "duergar", "mind flayer",
                         "intellect devourer", "myconid", "gelationous cube", "beholder",
                         "swarm of cranium rats", "kuo-toa", "carrion crawler", "troll",
                         "swarm of bats"]

    return random.choice(underdark_enemies)


def damage_character(character):
    """
    Reduce the current HP of the character by 1.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: reduces the value of character["Current HP"] by 1

    >>> new_character = make_character()
    >>> damage_character(new_character)
    >>> new_character
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4}
    >>> dying_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 1}
    >>> damage_character(dying_character)
    >>> dying_character
    {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 0}
    """
    character["Current HP"] -= 1


def guessing_game(character):
    """
    Ask the player to correctly guess a random number from 1 to 5 to defeat a foe, or take damage.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Current HP" key
    :postcondition: tells the player they have encountered a foe
    :postcondition: picks a random number from 1 to 5 inclusive
    :postcondition: asks the player to guess the number
    :postcondition: if player guesses correctly, prints success message
    :postcondition: if player guesses incorrectly, prints failure message
    :postcondition: if player guesses incorrectly, damages character
    """
    foe = pick_type_of_foe()
    vowels = ("a", "e", "i", "o", "u")
    indefinite_article = "An" if foe[0] in vowels else "A"
    print(indefinite_article, foe, "blocks your path!", end="\n\n")

    number = random.randint(1, 5)

    player_guess = int(input(f"Guess a number between 1 and 5 to defeat the {foe}: "))

    if player_guess == number:
        print("\nSuccess! You have slain the %s!" % foe, end="\n\n")
    else:
        print("\nOh no! You take 1 point of damage from the %s!" % foe, end="\n\n")
        damage_character(character)


def check_if_goal_attained(board, character):
    """
    Check if the character has reached the goal.

    :param board: A well-formed board dictionary
    :param character: A well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: checks if the character's location equals the goal location
    :return: a boolean that is True if character's location equals the goal location

    >>> end_game_character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 3}
    >>> board_5_by_5 = make_board(5, 5)
    >>> check_if_goal_attained(board_5_by_5, end_game_character)
    True
    >>> new_character = make_character()
    >>> check_if_goal_attained(board_5_by_5, new_character)
    False
    >>> new_character = make_character()
    >>> board_1_by_1 = make_board(1, 1)
    >>> check_if_goal_attained(board_1_by_1, new_character)
    True
    """
    goal_location = get_goal_location(board)
    character_location = get_character_location_as_tuple(character)

    return character_location == goal_location


def game():
    """
    Drive the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)

    character = make_character()

    achieved_goal = False

    while is_alive(character) and not achieved_goal:
        # Tell the user their status
        display_game_state(board, character)

        # Tell the user where they are
        describe_current_location(board, character)

        direction = get_user_choice()

        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)

            display_game_state(board, character)
            describe_current_location(board, character)

            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)

            achieved_goal = check_if_goal_attained(board, character)
        else:
            # Tell the user they can’t go in that direction
            print("\nThere is only the cold stone wall to the %s." % direction, end="\n\n")

    if is_alive(character):
        print("You reach the cave mouth and stagger out into the bright morning light.", end="\n\n")
        print("Congratulations! You escaped the Underdark!")
    else:
        display_game_state(board, character)
        print("The gods were not kind this day. You died before you could escape the Underdark.",
              end="\n\n")
        print("Game Over")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
