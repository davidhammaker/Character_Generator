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
    def __init__(self, race, alignment, cls):
        self._race = race
        self._alignment = alignment
        self._cls = cls

    def race(self):
        return self._race

    def alignment(self):
        return self._alignment

    def cls(self):
        return self._cls


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
