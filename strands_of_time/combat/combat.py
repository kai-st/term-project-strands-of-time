import random
import textwrap
from copy import deepcopy

from strands_of_time import RAINBOW_ORDER
from strands_of_time.character.character import print_strands, remove_random_strand, \
    create_character, has_all_colours_strands
from strands_of_time.location.board import check_for_restore, update_distance_to_level_goal, \
    create_game_board, set_level_goal
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


def build_thread_sequence(player_sequence: list[int], enemy_sequence: list[int],
                          colour_sequence: list[str], combat_strands: dict) -> list:
    """
    
    :param player_sequence:
    :param enemy_sequence:
    :param colour_sequence:
    :param combat_strands: 
    :return: 
    """
    thread_sequence = []
    thread_options = {-1: "/", 0: "|", 1: "\\"}
    for player_number, enemy_number in zip(player_sequence, enemy_sequence):
        player_has_strand = combat_strands[RAINBOW_ORDER[player_number]] >= 1
        if player_has_strand and enemy_number == 5 and player_number == 0:
            thread_sequence.append(1)
        elif player_has_strand and enemy_number == 0 and player_number == 5:
            thread_sequence.append(-1)
        elif (player_number == -1
                or player_number - enemy_number not in thread_options
                or not player_has_strand):
            thread_sequence.append(random.choice(list(thread_options.keys())))
        else:
            thread_sequence.append(player_number - enemy_number)
            combat_strands[RAINBOW_ORDER[player_number]] -= 1

    for thread, colour in zip(thread_sequence, colour_sequence):
        print(colourize(thread_options[thread], colour), end="")
    return thread_sequence


def handle_player_response(enemy_sequence: list[int], colour_sequence: list[str],
                           combat_strands: dict) -> list:
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

    thread_sequence = build_thread_sequence(player_sequence, enemy_sequence, colour_sequence,
                                            combat_strands)
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


def build_next_enemy_sequence(prev_enemy_sequence: list,
                              thread_sequence: list[int]) -> list:
    """
    Arrange the items from a given list into a new list sorted according to a given thread sequence.

    For a thread sequence of -1's, 0's, and 1's, the items at the equivalent positions in the
    previous sequence will stay in the same position on a 0, try to move right on a -1,
    and try to move left on a 1. Items will move in running groups. One group of running 1's will
    not move past a latter group of running 1's, but will be split by any 0's.

    :param prev_enemy_sequence: a list to be sorted according to thread_sequence
    :param thread_sequence: a list of integers containing -1's, 0's, and 1's, representing whether
    items in prev_enemy_sequence should move left, stay in the same position, or move right.
    :precondition: prev_enemy_sequence is a list
    :precondition: thread_sequence is a list
    :precondition: thread_sequence contains only the integers
    :precondition: thread_sequence and enemy sequence are the same length
    :postcondition: arranges the items from prev_enemy_sequence into a new list sorted according
    to a given thread sequence
    :return: a new sorted list of the items in prev_enemy_sequence

    >>> build_next_enemy_sequence(prev_enemy_sequence=[1, 2, 3], thread_sequence=[0, 0, 0])
    [1, 2, 3]
    >>> build_next_enemy_sequence(prev_enemy_sequence=[2, 1, 3], thread_sequence=[1, -1, 0])
    [1, 2, 3]
    >>> build_next_enemy_sequence(prev_enemy_sequence=[3, 2, 1], thread_sequence=[1, 0, -1])
    [1, 2, 3]
    """
    next_enemy_sequence = []
    move_left = []
    move_right = []
    first_left = 0
    for player_thread, prev_enemy_thread in zip(thread_sequence, prev_enemy_sequence):
        if not move_left and not move_right and -1 in thread_sequence[first_left:]:
            first_left = thread_sequence.index(-1, first_left)
            while first_left < len(thread_sequence) and thread_sequence[first_left] == -1:
                move_left.append(prev_enemy_sequence[first_left])
                first_left += 1

        if player_thread == 0:
            next_enemy_sequence.append(prev_enemy_thread)
        else:
            if player_thread == 1:
                move_right.append(prev_enemy_thread)

            try:
                next_left_moving_thread = move_left.pop(0)
            except IndexError:
                try:
                    next_right_moving_thread = move_right.pop(0)
                except IndexError:
                    print(f"No thread in movement lists for player thread"
                          f" {player_thread}, enemy "
                          f"thread{prev_enemy_thread}, defaulting to treating position as 0.")
                    next_enemy_sequence.append(prev_enemy_thread)
                else:
                    next_enemy_sequence.append(next_right_moving_thread)
            else:
                next_enemy_sequence.append(next_left_moving_thread)

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
        1: 0,
        2: 2,
        3: 4,
        4: 6
    }

    combat_strands = deepcopy(character["Strands"])

    enemy_sequence = (random.sample(list(range(len(RAINBOW_ORDER))), k=len(RAINBOW_ORDER))
                      + random.choices(range(len(RAINBOW_ORDER)),
                                       k=enemy_size_by_level[character["level"]]))

    colour_sequence = print_colour_sequence(enemy_sequence, combat_strands)
    strands_knotted = False
    while not strands_knotted and has_all_colours_strands({"Strands": combat_strands}):
        thread_sequence = handle_player_response(enemy_sequence, colour_sequence, combat_strands)

        has_sequence_error = True
        while has_sequence_error:
            try:
                enemy_sequence = build_next_enemy_sequence(enemy_sequence, thread_sequence)
            except ValueError:
                thread_sequence = handle_player_response(enemy_sequence, colour_sequence,
                                                         combat_strands)
            else:
                has_sequence_error = False

        colour_sequence = print_colour_sequence(enemy_sequence, combat_strands)

        if enemy_sequence == sorted(enemy_sequence):
            return True
        else:
            strands_knotted = percentage_chance_result(10)
            if strands_knotted:
                print("Oh no! Your Strands knotted!", end="\n\n")

    remove_random_strand(character)
    return False


