class Subrace:

    def __init__(self, name, names=None, sizes=None, types=None):
        self.name = name
        self.types = types
        self.sizes = sizes
        self.names = names

    def __repr__(self):
        return f'Subrace({self.name})'


class Race:

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
