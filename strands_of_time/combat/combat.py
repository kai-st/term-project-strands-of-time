import random


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
    return random.randrange(100) < 35
