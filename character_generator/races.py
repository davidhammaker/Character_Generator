from classes import Race, Subrace

# Dwarves
# Dwarf subraces
_dwarf_subrace_spec = {'Hill Dwarf': {'sizes': {'base_height': 44,
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
                                                    'wt_mod_value': 6}}}
_dwarf_subraces = []
for subrace in _dwarf_subrace_spec:
    _dwarf_subraces.append(Subrace
                           (name=subrace,
                            sizes=_dwarf_subrace_spec[subrace]['sizes']))

# Dwarf ages
_dwarf_age_range = [1, 350]
_dwarf_age_range_prime = [50, 100]

# Dwarf race
dwarves = Race(name='Dwarves',
               age_range=_dwarf_age_range,
               age_range_prime=_dwarf_age_range_prime,
               sizes=None,
               subraces=_dwarf_subraces)


# Elves
# Elf subraces
_elf_subrace_spec = {'High Elf': {'types': ['Sun Elf',
                                            'Moon Elf'],
                                  'sizes': {'base_height': 54,
                                            'ht_mod_count': 2,
                                            'ht_mod_value': 10,
                                            'base_weight': 90,
                                            'wt_mod_count': 1,
                                            'wt_mod_value': 4}},
                     'Wood Elf': {'types': None,
                                  'sizes': {'base_height': 54,
                                            'ht_mod_count': 2,
                                            'ht_mod_value': 10,
                                            'base_weight': 100,
                                            'wt_mod_count': 1,
                                            'wt_mod_value': 4}},
                     'Drow': {'types': None,
                              'sizes': {'base_height': 53,
                                        'ht_mod_count': 2,
                                        'ht_mod_value': 6,
                                        'base_weight': 75,
                                        'wt_mod_count': 1,
                                        'wt_mod_value': 6}}}
_elf_subraces = []
for subrace in _elf_subrace_spec:
    _elf_subraces.append(Subrace
                         (name=subrace,
                          sizes=_elf_subrace_spec[subrace]['sizes'],
                          types=_elf_subrace_spec[subrace]['types']))

# Elf ages
_elf_age_range = [1, 750]
_elf_age_range_prime = [100, 150]

# Elf race
elves = Race(name='Elves',
             age_range=_elf_age_range,
             age_range_prime=_elf_age_range_prime,
             sizes=None,
             subraces=_elf_subraces)


# Halflings
# Halfling subraces
_halfling_subrace_spec = ['Lightfoot', 'Stout']
_halfling_subraces = [Subrace(name=subrace)
                      for subrace in _halfling_subrace_spec]

# Halfling sizes
_halfling_sizes = {'base_height': 31,
                   'ht_mod_count': 2,
                   'ht_mod_value': 4,
                   'base_weight': 35,
                   'wt_mod_count': 1,
                   'wt_mod_value': 1}

# Halfling ages
_halfling_age_range = [1, 150]
_halfling_age_range_prime = [20, 40]

# Halfling race
halflings = Race(name='Halflings',
                 age_range=_halfling_age_range,
                 age_range_prime=_halfling_age_range_prime,
                 sizes=_halfling_sizes,
                 subraces=_halfling_subraces)


# Humans
# Human subraces
_human_subrace_spec = ['Standard Calishite',
                       'Standard Chondathan',
                       'Standard Damaran',
                       'Standard Illuskan',
                       'Standard Mulan',
                       'Standard Rashemi',
                       'Standard Shou',
                       'Standard Tethyrian',
                       'Standard Turami',
                       'Variant Calishite',
                       'Variant Chondathan',
                       'Variant Damaran',
                       'Variant Illuskan',
                       'Variant Mulan',
                       'Variant Rashemi',
                       'Variant Shou',
                       'Variant Tethyrian',
                       'Variant Turami']
_human_subraces = [Subrace(name=subrace)
                   for subrace in _human_subrace_spec]

# Human sizes
_human_sizes = {'base_height': 56,
                'ht_mod_count': 2,
                'ht_mod_value': 10,
                'base_weight': 110,
                'wt_mod_count': 2,
                'wt_mod_value': 4}

# Human ages
_human_age_range = [1, 100]
_human_age_range_prime = [17, 30]

# Human race
humans = Race(name='Humans',
              age_range=_human_age_range,
              age_range_prime=_human_age_range_prime,
              sizes=_human_sizes,
              subraces=_human_subraces)


# Dragonborn
# Dragonborn sizes
_dragonborn_sizes = {'base_height': 66,
                     'ht_mod_count': 2,
                     'ht_mod_value': 8,
                     'base_weight': 175,
                     'wt_mod_count': 2,
                     'wt_mod_value': 6}

# Dragonborn ages
_dragonborn_age_range = [1, 80]
_dragonborn_age_range_prime = [15, 25]

# Dragonborn race
dragonborn = Race(name='Dragonborn',
                  age_range=_dragonborn_age_range,
                  age_range_prime=_dragonborn_age_range_prime,
                  sizes=_dragonborn_sizes,
                  subraces=None)


# Gnomes
# Gnome subraces
_gnome_subraces_spec = ['Forest Gnome', 'Rock Gnome']
_gnome_subraces = [Subrace(name=subrace)
                   for subrace in _gnome_subraces_spec]

# Gnome sizes
_gnome_sizes = {'base_height': 35,
                'ht_mod_count': 2,
                'ht_mod_value': 4,
                'base_weight': 35,
                'wt_mod_count': 1,
                'wt_mod_value': 1}

# Gnome ages
_gnome_age_range = [1, 500]
_gnome_age_range_prime = [40, 60]

# Gnome race
gnomes = Race(name='Gnomes',
              age_range=_gnome_age_range,
              age_range_prime=_gnome_age_range_prime,
              sizes=_gnome_sizes,
              subraces=_gnome_subraces)


# Half-Elves
# Half-Elf sizes
_half_elf_sizes = {'base_height': 57,
                   'ht_mod_count': 2,
                   'ht_mod_value': 8,
                   'base_weight': 110,
                   'wt_mod_count': 2,
                   'wt_mod_value': 4}

# Half-Elf ages
_half_elf_age_range = [1, 180],
_half_elf_age_range_prime = [20, 40]

# Half-Elf race
half_elves = Race(name='Half-Elves',
                  age_range=_half_elf_age_range,
                  age_range_prime=_half_elf_age_range_prime,
                  sizes=_half_elf_sizes,
                  subraces=None)


# Half-Orcs
# Half-Orc sizes
_half_orc_sizes = {'base_height': 58,
                   'ht_mod_count': 2,
                   'ht_mod_value': 10,
                   'base_weight': 140,
                   'wt_mod_count': 2,
                   'wt_mod_value': 6}

# Half-Orc ages
_half_orc_age_range = [1, 75],
_half_orc_age_range_prime = [14, 25]

# Half-Orc race
half_orcs = Race(name='Half-Orcs',
                 age_range=_half_orc_age_range,
                 age_range_prime=_half_orc_age_range_prime,
                 sizes=_half_orc_sizes,
                 subraces=None)


# Tieflings
# Tiefling sizes
_tiefling_sizes = {'base_height': 57,
                   'ht_mod_count': 2,
                   'ht_mod_value': 8,
                   'base_weight': 110,
                   'wt_mod_count': 2,
                   'wt_mod_value': 4}

# Tiefling ages
_tiefling_age_range = [1, 110],
_tiefling_age_range_prime = [17, 30]

# Tiefling race
tieflings = Race(name='Tieflings',
                 age_range=_tiefling_age_range,
                 age_range_prime=_tiefling_age_range_prime,
                 sizes=_tiefling_sizes,
                 subraces=None)
