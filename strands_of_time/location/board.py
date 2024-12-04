import random
import itertools

from strands_of_time import RAINBOW_ORDER
from strands_of_time.character.character import get_character_location_as_tuple, create_character
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

    :param columns: a positive non-zero integer number of columns to create
    :param rows: a positive non-zero integer number of rows to create
    :param epoch_boundaries: a list containing 2 positive non-zero integer column numbers before
    which the time period changes
    :precondition: rows must be an integer greater than 0
    :precondition: columns must be an integer greater than 0
    :precondition: epoch_boundaries must be a list of ints greater than 0 and less than columns
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
    :raises ValueError: if columns is not greater than 0
    :raises ValueError: if rows is not greater than 0
    :raises ValueError: if epoch_boundaries contains numbers less than 1
    :raises ValueError: if epoch_boundaries contains numbers not less than columns
    :raises ValueError: if epoch_boundaries is not of length 2

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
    if not isinstance(columns, int):
        raise TypeError("columns must be an integer")

    if not isinstance(rows, int):
        raise TypeError("rows must be an integer")

    if not isinstance(epoch_boundaries, list):
        raise TypeError("epoch_boundaries must be an list")

    for epoch_boundary in epoch_boundaries:
        if not isinstance(epoch_boundary, int):
            raise TypeError("All items in epoch_boundaries must be integers")

    if columns < 1:
        raise ValueError("columns must be greater than 0")

    if rows < 1:
        raise ValueError("rows must be greater than 0")

    if len(epoch_boundaries) != 2:
        raise ValueError("The length of epoch_boundaries must be 2")

    for boundary in epoch_boundaries:
        if boundary < 1:
            raise ValueError("epoch_boundaries cannot contain numbers less than 1")
        if boundary >= columns:
            raise ValueError("epoch_boundaries cannot contain numbers equal to or greater than "
                             "the number of columns")

    coordinates = itertools.product(range(columns), range(rows))

    cretaceous_locations = generate_epoch_locations(columns * epoch_boundaries[0], "cretaceous")
    medieval_locations = generate_epoch_locations(columns * (epoch_boundaries[1] -
                                                             epoch_boundaries[0]), "medieval")
    future_locations = generate_epoch_locations(columns * (columns -
                                                           epoch_boundaries[1]), "future")
    locations = itertools.chain(cretaceous_locations, medieval_locations, future_locations)

    board: dict[tuple or str, str or dict or list[int]] = dict(zip(coordinates, locations))
    board["epoch boundaries"] = epoch_boundaries


    def select_random_locations(number_of_selections: int) -> list[tuple[int, int]]:
        return random.sample(list(coordinates), k=number_of_selections)


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
    """
    location_fragments = {
        "cretaceous": {
            "places": [
                "a sprawling grassland",
                "a lush tropical forest",
                "a forest of towering conifers",
                "a fern-choked swamp"
            ],
            "near sights": [
                "early birds glide through the air",
                "primitive mammals scurry along the ground",
                "some of the first flowering plants are blooming"
            ],
            "far sights": [
                "a T-Rex stalking it's prey",
                "a herd of triceratops grazing contentedly",
                "enormous sauropods lumbering across the landscape",
                "velociraptors sprinting after small creatures"
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
                "a religious ceremony is taking place"
                "elites mingle and show off their finery"
            ],
            "far sights": [
                "farmers working their crops",
                "buildings under-construction in the local style",
                "boats moored at a dock",
                "goods being hauled to the city for sale"
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
                "flying shuttles ferrying people between planet and low orbit",
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


def main():
    """
    Drive the program.
    """
    # strands_demo_character = {
    #     'Strands': {
    #         'Blue': 2,
    #         'Green': 2,
    #         'Orange': 2,
    #         'Red': 2,
    #         'Violet': 2,
    #         'Yellow': 2
    #     }}

    functions_to_demo = [
        (create_game_board, [9, 3, [3, 6]]),
    ]

    demonstrate_functions(functions_to_demo)


if __name__ == '__main__':
    main()
