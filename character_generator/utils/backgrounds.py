from character_generator.utils.classes import Background, Money

# Acolyte
# Acolyte skill proficiencies
_acolyte_skill_profs = ['Insight',
                        'Religion']

# Acolyte equipment
_acolyte_equipment = ['5 sticks of incense', 'vestments',
                      'common clothes']
_acolyte_equipment_selections = [['Amulet', 'Emblem', 'Reliquary'],
                                 ['Prayer book', 'Prayer wheel']]

# Acolyte details
_acolyte_details = 'Feature: Shelter of the Faithful'

# Acolyte characteristics
_acolyte_personalities = \
    ['I idolize a particular hero of my faith, and constantly refer to that person\'s deeds and example.',
     'I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.',
     'I see omens in every event and action. The gods try to speak to us, we just need to listen.',
     'Nothing can shake my optimistic attitude.',
     'I quote sacred texts and proverbs in almost every situation.',
     'I misquote sacred texts and proverbs in almost every situation.',
     'I am tolerant of other faiths and respect the worship of other gods.',
     'I am intolerant of other faiths and condemn the worship of other gods.',
     'I\'ve enjoyed fine food, drink, and high society among my temple\'s elite. Rough living grates on me.',
     'I\'ve spent so long in the temple that I have little practical experience dealing with people in the outside world.']
_acolyte_ideals = \
    ['Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)',
     'Charity. I always try to help those in need, no matter what the personal cost. (Good)',
     'Change. We must help bring about the changes the gods are constantly working in the world. (Chaotic)',
     'Power. I hope to one day rise to the top of my faith\'s religious hierarchy. (Lawful)',
     'Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well. (Lawful)',
     'Aspiration. I seek to prove myself worthy of my god\'s favor by matching my actions against his or her teachings.']
_acolyte_bonds = \
    ['I would die to recover an ancient relic of my faith that was lost long ago.',
     'I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.',
     'I owe my life to the priest who took me in when my parents died.',
     'Everything I do is for the common people.',
     'I will do anything to protect the temple where I served.',
     'I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.']
_acolyte_flaws = \
    ['I judge others harshly, and myself even more severely.',
     'I put too much trust in those who wield power within my temple\'s heirarchy.',
     'My piety sometimes leads me to blindly trust those that profess faith in my god.',
     'I am inflexible in my thinking.',
     'I am suspicious of strangers and expect the worst of them.',
     'Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.']

# Acolyte Background
acolyte = \
    Background(name='Acolyte',
               skill_profs=_acolyte_skill_profs,
               tool_profs=None,
               tool_prof_selection=None,
               equipment=_acolyte_equipment,
               equipment_selections=_acolyte_equipment_selections,
               selections=None,
               money=Money(gp=15),
               languages=2,
               details=_acolyte_details,
               personalities=_acolyte_personalities,
               ideals=_acolyte_ideals,
               bonds=_acolyte_bonds,
               flaws=_acolyte_flaws)

# Charlatan
# Charlatan skill proficiencies
_charlatan_skill_profs = ['Deception',
                          'Sleight of Hand']

# Charlatan tool proficiencies
_charlatan_tool_profs = ['disguise kit',
                         'forgery kit']

# Charlatan equipment
_charlatan_equipment = ['fine clothes', 'disguise kit']
_charlatan_equipment_selections = \
    [['ten stoppered bottles filled with colored liquid',
      'a set of weighted dice', 'a deck of marked cards',
      'a signet ring of an imaginary duke']]

# Charlatan selection
_charlatan_selection = \
    ['Favorite scheme: I cheat at games of chance.',
     'Favorite scheme: I shave coins or forge documents.',
     'Favorite scheme: I insinuate myself into people\'s lives to prey on their weakness and secure their fortunes.',
     'Favorite scheme: I put on new identities like clothes.',
     'Favorite scheme: I run sleight-of-hand cons on street corners.',
     'Favorite scheme: I convince people that worthless junk is worth their hard-earned money.']

# Charlatan details
_charlatan_details = 'Feature: False Identity'

# Charlatan characteristics
_charlatan_personalities = \
    ['I fall in and out of love easily, and am always pursuing someone.',
     'I have a joke for every occasion, especially occasions where humor is inappropriate.',
     'Flattery is my preferred trick for getting what I want.',
     'I\'m a born gambler who can\'t resist taking a risk for a potential payoff.',
     'I lie about almost everything, even when there\'s no good reason to.',
     'Sarcasm and insults are my weapons of choice.',
     'I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.',
     'I pocket anything I see that might have some value.']
_charlatan_ideals = \
    ['Independence. I am a free spirit--no one tells me what to do. (Chaotic)',
     'Fairness. I never target people who can\'t afford to lose a few coins. (Lawful)',
     'Charity. I distribute the money I acquire to the people who really need it. (Good)',
     'Creativity. I never run the same con twice. (Chaotic)',
     'Friendship. Material goods come and go. Bonds of friendship last forever. (Good)',
     'Aspiration. I\'m determined to make something of myself.']
