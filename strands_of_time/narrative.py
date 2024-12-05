from strands_of_time.utils import colourize


def get_level_info(level: int) -> dict:
    """

    :param level:
    :return:
    """
    level_info = {
        1: {
            "to find": "the Bobbin",
            "boss": "moths",
            "goal description": (f"Here you see an object that looks vaguely like a dumbbell, "
                                 f"but seems to be made of the same silvery material as Spindle. "
                                 f"Between you and it, though, is a swarm of fluttering ink-black"
                                 f" shapes.\n\n"
                                 f"{colourize('"Ugh, moths, I should have known"', "magenta)}")}"),
            "success": f"You pick up the Bobbin and to your surprise, it rises into the air to "
                       f"hover over your left shoulder. It seems to resonate with your threads. "
                       f"You now have many more than you did even at the beginning",
            },
        2: {
            "to find": "the Loom",
            "boss": "moths",
            "goal description": (f"Here you see what look like nothing so much as a pair of "
                                 f"shiny bracers.\n\n"
                                 f"{colourize('"Yes, that\'s the Loom. It\'s metaphorical."', 
                                              "magenta)}")}\n\nAn even large swarm of moths "
                                 f"surround the Loom than were drawn to the Bobbin"),
            "success": f"You pick the Loom up and it does seem to function very much like a pair "
                       f"of bracers. At least until you get them on. Then you see why it's called "
                       f"the Loom as your Strands seem to fan out in front of you, multiplied "
                       f"again into a dazzling array.",
            },
        3: {
            "to find": "the Time Weaver",
            "boss": "void creature",
            "goal description": (f"Here you finally find the Time Weaver. They look remarkably "
                                 f"human, if taller and thinner than most, and dressed in what "
                                 f"look like layered wrappings of braided metals. The creature "
                                 f"looming over them, however, is not human at all. It appears "
                                 f"to be made of the same dark void that the moths were, "
                                 f"but it's well over two meters tall\n\n"
                                 f"{colourize('"Ugh, moths, I should have known"', "magenta)}")}"),
            "success": (f"The freed Time Weaver offers you a slight bow.\n\n{
            colourize(
                'Thank you.I\'m not sure I would have been able to defeat that void crawler '
                'without my Spindle. Those things think spacetime is a tasty snack.', "aqua")}"
                        f"\n\nThey take Spindle from your hand and your rainbow of "
                        f"Strands fades away.\n\n"
                        f"{colourize('Come now, I will return you to your time.\n\nUnless'
                                     ' you would rather join us? You seem to have the makings of '
                                     'a Time Weaver...', "aqua")}"),
            },
    }
    return level_info[level]


def main():
    """
    Draive the program.
    """
    pass


if __name__ == '__main__':
    main()
