import textwrap

from strands_of_time.utils import colourize


def get_level_info(level: int) -> dict:
    """

    :param level:
    :return:
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
            "goal description": (f"Here you see what look like nothing so much as a pair of "
                                 f"shiny bracers.\n\n"
                                 f"{colourize('"Yes, that\'s the Loom. It\'s metaphorical."',
                                              "magenta")}\n\nAn even large swarm of moths "
                                 f"surround the Loom than were drawn to the Bobbin"),
            "success": f"You pick the Loom up and it does seem to function very much like a pair "
                       f"of bracers. At least until you get them on. Then you see why it's called "
                       f"the Loom as your Strands seem to fan out in front of you, multiplied "
                       f"again into a dazzling array.",
        },
        3: {
            "to find": "Time Weaver",
            "boss": "void creature",
            "goal description": (f"Here you finally find the Time Weaver. They look remarkably "
                                 f"human, if taller and thinner than most, and dressed in what "
                                 f"look like layered wrappings of braided metals. The creature "
                                 f"looming over them, however, is not human at all. It appears "
                                 f"to be made of the same dark void that the moths were, "
                                 f"but it's well over two meters tall."),
            "success": (f"The freed Time Weaver offers you a slight bow."
                        f"\n\n{colourize('Thank you.I\'m not sure I would have been able to '
                                         'defeat that void crawler without my Spindle. Those things'
                                         ' think spacetime is a tasty snack.', "aqua")}"
                        f"\n\nThey take Spindle from your hand and your rainbow of "
                        f"Strands fades away.\n\n"
                        f"{colourize('Come now, I will return you to your time.\n\nUnless'
                                     ' you would rather join us? You seem to have the makings of '
                                     'a Time Weaver...', "aqua")}"),
        },
    }
    return level_info[level]


def print_intro():
    print(
        textwrap.fill("You awaken lying on freezing cold stone surrounded by darkness so black you "
                      "could never have imagined it. You try to feel around to get a sense of "
                      "where you could possibly be when your hand touches smooth cylindrical "
                      "object which suddenly lights up "
                      "with a dim glow and you hear a voice in your head,", width=100),
        textwrap.fill(
            colourize('"Oh, thank god you\'re here, I don\'t even know how long-\n\nWait, '
                      'you\'re not a Time Weaver! How in spacetime did you get here?\n\nWell, '
                      'nothing for it, I guess. I\'m Spindle. Welcome to the heat death of the '
                      'universe."', "magenta"), width=100),
        textwrap.fill("You try to take this in.\n\nSpindle is made of a strange silvery material. "
                      "Maybe some sort of alien alloy. It's shape does sort of resemble a "
                      "spindle, you suppose.", width=100),
        textwrap.fill(
            colourize('"But now that you\'re here, we might just be able to get sometime else. I '
                      'don\'t know what happened to my Time Weaver, but certainly something '
                      'drastic to get me stuck out here without a source of bio-power. We have '
                      'to find them.\n\nI think you got what it takes to time travel. Here, '
                      'try this."',
                      "magenta"), width=100),
        textwrap.fill("Spindle seems to do something to your brain and suddenly it\'s like you "
                      "can see another layer of reality overlaid on the physical world. All "
                      "around you you can see the fabric of spacetime itself, and radiating out "
                      "from Spindle, strands of light in all the colours of the rainbow.",
                      width=100),
        textwrap.fill(
            colourize('"These Strands will let you travel across wide gulfs in time. I can only '
                      'provide you with a few of each colour by myself, but if we can '
                      'track down the other two '
                      'instruments my Time Weaver had with them, they should boost your Stand '
                      'count and eventually lead us to the Time Weaver.\n\nWe\'ll go after '
                      'the Bobbin first. My reading say it\'s somewhere in these three time '
                      'periods. Your guess is as good as mine where to start. You\'ll be able to '
                      'make small hops '
                      'freely within each time period, but  you will need to spend a Strand to '
                      'jump farther distances or between periods."',
                      "magenta"), width=100),
        sep="\n\n",
        end="\n\n")


def print_combat_instructions():
    print(
        textwrap.fill(
            colourize('"Aha! A Tear! Whatever got the Time Weaver has definitely been here."',
                      "magenta"), width=100
        ),
        textwrap.fill("With you're spacetime sight you can se what looks like a dark hole in the "
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
                      f"into rainbow order.\n\nThe Tear will have pattern of coloured threads "
                      f"represented "
                      f"by their first letter. You can use your Strands to pull them into order. "
                      f"Play your Strands under each of the Tear's threads by entering the "
                      f"a Strand colour's number from 1 to 6. Playing the same colour under a "
                      f"thread will keep it in the same place for the next round while playing "
                      f"the colour immediately before it in rainbow order will pull it to the "
                      f"left and playing the colour immediately after it will pull it to the "
                      f"right. You can also play a 0 if you are running low on Strands or "
                      f"otherwise want to let a tread behave randomly.\n\nIt may take a few round "
                      f"to get all the threads in order, but each round comes with a chance your "
                      f"Strands will become knotted and if that happens or you play all your "
                      f"threads, you'll love the fight.\n\n Give it a try.", width=100
                      ),
        sep="\n\n",
        end="\n\n")


def main():
    """
    Draive the program.
    """
    pass


if __name__ == '__main__':
    main()
