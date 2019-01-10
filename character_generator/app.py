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
            ['Human', [['Standard',
                        'Variant'],
                       ['Calishite',
                        'Chondathan',
                        'Damaran',
                        'Illuskan',
                        'Mulan',
                        'Rashemi',
                        'Shou',
                        'Tethyrian',
                        'Turami']]],
            ['Gnome', ['Forest Gnome', 'Rock Gnome']]]

# Numbers: Base height, height modifier dice count, height modifier dice
# value, base weight, weight modifier dice count, weight modifier dice
# value. Exception: Halflings and Gnomes add height modifier to weight.
sizes = [['Human', [56, 2, 10, 110, 2, 4]],
         ['Hill Dwarf', [44, 2, 4, 115, 2, 6]],
         ['Mountain Dwarf', [48, 2, 4, 130, 2, 6]],
         ['High Elf (Sun Elf)', [54, 2, 10, 90, 1, 4]],
         ['High Elf (Moon Elf)', [54, 2, 10, 90, 1, 4]],
         ['Wood Elf', [54, 2, 10, 100, 1, 4]],
         ['Dark Elf (Drow)', [53, 2, 6, 75, 1, 6]],
         ['Halfling', [31, 2, 4, 35, 1, 1]],
         ['Dragonborn', [66, 2, 8, 175, 2, 6]],
         ['Gnome', [35, 2, 4, 35, 1, 1]],
         ['Half-Elf', [57, 2, 8, 110, 2, 4]],
         ['Half-Orc', [58, 2, 10, 140, 2, 6]],
         ['Tiefling', [57, 2, 8, 110, 2, 4]]]

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

    def __init__(self, race, height, weight, alignment, cls, background,
                 subrace=None, archetype=None):
        self._race = race
        self._subrace = subrace
        self._height = height
        self._weight = weight
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
        """Return subrace as a string."""
        return self._subrace

    def height(self):
        """Return height as a string."""
        return self._height

    def weight(self):
        """Return weight as a string."""
        return self._weight

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
        evil_permitted: bool; True to include evil alignments in random
        alignment generation. Default: False

    Returns:
        new_character: A Character instance.
    """

    # Determine whether alignments may be evil
    if evil_permitted:
        alignment = alignments[int(random() * len(alignments))]
    else:
        alignment = alignments_modded[int(random()
                                          * len(alignments_modded))]

    # Select a race
    race = races[int(random() * len(races))]

    # Select a subrace
    subrace = None
    for selection in subraces:

        # Subrace selection for non-humans
        if race != 'Human' and race in selection:
            subrace = selection[1][int(random() * len(selection[1]))]

        # Human ethnicity and standard/variant selection
        elif race == 'Human' and race in selection:
            types = selection[1][0]
            ethnic_groups = selection[1][1]
            subrace = f'{types[int(random() * len(types))]} ' \
                f'({ethnic_groups[int(random() * len(ethnic_groups))]})'

    # Specify type of High Elf, if applicable
    if subrace:
        if 'High Elf' in subrace:
            subrace = f'High Elf ' \
                f'({subrace[1][int(random() * len(subrace[1]))]})'

    # Determine height and weight
    weight_raw = None
    height_raw = None

    def get_height_weight(formula):
        """Calculates the height and weight of a character.

        Arguments:
            formula: list; in order, items in the list are base height,
            height modifier dice count, height modifier dice value, base
            weight, weight modifier dice count, weight modifier dice
            value.

        Returns:
            height: int; height of the character.
            weight: int; weight of the character.
        """

        base_height = formula[0]
        ht_dice_count = formula[1]
        ht_dice_value = formula[2]
        base_weight = formula[3]
        wt_dice_count = formula[4]
        wt_dice_value = formula[5]

        # Determine height
        height_mod = ht_dice_count * int(random() * ht_dice_value)
        height = base_height + height_mod + 1

        # Determine weight
        weight_mod = wt_dice_count * int(random() * wt_dice_value)
        weight = base_weight + ((height_mod + 1) * (weight_mod + 1))

        return height, weight

    # Height and weight for dwarves and elves
    if race == 'Dwarf' or race == 'Elf':
        for formula in sizes:
            if subrace in formula:
                height_raw, weight_raw = get_height_weight(formula[1])

    # Height and weight for other races
    else:
        for formula in sizes:
            if race in formula:
                height_raw, weight_raw = get_height_weight(formula[1])

    # Clean up height
    feet = 0
    inches = height_raw
    while inches >= 12:
        inches -= 12
        feet += 1
    height = f'{feet}\'{inches}"'

    # Clean up weight
    weight = f'{weight_raw} lb.'

    # Select a class
    cls = classes[int(random() * len(classes))]

    # Select an archetype
    archetype = None
    for selection in archetypes:

        # Archetype selection for non-warlocks
        if cls != 'Warlock' and cls in selection:
            archetype = selection[1][int(random() * len(selection[1]))]

        # Warlock Archetype selection (Patron and Pact)
        elif cls == 'Warlock' and cls in selection:
            patrons = selection[1][0]
            pacts = selection[1][1]
            archetype = f'{patrons[int(random() * len(patrons))]} ' \
                f'({pacts[int(random() * len(pacts))]})'

    # Specify Druid's Land, if applicable
    if 'Circle of the Land' in archetype:
        archetype = f'Circle of the Land ' \
            f'({archetype[1][int(random() * len(archetype[1]))]})'

    # Specify Sorcerer's Dragon, if applicable
    if 'Draconic Bloodline' in archetype:
        archetype = f'Draconic Bloodline ' \
            f'({archetype[1][int(random() * len(archetype[1]))]})'

    # Select background
    background = backgrounds[int(random() * len(backgrounds))]

    # Generate character
    new_character = Character(race=race,
                              alignment=alignment,
                              cls=cls,
                              background=background,
                              subrace=subrace,
                              archetype=archetype,
                              height=height,
                              weight=weight)

    return new_character


if __name__ == '__main__':
    if '--evil-permitted' in sys.argv or '-ep' in sys.argv:
        evil_permitted = True
    else:
        evil_permitted = False

    new_character = character_generator(evil_permitted=evil_permitted)

    print(f'''Race: {new_character.race()}
Subrace: {new_character.subrace()}
Alignment: {new_character.alignment()[0]} {new_character.alignment()[1]}
Class: {new_character.cls()}''')
