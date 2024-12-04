import random
import itertools
import textwrap

from strands_of_time import RAINBOW_ORDER
from strands_of_time.character.character import get_character_location_as_tuple
from strands_of_time.location import EPOCHS
from strands_of_time.utils import demonstrate_functions


def create_game_board(columns: int,
                      rows: int,
                      epoch_boundaries: list[int]) -> tuple[dict[tuple or str, dict or list[int]],
callable]:
    """
    Construct a 2D gameboard with locations laid out in a given numbers of rows and columns.

    The gameboard will be represented by a dictionary with keys of tuples representing the
    (x,y) coordinates of each location, and values containing dictionaries with descriptions for
    each location and what colour of Strand can be restored there, if any. It will also contain
    a key "epoch boundaries" with a list of column numbers before which the time period changes.

    :param columns: a positive integer greater than 2 number of columns to create
    :param rows: a positive integer greater than 1 number of rows to create
    :param epoch_boundaries: a list containing 2 positive non-zero integer column numbers before
    which the time period changes
    :precondition: columns must be an integer greater than 2
    :precondition: rows must be an integer greater than 1
    :precondition: epoch_boundaries must be a list of different ints greater than 0 and less than
    columns in incresing order
    :precondition: epoch_boundaries must have a length of 2
    :postcondition: constructs a dictionary representing a game board with rows * column number
    of locations
    :postcondition: stores each location in the dictionary with a tuple containing the location's
    coordinates as the key and dictionary as the value containing the key "description" with a
    string containing the location's description
    :postcondition: marks which locations restore Strands with a key "gives Strand" and a colour
    value
    :postcondition: stores the epoch_boundaries in a key "epoch boundaries"
    :return: a dictionary representing the gameboard with the key "epoch boundaries" with
    epoch_boundaries as a value and keys (x-coordinate, y-coordinate) for each location and
    dictionary values containing "description" keys with string values for each location and a
    "gives Stand" key with a colour string value if the location gives a stand
    :raises TypeError: if columns is not an integer
    :raises TypeError: if rows is not an integer
    :raises TypeError: if epoch_boundaries is not a list
    :raises TypeError: if epoch_boundaries contains items that are not integers
    :raises ValueError: if columns is not greater than 2
    :raises ValueError: if rows is not greater than 1
    :raises ValueError: if epoch_boundaries contains numbers less than 1
    :raises ValueError: if epoch_boundaries contains numbers not less than columns
    :raises ValueError: if epoch_boundaries is not of length 2
    :raises ValueError: if epoch_boundaries values do not increase as with index

    >>> create_game_board(3, 2, [1, 2]) # doctest: +SKIP
    ({
        (0, 0): {'description': "You're in a forest of towering conifers. Around you primitive
        mammals scurry along the ground. In the distance you can see a T-Rex stalking it's prey.",
        'gives Strand': 'Green'},
        (0, 1): {'description': "You're in a fern-choked swamp. Around you primitive mammals scurry
        along the ground. In the distance you can see enormous sauropods lumbering across the
        landscape.", 'gives Strand': 'Orange'},
        (1, 0): {'description': "You're in Medieval London. Around you a religious ceremony is
        taking place. In the distance you can see goods being hauled to the city for sale.",
        'gives Strand': 'Yellow'},
        (1, 1): {'description': "You're in Mansa Musa's Mali Empire. Around you merchants hawk
        their wears in a bustling market. In the distance you can see goods being hauled to the city
        for sale.", 'gives Strand': 'Red'},
        (2, 0): {'description': "You're in the outer ring of a space station. Around you
        incomprehensible machines hum and blink. In the distance you can see starlight glinting off
        the ice of majestic planetary rings.", 'gives Strand': 'Violet'},
        (2, 1): {'description': "You're in the passenger lounge of a starship. Around you
        incomprehensible machines hum and blink. In the distance you can see starlight glinting off
        the ice of majestic planetary rings.", 'gives Strand': 'Blue'},
        'epoch boundaries': [1, 2]
    },
    <function create_game_board.<locals>.select_random_locations at 0x000001D6CF419300>
    )
    """
    if not isinstance(columns, int):
        raise TypeError("columns must be an integer")

    if not isinstance(rows, int):
        raise TypeError("rows must be an integer")

    if not isinstance(epoch_boundaries, list):
        raise TypeError("epoch_boundaries must be an list")

    for epoch_boundary in epoch_boundaries:
        if not isinstance(epoch_boundary, int):
            raise TypeError("All items in epoch_boundaries must be integers")

    if columns < 3:
        raise ValueError("columns must be greater than 2")

    if rows < 2:
        raise ValueError("rows must be greater than 1")

    if len(epoch_boundaries) != 2:
        raise ValueError("The length of epoch_boundaries must be 2")

    if epoch_boundaries[1] <= epoch_boundaries[0]:
        raise ValueError("epoch_boundaries must different and in increasing order")

    for boundary in epoch_boundaries:
        if boundary < 1:
            raise ValueError("epoch_boundaries cannot contain numbers less than 1")
        if boundary >= columns:
            raise ValueError("epoch_boundaries cannot contain numbers equal to or greater than "
                             "the number of columns")

    coordinates = list(itertools.product(range(columns), range(rows)))

    cretaceous_locations = generate_epoch_locations(rows * epoch_boundaries[0], "cretaceous")
    medieval_locations = generate_epoch_locations(rows * (epoch_boundaries[1] -
                                                          epoch_boundaries[0]), "medieval")
    future_locations = generate_epoch_locations(rows * (columns -
                                                        epoch_boundaries[1]), "future")
    locations = itertools.chain(cretaceous_locations, medieval_locations, future_locations)

    board: dict[tuple or str, str or dict or list[int]] = dict(zip(coordinates, locations))
    board["epoch boundaries"] = epoch_boundaries


    def select_random_locations(number_of_selections: int) -> list[tuple[int, int]]:
        if number_of_selections > len(coordinates):
            raise ValueError(f"number_of_selections must be less than {len(coordinates)}")
        return random.sample(coordinates, k=number_of_selections)


    light_springs = select_random_locations(len(RAINBOW_ORDER))
    for spring_location, colour in zip(light_springs, RAINBOW_ORDER):
        board[spring_location]["gives Strand"] = colour

    return board, select_random_locations


