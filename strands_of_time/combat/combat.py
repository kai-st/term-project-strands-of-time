import random
from copy import deepcopy

from strands_of_time import RAINBOW_ORDER
from strands_of_time.character.character import print_strands, has_strands, remove_random_strand
from strands_of_time.utils import colourize


def percentage_chance_result(percentage: int) -> bool:
    return random.randrange(100) < percentage


def check_for_foes():
    """
    Check if the player encounters an enemy, given a 35% chance of an encounter.

    :postcondition: checks if the player encounters an enemy, given a 35% chance of an encounter.
    :return: a boolean that is True the 35% of the time

    >>> check_for_foes() # doctest: +SKIP
    True
    >>> check_for_foes() # doctest: +SKIP
    False
    """
    return percentage_chance_result(35)


def handle_player_response(enemy_sequence: list[int], colour_sequence: list[str], combat_strands:
                           dict) -> list:
    """
    
    :param enemy_sequence: 
    :param colour_sequence: 
    :param combat_strands: 
    :return: 
    """
    player_input_sequence = input()
    player_sequence = None
    has_error = True

    while has_error:
        if len(player_input_sequence) != len(enemy_sequence):
            print("Must match sequence length. Please try again.")
            player_input_sequence = input()
            continue

        try:
            player_sequence = [int(digit) - 1 for digit in player_input_sequence]
        except (ValueError, TypeError):
            print("Your sequence can only include integers from 0-6")
            player_input_sequence = input()
        else:
            if min(player_sequence) < 0 or max(player_sequence) > 6:
                print("Your sequence can only include integers from 0-6")
                player_input_sequence = input()
            else:
                has_error = False

    thread_sequence = []
    thread_options = {-1: "/", 0: "|", 1: "\\"}
    for player_number, enemy_number in zip(player_sequence, enemy_sequence):
        if (player_number == 0
                or player_number - enemy_number not in thread_options
                or combat_strands[RAINBOW_ORDER[player_number]] < 1):
            thread_sequence.append(random.choice(list(thread_options.keys())))
        else:
            thread_sequence.append(player_number - enemy_number)
            combat_strands[RAINBOW_ORDER[player_number]] -= 1

    for thread, colour in zip(thread_sequence, colour_sequence):
        print(colourize(thread_options[thread], colour), end="")
    print()
    return thread_sequence


def print_colour_sequence(enemy_sequence: list[int], combat_strands: dict) -> list[str]:
    """

    :param combat_strands:
    :param enemy_sequence:
    :return:
    """
    enemy_sequence_as_colours = [RAINBOW_ORDER[colour_number] for colour_number in enemy_sequence]
    for colour in enemy_sequence_as_colours:
        print(colourize(colour[0], colour), end="")
    print(" <-- Spacetime Threads   Available", end=" ")
    print_strands({"Strands": combat_strands})
    print()
    return enemy_sequence_as_colours


def build_next_enemy_sequence(prev_enemy_sequence, thread_sequence):
    """

    :param prev_enemy_sequence:
    :param thread_sequence:
    :return:
    """
    next_enemy_sequence = []
    move_left = []
    move_right = []
    index = 0
    while index < len(prev_enemy_sequence):
        if len(move_left) == 0 and len(move_right) == 0:
            first_left = thread_sequence.index(-1, index)
            thread_index = first_left
            while thread_index < len(thread_sequence[first_left:]):
                if thread_sequence[thread_index] != -1:
                    break
                move_left.append(prev_enemy_sequence[thread_index])
                thread_index += 1

        if thread_sequence[index] == 0:
            next_enemy_sequence.append(prev_enemy_sequence[index])
        elif thread_sequence[index] == 1:
            move_right.append(prev_enemy_sequence[index])
        if len(move_left) == 0:
            temp = move_right.pop(0)
            next_enemy_sequence.append(temp)
        else:
            temp = move_left.pop(0)
            next_enemy_sequence.append(temp)

        index += 1
    return next_enemy_sequence


def combat(character: dict) -> bool:
    """
    Drive a combat encounter and determine the outcome.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary with a "Strands" key that is a dictionary with
    number values
    :postcondition: drives a combat encounter and determines the outcome
    :return: a boolean set to true if the character won the combat
    """
    enemy_size_by_level = {
        1: 6,
        2: 10,
        3: 14,
        4: 18
    }

    combat_strands = deepcopy(character["Strands"])

    enemy_sequence = random.choices(range(len(RAINBOW_ORDER)),
                                    k=enemy_size_by_level[character["level"]])

    colour_sequence = print_colour_sequence(enemy_sequence, combat_strands)
    strands_knotted = False
    while not strands_knotted and has_strands({"Strands": combat_strands}):
        thread_sequence = handle_player_response(enemy_sequence, colour_sequence, combat_strands)
        enemy_sequence = build_next_enemy_sequence(enemy_sequence, thread_sequence)

        print_colour_sequence(enemy_sequence, combat_strands)

        if enemy_sequence == sorted(enemy_sequence):
            return True
        else:
            strands_knotted = percentage_chance_result(10)

    remove_random_strand(character)
    return False
