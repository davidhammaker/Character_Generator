import sys
from random import random

races = {'Dwarf': {'subraces': {'Hill Dwarf': {'sizes': {'base_height': 44,
                                                         'ht_mod_count': 2,
                                                         'ht_mod_value': 4,
                                                         'base_weight': 115,
                                                         'wt_mod_count': 2,
                                                         'wt_mod_value': 6}},
                                'Mountain Dwarf': {'sizes': {'base_height': 48,
                                                             'ht_mod_count': 2,
                                                             'ht_mod_value': 4,
                                                             'base_weight': 130,
                                                             'wt_mod_count': 2,
                                                             'wt_mod_value': 6}}},
                   'size_category': 'subracial',
                   'age_range': [1, 350],
                   'age_range_prime': [50, 100]},
         'Elf': {'subraces': {'High Elf': {'types': ['High Elf (Sun Elf)',
                                                     'High Elf (Moon Elf)'],
                                           'sizes': {'base_height': 54,
                                                     'ht_mod_count': 2,
                                                     'ht_mod_value': 10,
                                                     'base_weight': 90,
                                                     'wt_mod_count': 1,
                                                     'wt_mod_value': 4}},
                              'Wood Elf': {'types': ['Wood Elf'],
                                           'sizes': {'base_height': 54,
                                                     'ht_mod_count': 2,
                                                     'ht_mod_value': 10,
                                                     'base_weight': 100,
                                                     'wt_mod_count': 1,
                                                     'wt_mod_value': 4}},
                              'Drow': {'types': ['Drow'],
                                       'sizes': {'base_height': 53,
                                                 'ht_mod_count': 2,
                                                 'ht_mod_value': 6,
                                                 'base_weight': 75,
                                                 'wt_mod_count': 1,
                                                 'wt_mod_value': 6}}},
                 'size_category': 'subracial',
                 'age_range': [1, 750],
                 'age_range_prime': [100, 150]},
         'Halfling': {'subraces': ['Lightfoot', 'Stout'],
                      'sizes': {'base_height': 31,
                                'ht_mod_count': 2,
                                'ht_mod_value': 4,
                                'base_weight': 35,
                                'wt_mod_count': 1,
                                'wt_mod_value': 1},
                      'size_category': 'racial',
                      'age_range': [1, 150],
                      'age_range_prime': [20, 40]},
         'Human': {'subraces': {'types': ['Standard',
                                          'Variant'],
                                'ethnic_groups': ['Calishite',
                                                  'Chondathan',
                                                  'Damaran',
                                                  'Illuskan',
                                                  'Mulan',
                                                  'Rashemi',
                                                  'Shou',
                                                  'Tethyrian',
                                                  'Turami']},
                   'sizes': {'base_height': 56,
                             'ht_mod_count': 2,
                             'ht_mod_value': 10,
                             'base_weight': 110,
                             'wt_mod_count': 2,
                             'wt_mod_value': 4},
                   'size_category': 'racial',
                   'age_range': [1, 100],
                   'age_range_prime': [17, 30]},
         'Dragonborn': {'subraces': None,
                        'sizes': {'base_height': 66,
                                  'ht_mod_count': 2,
                                  'ht_mod_value': 8,
                                  'base_weight': 175,
                                  'wt_mod_count': 2,
                                  'wt_mod_value': 6},
                        'size_category': 'racial',
                        'age_range': [1, 80],
                        'age_range_prime': [15, 25]},
         'Gnome': {'subraces': ['Forest Gnome', 'Rock Gnome'],
                   'sizes': {'base_height': 35,
                             'ht_mod_count': 2,
                             'ht_mod_value': 4,
                             'base_weight': 35,
                             'wt_mod_count': 1,
                             'wt_mod_value': 1},
                   'size_category': 'racial',
                   'age_range': [1, 500],
                   'age_range_prime': [40, 60]},
         'Half-Elf': {'subraces': None,
                      'sizes': {'base_height': 57,
                                'ht_mod_count': 2,
                                'ht_mod_value': 8,
                                'base_weight': 110,
                                'wt_mod_count': 2,
                                'wt_mod_value': 4},
                      'size_category': 'racial',
                      'age_range': [1, 180],
                      'age_range_prime': [20, 40]},
         'Half-Orc': {'subraces': None,
                      'sizes': {'base_height': 58,
                                'ht_mod_count': 2,
                                'ht_mod_value': 10,
                                'base_weight': 140,
                                'wt_mod_count': 2,
                                'wt_mod_value': 6},
                      'size_category': 'racial',
                      'age_range': [1, 75],
                      'age_range_prime': [14, 25]},
         'Tiefling': {'subraces': None,
                      'sizes': {'base_height': 57,
                                'ht_mod_count': 2,
                                'ht_mod_value': 8,
                                'base_weight': 110,
                                'wt_mod_count': 2,
                                'wt_mod_value': 4},
                      'size_category': 'racial',
                      'age_range': [1, 110],
                      'age_range_prime': [17, 30]}}

