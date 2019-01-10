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

subraces = [['Dwarf', ['Hill Dwarf', 'Mountain Dwarf']],
            ['Elf', [['High Elf', ['Sun Elf', 'Moon Elf']],
                     'Wood Elf',
                     'Dark Elf (Drow)']],
            ['Halfling', ['Lightfoot', 'Stout']],
            ['Human', ['Standard', 'Variant']],
            ['Gnome', ['Forest Gnome', 'Rock Gnome']]]

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

backgrounds = ['Acolyte',
               'Charlatan',
               'Criminal',
               'Entertainer',
               'Folk Hero',
               'Guild Artisan',
               'Hermit',
               'Noble',
               'Outlander',
               'Sage',
               'Sailor',
               'Soldier',
               'Urchin']


class Character:
    """A class defining generated characters. Use the
    'character_generator' method to randomly generate values for a
    character."""

    def __init__(self, race, alignment, cls, background, subrace=None):
        self._race = race
        self._subrace = subrace
        self._alignment = alignment
        self._cls = cls
        self._background = background

    def __repr__(self):
        return f"<Character '{self._race}', '{self._alignment[0]} " \
            f"{self._alignment[1]}', '{self._cls}'>"

    def race(self):
        """Return race as a string."""
        return self._race

    def subrace(self):
        return self._subrace

    def alignment(self):
        """Return alignment as a list."""
        return self._alignment

    def cls(self):
        """Return class as a string."""
        return self._cls

    def background(self):
        """Return background as a string."""
        return self._background


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

    # Select a subrace
    subrace = None
    for selection in subraces:
        if race in selection:
            subrace = selection[1][int(random() * len(selection[1]))]
    # Specify type of High Elf
    if subrace:
        if 'High Elf' in subrace:
            subrace = f'High Elf ({subrace[1][int(random() * 2)]})'

    cls = classes[int(random() * len(classes))]

    background = backgrounds[int(random() * len(backgrounds))]

    c = Character(race=race, alignment=alignment, cls=cls, background=background, subrace=subrace)

    return c


if __name__ == '__main__':
    if '--evil-permitted' in sys.argv or '-ep' in sys.argv:
        evil_permitted = True
    else:
        evil_permitted = False

    c = character_generator(evil_permitted=evil_permitted)

    print(f'''Race: {c.race()}
Subrace: {c.subrace()}
Alignment: {c.alignment()[0]} {c.alignment()[1]}
Class: {c.cls()}''')
