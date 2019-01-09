import sys
from random import random

races = ['Dwarf',
         'Elf',
         'Halfling',
         'Human',
         'Dragonborn',
         'Gnome',
         'Half-Elf',
         'Half-Orc',
         'Tiefling']

classes = ['Barbarian',
           'Bard',
           'Cleric',
           'Druid',
           'Fighter',
           'Monk',
           'Paladin',
           'Ranger',
           'Rogue',
           'Sorcerer',
           'Warlock',
           'Wizard']

alignments = [['Lawful', 'Good'],
              ['Lawful', 'Neutral'],
              ['Lawful', 'Evil'],
              ['Neutral', 'Good'],
              ['Neutral', 'Neutral'],
              ['Neutral', 'Evil'],
              ['Chaotic', 'Good'],
              ['Chaotic', 'Neutral'],
              ['Chaotic', 'Evil']]

alignments_modded = [['Lawful', 'Good'],
                     ['Lawful', 'Neutral'],
                     ['Neutral', 'Good'],
                     ['Neutral', 'Neutral'],
                     ['Chaotic', 'Good'],
                     ['Chaotic', 'Neutral']]


class Character:
    """A class defining generated characters. Use the
    'character_generator' method to randomly generate values for a
    character."""

    def __init__(self, race, alignment, cls):
        self._race = race
        self._alignment = alignment
        self._cls = cls

    def __repr__(self):
        return f"<Character '{self._race}', '{self._alignment[0]} " \
            f"{self._alignment[1]}', '{self._cls}'>"

    def race(self):
        """Return race as a string."""
        return self._race

    def alignment(self):
        """Return alignment as a list."""
        return self._alignment

    def cls(self):
        """Return class as a string."""
        return self._cls


def character_generator(evil_permitted=False):
    """Generate random values for a Character, then return the newly
    generated character.

    Arguments:
        evil_permitted: Set to True to include evil alignments in random
        alignment generation. Default: False

    Returns:
        c: A Character instance.
    """

    if evil_permitted:
        alignment = alignments[int(random() * len(alignments))]
    else:
        alignment = alignments_modded[int(random()
                                          * len(alignments_modded))]

    race = races[int(random() * len(races))]

    cls = classes[int(random() * len(classes))]

    c = Character(race=race, alignment=alignment, cls=cls)

    return c


if __name__ == '__main__':
    try:
        if sys.argv[1] == '--evil-permitted' or sys.argv[1] == '-ep':
            alignment = alignments[int(random() * len(alignments))]
        else:
            alignment = alignments_modded[int(random()
                                              * len(alignments_modded))]
    except IndexError:
        alignment = alignments_modded[int(random()
                                          * len(alignments_modded))]

    race = races[int(random() * len(races))]

    cls = classes[int(random() * len(classes))]

    c = Character(race=race, alignment=alignment, cls=cls)

    print(f'''Race: {c.race()}
Alignment: {c.alignment()[0]} {c.alignment()[1]}
Class: {c.cls()}''')