_charlatan_bonds = \
    ['I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.',
     'I owe everything to my mentor--a horrible person who\'s probably rotting in jail somewhere.',
     'Somewhere out there, I have a child who doesn\'t know me. I\'m making the world better for him or her.',
     'I come from a noble family, and one day I\'ll reclame my lands and title from those who stole them from me.',
     'A powerful person killed someone I love. Some day soon, I\'ll have my revenge.',
     'I swindled and ruined a person who didn\'t deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.']
_charlatan_flaws = \
    ['I can\'t resist a pretty face.',
     'I\'m always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.',
     'I\'m conviniced that no one could ever fool me the way I fool others.',
     'I\'m too greedy for my own good. I can\'t resist taking a risk if there\'s money involved.',
     'I can\'t resist swindling people who are more powerful than me.',
     'I hate to admit it and will hate myself for it, but I\'ll run and preserve my own hide if the going gets tough.']

# Charlatan Background
charlatan = \
    Background(name='Charlatan',
               skill_profs=_charlatan_skill_profs,
               tool_profs=_charlatan_tool_profs,
               tool_prof_selection=None,
               equipment=_charlatan_equipment,
               equipment_selections=_charlatan_equipment_selections,
               selections=_charlatan_selection,
               money=Money(gp=15),
               languages=0,
               details=_charlatan_details,
               personalities=_charlatan_personalities,
               ideals=_charlatan_ideals,
               bonds=_charlatan_bonds,
               flaws=_charlatan_flaws)

# Criminal
# Criminal skill proficiencies
_criminal_skill_profs = \
    ['Deception',
     'Stealth']

# Criminal tool proficiencies
_criminal_tool_profs = \
    ['thieves\' tools']
_criminal_tool_prof_selection = \
    ['dice set', 'dragonchess set',
     'playing card set',
     'Three-Dragon Ante set']

# Criminal equipment
_criminal_equipment = ['crowbar', 'dark common clothes with hood']

# Criminal selection
_criminal_selection = \
    ['Criminal Specialty: Blackmailer',
     'Criminal Specialty: Burglar',
     'Criminal Specialty: Enforcer',
     'Criminal Specialty: Fence',
     'Criminal Specialty: Highway robber',
     'Criminal Specialty: Hired killer',
     'Criminal Specialty: Pickpocket',
     'Criminal Specialty: Smuggler']

# Criminal details
_criminal_details = 'Feature: Criminal Contact'

# Criminal characteristics
_criminal_personalities = \
    ['I always have a plan for what to do when things go wrong.',
     'I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.',
     'The first thing I do in a new place is note the locations of everything valuable -- or where such things could be hidden.',
     'I would rather make a new friend than a new enemy.',
     'I am incredibly slow to trust. Those who seem the fairest often have the most to hide.',
     'I don\'t pay attention to the risks in a situation. Never tell me the odds.',
     'The best way to get me to do something is to tell me I can\'t do it.',
     'I blow up at the slightest insult.']
_criminal_ideals = \
    ['Honor. I don\'t steal from others in the trade. (Lawful)',
     'Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)',
     'Charity. I steal from the wealthy so that I can help people in need. (Good)',
     'Greed. I will do whatever it takes to become wealthy. (Evil)',
     'People. I\'m loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)',
     'Redemption. There\'s a spark of good in everyone. (Good)']
_criminal_bonds = \
    ['I\'m trying to pay off an old debt I owe to a generous benefactor.',
     'My ill-gotten gains go to support my family.',
     'Something important was taken from me, and I aim to steal it back.',
     'I will become the greatest thief that ever lived.',
     'I\'m guilty of a terrible crime. I hope I can redeem myself for it.',
     'Someone I loved died because of a mistake I made. That will never happen again.']
_criminal_flaws = \
    ['When I see something valuable, I can\'t think about anything but how to steal it.',
     'When faced with a choice between money and my friends, I usually choose the money.',
     'If there\'s a plan, I\'ll forget it. If I don\'t forget it, I\'ll ignore it.',
     'I have a "tell" that reveals when I\'m lying.',
     'I turn tail and run when things look bad.',
     'An innocent person is in prison for a crime that I committed. I\'m okay with that.']

# Criminal Background
criminal = \
    Background(name='Criminal',
               skill_profs=_criminal_skill_profs,
               tool_profs=_criminal_tool_profs,
               tool_prof_selection=_criminal_tool_prof_selection,
               equipment=_criminal_equipment,
               equipment_selections=None,
               selections=_criminal_selection,
               money=Money(gp=15),
               languages=0,
               details=_criminal_details,
               personalities=_criminal_personalities,
               ideals=_criminal_ideals,
               bonds=_criminal_bonds,
               flaws=_criminal_flaws)
