from random import random
from character_generator.utils.methods import select, roll
from character_generator.utils.details import alignments
from character_generator.utils.races import (dwarf, elf, halfling,
                                             human, dragonborn, gnome,
                                             half_elf, half_orc,
                                             tiefling)
from character_generator.utils.klasses import (barbarian, bard, cleric,
                                               druid, fighter, monk,
                                               paladin, ranger, rogue,
                                               sorcerer, warlock,
                                               wizard)
from character_generator.utils.backgrounds import (acolyte,
                                                   charlatan,
                                                   criminal,
                                                   entertainer,
                                                   folkhero,
                                                   guildartisan,
                                                   hermit,
                                                   noble,
                                                   outlander,
                                                   sage,
                                                   sailor,
                                                   soldier,
                                                   urchin)


class Character:
    """A class defining generated characters."""

    def __init__(self, name, race, height, weight, alignment, klass,
                 background, gender, age, subrace=None, archetype=None,
                 archetype_sub=None, subrace_sub=None, level=1):
        self.name = name
        self.race = race
        self.subrace = subrace
        self.subrace_sub = subrace_sub
        self.height = height
        self.weight = weight
        self.gender = gender
        self.age = age
        self.alignment = alignment
        self.klass = klass
        self.background = background
        self.archetype = archetype
        self.archetype_sub = archetype_sub
        self.level = level

    def __repr__(self):
        return f"Character('{self.name}', '{self.race.name}', " \
               f"'{self.klass.name}')"

    races = [dwarf, elf, halfling, human, dragonborn, gnome, half_elf,
             half_orc, tiefling]
    race_names = ['dwarf', 'elf', 'halfling', 'human', 'dragonborn',
                  'gnome', 'half-elf', 'half-orc', 'tiefling']
    klasses = [barbarian, bard, cleric, druid, fighter, monk, paladin,
               ranger, rogue, sorcerer, warlock, wizard]
    klasses_names = ['barbarian', 'bard', 'cleric', 'druid', 'fighter',
                     'monk', 'paladin', 'ranger', 'rogue', 'sorcerer',
                     'warlock', 'wizard']
    backgrounds = [acolyte, charlatan, criminal, entertainer, folkhero,
                   guildartisan, hermit, noble, outlander, sage, sailor,
                   soldier, urchin]

    @staticmethod
    def age_select(minimum, maximum, median=-1):
        """Select an age for a character.

        Arguments:
            minimum: int; the character's minimum allowed age.

            maximum: int; the character's maximum allowed age.

            median: int; the median age used in age generation. Ages
            will tend toward the median. Default -1

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

    @staticmethod
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

    @classmethod
    def create(cls, level=1, race=None, subrace=None, subrace_sub=None,
               gender=None, age=None, age_range_wide=False, name=None,
               alignment=None, no_evil=True, height=None, weight=None,
               klass=None, archetype=None, archetype_sub=None,
               background=None):
        """Create a new Character based on supplied user input and
        randomly generated values.

        Arguments:
            level: int; the Character's level. Default 1

            race: str; the Character's race as a string rather than a
            Race object. Default None

            subrace: str; the Character's subrace as a string rather
            than a Subrace object. Default None

            gender: str; the Character's gender. Default None

            age: int; the Character's age in years. Default None

            age_range_wide: bool; if True, the returned value for age
            will be selected from the entire range of ages permitted by
            the Character's race. If False, the returned value for age
            will be selected from a restricted range of ages that
            approximate a young adult age. Default False

            name: str; the Character's name. Default None

            alignment: list; the Character's alignment, supplied as a
            list of length 2. The first item in the list must be
            'Lawful', 'Neutral', or 'Chaotic', and the second item in
            the list must be 'Good', 'Neutral', or 'Evil'. Default None

            no_evil: bool; if True, randomly generated alignment may not
            include an 'Evil' alignment. If False, randomly generated
            alignment may include an 'Evil' alignment. Default True

            height: int; the Character's height in inches. Default None

            weight: int; the Character's weight in inches. Default None

            klass: str; the Character's class as a string rather than a
            Klass object. Default None

            archetype: str; the Character's class as a string rather
            than an Archetype object. Default None

            archetype_sub: str; the Character's archetype subcategory.
            Default None

            background: str; the Character's background. Default None

        Returns:
            A Character object.
        """

        # Validate level
        if type(level) != int:
            raise TypeError("'level' must be entered as an integer.")
        elif level < 1:
            raise ValueError("'level' cannot be less than 1.")
        elif level > 20:
            raise ValueError("'level' cannot be greater than 20.")

        # Validate supplied race, if any
        if race:
            if type(race) != str:
                raise TypeError("'race' must be entered as a string.")
            elif race.lower() not in cls.race_names:
                raise NameError(f"'{race}' is not a valid race.")
            else:
                for one_race in cls.races:
                    if race.title() == one_race.name:
                        race = one_race
                        break

        # Select race if not supplied
        else:
            race = select(cls.races)

        # Validate supplied subrace, if any
        if subrace:
            if not race.subraces:
                raise ValueError(f"'{race}' does not have subraces.")
            else:
                valid_subrace = False
                for one_subrace in race.subraces:
                    if subrace.lower() == one_subrace.name.lower():
                        valid_subrace = True
                        subrace = one_subrace
                        break
                if not valid_subrace:
                    raise NameError(f"'{subrace}' is not a valid "
                                    f"subrace for '{race}'.")

        # Select subrace if not supplied
        else:
            if race.subraces:
                subrace = select(race.subraces)

        # Validate supplied subrace subcategory, if any
        if subrace_sub:
            if type(subrace_sub) != str:
                raise TypeError("'subrace_sub' must be entered as a "
                                "string.")
            elif subrace_sub.title() not in subrace.subcategories:
                raise NameError(f"'{subrace_sub}' is not a valid "
                                f"subcategory of '{subrace.name}'.")
            else:
                for one_subrace_sub in subrace.subcategories:
                    if subrace_sub.title() == one_subrace_sub:
                        subrace_sub = one_subrace_sub
                        break

        # Select subrace subcategory if not supplied
        else:
            if subrace:
                if subrace.subcategories:
                    subrace_sub = select(subrace.subcategories)

        # Validate supplied gender, if any
        if gender:
            if type(gender) != str:
                raise TypeError("'gender' must be entered as a string.")
            elif gender.lower() not in ['male', 'female']:
                raise NameError(f"'{gender}' is not a valid gender.")
            gender = gender.capitalize()

        # Select gender if not supplied
        else:
            gender = select(['Male', 'Female'])

        # Validate supplied age, if any
        if age:
            if type(age) != int:
                raise TypeError("'age' must be entered as an integer.")
            elif not (race.age_range[0] <= age <= race.age_range[1]):
                raise ValueError(f"Age is out of range. Must be "
                                 f"between {race.age_range[0]} and "
                                 f"{race.age_range[1]} for '{race}'.")

        # Select age if not supplied
        else:
            if age_range_wide:
                age = cls.age_select(*race.age_range)
            else:
                age = cls.age_select(*race.age_range_prime)

        # Validate supplied name, if any
        if name:
            if type(name) != str:
                raise TypeError("'name' must be entered as a string.")

        # Begin name selection if not supplied
        else:
            name = ''
            given_name = ''
            family_name = ''

            # Half-Elf, Half-Orc name selection
            if race.name == 'Half-Elf' or race.name == 'Half-Orc':
                name = select(race.names[gender])

            # Tiefling name selection
            elif race.name == 'Tiefling':
                virtue = select([True, False])
                if virtue:
                    name = select(race.names['Virtue'])
                else:
                    name = select(race.names[gender])

            # Subrace-specific name selection (Human)
            elif race.name == 'Human':
                given_name = select(subrace.names[gender])
                family_name = select(subrace.names['Family'])

            # Dwarf, Elf, Halfling, Dragonborn, Gnome name selection
            elif race.names:
                given_name = select(race.names[gender])

                # Elf child name selection
                if race.name == 'Elf' and age < 100:
                    given_name = select(race.names['Child'])

                # Add Gnome nickname
                if race.name == 'Gnome':
                    nickname = select(race.names['Nickname'])
                    given_name += f' ({nickname})'

                family_name = select(race.names['Family'])

            # Otherwise, raise an error; something went wrong
            else:
                raise NotImplementedError('A name could not be '
                                          'generated.')

            # Construct name
            # Dragonborn name
            if race.name == 'Dragonborn':
                name = f'{family_name} {given_name}'

            # Other names
            elif race.name not in ['Half-Elf', 'Half-Orc', 'Tiefling']:
                name = f'{given_name} {family_name}'

        # Validate supplied alignment, if any
        if alignment:
            if type(alignment) != list:
                raise TypeError('Alignment must be a list.')
            else:
                for part in range(len(alignment)):
                    alignment[part] = alignment[part].capitalize()
            if alignment not in alignments:
                raise NameError(f"'{alignment}' is not a valid "
                                f"alignment.")

        # Select alignment if not supplied
        else:
            if no_evil:
                alignment = select(alignments)
                while 'Evil' in alignment:
                    alignment = select(alignments)
            else:
                alignment = select(alignments)

        # Validate supplied height, if any
        if height:
            if type(height) != int:
                raise TypeError('Height must be an integer (inches).')
            elif height < 12:
                raise ValueError('Height must be at least 12 inches.')
            elif height > 120:
                raise ValueError('Height must be at most 120 inches.')

        # Validate supplied weight, if any
        if weight:
            if type(weight) != int:
                raise TypeError('Weight must be an integer (pounds).')
            elif weight < 8:
                raise ValueError('Weight must be at least 8 pounds.')
            elif weight > 800:
                raise ValueError('Weight must be at most 800 pounds.')

        # Select raw height and weight if one or both are not supplied
        height_raw = 0
        weight_raw = 0
        if not height or not weight:
            if race.name == 'Elf' or race.name == 'Dwarf':
                formula = subrace.sizes
            else:
                formula = race.sizes
            height_raw, weight_raw = cls.get_height_weight(**formula)

        # Determine height
        # Use supplied height, if any
        if height:
            height_raw = height
        feet = 0
        inches = height_raw
        while inches >= 12:
            inches -= 12
            feet += 1
        height = f'{feet}\'{inches}"'

        # Determine weight
        # Use supplied weight, if any
        if weight:
            weight_raw = weight
        weight = f'{weight_raw} lb.'

        # Validate supplied klass, if any
        if klass:
            if type(klass) != str:
                raise TypeError("'klass' must be entered as a string.")
            elif klass.lower() not in cls.klasses_names:
                raise NameError(f"'{klass}' is not a valid klass.")
            else:
                for one_klass in cls.klasses:
                    if klass.title() == one_klass.name:
                        klass = one_klass
                        break

        # Select klass if not supplied
        else:
            klass = select(cls.klasses)

        # Validate supplied archetype, if any
        if archetype:
            if type(archetype) != str:
                raise TypeError("'archetype' must be entered as a "
                                "string.")
            elif klass.archetype_level_req:
                if level < klass.archetype_level_req:
                    raise ValueError(f"'{klass.name}' restricts "
                                     f"archetypes to level "
                                     f"{klass.archetype_level_req} and "
                                     f"higher.")
            valid_archetype = False
            for one_archetype in klass.archetypes:
                if archetype.title() == one_archetype.name.title():
                    valid_archetype = True
                    archetype = one_archetype
                    break
            if not valid_archetype:
                raise NameError(f"'{archetype}' is not a valid "
                                f"archetype.")

        # Select archetype if not supplied
        else:
            if klass.archetype_level_req:
                if level >= klass.archetype_level_req:
                    archetype = select(klass.archetypes)

        # Validate archetype subcategory, if supplied
        if archetype_sub:
            if type(archetype_sub) != str:
                raise TypeError("'archetype_sub' must be entered as a "
                                "string.")
            elif not archetype:
                raise AttributeError("A non-existent archetype cannot "
                                     "have a subcategory.")
            elif not archetype.subcategories:
                raise AttributeError(f"'{archetype.name}' has no "
                                     f"subcategories.")
            else:
                valid_archetype_sub = False
                for one_archetype_sub in archetype.subcategories:
                    if archetype_sub.title() == one_archetype_sub:
                        valid_archetype_sub = True
                        archetype_sub = one_archetype_sub
                        break
                if not valid_archetype_sub:
                    raise NameError(f"'{archetype_sub}' is not a valid "
                                    f"archetype subcategory.")

        # Select archetype subcategory if not supplied
        elif archetype:
            if archetype.subcategories:
                archetype_sub = select(archetype.subcategories)

        # Validate supplied background, if any
        if background:
            if type(background) != str:
                raise TypeError("'background' must be entered as a "
                                "string.")
            valid_background = False
            for one_background in cls.backgrounds:
                if background.title() == one_background.name:
                    valid_background = True
                    background = one_background
                    break
            if not valid_background:
                raise NameError(f"'{background}' is not a valid "
                                f"background.")

        # Select background if not supplied
        else:
            background = select(cls.backgrounds)

        # Put it all together
        return cls(name=name,
                   race=race,
                   height=height,
                   weight=weight,
                   alignment=alignment,
                   klass=klass,
                   background=background,
                   gender=gender,
                   age=age,
                   subrace=subrace,
                   subrace_sub=subrace_sub,
                   archetype=archetype,
                   archetype_sub=archetype_sub,
                   level=level)
