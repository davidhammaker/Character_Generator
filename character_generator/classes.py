class Subrace:

    def __init__(self, name, sizes=None, types=None):
        self.name = name
        self.types = types
        self.sizes = sizes

    def __repr__(self):
        return f'Subrace({self.name})'


class Race:

    def __init__(self, name, age_range, age_range_prime,
                 sizes=None, subraces=None):
        self.name = name
        self.age_range = age_range
        self.age_range_prime = age_range_prime
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