def generate_epoch_locations(number_of_locations: int, epoch: str) -> list[dict[str, str]]:
    """
    Assemble a list of location descriptions for the given epoch.

    :param number_of_locations: a positive integer number of location descriptions to generate
    :param epoch: a string representing the time period to generate locations for
    :precondition: number_of_locations must be a positive integer greater than 0
    :precondition: epoch must be a string containing "cretaceous", "medieval", or "future"
    :postcondition: assembles a list of number_of_location location descriptions for epoch
    :return: a list of dictionaries with the key "description" and a location description as the
    value
    :raises TypeError: if number_of_locations is not an integer
    :raises TypeError: if epoch is not a string
    :raises KeyError: if epoch is not "cretaceous", "medieval", or "future"
    :raises ValueError: if number_of_locations is not greater than 0

    >>> generate_epoch_locations(1, "future") # doctest: +SKIP
    [{'description': "You're in the passenger lounge of a starship. Around you "
                     'humans and aliens alike go about their day. In the distance '
                     'you can see sleak white shuttles ferrying people between planet '
                     'and low orbit.'}]
    >>> generate_epoch_locations(3, "medieval") # doctest: +SKIP
    [{'description': "You're in Medieval London. Around you merchants hawk their "
                     'wears in a bustling market. In the distance you can see '
                     'farmers working their crops.'},
     {'description': "You're in Ming Dynasty China. Around you merchants hawk "
                     'their wears in a bustling market. In the distance you can '
                     'see buildings under-construction in the local style.'},
     {'description': "You're in the newly build Mexica city of Tenochtitlán. "
                     'Around you a religious ceremony is taking place. In the '
                     'distance you can see boats moored at a dock.'}]
    """
    location_fragments = {
        "cretaceous": {
            "places": [
                "a sprawling grassland",
                "a lush tropical forest",
                "a forest of towering conifers",
                "a fern-choked swamp",
            ],
            "near sights": [
                "early birds glide through the air",
                "primitive mammals scurry along the ground",
                "some of the first flowering plants are blooming",
            ],
            "far sights": [
                "a T-Rex stalking it's prey",
                "a herd of triceratops grazing contentedly",
                "enormous sauropods lumbering across the landscape",
                "velociraptors sprinting after small creatures",
            ]
        },
        "medieval": {
            "places": [
                "Ming Dynasty China",
                "Medieval London",
                "Mansa Musa's Mali Empire",
                "the newly build Mexica city of Tenochtitlán"
            ],
            "near sights": [
                "merchants hawk their wears in a bustling market",
                "craftspeople fashion the necessities of daily life",
                "a religious ceremony is taking place",
                "elites mingle and show off their finery",
            ],
            "far sights": [
                "farmers working their crops",
                "buildings under-construction in the local style",
                "boats moored at a dock",
                "goods being hauled to the city for sale",
            ],
        },
        "future": {
            "places": [
                "the passenger lounge of a starship",
                "a city out of a sci-fi novel",
                "the outer ring of a space station",
            ],
            "near sights": [
                "humans and aliens alike go about their day",
                "incomprehensible machines hum and blink",
                "swarms of small robots take care of menial tasks",
                "androids chat about a sport you've never heard of"
            ],
            "far sights": [
                "the twin suns of an alien planetary system",
                "sleek white shuttles ferrying people between planet and low orbit",
                "starlight glinting off the ice of majestic planetary rings",
            ],
        },
    }

    if not isinstance(number_of_locations, int):
        raise TypeError("number_of_locations must be an integer")

    if not isinstance(epoch, str):
        raise TypeError("epoch must be an string")

    if number_of_locations < 1:
        raise ValueError("number_of_locations must be greater than 0")

    if epoch not in location_fragments:
        raise ValueError('epoch must be "cretaceous", "medieval", or "future"')

    location_descriptions = []
    for _ in range(number_of_locations):
        place = random.choice(location_fragments[epoch]["places"])
        nearby = random.choice(location_fragments[epoch]["near sights"])
        distance_view = random.choice(location_fragments[epoch]["far sights"])
        location_descriptions.append({"description": f"You're in {place}. Around you {nearby}. In "
                                                     f"the distance you can see {distance_view}."})

    return location_descriptions