classes = {'Barbarian': ['Path of the Berserker', 'Path of the Totem Warrior'],
           'Bard': ['College of Lore', 'College of Valor'],
           'Cleric': ['Life Domain',
                      'Light Domain',
                      'Nature Domain',
                      'Tempest Domain',
                      'Trickery Domain',
                      'War Domain'],
           'Druid': {'Circle of the Land': ['Arctic',
                                            'Coast',
                                            'Desert',
                                            'Forest',
                                            'Grassland',
                                            'Mountain',
                                            'Swamp',
                                            'Underdark'],
                     'Circle of the Moon': ['Circle of the Moon']},
           'Fighter': ['Champion', 'Battle Master', 'Eldritch Knight'],
           'Monk': ['Way of the Open Hand', 'Way of Shadow', 'Way of the Four Elements'],
           'Paladin': ['Oauth of Devotion', 'Oauth of the Ancients', 'Oath of Vengeance'],
           'Ranger': ['Hunter', 'Beast Master'],
           'Rogue': ['Thief', 'Assassin', 'Archane Trixter'],
           'Sorcerer': {'Draconic Bloodline': ['Black',
                                               'Blue',
                                               'Brass',
                                               'Bronze',
                                               'Copper',
                                               'Gold',
                                               'Green',
                                               'Red',
                                               'Silver',
                                               'White'],
                        'Wild Magic': ['Wild Magic']},
           'Warlock': ['The Archfey', 'The Fiend', 'The Great Old One'],
           'Wizard': ['School of Abjuration',
                      'School of Conjuration',
                      'School of Divination',
                      'School of Enchantment',
                      'School of Evocation',
                      'School of Illusion',
                      'School of Necromancy',
                      'School of Transmutation']}


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
                 gender, age, subrace=None, archetype=None, level=1):
        self._race = race
        self._subrace = subrace
        self._height = height
        self._weight = weight
        self._gender = gender
        self._age = age
        self._alignment = alignment
        self._cls = cls
        self._background = background
        self._archetype = archetype
        self._level = level

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

    def gender(self):
        """Return gender as a string."""
        return self._gender

    def age(self):
        """Return age as an integer."""
        return self._age

    def alignment(self):
        """Return alignment as a string."""
        return f'{self._alignment[0]} {self._alignment[1]}'

    def cls(self):
        """Return class as a string."""
        return self._cls

    def archetype(self):
        """Return archetype as a string."""
        return self._archetype

    def background(self):
        """Return background as a string."""
        return self._background

    def level(self):
        """Return level as an integer."""
        return self._level


