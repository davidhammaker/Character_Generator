from character_generator.utils.classes import Race, Subrace

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
                            sizes=
                            _dwarf_subrace_spec[subrace]['sizes']))

# Dwarf ages
_dwarf_age_range = [1, 350]
_dwarf_age_range_prime = [50, 100]

# Dwarf names
_dwarf_names = {'Male': ['Adrik', 'Albrich', 'Baern', 'Barendd',
                         'Brottor', 'Bruenor', 'Dain', 'Darrak',
                         'Delg', 'Eberk', 'Einkil', 'Fargrim',
                         'Flint', 'Gardain', 'Harbek', 'Kildrak',
                         'Morgran', 'Orsik', 'Oskar', 'Rangrim',
                         'Rurik', 'Taklinn', 'Thoradin', 'Thorin',
                         'Tordek', 'Traubon', 'Travok', 'Ulfgar',
                         'Veit', 'Vondal'],
                'Female': ['Amber', 'Artin', 'Audhild', 'Bardryn',
                           'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn',
                           'Finellen', 'Gunnloda', 'Gurdis',
                           'Helja', 'Hlin', 'Kathra', 'Kristryd',
                           'Ilde', 'Liftrasa', 'Mardred',
                           'Riswynn', 'Sannl', 'Torbera', 'Torgga',
                           'Vistra'],
                'Family': ['Balderk', 'Battlehammer', 'Brawnanvil',
                           'Dankil', 'Fireforge', 'Frostbeard',
                           'Gorunn', 'Holderhek', 'Ironfist',
                           'Loderr', 'Lutgehr', 'Rumnaheim',
                           'Strakeln', 'Torunn', 'Ungart']}

