from character_generator.utils.classes import Background, Money

# Items common to more than one Background
_instruments = \
    ['bagpipes',
     'drum',
     'dulcimer',
     'fluit',
     'lute',
     'lyre',
     'horn',
     'pan flute',
     'shawm',
     'viol']
_artisan_tools = \
    ['alchemist\'s supplies',
     'brewer\'s supplies',
     'calligrapher\'s supplies',
     'carpenter\'s tools',
     'cartographer\'s tools',
     'cobbler\'s tools',
     'cook\'s utensils',
     'glassblower\'s tools',
     'jeweler\'s tools',
     'leatherworker\'s tools',
     'mason\'s tools',
     'painter\'s supplies',
     'potter\'s tools',
     'smith\'s tools',
     'tinker\'s tools',
     'weaver\'s tools',
     'woodcarver\'s tools']

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
_acolyte_details = 'Feature: Shelter of the Faithful (pg. 127)'

# Acolyte characteristics
_acolyte_personalities = \
    ['I idolize a particular hero of my faith, and constantly refer to that person\'s deeds and example.',
     'I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.',
     'I see omens in every event and action. The gods try to speak to us, we just need to listen.',
     'Nothing can shake my optimistic attitude.',
     'I quote (or misquote) sacred texts and proverbs in almost every situation.',
     'I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.',
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
_charlatan_details = 'Feature: False Identity (pg. 128)'

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
    ['dice set',
     'dragonchess set',
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
_criminal_details = 'Feature: Criminal Contact (pg. 129)'

# Criminal characteristics
_criminal_personalities = \
    ['I always have a plan for what to do when things go wrong.',
     'I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.',
     'The first thing I do in a new place is note the locations of everything valuable--or where such things could be hidden.',
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


# Entertainer
# Entertainer skill proficiencies
_entertainer_skill_profs = \
    ['Acrobatics',
     'Performance']

# Entertainer tool proficiencies
_entertainer_tool_profs = \
    ['disguise kit']
_entertainer_tool_prof_selection = \
    _instruments

# Entertainer equipment
_entertainer_equipment = ['costume']
_entertainer_equipment_selections = \
    [[instrument for instrument in _entertainer_tool_prof_selection],
     ['love letter (admirer\'s favor)',
      'lock of hair (admirer\'s favor)',
      'trinket (admirer\'s favor)']]

# Entertainer selection
_entertainer_selection = \
    ['Entertainer Routine: Actor',
     'Entertainer Routine: Dancer',
     'Entertainer Routine: Fire-eater',
     'Entertainer Routine: Jester',
     'Entertainer Routine: Juggler',
     'Entertainer Routine: Instrumentalist',
     'Entertainer Routine: Poet',
     'Entertainer Routine: Singer',
     'Entertainer Routine: Storyteller',
     'Entertainer Routine: Tumbler']

# Entertainer details
_entertainer_details = 'Feature: By Popular Demand (pg. 130)'

# Entertainer characteristics
_entertainer_personalities = \
    ['I know a story relevant to almost every situation.',
     'Whenever I come to a new place, I collect local rumors and spread gossip.',
     'I\'m a hopeless romantic, always searching for that "special someone."',
     'Nobody stays angry at me or around me for long, since I can defuse any amount of tension.',
     'I love a good insult, even one directed at me.',
     'I get bitter if I\'m not the center of attention.',
     'I\'ll settle for nothing less than perfection.',
     'I change my mood or my mind as quickly as I change key in a song.']
_entertainer_ideals = \
    ['Beauty. When I perform, I make the world better than it was. (Good)',
     'Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are. (Lawful)',
     'Creativity. The world is in need of new ideas and bold action. (Chaotic)',
     'Greed. I\'m only in it for the money and fame. (Evil)',
     'People. I like seeing the smiles on people\'s faces when I perform. That\'s all that matters. (Neutral)',
     'Honesty. Art should reflect the soul; it should come from within and reveal who we really are. (Any)']
_entertainer_bonds = \
    ['My instrument is my most treasured possession, and it reminds me of someone I love.',
     'Someone stole my precious instrument, and someday I\'ll get it back.',
     'I want to be famous, whatever it takes.',
     'I idolize a hero of the old tales and measure my deeds against that person\'s.',
     'I will do anything to prove myself superior to my hated rival.',
     'I would do anything for the other members of my old troupe.']
_entertainer_flaws = \
    ['I\'ll do anything to win fame and renown.',
     'I\'m a sucker for a pretty face.',
     'A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.',
     'I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.',
     'I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.',
     'Despite my best efforts, I am unreliable to my friends.']

# Entertainer Background
entertainer = \
    Background(name='Entertainer',
               skill_profs=_entertainer_skill_profs,
               tool_profs=_entertainer_tool_profs,
               tool_prof_selection=_entertainer_tool_prof_selection,
               equipment=_entertainer_equipment,
               equipment_selections=_entertainer_equipment_selections,
               selections=_entertainer_selection,
               money=Money(gp=15),
               languages=0,
               details=_entertainer_details,
               personalities=_entertainer_personalities,
               ideals=_entertainer_ideals,
               bonds=_entertainer_bonds,
               flaws=_entertainer_flaws)


# Folk Hero
# Folk Hero skill proficiencies
_folkhero_skill_profs = \
    ['Animal Handling',
     'Survival']

# Folk Hero tool proficiencies
_folkhero_tool_profs = \
    ['vehicles (land)']
_folkhero_tool_prof_selection = \
    _artisan_tools

# Folk Hero equipment
_folkhero_equipment = ['shovel', 'iron pot', 'common clothes']
_folkhero_equipment_selections = \
    [[tool for tool in _folkhero_tool_prof_selection]]

# Folk Hero selection
_folkhero_selection = \
    ['Defining Event: I stood up to a tyrant\'s agents.',
     'Defining Event: I saved people during a natural disaster.',
     'Defining Event: I stood alone against a terrible monster.',
     'Defining Event: I stole from a corrup merchant to help the poor.',
     'Defining Event: I led a militia to fight off an invading army.',
     'Defining Event: I broke into a tyrant\'s castle and stole weapons to arm the people.',
     'Defining Event: I trained the peasantry to use farm implements as weapons against a tyrant\'s soldiers.',
     'Defining Event: A lord rescinded an unpopular decree after I led a symbolic act of protest against it.',
     'Defining Event: A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.',
     'Defining Event: Recruited into a lord\'s army, I rose to leadership and was commended for my heroism.']

# Folk Hero details
_folkhero_details = 'Feature: Rustic Hospitality (pg. 131)'

# Folk Hero characteristics
_folkhero_personalities = \
    ['I judge people by their actions, not their words.',
     'If someone is in trouble, I\'m always ready to lend help.',
     'When I set my mind to something, I follow through no matter what gets in my way.',
     'I have a strong sense of fair play and always try to find the most equitable solution to arguments.',
     'I\'m confident in my own abilities and do what I can to instill confidence in others.',
     'Thinking is for other people. I prefer action.',
     'I misuse long words in an attempt to sound smarter.',
     'I get bored easily. When am I going to get on with my destiny?']
_folkhero_ideals = \
    ['Respect. People deserve to be treated with dignity and respect. (Good)',
     'Fairness. No one should get preferential treatment before the law, and no one is above the law. (Lawful)',
     'Freedom. Tyrants must not be allowed to oppress the people. (Chaotic)',
     'Might. If I become strong, I can take what I want--what I deserve. (Evil)',
     'Sincerity. There\'s no good in pretending to be something I\'m not. (Neutral)',
     'Destiny. Nothing and no one can steer me away from my higher calling. (Any)']
_folkhero_bonds = \
    ['I have a family, but I have no idea where they are. One day, I hope to see them again.',
     'I worked the land, I love the land, and I will protect the land.',
     'A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.',
     'My tools are symbols of my past life, and I carry them so that I will never forget my roots.',
     'I protect those who cannot protect themselves',
     'I wish my childhood sweetheart had come with me to pursue my destiny.']
_folkhero_flaws = \
    ['The tyrant who rules my land will stop at nothing to see me killed.',
     'I\'m convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.',
     'The people who knew me when I was young know my shameful secret, so I can never go home again.',
     'I have a weakness for the vices of the city, especially hard drink.',
     'Secretly, I believe that things would be better if I were a tyrant lording over the land.',
     'I have trouble trusting in my allies.']

# Folk Hero Background
folkhero = \
    Background(name='Folk Hero',
               skill_profs=_folkhero_skill_profs,
               tool_profs=_folkhero_tool_profs,
               tool_prof_selection=_folkhero_tool_prof_selection,
               equipment=_folkhero_equipment,
               equipment_selections=_folkhero_equipment_selections,
               selections=_folkhero_selection,
               money=Money(gp=10),
               languages=0,
               details=_folkhero_details,
               personalities=_folkhero_personalities,
               ideals=_folkhero_ideals,
               bonds=_folkhero_bonds,
               flaws=_folkhero_flaws)


# Guild Artisan
# Guild Artisan skill proficiencies
_guildartisan_skill_profs = \
    ['Insight',
     'Persuasion']

# Guild Artisan tool proficiencies
_guildartisan_tool_prof_selection = \
    _artisan_tools

# Guild Artisan equipment
_guildartisan_equipment = \
    ['letter of introduction from your guild', 'traveler\'s clothes']
_guildartisan_equipment_selections = \
    [[tool for tool in _guildartisan_tool_prof_selection]]

# Guild Artisan selection
_guildartisan_selection = \
    ['Guild Business: Alchemists and apothecaries',
     'Guild Business: Armorers, locksmiths, and finesmiths',
     'Guild Business: Brewers, distillers, vintners',
     'Guild Business: Calligraphers, scribes, and scriveners',
     'Guild Business: Carpenters, roofers, and plasterers',
     'Guild Business: Cartographers, surveyors, and chart-makers',
     'Guild Business: Cobblers and shoemakers',
     'Guild Business: Cooks and bakers',
     'Guild Business: Glassblowers and glaziers',
     'Guild Business: Jewelers and gemcutters',
     'Guild Business: Leatherworkers, skinners, and tanners',
     'Guild Business: Masons and stonecutters',
     'Guild Business: Painters, limners, and sign-makers',
     'Guild Business: Potters and tile-makers',
     'Guild Business: Shipwrights and sailmakers',
     'Guild Business: Smiths and metal-forgers',
     'Guild Business: Tinkers, pewterers, and casters',
     'Guild Business: Wagon-makers and wheelwrights',
     'Guild Business: Weavers and dyers',
     'Guild Business: Woodcarvers, coopers, and bowyers']

# Guild Artisan details
_guildartisan_details = 'Feature: Guild Membership (pg. 133)'

# Guild Artisan characteristics
_guildartisan_personalities = \
    ['I believe that anything worth doing is worth doing right. I can\'t help it--I\'m a perfectionist.',
     'I\'m a snob who looks down on those who can\'t appreciate fine art.',
     'I always want to know how things work and what makes people tick.',
     'I\'m full of witty aphorisms and have a proverb for every occasion.',
     'I\'m rude to people who lack my commitment to hard work and fair play.',
     'I like to talk at length about my profession.',
     'I don\'t part with my money easily and will haggle tirelessly to get the best deal possible.',
     'I\'m well known for my work, and I want to make sure everyone appreciates it. I\'m always taken aback when people haven\'t heard of me.']
_guildartisan_ideals = \
    ['Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization. (Lawful)',
     'Generosity. My talents were to me so that I could use them to benefit the world. (Good)',
     'Freedom. Everyone should be free to pursue his or her own livelihood. (Chaotic)',
     'Greed. I\'m only in it for the money. (Evil)',
     'People. I\'m committed to the people I care about, not the ideals. (Neutral)',
     'Aspiration. I work hard to be the best there is at my craft. (Any)']
_guildartisan_bonds = \
    ['The workshop where I learned my trade is the most important place in the world to me.',
     'I created a great work for someone, and then found them unworthy to receive it. I\'m still looking for someone worthy.',
     'I owe my guild a great debt for forging me into the person I am today.',
     'I pursue wealth to secure someone\'s love.',
     'One day I will return to my guild and prove that I am the greatest artisan of them all.',
     'I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.']
_guildartisan_flaws = \
    ['I\'ll do anything to get my hands on something rare or priceless.',
     'I\'m quick to assume that someone is trying to cheat me.',
     'No one must ever learn that I once stole money from guild coffers.',
     'I\'m never satisfied with what I have--I always want more.',
     'I would kill to acquire a noble title.',
     'I\'m horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I\'m surrounded by rivals.']

# Guild Artisan Background
guildartisan = \
    Background(name='Guild Artisan',
               skill_profs=_guildartisan_skill_profs,
               tool_profs=None,
               tool_prof_selection=_guildartisan_tool_prof_selection,
               equipment=_guildartisan_equipment,
               equipment_selections=_guildartisan_equipment_selections,
               selections=_guildartisan_selection,
               money=Money(gp=15),
               languages=1,
               details=_guildartisan_details,
               personalities=_guildartisan_personalities,
               ideals=_guildartisan_ideals,
               bonds=_guildartisan_bonds,
               flaws=_guildartisan_flaws)


# Hermit
# Hermit skill proficiencies
_hermit_skill_profs = \
    ['Medicine',
     'Religion']

# Hermit tool proficiencies
_hermit_tool_profs = \
    ['herbalism kit']
_hermit_tool_prof_selection = \
    None

# Hermit equipment
_hermit_equipment = \
    ['scroll case stuffed full of notes from your studies or prayers',
     'winter blanket',
     'common clothes',
     'herbalism kit']
_hermit_equipment_selections = \
    None

# Hermit selection
_hermit_selection = \
    ['Life of Seclusion: I was searching for spiritual enlightenment.',
     'Life of Seclusion: I was partaking of communal living in accordance with the dictates of a religious order.',
     'Life of Seclusion: I was exiled for a crime I didn\'t commit.',
     'Life of Seclusion: I retreated from society after a life-altering event.',
     'Life of Seclusion: I needed a quiet place to work on my art, literature, music, or manifesto.',
     'Life of Seclusion: I needed to commune with nature, far from civilization.',
     'Life of Seclusion: I was the caretaker of an ancient ruin or relic.',
     'Life of Seclusion: I was a pilgrim in search of a person, place, or relic of spiritual significance.']

# Hermit details
_hermit_details = 'Feature: Discovery (pg. 134)'

# Hermit characteristics
_hermit_personalities = \
    ['I\'ve been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.',
     'I am utterly serene, even in the face of disaster.',
     'The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.',
     'I feel tremendous empathy for all who suffer.',
     'I\'m oblivious to etiquette and social expectations.',
     'I connect everything that happens to me to a grand, cosmic plan.',
     'I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.',
     'I am working on a grand philosophical theory and love sharing my ideas.']
_hermit_ideals = \
    ['Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)',
     'Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking. (Lawful)',
     'Free Thinking. Inquiry and curiosity are the pillars of progress. (Chaotic)',
     'Power. Solitude and contemplation are paths toward mystical or magical power. (Evil)',
     'Live and Let Liv. Meddling in the affairs of others only causes trouble. (Neutral)',
     'Self-Knowledge. If you know yourself, there\'s nothing left to know. (Any)']
_hermit_bonds = \
    ['Nothing is more important than the members of my hermitage, order, or association.',
     'I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.',
     'I\'m still seeking the enlightenment I pursued in my seclusion, and it still eludes me.',
     'I entered seclusion because I loved someone I could not have.',
     'Should my discovery come to light, it could bring ruin to the world.',
     'My isolation gave me great insight into a great evil that only I can destroy.']
_hermit_flaws = \
    ['Now that I\'ve returned to the world, I enjoy its delights a little too much.',
     'I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.',
     'I am dogmatic in my thoughts and philosophy.',
     'I let my need to win arguments overshadow friendships and harmony.',
     'I\'d risk too much to uncover a lost bit of knowledge.',
     'I like keeping secrets and won\'t share them with anyone.']

# Hermit Background
hermit = \
    Background(name='Hermit',
               skill_profs=_hermit_skill_profs,
               tool_profs=_hermit_tool_profs,
               tool_prof_selection=_hermit_tool_prof_selection,
               equipment=_hermit_equipment,
               equipment_selections=_hermit_equipment_selections,
               selections=_hermit_selection,
               money=Money(gp=5),
               languages=1,
               details=_hermit_details,
               personalities=_hermit_personalities,
               ideals=_hermit_ideals,
               bonds=_hermit_bonds,
               flaws=_hermit_flaws)


# Noble
# Noble skill proficiencies
_noble_skill_profs = \
    ['History',
     'Persuasion']

# Noble tool proficiencies
_noble_tool_profs = \
    None
_noble_tool_prof_selection = \
    ['dice set',
     'dragonchess set',
     'playing card set',
     'Three-Dragon Ante set']

# Noble equipment
_noble_equipment = \
    ['fine clothes',
     'signet ring',
     'scroll of pedigree']
_noble_equipment_selections = \
    None

# Noble selection
_noble_selection = \
    None

# Noble details
_noble_details = 'Feature: Position of Privilege (pg. 135)'

# Noble characteristics
_noble_personalities = \
    ['My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.',
     'The common folk love me for my kindness and generosity.',
     'No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.',
     'I take great pains to always look my best and follow the latest fashions.',
     'I don\'t like getting my hands dirty, and I won\'t be caught dead in unsuitable accommodations.',
     'Despite my noble birth, I do not place myself above other folk. We all have the same blood.',
     'My favor, once lost, is lost forever.',
     'If you do me an injury, I will crush you, ruin your name, and salt your fields.']
_noble_ideals = \
    ['Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity. (Good)',
     'Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine. (Lawful)',
     'Independence. I must prove that I can handle myself without the coddling of my family. (Chaotic)',
     'Power. If I can attain more power, no one will tell me what to do. (Evil)',
     'Family. Blood runs thicker than water. (Any)',
     'Noble Obligation. It is my duty to protect and care for the people beneath me. (Good)']
_noble_bonds = \
    ['I will face any challenge to win the approval of my family.',
     'My house\'s alliance with another noble family must be sustained at all costs.',
     'Nothing is more important than the other members of my family.',
     'I am in love with the heir of a family that my family dispises.',
     'My loyalty to my sovereign is unwavering.',
     'The common folk must see me as a hero of the people.']
_noble_flaws = \
    ['I secretly believe that everyone is beneath me.',
     'I hide a truly scandalous secret that could ruin my family forever.',
     'I too often hear veiled insults and threats in every word addressed to me, and I\'m quick to anger.',
     'I have an insatiable desire for carnal pleasures.',
     'In fact, the world does revolve around me.',
     'By my words and actions, I often bring shame to my family.']

# Noble Background
noble = \
    Background(name='Noble',
               skill_profs=_noble_skill_profs,
               tool_profs=_noble_tool_profs,
               tool_prof_selection=_noble_tool_prof_selection,
               equipment=_noble_equipment,
               equipment_selections=_noble_equipment_selections,
               selections=_noble_selection,
               money=Money(gp=25),
               languages=1,
               details=_noble_details,
               personalities=_noble_personalities,
               ideals=_noble_ideals,
               bonds=_noble_bonds,
               flaws=_noble_flaws)