def handle_regular_combat(board, character):
    """

    :param board:
    :param character:
    :return:
    """
    print(colourize('"Look, a Tear!"', "magenta"), end="\n\n")
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
    print(f"You found the {level_info["to find"]}!",
          textwrap.fill(level_info["goal description"], width=100),
          textwrap.fill(f"As you approach the {level_info["to find"]}, the"
                        f" {level_info["boss"]} start to unravel the spacetime in front of you, "
                        f"opening a Tear larger than any you've seen yet. Can you mend it "
                        f"fast enough to get to the {level_info["to find"]}?", width=100),
          end="\n\n", sep="\n\n")
    character["level"] += 1
    if combat(character):
        for colour in character["Strands"]:
            character["Strands"][colour] = 5 * character["level"]
        print(f"You have driven away the {level_info["boss"]} and liberated "
              f"the {level_info["to find"]}!", textwrap.fill(level_info["success"], width=100),
              end="\n\n",
              sep="\n\n")
        if character["level"] < 4:
            new_level_info = get_level_info(character["level"])
            print(colourize(f'"Now that you have the {level_info["to find"]}, '
                            f'we should be able to track '
                            f'down the {new_level_info["to find"]}!"', "magenta"), end="\n\n")
    else:
        character["level"] -= 1
        print(textwrap.fill(f"The {level_info["boss"]} escaped to a new time and location with "
                            f"the {level_info["to find"]}. You will have to track them down again",
                            width=100),
              end="\n\n")
    character["last distance to goal"] = None


def print_combat_example():
    """
    Print an example of Time Weaving combat for the player.

    :postcondition: prints an example of Time Weaving combat for the player
    """
    example_character_strands = create_character(5)["Strands"]
    example_enemy_sequence = [2, 1, 0, 4, 5, 3]
    example_input = "426613"
    example_player_sequence = [int(digit) - 1 for digit in example_input]

    colour_sequence = print_colour_sequence(example_enemy_sequence, example_character_strands)
    print(example_input, "<-- Your play for the round")
    example_thread_sequence = build_thread_sequence(example_player_sequence,
                                                    example_enemy_sequence,
                                                    colour_sequence,
                                                    example_character_strands)
    print(" <-- How the threads are moving")
    new_enemy_sequence = build_next_enemy_sequence(example_enemy_sequence, example_thread_sequence)
    print_colour_sequence(new_enemy_sequence, example_character_strands)
    print("Tear mended!", end="\n\n")


