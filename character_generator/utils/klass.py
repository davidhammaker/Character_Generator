from character_generator.utils.classes import Klass, Archetype

# Barbarian
# Barbarian archetypes
_barbarian_archetypes = [Archetype('Path of the Berserker'),
                         Archetype('Path of the Totem Warrior')]

# Barbarian Klass
barbarian = Klass(name='Barbarian',
                  archetypes=_barbarian_archetypes,
                  archetype_level_requirement=3)


# Bard
# Bard archetypes
_bard_archetypes = [Archetype('College of Lore'),
                    Archetype('College of Valor')]

# Bard Klass
bard = Klass(name='Bard',
             archetypes=_bard_archetypes,
             archetype_level_requirement=3)


# Cleric
# Cleric archetypes
_cleric_archetypes = [Archetype('Life Domain'),
                      Archetype('Light Domain'),
                      Archetype('Nature Domain'),
                      Archetype('Tempest Domain'),
                      Archetype('Trickery Domain'),
                      Archetype('War Domain')]

# Cleric Klass
cleric = Klass(name='Cleric',
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

# Druid Klass
druid = Klass(name='Druid',
              archetypes=_druid_archetypes,
              archetype_level_requirement=2)


# Fighter
# Fighter Archetypes
_fighter_archetypes = [Archetype('Champion'),
                       Archetype('Battle Master'),
                       Archetype('Eldritch Knight')]

# Fighter Klass
fighter = Klass(name='Fighter',
                archetypes=_fighter_archetypes,
                archetype_level_requirement=3)


# Monk
# Monk Archetypes
_monk_archetypes = [Archetype('Way of the Open Hand'),
                    Archetype('Way of Shadow'),
                    Archetype('Way of the Four Elements')]

# Monk Klass
monk = Klass(name='Monk',
             archetypes=_monk_archetypes,
             archetype_level_requirement=3)

# Paladin
# Paladin Archetypes
_paladin_archetypes = [Archetype('Oauth of Devotion'),
                       Archetype('Oauth of the Ancients'),
                       Archetype('Oath of Vengeance')]

# Paladin Klass
paladin = Klass(name='Paladin',
                archetypes=_paladin_archetypes,
                archetype_level_requirement=3)


# Ranger
# Ranger Archetypes
_ranger_archetypes = [Archetype('Hunter'), Archetype('Beast Master')]

# Ranger Klass
ranger = Klass(name='Ranger',
               archetypes=_ranger_archetypes,
               archetype_level_requirement=3)


# Rogue
# Rogue Archetypes
_rogue_archetypes = [Archetype('Thief'),
                     Archetype('Assassin'),
                     Archetype('Arcane Trickster')]

# Rogue Klass
rogue = Klass(name='Rogue',
              archetypes=_rogue_archetypes,
              archetype_level_requirement=3)


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

# Sorcerer Klass
sorcerer = Klass(name='Sorcerer',
                 archetypes=_sorcerer_archetypes)


# Warlock
# Warlock Archetypes
_warlock_archetypes = [Archetype('The Archfey'),
                       Archetype('The Fiend'),
                       Archetype('The Great Old One')]

# Warlock Klass
warlock = Klass(name='Warlock',
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

# Wizard Klass
wizard = Klass(name='Wizard',
               archetypes=_wizard_archetypes,
               archetype_level_requirement=2)
