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

archetypes = [['Barbarian', ['Path of the Berserker',
                             'Path of the Totem Warrior']],
              ['Bard', ['College of Lore',
                        'College of Valor']],
              ['Cleric', ['Life Domain',
                          'Light Domain',
                          'Nature Domain',
                          'Tempest Domain',
                          'Trickery Domain',
                          'War Domain']],
              ['Druid', [['Circle of the Land', ['Arctic',
                                                 'Coast',
                                                 'Desert',
                                                 'Forest',
                                                 'Grassland',
                                                 'Mountain',
                                                 'Swamp',
                                                 'Underdark']],
                         'Circle of the Moon']],
              ['Fighter', ['Champion',
                           'Battle Master',
                           'Eldritch Knight']],
              ['Monk', ['Way of the Open Hand',
                        'Way of Shadow',
                        'Way of the Four Elements']],
              ['Paladin', ['Oauth of Devotion',
                           'Oauth of the Ancients',
                           'Oath of Vengeance']],
              ['Ranger', ['Hunter',
                          'Beast Master']],
              ['Rogue', ['Thief',
                         'Assassin',
                         'Archane Trixter']],
              ['Sorcerer', [['Draconic Bloodline', ['Black',
                                                    'Blue',
                                                    'Brass',
                                                    'Bronze',
                                                    'Copper',
                                                    'Gold',
                                                    'Green',
                                                    'Red',
                                                    'Silver',
                                                    'White']],
                            'Wild Magic']],
              ['Warlock', [['The Archfey',
                            'The Fiend',
                            'The Great Old One'],
                           ['Pact of the Chain',
                            'Pact of the Blade',
                            'Pact of the Tome']]],
              ['Wizard', ['School of Abjuration',
                          'School of Conjuration',
                          'School of Divination',
                          'School of Enchantment',
                          'School of Evocation',
                          'School of Illusion',
                          'School of Necromancy',
                          'School of Transmutation']]]

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

    def __init__(self, race, alignment, cls, background, subrace=None,
                 archetype=None):
        self._race = race
        self._subrace = subrace
        self._alignment = alignment
        self._cls = cls
        self._background = background
        self._archetype = archetype

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

    def archetype(self):
        """Return archetype as a string."""
        return self._archetype

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
            subrace = f'High Elf ' \
                f'({subrace[1][int(random() * len(subrace[1]))]})'

    cls = classes[int(random() * len(classes))]

    # Select an archetype
    archetype = None
    for selection in archetypes:
        if cls != 'Warlock' and cls in selection:
            archetype = selection[1][int(random() * len(selection[1]))]
        # Warlock Archetype selection (Patron and Pact)
        elif cls == 'Warlock' and cls in selection:
            patrons = selection[1][0]
            pacts = selection[1][1]
            archetype = f'{patrons[int(random() * len(patrons))]} ' \
                f'({pacts[int(random() * len(pacts))]})'
    # Specify Druid's Land
    if 'Circle of the Land' in archetype:
        archetype = f'Circle of the Land ' \
            f'({archetype[1][int(random() * len(archetype[1]))]})'
    # Specify Sorcerer's Dragon
    if 'Draconic Bloodline' in archetype:
        archetype = f'Draconic Bloodline ' \
            f'({archetype[1][int(random() * len(archetype[1]))]})'

    background = backgrounds[int(random() * len(backgrounds))]

    c = Character(race=race,
                  alignment=alignment,
                  cls=cls,
                  background=background,
                  subrace=subrace,
                  archetype=archetype)

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