def print_combat_instructions():
    """
    Print the instructions for Time Weaving combat for the player.

    :postcondition: prints the instructions for Time Weaving combat for the player
    """
    print(
        textwrap.fill(
            colourize('"Aha! A Tear! Whatever got the Time Weaver has definitely been here."',
                      "magenta"), width=100
        ),
        textwrap.fill("With your spacetime sight you can see what looks like a dark hole in the "
                      "fabric of reality", width=100
                      ),
        textwrap.fill(
            colourize('"You should be able to mend the Tear with your Strands, just be careful '
                      'they don\'t get knotted, or you\'ll lose one permanently until we can '
                      'find the Bobbin. If you can mend the Tear, I should be able to start '
                      'tracking it."',
                      "magenta"), width=100
        ),
        textwrap.fill(f"To mend a Tear, you need to put the tangled threads of spacetime back "
                      f"into rainbow order (Reds, Oranges, Yellows, Greens, Blues, "
                      f"Violets).", width=100
                      ),
        textwrap.fill(f"The Tear will have pattern of coloured threads "
                      f"represented "
                      f"by their first letter. You can use your Strands to pull them into order. "
                      f"Play your Strands under each of the Tear's threads by entering the "
                      f"a Strand colour's number from 1 to 6. Playing the same colour under a "
                      f"thread will keep it in the same place for the next round while playing "
                      f"the colour immediately before it in rainbow order will pull it to the "
                      f"left and playing the colour immediately after it will pull it to the "
                      f"right. Reds and Violets will pull each other towards the outsides. You "
                      f"can also play a 0 if you want to let a thread behave "
                      f"randomly. For example:", width=100
                      ),
        sep="\n\n",
        end="\n\n")
    print_combat_example()
    print(
        textwrap.fill(f"It may take a few rounds "
                      f"to get all the threads in order, but each round comes with a chance your "
                      f"Strands will become knotted, and if that happens, or you play all your "
                      f"threads of any colour, you won't be able to mend the Tear and Spindle "
                      f"won't be able to tell if you are getting closer to your goal.", width=100),
        f"Give it a try.",
        sep="\n\n",
        end="\n\n")


def main():
    """
    Drive the program
    """
    print_combat_instructions()
    chosen_level = input("Enter a level 1-3 to run a combat for, or q to quit: ")
    while chosen_level.casefold() != "q":
        level_error = True
        level = 1
        while level_error:
            try:
                level = int(chosen_level)
            except (ValueError, TypeError):
                if chosen_level == "q":
                    return
                print("level must be an integer greater than 0")
                chosen_level = input("Enter a level 1-3 to run a combat for, or q to quit: ")
            else:
                if level < 1:
                    print("level must be greater than 0")
                    chosen_level = input("Enter a level 1-3 to run a combat for, or q to quit: ")
                else:
                    level_error = False

        demo_board, get_random_locations = create_game_board(9, 3, [3, 6])
        demo_character = create_character(5 * level)
        demo_character["level"] = level
        demo_character["X-coordinate"] = 3
        demo_character["Y-coordinate"] = 0
        set_level_goal(demo_board, demo_character, get_random_locations)

        combat_type = (input("Enter r to run a regular combat, b to run a boss combat, "
                             "or q to quit: ").lower())

        while combat_type not in ["q", "r", "b"]:
            print("You may only enter r, b, or q")
            combat_type = (input("Enter r to run a regular combat, b to run a boss combat, "
                                 "or q to quit: ").lower())

        if combat_type == "q":
            return
        elif combat_type == "r":
            handle_regular_combat(demo_board, demo_character)
        elif combat_type == "b":
            handle_boss_combat(demo_character)

        chosen_level = input("enter a level 1-3 to run a combat for, or q to quit: ")


if __name__ == '__main__':
    main()
