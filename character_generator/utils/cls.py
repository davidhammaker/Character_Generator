from character_generator.utils.classes import Cls, Archetype

# Barbarian
# Barbarian archetypes
_barbarian_archetypes = [Archetype('Path of the Berserker'),
                         Archetype('Path of the Totem Warrior')]

# Barbarian Cls
barbarian = Cls(name='Barbarian',
                archetypes=_barbarian_archetypes)


# Bard
# Bard archetypes
_bard_archetypes = [Archetype('College of Lore'),
                    Archetype('College of Valor')]

# Bard Cls
bard = Cls(name='Bard',
           archetypes=_bard_archetypes)


# Cleric
# Cleric archetypes
_cleric_archetypes = [Archetype('Life Domain'),
                      Archetype('Light Domain'),
                      Archetype('Nature Domain'),
                      Archetype('Tempest Domain'),
                      Archetype('Trickery Domain'),
                      Archetype('War Domain')]

# Cleric Cls
cleric = Cls(name='Cleric',
             archetypes=_cleric_archetypes)


# Druid
# Druid Archetypes
_druid_archetypes = [Archetype(name='Circle of the Land',
                               subcategories=['Arctic',
                                              'Coast',
                                              'Desert',
                                              'Forest',
                                              'Grassland',
                                              'Mountain',
                                              'Swamp',
                                              'Underdark']),
                     Archetype(name='Circle of the Moon')]

# Druid Cls
druid = Cls(name='Druid',
            archetypes=_druid_archetypes)


# Fighter
# Fighter Archetypes
_fighter_archetypes = [Archetype('Champion'),
                       Archetype('Battle Master'),
                       Archetype('Eldritch Knight')]

# Fighter Cls
fighter = Cls(name='Fighter',
              archetypes=_fighter_archetypes)


# Monk
# Monk Archetypes
_monk_archetypes = [Archetype('Way of the Open Hand'),
                    Archetype('Way of Shadow'),
                    Archetype('Way of the Four Elements')]

# Monk Cls
monk = Cls(name='Monk',
           archetypes=_monk_archetypes)

# Paladin
# Paladin Archetypes
_paladin_archetypes = [Archetype('Oauth of Devotion'),
                       Archetype('Oauth of the Ancients'),
                       Archetype('Oath of Vengeance')]

# Paladin Cls
paladin = Cls(name='Paladin',
              archetypes=_paladin_archetypes)


# Ranger
# Ranger Archetypes
_ranger_archetypes = [Archetype('Hunter'), Archetype('Beast Master')]

# Ranger Cls
ranger = Cls(name='Ranger',
             archetypes=_ranger_archetypes)


# Rogue
# Rogue Archetypes
_rogue_archetypes = [Archetype('Thief'),
                     Archetype('Assassin'),
                     Archetype('Arcane Trickster')]

# Rogue Cls
rogue = Cls(name='Rogue',
            archetypes=_rogue_archetypes)


# Sorcerer
# Sorcerer Archetypes
_sorcerer_archetypes = [Archetype(name='Draconic Bloodline',
                                  subcategories=['Black',
                                                 'Blue',
                                                 'Brass',
                                                 'Bronze',
                                                 'Copper',
                                                 'Gold',
                                                 'Green',
                                                 'Red',
                                                 'Silver',
                                                 'White']),
                        Archetype(name='Wild Magic')]

# Sorcerer Cls
sorcerer = Cls(name='Sorcerer',
               archetypes=_sorcerer_archetypes)


# Warlock
# Warlock Archetypes
_warlock_archetypes = [Archetype('The Archfey'),
                       Archetype('The Fiend'),
                       Archetype('The Great Old One')]

# Warlock Cls
warlock = Cls(name='Warlock',
              archetypes=_warlock_archetypes)


# Wizard
# Wizard Archetypes
_wizard_archetypes = [Archetype('School of Abjuration'),
                      Archetype('School of Conjuration'),
                      Archetype('School of Divination'),
                      Archetype('School of Enchantment'),
                      Archetype('School of Evocation'),
                      Archetype('School of Illusion'),
                      Archetype('School of Necromancy'),
                      Archetype('School of Transmutation')]

# Wizard Cls
wizard = Cls(name='Wizard',
             archetypes=_wizard_archetypes)