# Dwarf race
dwarves = Race(name='Dwarves',
               age_range=_dwarf_age_range,
               age_range_prime=_dwarf_age_range_prime,
               names=_dwarf_names,
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

# Elf names
_elf_names = {'Male': ['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust',
                       'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan',
                       'Erevan', 'Galinndan', 'Hadarai', 'Heian',
                       'Himo', 'Immeral', 'Ivellios', 'Laucian',
                       'Mindartis', 'Paelias', 'Peren', 'Quarion',
                       'Riardon', 'Rolen', 'Soveliss', 'Thamior',
                       'Tharivol', 'Theren', 'Varis'],
              'Female': ['Adrie', 'Althaea', 'Anastrianna', 'Andraste',
                         'Antinua', 'Bethrynna', 'Birel', 'Caelynn',
                         'Drusilia', 'Enna', 'Felosial', 'Ielenia',
                         'Jelenneth', 'Keyleth', 'Leshanna', 'Lia',
                         'Meriele', 'Mialee', 'Naivara', 'Quelenna',
                         'Quillathe', 'Sariel', 'Shanairra', 'Shava',
                         'Silaqui', 'Theirastra', 'Thia', 'Vadania',
                         'Valanthe', 'Xanaphia'],
              'Family': ['Amakiir', 'Amastacia', 'Galanodel',
                         'Holimion', 'Ilphelkiin', 'Liadon',
                         'Melamine', 'Naïlo', 'Siannodel',
                         'Xiloscient'],
              'Child': ['Ara', 'Bryn', 'Del', 'Eryn', 'Faen', 'Innil',
                        'Lael', 'Mella', 'Naill', 'Naeris', 'Phann',
                        'Rael', 'Rinn', 'Sai', 'Syllin', 'Thia',
                        'Vall']}

# Elf race
elves = Race(name='Elves',
             age_range=_elf_age_range,
             age_range_prime=_elf_age_range_prime,
             names=_elf_names,
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

# Halfling names
_halfling_names = {'Male': ['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon',
                            'Errich', 'Finnan', 'Garret', 'Lindal',
                            'Lyle', 'Merric', 'Milo', 'Osborn',
                            'Perrin', 'Reed', 'Roscoe', 'Wellby'],
                   'Female': ['Andry', 'Bree', 'Callie', 'Cora',
                              'Euphemia', 'Jillian', 'Kithri',
                              'Lavinia', 'Lidda', 'Merla', 'Nedda',
                              'Paela', 'Portia', 'Seraphina', 'Shaena',
                              'Trym', 'Vani', 'Verna'],
                   'Family': ['Brushgather', 'Goodbarrel',
                              'Greenbottle', 'High-hill', 'Hilltopple',
                              'Leagallow', 'Tealeaf', 'Thorngate',
                              'Tosscobble', 'Underbough']}

# Halfling race
halflings = Race(name='Halflings',
                 age_range=_halfling_age_range,
                 age_range_prime=_halfling_age_range_prime,
                 names=_halfling_names,
                 sizes=_halfling_sizes,
                 subraces=_halfling_subraces)


# Humans
# Human subraces
_human_subrace_spec = \
    {'Standard Calishite': {'Male': ['Aseir', 'Bardeid', 'Haseid',
                                     'Khemed', 'Mehmed', 'Suleiman',
                                     'Zasheir'],
                            'Female': ['Atala', 'Ceidil', 'Hama',
                                       'Jasmal', 'Meilil', 'Seipora',
                                       'Yasheira', 'Zasheida'],
                            'Family': ['Basha', 'Dumein', 'Jassan',
                                       'Khalid', 'Mostana', 'Pashar',
                                       'Rein']},
     'Standard Chondathan': {'Male': ['Darvin', 'Dorn', 'Evendur',
                                      'Gorstag', 'Grim', 'Helm',
                                      'Malark', 'Morn', 'Randal',
                                      'Stedd'],
                             'Female': ['Arveene', 'Esvele', 'Jhessail',
                                        'Kerri', 'Lureene', 'Miri',
                                        'Rowan', 'Shandri', 'Tessele'],
                             'Family': ['Amblecrown', 'Buckman',
                                        'Dundragon', 'Evenwood',
                                        'Greycastle', 'Tallstag']},
     'Standard Damaran': {'Male': ['Bor', 'Fodel', 'Glar', 'Grigor',
                                   'Igan', 'Ivor', 'Kosef', 'Mival',
                                   'Orel', 'Pavel', 'Sergor'],
                          'Female': ['Alethra', 'Kara', 'Katernin',
                                     'Mara', 'Natali', 'Olma', 'Tana',
                                     'Zora'],
                          'Family': ['Bersk', 'Chernin', 'Dotsk',
                                     'Kulenov', 'Marsk', 'Nemetsk',
                                     'Shemov', 'Starag']},
     'Standard Illuskan': {'Male': ['Ander', 'Blath', 'Bran', 'Frath',
                                    'Geth', 'Lander', 'Luth', 'Malcer',
                                    'Stor', 'Taman', 'Urth'],
                           'Female': ['Amafrey', 'Betha', 'Cefrey',
                                      'Kethra', 'Mara', 'Olga',
                                      'Silifrey', 'Westra'],
                           'Family': ['Brightwood', 'Helder',
                                      'Hornraven', 'Lackman',
                                      'Stormwind', 'Windriver']},
     'Standard Mulan': {'Male': ['Aoth', 'Bareris', 'Ehput-Ki',
                                 'Kethoth', 'Mumed', 'Ramas',
                                 'So-Kehur', 'Thazar-De', 'Urhur'],
                        'Female': ['Arizima', 'Chathi', 'Nephis',
                                   'Nulara', 'Murithi', 'Sefris',
                                   'Thola', 'Umara', 'Zolis'],
                        'Family': ['Ankhalab', 'Anskuld', 'Fezim',
                                   'Halpet', 'Nathandem', 'Sepret',
                                   'Uuthrakt']},
     'Standard Rashemi': {'Male': ['Borivik', 'Faurgar', 'Jandar',
                                   'Kanithar', 'Madislak', 'Ramevik',
                                   'Shaumar', 'Vladislav'],
                          'Female': ['Fyevarra', 'Hulmarra', 'Immith',
                                     'Imzel', 'Navarra', 'Shevarra',
                                     'Tammith', 'Yuldra'],
                          'Family': ['Chergoba', 'Dyernina',
                                     'Iltazyara', 'Murnyethara',
                                     'Stayanoga', 'Ulmokina']},
     'Standard Shou': {'Male': ['An', 'Chen', 'Chi', 'Fai', 'Jiang',
                                'Jun', 'Lian', 'Long', 'Meng', 'On',
                                'Shan', 'Shui', 'Wen'],
                       'Female': ['Bai', 'Chao', 'Jia', 'Lei', 'Mei',
                                  'Qiao', 'Shui', 'Tai'],
                       'Family': ['Chien', 'Huang', 'Kao', 'Kung',
                                  'Lao', 'Ling', 'Mei', 'Pin', 'Shin',
                                  'Sum', 'Tan', 'Wan']},
     'Standard Tethyrian': {'Male': ['Darvin', 'Dorn', 'Evendur',
                                     'Gorstag', 'Grim', 'Helm',
                                     'Malark', 'Morn', 'Randal',
                                     'Stedd'],
                            'Female': ['Arveene', 'Esvele', 'Jhessail',
                                       'Kerri', 'Lureene', 'Miri',
                                       'Rowan', 'Shandri', 'Tessele'],
                            'Family': ['Amblecrown', 'Buckman',
                                       'Dundragon', 'Evenwood',
                                       'Greycastle', 'Tallstag']},
     'Standard Turami': {'Male': ['Anton', 'Diero', 'Marcon', 'Pieron',
                                  'Ricardo', 'Romero', 'Salazar',
                                  'Umbero'],
                         'Female': ['Balama', 'Dona', 'Faila', 'Jalana',
                                    'Luisa', 'Marta', 'Quara', 'Selise',
                                    'Vonda'],
                         'Family': ['Agosto', 'Astorio', 'Calabra',
                                    'Domine', 'Falone', 'Marivaldi',
                                    'Pisacar', 'Ramondo']},
     'Variant Calishite': {'Male': ['Aseir', 'Bardeid', 'Haseid',
                                    'Khemed', 'Mehmed', 'Suleiman',
                                    'Zasheir'],
                           'Female': ['Atala', 'Ceidil', 'Hama',
                                      'Jasmal', 'Meilil', 'Seipora',
                                      'Yasheira', 'Zasheida'],
                           'Family': ['Basha', 'Dumein', 'Jassan',
                                      'Khalid', 'Mostana', 'Pashar',
                                      'Rein']},
     'Variant Chondathan': {'Male': ['Darvin', 'Dorn', 'Evendur',
                                     'Gorstag', 'Grim', 'Helm',
                                     'Malark', 'Morn', 'Randal',
                                     'Stedd'],
                            'Female': ['Arveene', 'Esvele', 'Jhessail',
                                       'Kerri', 'Lureene', 'Miri',
                                       'Rowan', 'Shandri', 'Tessele'],
                            'Family': ['Amblecrown', 'Buckman',
                                       'Dundragon', 'Evenwood',
                                       'Greycastle', 'Tallstag']},
     'Variant Damaran': {'Male': ['Bor', 'Fodel', 'Glar', 'Grigor',
                                  'Igan', 'Ivor', 'Kosef', 'Mival',
                                  'Orel', 'Pavel', 'Sergor'],
                         'Female': ['Alethra', 'Kara', 'Katernin',
                                    'Mara', 'Natali', 'Olma', 'Tana',
                                    'Zora'],
                         'Family': ['Bersk', 'Chernin', 'Dotsk',
                                    'Kulenov', 'Marsk', 'Nemetsk',
                                    'Shemov', 'Starag']},
     'Variant Illuskan': {'Male': ['Ander', 'Blath', 'Bran', 'Frath',
                                   'Geth', 'Lander', 'Luth', 'Malcer',
                                   'Stor', 'Taman', 'Urth'],
                          'Female': ['Amafrey', 'Betha', 'Cefrey',
                                     'Kethra', 'Mara', 'Olga',
                                     'Silifrey', 'Westra'],
                          'Family': ['Brightwood', 'Helder',
                                     'Hornraven', 'Lackman',
                                     'Stormwind', 'Windriver']},
     'Variant Mulan': {'Male': ['Aoth', 'Bareris', 'Ehput-Ki',
                                'Kethoth', 'Mumed', 'Ramas',
                                'So-Kehur', 'Thazar-De', 'Urhur'],
                       'Female': ['Arizima', 'Chathi', 'Nephis',
                                  'Nulara', 'Murithi', 'Sefris',
                                  'Thola', 'Umara', 'Zolis'],
                       'Family': ['Ankhalab', 'Anskuld', 'Fezim',
                                  'Halpet', 'Nathandem', 'Sepret',
                                  'Uuthrakt']},
     'Variant Rashemi': {'Male': ['Borivik', 'Faurgar', 'Jandar',
                                  'Kanithar', 'Madislak', 'Ramevik',
                                  'Shaumar', 'Vladislav'],
                         'Female': ['Fyevarra', 'Hulmarra', 'Immith',
                                    'Imzel', 'Navarra', 'Shevarra',
                                    'Tammith', 'Yuldra'],
                         'Family': ['Chergoba', 'Dyernina',
                                    'Iltazyara', 'Murnyethara',
                                    'Stayanoga', 'Ulmokina']},
     'Variant Shou': {'Male': ['An', 'Chen', 'Chi', 'Fai', 'Jiang',
                               'Jun', 'Lian', 'Long', 'Meng', 'On',
                               'Shan', 'Shui', 'Wen'],
                      'Female': ['Bai', 'Chao', 'Jia', 'Lei', 'Mei',
                                 'Qiao', 'Shui', 'Tai'],
                      'Family': ['Chien', 'Huang', 'Kao', 'Kung',
                                 'Lao', 'Ling', 'Mei', 'Pin', 'Shin',
                                 'Sum', 'Tan', 'Wan']},
     'Variant Tethyrian': {'Male': ['Darvin', 'Dorn', 'Evendur',
                                    'Gorstag', 'Grim', 'Helm',
                                    'Malark', 'Morn', 'Randal',
                                    'Stedd'],
                           'Female': ['Arveene', 'Esvele', 'Jhessail',
                                      'Kerri', 'Lureene', 'Miri',
                                      'Rowan', 'Shandri', 'Tessele'],
                           'Family': ['Amblecrown', 'Buckman',
                                      'Dundragon', 'Evenwood',
                                      'Greycastle', 'Tallstag']},
     'Variant Turami': {'Male': ['Anton', 'Diero', 'Marcon', 'Pieron',
                                 'Ricardo', 'Romero', 'Salazar',
                                 'Umbero'],
                        'Female': ['Balama', 'Dona', 'Faila', 'Jalana',
                                   'Luisa', 'Marta', 'Quara', 'Selise',
                                   'Vonda'],
                        'Family': ['Agosto', 'Astorio', 'Calabra',
                                   'Domine', 'Falone', 'Marivaldi',
                                   'Pisacar', 'Ramondo']}}
_human_subraces = [Subrace(name=subrace,
                           names=_human_subrace_spec[subrace])
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

# Dragonborn names
_dragonborn_names = {'Male': ['Arjhan', 'Balasar', 'Bharash', 'Donaar',
                              'Ghesh', 'Heskan', 'Kriv', 'Medrash',
                              'Mehen', 'Nadarr', 'Pandjed', 'Patrin',
                              'Rhogar', 'Shamash', 'Shedinn', 'Tarhun',
                              'Torinn'],
                     'Female': ['Akra', 'Biri', 'Daar', 'Farideh',
                                'Harann', 'Havilar', 'Jheri', 'Kava',
                                'Korinn', 'Mishann', 'Nala', 'Perra',
                                'Raiann', 'Sora', 'Surina', 'Thava',
                                'Uadjit'],
                     'Family': ['Clethtinthiallor', 'Daardendrian',
                                'Delmirev', 'Drachadandion',
                                'Fenkenkabradon', 'Kepeshkmolik',
                                'Kerrhylon', 'Kimbatuul',
                                'Linxakasendalor', 'Myastan',
                                'Nemmonis', 'Norixius',
                                'Ophinshtalajiir', 'Prexijandilin',
                                'Shestendiliath', 'Turnuroth',
                                'Verthisathurgiesh', 'Yarjerit']}

# Dragonborn race
dragonborn = Race(name='Dragonborn',
                  age_range=_dragonborn_age_range,
                  age_range_prime=_dragonborn_age_range_prime,
                  names=_dragonborn_names,
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

# Gnome names
_gnome_names = {'Male': ['Alston', 'Alvyn', 'Boddynock', 'Brocc',
                         'Burgell', 'Dimble', 'Eldon', 'Erky', 'Fonkin',
                         'Frug', 'Gerbo', 'Gimble', 'Glim', 'Jebeddo',
                         'Kellen', 'Namfoodle', 'Orryn', 'Roondar',
                         'Seebo', 'Sindri', 'Warryn', 'Wrenn', 'Zook'],
                'Female': ['Bimpnottin', 'Breena', 'Caramip', 'Carlin',
                           'Donella', 'Duvamil', 'Ella', 'Ellyjobell',
                           'Ellywick', 'Lilli', 'Loopmottin', 'Lorilla',
                           'Mardnab', 'Nissa', 'Nyx', 'Oda', 'Orla',
                           'Roywyn', 'Shamil', 'Tana', 'Waywocket',
                           'Zanna'],
                'Family': ['Beren', 'Daergel', 'Folkor', 'Garrick',
                           'Nackle', 'Murnig', 'Ningel', 'Raulnor',
                           'Scheppen', 'Timbers', 'Turen'],
                'Nickname': ['Aleslosh', 'Ashhearth', 'Badger', 'Cloak',
                             'Doublelock', 'Filchbatter', 'Fnipper',
                             'Ku', 'Nim', 'Oneshoe', 'Pock',
                             'Sparklegem', 'Stumbleduck']}

# Gnome race
gnomes = Race(name='Gnomes',
              age_range=_gnome_age_range,
              age_range_prime=_gnome_age_range_prime,
              names=_gnome_names,
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

# Half-Elf names
_half_elf_names = {'Male': [],
                   'Female': []}
# Retrieve human names
for subrace in humans.names:
    _half_elf_names['Male'] += humans.names[subrace]['Male']
    _half_elf_names['Female'] += humans.names[subrace]['Female']
# Retrieve elf names
_half_elf_names['Male'] += elves.names['Male']
_half_elf_names['Female'] += elves.names['Female']
# Eliminate duplicate names
_half_elf_names['Male'] = list(set(_half_elf_names['Male']))
_half_elf_names['Female'] = list(set(_half_elf_names['Female']))

# Half-Elf race
half_elves = Race(name='Half-Elves',
                  age_range=_half_elf_age_range,
                  age_range_prime=_half_elf_age_range_prime,
                  names=_half_elf_names,
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

# Half-Orc names
_half_orc_names = {'Male': ['Dench', 'Feng', 'Gell', 'Henk', 'Holg',
                            'Imsh', 'Keth', 'Mhurren', 'Ront', 'Shump',
                            'Thokk'],
                   'Female': ['Baggi', 'Emen', 'Engong', 'Kansif',
                              'Myev', 'Neega', 'Ovak', 'Ownka',
                              'Shautha', 'Sutha', 'Vola', 'Volen',
                              'Yevelda']}

# Half-Orc race
half_orcs = Race(name='Half-Orcs',
                 age_range=_half_orc_age_range,
                 age_range_prime=_half_orc_age_range_prime,
                 names=_half_orc_names,
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

# Tiefling names
_tiefling_names = {'Male': ['Akmenos', 'Amnon', 'Barakas', 'Damakos',
                            'Ekemon', 'Iados', 'Kairon', 'Leucis',
                            'Melech', 'Mordai', 'Morthos', 'Pelaios',
                            'Skamos', 'Therai'],
                   'Female': ['Akta', 'Anakis', 'Bryseis', 'Criella',
                              'Damaia', 'Ea', 'Kallista', 'Lerissa',
                              'Makaria', 'Nemeia', 'Orianna', 'Phelaia',
                              'Rieta'],
                   'Virtue': ['Art', 'Carrion', 'Chant', 'Creed',
                              'Despair', 'Excellence', 'Fear', 'Glory',
                              'Hope', 'Ideal', 'Music', 'Nowhere',
                              'Open', 'Poetry', 'Quest', 'Random',
                              'Reverence', 'Sorrow', 'Temerity',
                              'Torment', 'Weary']}

# Tiefling race
tieflings = Race(name='Tieflings',
                 age_range=_tiefling_age_range,
                 age_range_prime=_tiefling_age_range_prime,
                 names=_tiefling_names,
                 sizes=_tiefling_sizes,
                 subraces=None)
