"""
Kai Steingarten
A01435070
"""
from strands_of_time.character.character import print_strands, create_character, \
    get_character_location_as_tuple, has_all_colours_strands, find_colours_with_0_strands
from strands_of_time.combat.combat import handle_regular_combat, check_for_foes, handle_boss_combat, \
    print_combat_instructions
from strands_of_time.location.board import print_current_epoch, print_map, create_game_board, \
    set_starting_location, describe_current_location, set_level_goal, check_for_restore
from strands_of_time.location.move import handle_movement
from strands_of_time.narrative import print_intro


def show_game_state(board: dict, character: dict):
    """
    Print the character's current time period, Strand counts, and the map.

    :param board: a well-formed board dictionary
    :param character: a well-formed character dictionary
    :precondition: board must be a dictionary with (X, Y) keys
    :precondition: character must be a dictionary with "X-coordinate", "Y-coordinate",
    and "Strands" keys
    :postcondition: prints character's current time period, Strand counts, and the map
    """
    print_current_epoch(board, character)
    print(" ---  Your", end=" ")
    print_strands(character)
    print()
    print_map(board, character)


def game():
    """
    Drive the game.
    """
    rows = 3
    columns = 9
    epoch_boundaries = [3, 6]
    initial_number_of_strands = 5
    board, get_random_locations = create_game_board(columns, rows, epoch_boundaries)

    print_intro()

    character = create_character(initial_number_of_strands)

    set_starting_location(board, character)

    describe_current_location(board, character)
    show_game_state(board, character)

    print_combat_instructions()
    handle_regular_combat(board, character)

    while has_all_colours_strands(character) and character["level"] <= 3:
        set_level_goal(board, character, get_random_locations)
        show_game_state(board, character)

        while has_all_colours_strands(character):
            handle_movement(board, character)
            # Tell the user where they are
            describe_current_location(board, character)
            # Tell the user their status
            show_game_state(board, character)
    #
            if board["level goal"] != get_character_location_as_tuple(character):
                there_is_a_challenger = check_for_foes()
                if there_is_a_challenger:
                    handle_regular_combat(board, character)
                    show_game_state(board, character)
                else:
                    check_for_restore(board, character)
            else:
                handle_boss_combat(character)
                break

    if character["level"] > 3:
        print("Congratulation, you win!")
    else:
        show_game_state(board, character)
        print(f"You ran out of {find_colours_with_0_strands(character)[0]} strands.", ("Spindle's "
              "glow fades and you are now trapped in time."), sep="\n\n", end="\n\n")
        print("Game Over")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