def print_current_epoch(board: dict, character: dict):
    """
    Print the character's current time period.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with an "epoch boundaries" key
    :precondition: character must be a dictionary with an "X-coordinate" key
    :postcondition: prints the character's current time period
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if board does not have an "epoch boundaries" key
    :raises KeyError: if character does not have an "X-coordinate" key

    >>> print_current_epoch(board={"epoch boundaries": [3, 6]}, character={"X-coordinate": 0})
    ... # doctest: +NORMALIZE_WHITESPACE
    Time Period: The Cretaceous Era
    >>> print_current_epoch(board={"epoch boundaries": [2, 4]}, character={"X-coordinate": 2})
    ... # doctest: +NORMALIZE_WHITESPACE
    Time Period: The 14th Century, A.D.
    >>> print_current_epoch(board={"epoch boundaries": [1, 4]}, character={"X-coordinate": 6})
    ... # doctest: +NORMALIZE_WHITESPACE
    Time Period: The 26th Century, A.D.
    """
    if not isinstance(board, dict):
        raise TypeError("board must be a dictionary")

    if not isinstance(character, dict):
        raise TypeError("character must be a dictionary")

    if "epoch boundaries" not in board:
        raise KeyError('board must have an "epoch boundaries" key')

    if "X-coordinate" not in character:
        raise KeyError('character must have an "X-coordinate" key')

    time_period = EPOCHS[0]

    if character["X-coordinate"] >= board["epoch boundaries"][0]:
        time_period = EPOCHS[1]

    if character["X-coordinate"] >= board["epoch boundaries"][1]:
        time_period = EPOCHS[2]

    print(f"Time Period: {time_period}", end=" ")


