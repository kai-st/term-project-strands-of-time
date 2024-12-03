from strands_of_time import RAINBOW_ORDER


def colourize(message: str, colour: str) -> str:
    """
    Wrap a string in ANSI escape sequences to print it in a given colour and then reset to default.

    Available colours are Red, Orange, Yellow, Green, Blue, Violet, Magenta, Pink.

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

    colour_printing_sequences["Magenta"] = "\033[38;5;126m"
    colour_printing_sequences["Pink"] = "\033[38;5;207m"

    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    if not isinstance(colour, str):
        raise TypeError("Colour must be a string")

    if colour not in colour_printing_sequences:
        raise ValueError("Colour must be Red, Orange, Yellow, Green, Blue, Violet, Magenta, "
                         "or Pink")

    return f"{colour_printing_sequences[colour]}{message}{reset_sequence}"


def demonstrate_functions(functions: list[tuple[callable, list]]):
    """
    Print a list of functions with their names and an example.

    :param functions: a list of tuples containing functions and example arguments to call them with
    :precondition: functions must be a list of tuples
    :precondition: each tuple in functions must contain a function followed by a list of example
    arguments to call it with that matches it's function annotations
    :postcondition: prints a list of functions with their names and an example
    """
    pass