def character_generator(age_prime=True, evil_permitted=False, level=1):
    """Generate random values for a Character, then return the newly
    generated character.

    Arguments:
        age_prime: bool; True to use only prime ages, False to include
        all possible ages. Default: True

        evil_permitted: bool; True to include evil alignments in random
        alignment generation. Default: False

        level: int; character level. Default: 1

    Returns:
        new_character: A Character instance.
    """

    def select(lst):
        """Select a random value from a given list.

        Arguments:
            lst: list; the list from which a value will be selected.

        Returns:
            One item selected randomly from the list.
        """
        return lst[int(random() * len(lst))]

    # Determine whether alignments may be evil
    if evil_permitted:
        alignment = select(alignments)
    else:
        alignment = select(alignments_modded)

    # Validate level
    if type(level) != int:
        try:
            level = int(level)
        except TypeError:
            level = 1
        except ValueError:
            level = 1
    if level < 1:
        level = 1
    elif level > 20:
        level = 20

    # Select a race
    race = select(list(races))

    # Select a subrace
    subrace = None
    subraces = races[race]['subraces']
    if subraces:

        # Subrace selection for elves
        if race == 'Elf':

            # Select meta_subrace (High Elf, Wood Elf, Drow)
            meta_subrace = select(list(subraces))

            # Select subrace from types(High elves will have multiple
            # types)
            subrace = select(subraces[meta_subrace]['types'])

        # Subrace selection for humans
        elif race == 'Human':
            # Select ethnic group
            ethnic_group = select(list(subraces['ethnic_groups']))

            # Select type (standard or variant)
            type_group = select(list(subraces['types']))

            # Combine type and ethnic group
            subrace = f'{type_group} {ethnic_group}'

        # Subrace selection for non-humans
        else:
            subrace = select(list(subraces))

    # Determine height and weight
    weight_raw = None
    height_raw = None

    def roll(count, value):
        """Return a total value from rolled dice.

        Arguments:
            count: int; the number of dice to roll.

            value: int; the value of each die.

        Returns:
            total: int; the sum total of all rolls.
        """

        total = 0
        for _ in range(count):
            total += int(random() * value) + 1
        return total

    def get_height_weight(base_height, ht_mod_count, ht_mod_value,
                          base_weight, wt_mod_count, wt_mod_value):
        """Calculate the height and weight of a character.

        Arguments:
            base_height: int; base height of the character.

            ht_mod_count: int; number of dice for height modifier.

            ht_mod_value: int; value of dice for height modifier.

            base_weight: int; base weight of the character.

            wt_mod_count: int; number of dice for weight modifier.

            wt_mod_value: int; value of dice for weight modifier.

        Returns:
            height: int; height of the character.

            weight: int; weight of the character.
        """

        # Determine height
        height_mod = roll(ht_mod_count, ht_mod_value)
        height = base_height + height_mod

        # Determine weight
        weight_mod = roll(wt_mod_count, wt_mod_value)
        weight = base_weight + (height_mod * weight_mod)

        return height, weight

    # Determine whether character size depends on race or subrace, then
    # use the appropriate formula accordingly
    if races[race]['size_category'] == 'racial':
        formula = races[race]['sizes']
    else:
        if 'High Elf' in subrace:
            formula = races[race]['subraces']['High Elf']['sizes']
        else:
            formula = races[race]['subraces'][subrace]['sizes']

    height_raw, weight_raw = get_height_weight(**formula)

    # Clean up height
    feet = 0
    inches = height_raw
    while inches >= 12:
        inches -= 12
        feet += 1
    height = f'{feet}\'{inches}"'

    # Clean up weight
    weight = f'{weight_raw} lb.'

    # Select gender
    gender = select(['Male', 'Female'])

    # Select age
    def age_select(minimum, maximum, median=-1):
        """Select an age for a character.

        Arguments:
            minimum: int; the character's minimum allowed age.

            maximum: int; the character's maximum allowed age.

            median: int; the median age used in age generation. Ages
            will tend toward the median. Default: -1

        Returns:
            final_age: int; the character's selected age.
        """

        # Create a list of all possible ages
        ages = [number for number in range(minimum, maximum)]

        # Use the median to determine a center for age generation. If
        # the median is default or otherwise invalid, the selected
        # center will be selected from the center of the list of ages.
        try:
            center = ages[-ages.index(median)]
        except ValueError:
            center = int(len(ages) / 2)
        except TypeError:
            center = int(len(ages) / 2)

        # Create a list of probabilities, which relates to the list of
        # ages. Each item in "probs" represents the probability that an
        # item of the same index in "ages" will be selected. Items in
        # the center of "probs" have highest probability.
        probs_left = [number / center for number in range(int(center))]
        probs_right = reversed(probs_left)
        probs = probs_left + list(probs_right)

        # Adjust list lengths of "probs" and/or "ages" if necessary
        while len(ages) < len(probs):
            ages.insert(0, 0)
        while len(ages) > len(probs):
            probs.insert(0, 0)

        # Create a list of numbers, where each number in the list
        # represents the number of occurrences that an item of the same
        # index in "ages" will have in "select_group", from which the
        # age will be selected
        counts = [int(len(ages) * prob) for prob in probs]

        # Create a list of ages, where the number of occurrences of an
        # age represents the likelihood that the age will be selected.
        # The final age will be selectec from "select_group".
        select_group = []
        for age in ages:
            select_group += [age] * counts[ages.index(age)]

        # Select and return the final age
        final_age = select_group[int(random() * len(select_group))]
        return final_age

    # Determine age range
    if age_prime:
        age_range = races[race]['age_range_prime']
    else:
        age_range = races[race]['age_range']

    # Use age_range and age_select to select age
    age = age_select(*age_range)

    # Select a class
    cls = select(list(classes))

    # Select an archetype
    archetype = None

    # Selection for standard archetypes
    if type(classes[cls]) == list:
        archetype = select(classes[cls])

    # Selection for archetypes with many variations, like Druids and
    # Sorcerers
    else:
        archetype_raw = select(list(classes[cls]))
        archetype_variant = select(classes[cls][archetype_raw])
        if archetype_raw != archetype_variant:
            archetype = f'{archetype_raw} ({archetype_variant})'
        else:
            archetype = f'{archetype_raw}'

    # Ensure that character is high enough level for archetype
    level_2_archetype_classes = ['Druid',
                                 'Wizard']
    level_3_archetype_classes = ['Barbarian',
                                 'Bard',
                                 'Fighter',
                                 'Monk',
                                 'Paladin',
                                 'Ranger',
                                 'Rogue']

    if level < 2 and cls in level_2_archetype_classes:
        archetype = None
    if level < 3 and cls in level_3_archetype_classes:
        archetype = None

    # Select background
    background = select(backgrounds)

    # Generate character
    new_character = Character(race=race,
                              alignment=alignment,
                              cls=cls,
                              background=background,
                              subrace=subrace,
                              archetype=archetype,
                              height=height,
                              weight=weight,
                              gender=gender,
                              age=age,
                              level=level)

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
