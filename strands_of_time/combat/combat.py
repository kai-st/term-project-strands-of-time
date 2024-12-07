import random
import textwrap
from copy import deepcopy

from strands_of_time import RAINBOW_ORDER
from strands_of_time.character.character import print_strands, has_strands, remove_random_strand, \
    create_character
from strands_of_time.location.board import check_for_restore, update_distance_to_level_goal, \
    create_game_board
from strands_of_time.narrative import get_level_info
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
            if min(player_sequence) < -1 or max(player_sequence) > 5:
                print("Your sequence can only include integers from 0-6")
                player_input_sequence = input()
            else:
                has_error = False

    thread_sequence = []
    thread_options = {-1: "/", 0: "|", 1: "\\"}
    for player_number, enemy_number in zip(player_sequence, enemy_sequence):
        if (player_number == -1
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
    first_left = 0
    while index < len(prev_enemy_sequence):
        if len(move_left) == 0 and len(move_right) == 0 and -1 in thread_sequence[first_left:]:
            first_left = thread_sequence.index(-1, index)
            while first_left < len(thread_sequence):
                if thread_sequence[first_left] != -1:
                    break
                move_left.append(prev_enemy_sequence[first_left])
                first_left += 1

        if thread_sequence[index] == 0:
            next_enemy_sequence.append(prev_enemy_sequence[index])
        elif thread_sequence[index] == 1:
            move_right.append(prev_enemy_sequence[index])
        if thread_sequence[index] != 0:
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

        colour_sequence = print_colour_sequence(enemy_sequence, combat_strands)

        if enemy_sequence == sorted(enemy_sequence):
            return True
        else:
            strands_knotted = percentage_chance_result(10)
            if strands_knotted:
                print("Oh no! Your Strands knotted!")

    remove_random_strand(character)
    return False


def handle_regular_combat(board, character):
    """

    :param board:
    :param character:
    :return:
    """
    if combat(character):
        print("You have successfully mended the fabric of spacetime!", end="\n\n")
        update_distance_to_level_goal(board, character)
        check_for_restore(board, character)

    else:
        print("You were unable to mend the fabric of spacetime.", end="\n\n")


def handle_boss_combat(character):
    """

    :param character:
    :return:
    """
    level_info = get_level_info(character["level"])
    print(textwrap.fill(level_info["goal description"]), textwrap.fill(f"As you approach the"
                                                      f" {level_info["to find"]}, the"
                                           f" {level_info["boss"]} start to "
                                           f"unravel the spacetime in "
                                           f"front of you, "
                                           f"opening a hole "
                                           f"larger than any you've seen yet. Can you mend it "
                                           f"fast enough to get to the"
                                           f"{level_info["to find"]}?"), end="\n\n", sep="\n\n")
    character["level"] += 1
    if combat(character):
        for colour in character["Strands"]:
            character["Strands"][colour] = 5 * character["level"]
        print(f"You have driven away the {level_info["boss"]} and liberated "
              f"the {level_info["to find"]}.", textwrap.fill(level_info["success"]), end="\n\n",
                                                                                      sep="\n\n" )
        if character["level"] < 4:
            new_level_info = get_level_info(character["level"])
            print(colourize(f"Now that you have the {level_info["to find"]}, "
                            f"we should be able to track "
                  f"down the {new_level_info["goal"]}.", "magenta"), end="\n\n")
    else:
        character["level"] -= 1
        print(f"The {level_info["boss"]} escaped to a new time and location with "
              f"the {level_info["to find"]}. You will have to track them down again", end="\n\n")
    character["last distance to goal"] = None


def main():
    """
    Drive the program
    """
    demo_board, _ = create_game_board(9, 3, [3, 6])
    demo_character = create_character(3)
    demo_character["X-coordinate"] = 3
    demo_character["Y-coordinate"] = 0

    handle_regular_combat(demo_board, demo_character)


if __name__ == '__main__':
    main()