def describe_current_location(board, character):
    """
    Print the description of the character's current location.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys with dictionary values that
    include "description" keys
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: prints the description of the character's current location.
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if board does not have tuple keys
    :raises KeyError: if board locations do not have "description keys
    :raises KeyError: if character does not have an "X-coordinate" key
    :raises KeyError: if character does not have an "Y-coordinate" key
    """
    if not isinstance(board, dict):
        raise TypeError("board must be a dictionary")

    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "X-coordinate" not in character:
        raise KeyError("character must have 'X-coordinate' key")

    if "Y-coordinate" not in character:
        raise KeyError("character must have 'Y-coordinate' key")

    tuple_keys = [key for key in board if isinstance(key, tuple)]
    if len(tuple_keys) < 1:
        raise KeyError("board must have tuple keys")

    for key in tuple_keys:
        if "description" not in board[key]:
            raise KeyError('board locations must have "description" keys')

    current_location = get_character_location_as_tuple(character)

    print(textwrap.fill(board[current_location]["description"]), end="\n\n")


def set_starting_location(board: dict, character: dict):
    """
    Set the character's location to a starting location in the player's chosen epoch.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with an "epoch boundaries" key
    :precondition: character must be a dictionary with "X-coordinate" and "Y-coordinate" keys
    :postcondition: sets the character's location to a starting location in the player's chosen
    epoch
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if board does not have an "epoch boundaries" key
    :raises KeyError: if character does not have an "X-coordinate" key
    :raises KeyError: if character does not have an "Y-coordinate" key
    """
    if not isinstance(board, dict):
        raise TypeError("board must be a dictionary")

    if not isinstance(character, dict):
        raise TypeError("character must be an dictionary")

    if "X-coordinate" not in character:
        raise KeyError("character must have 'X-coordinate' key")

    if "Y-coordinate" not in character:
        raise KeyError("character must have 'Y-coordinate' key")

    if "epoch boundaries" not in board:
        raise KeyError('board must have an "epoch boundaries" key')


    def get_player_starting_epoch():
        epoch_menu = ""
        for number, epoch in enumerate(EPOCHS, 1):
            epoch_menu += f" {number}. {epoch}"
            if number != len(EPOCHS):
                epoch_menu += ","

        player_epoch = input(f"Enter the time period you would like to start in:{epoch_menu}\n")

        has_error = True
        while has_error or player_epoch not in [1, 2, 3]:
            try:
                player_epoch = int(player_epoch)
            except TypeError:
                print("Entry must be 1, 2, or 3. Please try again.")
                player_epoch = input(
                    f"Enter the time period you would like to start in:{epoch_menu}\n")
            else:
                has_error = False

        return player_epoch


    player_starting_epoch = get_player_starting_epoch()

    locations = [key for key in board if isinstance(key, tuple)]

    if player_starting_epoch == 1:
        locations_in_epoch_1 = filter(lambda location: location[0] < board["epoch boundaries"][0],
                                      locations)

        starting_location = random.choice(list(locations_in_epoch_1))

    elif player_starting_epoch == 2:
        locations_in_epoch_2 = filter(lambda location: board["epoch boundaries"][0] <= location[0]
                                      < board["epoch boundaries"][1], locations)

        starting_location = random.choice(list(locations_in_epoch_2))

    else:
        locations_in_epoch_3 = filter(lambda location: location[0] >= board["epoch boundaries"][1],
                                      locations)

        starting_location = random.choice(list(locations_in_epoch_3))

    character["X-coordinate"] = starting_location[0]
    character["Y-coordinate"] = starting_location[1]


def main():
    """
    Drive the program.
    """
    demo_board, _ = create_game_board(3, 2, [1, 2])
    demo_character_coordinates = {"X-coordinate": 2, "Y-coordinate": 1}

    functions_to_demo = [
        (create_game_board, [3, 2, [1, 2]]),
        (generate_epoch_locations, [3, "medieval"]),
        (describe_current_location, [demo_board, demo_character_coordinates]),
        (set_starting_location, [demo_board, demo_character_coordinates]),
    ]

    demonstrate_functions(functions_to_demo)
    print(demo_character_coordinates)


if __name__ == '__main__':
    main()
