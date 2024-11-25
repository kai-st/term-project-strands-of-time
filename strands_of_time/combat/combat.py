import random


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
