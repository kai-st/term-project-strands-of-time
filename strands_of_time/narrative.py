import textwrap

from strands_of_time.utils import colourize, demonstrate_functions


def get_level_info(level: int) -> dict:
    """
    Provide the information to customize the narrative for a given level.

    :param level: an integer between 1 and 3 indicating the level being described
    :precondition: level is an integer from 1 to 3
    :postcondition: provides a dictionary with the information to customize the narrative for level
    :return: a dictionary for level with the keys "to find", "boss", "goal description",
    and "success"
    """
    level_info = {
        1: {
            "to find": "Bobbin",
            "boss": "moths",
            "goal description": (f"Here you see an object that looks vaguely like a dumbbell, "
                                 f"but seems to be made of the same silvery material as Spindle. "
                                 f"Between you and it, though, is a swarm of fluttering ink-black"
                                 f" shapes.{colourize('\n\n"Ugh, moths, I should have known"',
                                                      "magenta")}"),
            "success": f"You pick up the Bobbin and to your surprise, it rises into the air to "
                       f"hover over your left shoulder. It seems to resonate with your Strands. "
                       f"You now have many more than you did even at the beginning",
        },
        2: {
            "to find": "Loom",
            "boss": "moths",
            "goal description": (f"Here you see what look like nothing so much as a shiny pair of "
                                 f"vambraces.\n\n"
                                 f"{colourize('"Yes, that\'s the Loom. It\'s metaphorical."',
                                              "magenta")}\n\nAn even large swarm of moths "
                                 f"surround the Loom than were drawn to the Bobbin"),
            "success": f"You pick the Loom up and it does seem to function very much like a pair "
                       f"of vambraces. At least until you get them on. Then you see why it's "
                       f"called "
                       f"the Loom as your Strands seem to fan out in front of you, multiplied "
                       f"again into a dazzling array.",
        },
        3: {
            "to find": "Time Weaver",
            "boss": "void creature",
            "goal description": (f"Here you finally find the Time Weaver. They look remarkably "
                                 f"human, if taller and thinner than most, and dressed in "
                                 f"what "
                                 f"look like layered wrappings of braided metals. The creature "
                                 f"looming over them, however, is not human at all. It appears "
                                 f"to be made of the same dark void that the moths were, "
                                 f"but it's well over two meters tall."),
            "success": (f'The freed Time Weaver offers you a slight bow.'
                        f'\n\n{colourize('"Thank you.I\'m not sure I would have been able to '
                                         'defeat that void crawler without my Spindle. Those things'
                                         ' think spacetime is a tasty snack."', "aqua")}'
                        f'\n\nThey take Spindle from your hand and your rainbow of '
                        f'Strands fades away.\n\n'
                        f'{colourize('"Come now, I will return you to your time.\n\nUnless'
                                     ' you would rather join us? You seem to have the makings of '
                                     'a Time Weaver..."', "aqua")}'),
        },
    }
    return level_info[level]


def print_intro():
    print(
        textwrap.fill("You awaken lying on freezing cold stone surrounded by darkness so black you "
                      "could never have imagined it. You try to feel around to get a sense of "
                      "where you could possibly be, when your hand touches a smooth cylindrical "
                      "object that suddenly lights up "
                      "with a dim glow and you hear a voice in your head,", width=100),
        textwrap.fill(
            colourize('"Oh, thank god you\'re here, I don\'t even know how long-', "magenta"),
            width=100),
        textwrap.fill(
            colourize('"Wait, you\'re not a Time Weaver! How in spacetime did you get here?',
                      "magenta"), width=100),
        textwrap.fill(
            colourize('"Well, '
                      'nothing for it, I guess. I\'m Spindle. Welcome to the heat death of the '
                      'universe."', "magenta"), width=100),
        textwrap.fill("You try to take this in.", width=100),
        textwrap.fill("Spindle is made of a strange silvery material. "
                      "Maybe some sort of alien alloy? It's shape does sort of resemble a "
                      "spindle, you suppose.", width=100),
        textwrap.fill(
            colourize('"But now that you\'re here, we might just be able to get sometime else. I '
                      'don\'t know what happened to my Time Weaver, but certainly something '
                      'drastic to get me stuck out here without a source of bio-power. We have '
                      'to find them.',
                      "magenta"), width=100),
        textwrap.fill(
            colourize('"I think you\'ve got what it takes to time travel. Here, '
                      'try this."',
                      "magenta"), width=100),
        textwrap.fill("Spindle seems to do something to your brain and suddenly it\'s like you "
                      "can see another layer of reality overlaid on the physical world. All "
                      "around you, you can see the fabric of spacetime itself, and radiating out "
                      "from Spindle, strands of light in all the colours of the rainbow.",
                      width=100),
        textwrap.fill(
            colourize('"These Strands will let you travel across wide gulfs in time. I can only '
                      'provide you with a few of each colour by myself, but if we can '
                      'track down the other two '
                      'instruments my Time Weaver was carrying, they should boost your Stand '
                      'count and eventually lead us to the Time Weaver.',
                      "magenta"), width=100),
        textwrap.fill(
            colourize('"We\'ll go after '
                      'the Bobbin first. My readings say it\'s somewhere in these three time '
                      'periods. Your guess is as good as mine where to start. You\'ll be able to '
                      'make small hops '
                      'freely within each time period, but you will need to spend a Strand to '
                      'jump farther distances or between periods. Just remember you need at least '
                      'one Strand of each colour to keep me powered on."',
                      "magenta"), width=100),
        sep="\n\n",
        end="\n\n")


def main():
    """
    Drive the program.
    """
    demonstrate_functions([
        (print_intro, []),
        (get_level_info, [1]),
        (get_level_info, [2]),
        (get_level_info, [3]),
    ]
    )


if __name__ == '__main__':
    main()
