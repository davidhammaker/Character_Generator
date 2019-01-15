class Subrace:
    """A class defining subraces for each Race."""

    def __init__(self, name, names=None, sizes=None, types=None):
        self.name = name
        self.types = types
        self.sizes = sizes
        self.names = names

    def __repr__(self):
        return f'Subrace({self.name})'


class Race:
    """A class defining character races."""

    def __init__(self, name, age_range, age_range_prime, names=None,
                 sizes=None, subraces=None):
        self.name = name
        self.age_range = age_range
        self.age_range_prime = age_range_prime
        self._names = names
        self._sizes = sizes
        self.subraces = subraces

    def __repr__(self):
        return f'Race({self.name})'

    @property
    def sizes(self):
        if self._sizes:
            return self._sizes
        else:
            return {subrace.name: subrace.sizes
                    for subrace in self.subraces}

    @property
    def names(self):
        if self._names:
            return self._names
        else:
            return {subrace.name: subrace.names
                    for subrace in self.subraces}


class Archetype:
    """A class defining archetypes for each Cls."""

    def __init__(self, name, subcategories=None):
        self.name = name
        self.subcategories = subcategories

    def __repr__(self):
        return f'Archetype({self.name})'


class Cls:
    """A class defining character classes ('cls')."""

    def __init__(self, name, archetypes):
        self.name = name
        self.archetypes = archetypes

    def __repr__(self):
        return f'Cls({self.name})'


class Character:
    """A class defining generated characters."""

    def __init__(self, name, race, height, weight, alignment, cls,
                 background, gender, age, subrace=None, archetype=None,
                 level=1):
        self.name = name
        self.race = race
        self.subrace = subrace
        self.height = height
        self.weight = weight
        self.gender = gender
        self.age = age
        self.alignment = alignment
        self.cls = cls
        self.background = background
        self.archetype = archetype
        self.level = level

    def __repr__(self):
        return f"<Character '{self.race}', '{self.alignment[0]} " \
            f"{self.alignment[1]}', '{self.cls}'>"
