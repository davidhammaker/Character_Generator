class Subrace:
    """A class defining subraces for each Race."""

    def __init__(self, name, names=None, sizes=None,
                 subcategories=None):
        self.name = name
        self.subcategories = subcategories
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
    """A class defining archetypes for each Klass."""

    def __init__(self, name, subcategories=None):
        self.name = name
        self.subcategories = subcategories

    def __repr__(self):
        return f'Archetype({self.name})'


class Klass:
    """A class defining character classes ('klasses')."""

    def __init__(self, name, archetypes,
                 archetype_level_req=None):
        self.name = name
        self.archetypes = archetypes
        self.archetype_level_req = archetype_level_req

    def __repr__(self):
        return f'Klass({self.name})'


class Background:
    """A class defining character backgrounds."""

    def __init__(self, name, skill_profs, tool_profs,
                 tool_prof_selection, equipment, equipment_selections,
                 selections, money, personalities, ideals, bonds, flaws,
                 languages=None, details=None):
        self.name = name
        self.skill_profs = skill_profs
        self.tool_profs = tool_profs
        self.tool_prof_selection = tool_prof_selection
        self.equipment = equipment
        self.equipment_selections = equipment_selections
        self.selections = selections
        self.money = money
        self.personalities = personalities
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.languages = languages
        self.details = details

    def __repr__(self):
        return f"Background('{self.name}')"


class Money:
    """A class defining quantities of money."""

    def __init__(self, cp=0, sp=0, ep=0, gp=0, pp=0):
        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp

    def __repr__(self):
        total = ''
        if self.cp > 0:
            total += f'{self.cp}cp'
        if self.sp > 0:
            if total != '':
                total += ', '
            total += f'{self.sp}sp'
        if self.ep > 0:
            if total != '':
                total += ', '
            total += f'{self.ep}ep'
        if self.gp > 0:
            if total != '':
                total += ', '
            total += f'{self.gp}gp'
        if self.pp > 0:
            if total != '':
                total += ', '
            total += f'{self.pp}pp'
        return f'Money({total})'

    def __add__(self, other):
        cp = self.cp + other.cp
        sp = self.sp + other.sp
        ep = self.ep + other.ep
        gp = self.gp + other.gp
        pp = self.pp + other.pp
        return Money(cp=cp, sp=sp, ep=ep, gp=gp, pp=pp)

    def __sub__(self, other):
        cp = self.cp - other.cp
        sp = self.sp - other.sp
        ep = self.ep - other.ep
        gp = self.gp - other.gp
        pp = self.pp - other.pp
        return Money(cp=cp, sp=sp, ep=ep, gp=gp, pp=pp)
