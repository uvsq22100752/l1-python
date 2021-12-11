import discord
from discord.state import AutoShardedConnectionState
import unidecode
import requests
from bs4 import *
from pokedex1 import *


listechampion=['/Adriane','/Albert','/Alistair','/Alizée','/Aloé','/Amana','/Amaro','/Armando','/Artie','/Astera','/Auguste','/Bardane','/Bastien','/Blanche','/Blue','/Carolina','/Charles','/Chaz','/Chuck','/Cornélia','/Donna','/Erika','/Faïza','/Flo','/Frédo','/Giovanni','/Gladys','/Hector','/Inezia','/Iris','/Jasmine','/Jeannine','/Juan','/Kabu','/Kiméra','/Koga','/Lem','/Lino','/Lona','/Lovis','/Lévy & Tatia','/Major Bob','/Marc','/Morgane','/Mortimer','/Mélina','/Noa','/Norman','/Ondine','/Percy','/Peterson','/Pierre','/Pierrick','/Rachid','/Rosemary','/Roxanne','/Roy','/Sally','/Sandra','/Strykna','/Tanguy','/Tcheren','/Urup','/Valériane','/Violette','/Voltère','/Watson','/Zhu']




megaliste=['/Deoxys Attaque','/Deoxys Défense','/Deoxys Vitesse','/Cheniselle Sable','/Cheniselle Déchet','/Shaymin Céleste','/Giratina Originel','/Motisma Chaleur','/Motisma Lavage','/Motisma Froid','/Motisma Hélice','/Motisma Tonte','/Morphéo Solaire','/Morphéo Pluie','/Morphéo Blizzard','/Bargantua Bleu','/Darumacho Transe','/Meloetta','/Boréas Totémique','/Fulguris Totémique','/Démétéros Totémique','/Kyurem Noir','/Kyurem Blanc','/Keldeo Décidé','/Mistigrix Femelle','/Exagide Assaut','/Pitrouille Mini','/Pitrouille Maxi','/Pitrouille Ultra','/Banshitrouye Mini','/Banshitrouye Maxi','/Banshitrouye Ultra','/Méga Florizarre','/Méga Dracaufeu X','/Méga Dracaufeu Y','/Méga Tortank','/Méga Alakazam','/Méga-Ectoplasma','/Méga Kangourex','/Méga Scarabrute','/Méga Léviator','/Méga Ptéra','/Méga Mewtwo X','/Méga Mewtwo Y','/Méga Pharamp','/Méga Cizayox','/Méga Scarhino','/Méga Démolosse','/Méga Tyranocif','/Méga Braségali','/Méga Gardevoir','/Méga Mysdibule','/Méga Galeking','/Méga Charmina','/Méga Elecsprint','/Méga Branette','/Méga Absol','/Méga Carchacrok','/Méga Lucario','/Méga Blizzaroi','/Floette Bleu','/Méga Latias','/Méga Latios','/Méga Nanméouïe','/Méga Steelix','/Méga Jungko','/Méga Laggron','/Méga Diancie','/Méga Gallame','/Méga Lockpin','/Méga Rayquaza','/Méga Métalosse','/Méga Drattak','/Méga Oniglali','/Méga Altaria','/Méga Camérupt','/Méga Sharpedo','/Méga Ténéfix','/Méga Flagadoss','/Méga Roucarnage','/Méga Dardargnan','/Primo Groudon','/Primo Kyogre','/Hoopa Déchaîné','/Arceus Feu','/Arceus Fée','/Arceus Spectre','/Arceus Dragon','/Arceus Electrik','/Arceus Combat','/Arceus Vol','/Arceus Insecte','/Arceus Plante','/Arceus Sol','/Arceus Eau','/Arceus Poison','/Arceus Psy','/Arceus Roche','/Arceus Acier','/Arceus Glace','/Arceus Ténèbres','/Pikachu Lady','/Pikachu Fighter','/Pikachu Docteur','/Pikachu Star','/Pikachu Rockeur','/Flabébé Bleu','/Flabébé Orange','/Flabébé Blanc','/Flabébé Jaune','/Floette Bleue','/Floette Oranges','/Floette Blanches','/Floette Jaunes','/Florges Bleue','/Florges Oranges','/Florges Blanches','/Florges Jaunes','/Sancoki Orient','/Tritosor Orient','/Amphinobi Sasha','/Plumeline Pom-Pom','/Plumeline Hula','/Plumeline Buyo','/Lougaroc Nocturne','/Froussardine Banc','/Météno Noyau Rouge','/Rattata Alola','/Rattatac Alola','/Raichu Alola','/Sabelette Alola','/Sablaireau Alola','/Goupix Alola','/Feunard Alola','/Taupiqueur Alola','/Triopiqueur Alola','/Miaouss Alola','/Persian Alola','/Racaillou Alola','/Gravalanch Alola','/Grolem Alola','/Grotadmorv Alola','/Noadkoko Alola','/Ossatueur Alola',"/Tadmorv Alola"]




pokede=['Bulbizarre',
       'Herbizarre',
       'Florizarre',
       'Salamèche',
       'Reptincel',
       'Dracaufeu',
       'Carapuce',
       'Carabaffe',
       'Tortank',
       'Chenipan',
       'Chrysacier',
       'Papilusion',
       'Aspicot',
       'Coconfort',
       'Dardargnan',
       'Roucool',
       'Roucoups',
       'Roucarnage',
       'Rattata',
       'Rattatac',
       'Piafabec',
       'Rapasdepic',
       'Abo',
       'Arbok',
       'Pikachu',
       'Raichu',
       'Sabelette',
       'Sablaireau',
       'Nidoran♀',
       'Nidorina',
       'Nidoqueen',
       'Nidoran♂',
       'Nidorino',
       'Nidoking',
       'Mélofée',
       'Mélodelfe',
       'Goupix',
       'Feunard',
       'Rondoudou',
       'Grodoudou',
       'Nosferapti',
       'Nosferalto',
       'Mystherbe',
       'Ortide',
       'Rafflésia',
       'Paras',
       'Parasect',
       'Mimitoss',
       'Aéromite',
       'Taupiqueur',
       'Triopikeur',
       'Miaouss',
       'Persian',
       'Psykokwak',
       'Akwakwak',
       'Férosinge',
       'Colossinge',
       'Caninos',
       'Arcanin',
       'Ptitard',
       'Têtarte',
       'Tartard',
       'Abra',
       'Kadabra',
       'Alakazam',
       'Machoc',
       'Machopeur',
       'Mackogneur',
       'Chétiflor',
       'Boustiflor',
       'Empiflor',
       'Tentacool',
       'Tentacruel',
       'Racaillou',
       'Gravalanch',
       'Grolem',
       'Ponyta',
       'Galopa',
       'Ramoloss',
       'Flagadoss',
       'Magnéti',
       'Magnéton',
       'Canarticho',
       'Doduo',
       'Dodrio',
       'Otaria',
       'Lamantine',
       'Tadmorv',
       'Grotadmorv',
       'Kokiyas',
       'Crustabri',
       'Fantominus',
       'Spectrum',
       'Ectoplasma',
       'Onix',
       'Soporifik',
       'Hypnomade',
       'Krabby',
       'Krabboss',
       'Voltorbe',
       'Électrode',
       'Nœunœuf',
       'Noadkoko',
       'Osselait',
       'Ossatueur',
       'Kicklee',
       'Tygnon',
       'Excelangue',
       'Smogo',
       'Smogogo',
       'Rhinocorne',
       'Rhinoféros',
       'Leveinard',
       'Saquedeneu',
       'Kangourex',
       'Hypotrempe',
       'Hypocéan',
       'Poissirène',
       'Poissoroy',
       'Stari',
       'Staross',
       'M. Mime',
       'Insécateur',
       'Lippoutou',
       'Élektek',
       'Magmar',
       'Scarabrute',
       'Tauros',
       'Magicarpe',
       'Léviator',
       'Lokhlass',
       'Métamorph',
       'Évoli',
       'Aquali',
       'Voltali',
       'Pyroli',
       'Porygon',
       'Amonita',
       'Amonistar',
       'Kabuto',
       'Kabutops',
       'Ptéra',
       'Ronflex',
       'Artikodin',
       'Électhor',
       'Sulfura',
       'Minidraco',
       'Draco',
       'Dracolosse',
       'Mewtwo',
       'Mew',
       'Germignon',
       'Macronium',
       'Méganium',
       'Héricendre',
       'Feurisson',
       'Typhlosion',
       'Kaiminus',
       'Crocrodil',
       'Aligatueur',
       'Fouinette',
       'Fouinar',
       'Hoothoot',
       'Noarfang',
       'Coxy',
       'Coxyclaque',
       'Mimigal',
       'Migalos',
       'Nostenfer',
       'Loupio',
       'Lanturn',
       'Pichu',
       'Mélo',
       'Toudoudou',
       'Togepi',
       'Togetic',
       'Natu',
       'Xatu',
       'Wattouat',
       'Lainergie',
       'Pharamp',
       'Joliflor',
       'Marill',
       'Azumarill',
       'Simularbre',
       'Tarpaud',
       'Granivol',
       'Floravol',
       'Cotovol',
       'Capumain',
       'Tournegrin',
       'Héliatronc',
       'Yanma',
       'Axoloto',
       'Maraiste',
       'Mentali',
       'Noctali',
       'Cornèbre',
       'Roigada',
       'Feuforêve',
       'Zarbi',
       'Qulbutoké',
       'Girafarig',
       'Pomdepik',
       'Foretress',
       'Insolourdo',
       'Scorplane',
       'Steelix',
       'Snubbull',
       'Granbull',
       'Qwilfish',
       'Cizayox',
       'Caratroc',
       'Scarhino',
       'Farfuret',
       'Teddiursa',
       'Ursaring',
       'Limagma',
       'Volcaropod',
       'Marcacrin',
       'Cochignon',
       'Corayon',
       'Rémoraid',
       'Octillery',
       'Cadoizo',
       'Démanta',
       'Airmure',
       'Malosse',
       'Démolosse',
       'Hyporoi',
       'Phanpy',
       'Donphan',
       'Porygon2',
       'Cerfrousse',
       'Queulorior',
       'Debugant',
       'Kapoera',
       'Lippouti',
       'Élekid',
       'Magby',
       'Écrémeuh',
       'Leuphorie',
       'Raikou',
       'Entei',
       'Suicune',
       'Embrylex',
       'Ymphect',
       'Tyranocif',
       'Lugia',
       'Ho-Oh',
       'Celebi',
       'Arcko',
       'Massko',
       'Jungko',
       'Poussifeu',
       'Galifeu',
       'Braségali',
       'Gobou',
       'Flobio',
       'Laggron',
       'Medhyèna',
       'Grahyèna',
       'Zigzaton',
       'Linéon',
       'Chenipotte',
       'Armulys',
       'Charmillon',
       'Blindalys',
       'Papinox',
       'Nénupiot',
       'Lombre',
       'Ludicolo',
       'Grainipiot',
       'Pifeuil',
       'Tengalice',
       'Nirondelle',
       'Hélédelle',
       'Goélise',
       'Bekipan',
       'Tarsal',
       'Kirlia',
       'Gardevoir',
       'Arakdo',
       'Maskadra',
       'Balignon',
       'Chapignon',
       'Parécool',
       'Vigoroth',
       'Monaflèmit',
       'Ningale',
       'Ninjask',
       'Munja',
       'Chuchmur',
       'Ramboum',
       'Brouhabam',
       'Makuhita',
       'Hariyama',
       'Azurill',
       'Tarinor',
       'Skitty',
       'Delcatty',
       'Ténéfix',
       'Mysdibule',
       'Galekid',
       'Galegon',
       'Galeking',
       'Méditikka',
       'Charmina',
       'Dynavolt',
       'Élecsprint',
       'Posipi',
       'Négapi',
       'Muciole',
       'Lumivole',
       'Rosélia',
       'Gloupti',
       'Avaltout',
       'Carvanha',
       'Sharpedo',
       'Wailmer',
       'Wailord',
       'Chamallot',
       'Camérupt',
       'Chartor',
       'Spoink',
       'Groret',
       'Spinda',
       'Kraknoix',
       'Vibraninf',
       'Libégon',
       'Cacnea',
       'Cacturne',
       'Tylton',
       'Altaria',
       'Mangriff',
       'Séviper',
       'Séléroc',
       'Solaroc',
       'Barloche',
       'Barbicha',
       'Écrapince',
       'Colhomard',
       'Balbuto',
       'Kaorine',
       'Lilia',
       'Vacilys',
       'Anorith',
       'Armaldo',
       'Barpau',
       'Milobellus',
       'Morphéo',
       'Kecleon',
       'Polichombr',
       'Branette',
       'Skelénox',
       'Téraclope',
       'Tropius',
       'Éoko',
       'Absol',
       'Okéoké',
       'Stalgamin',
       'Oniglali',
       'Obalie',
       'Phogleur',
       'Kaimorse',
       'Coquiperl',
       'Serpang',
       'Rosabyss',
       'Relicanth',
       'Lovdisc',
       'Draby',
       'Drackhaus',
       'Drattak',
       'Terhal',
       'Métang',
       'Métalosse',
       'Regirock',
       'Regice',
       'Registeel',
       'Latias',
       'Latios',
       'Kyogre',
       'Groudon',
       'Rayquaza',
       'Jirachi',
       'Deoxys',
       'Tortipouss',
       'Boskara',
       'Torterra',
       'Ouisticram',
       'Chimpenfeu',
       'Simiabraz',
       'Tiplouf',
       'Prinplouf',
       'Pingoléon',
       'Étourmi',
       'Étourvol',
       'Étouraptor',
       'Keunotor',
       'Castorno',
       'Crikzik',
       'Mélokrik',
       'Lixy',
       'Luxio',
       'Luxray',
       'Rozbouton',
       'Roserade',
       'Kranidos',
       'Charkos',
       'Dinoclier',
       'Bastiodon',
       'Cheniti',
       'Cheniselle',
       'Papilord',
       'Apitrini',
       'Apireine',
       'Pachirisu',
       'Mustébouée',
       'Mustéflott',
       'Ceribou',
       'Ceriflor',
       'Sancoki',
       'Tritosor',
       'Capidextre',
       'Baudrive',
       'Grodrive',
       'Laporeille',
       'Lockpin',
       'Magirêve',
       'Corboss',
       'Chaglam',
       'Chaffreux',
       'Korillon',
       'Moufouette',
       'Moufflair',
       'Archéomire',
       'Archéodong',
       'Manzaï',
       'Mime Jr.',
       'Ptiravi',
       'Pijako',
       'Spiritomb',
       'Griknot',
       'Carmache',
       'Carchacrok',
       'Goinfrex',
       'Riolu',
       'Lucario',
       'Hippopotas',
       'Hippodocus',
       'Rapion',
       'Drascore',
       'Cradopaud',
       'Coatox',
       'Vortente',
       'Écayon',
       'Luminéon',
       'Babimanta',
       'Blizzi',
       'Blizzaroi',
       'Dimoret',
       'Magnézone',
       'Coudlangue',
       'Rhinastoc',
       'Bouldeneu',
       'Élekable',
       'Maganon',
       'Togekiss',
       'Yanmega',
       'Phyllali',
       'Givrali',
       'Scorvol',
       'Mammochon',
       'Porygon-Z',
       'Gallame',
       'Tarinorme',
       'Noctunoir',
       'Momartik',
       'Motisma',
       'Créhelf',
       'Créfollet',
       'Créfadet',
       'Dialga',
       'Palkia',
       'Heatran',
       'Regigigas',
       'Giratina',
       'Cresselia',
       'Phione',
       'Manaphy',
       'Darkrai',
       'Shaymin',
       'Archers',
       'Victini',
       'Vipélierre',
       'Lianaja',
       'Majaspic',
       'Gruikui',
       'Grotichon',
       'Roitiflam',
       'Moustillon',
       'Mateloutre',
       'Clamiral',
       'Ratentif',
       'Miradar',
       'Ponchiot',
       'Ponchien',
       'Mastouffe',
       'Chacripan',
       'Léopardus',
       'Feuillajou',
       'Feuiloutan',
       'Flamajou',
       'Flamoutan',
       'Flotajou',
       'Flotoutan',
       'Munna',
       'Mushana',
       'Poichigeon',
       'Colombeau',
       'Déflaisan',
       'Zébibron',
       'Zéblitz',
       'Nodulithe',
       'Géolithe',
       'Gigalithe',
       'Chovsourir',
       'Rhinolove',
       'Rototaupe',
       'Minotaupe',
       'Nanméouïe',
       'Charpenti',
       'Ouvrifier',
       'Bétochef',
       'Tritonde',
       'Batracné',
       'Crapustule',
       'Judokrak',
       'Karaclée',
       'Larveyette',
       'Couverdure',
       'Manternel',
       'Venipatte',
       'Scobolide',
       'Brutapode',
       'Doudouvet',
       'Farfaduvet',
       'Chlorobule',
       'Fragilady',
       'Bargantua',
       'Mascaïman',
       'Escroco',
       'Crocorible',
       'Darumarond',
       'Darumacho',
       'Maracachi',
       'Crabicoque',
       'Crabaraque',
       'Baggiguane',
       'Baggaïd',
       'Cryptéro',
       'Tutafeh',
       'Tutankafer',
       'Carapagos',
       'Mégapagos',
       'Arkéapti',
       'Aéroptéryx',
       'Miamiasme',
       'Miasmax',
       'Zorua',
       'Zoroark',
       'Chinchidou',
       'Pashmilla',
       'Scrutella',
       'Mesmérella',
       'Sidérella',
       'Nucléos',
       'Méios',
       'Symbios',
       'Couaneton',
       'Lakmécygne',
       'Sorbébé',
       'Sorboul',
       'Sorbouboul',
       'Vivaldaim',
       'Haydaim',
       'Emolga',
       'Carabing',
       'Lançargot',
       'Trompignon',
       'Gaulet',
       'Viskuse',
       'Moyade',
       'Mamanbo',
       'Statitik',
       'Mygavolt',
       'Grindur',
       'Noacier',
       'Tic',
       'Clic',
       'Cliticlic',
       'Anchwatt',
       'Lampéroie',
       'Ohmassacre',
       'Lewsor',
       'Neitram',
       'Funécire',
       'Mélancolux',
       'Lugulabre',
       'Coupenotte',
       'Incisache',
       'Tranchodon',
       'Polarhume',
       'Polagriffe',
       'Hexagel',
       'Escargaume',
       'Limaspeed',
       'Limonde',
       'Kungfouine',
       'Shaofouine',
       'Drakkarmin',
       'Gringolem',
       'Golemastoc',
       'Scalpion',
       'Scalproie',
       'Frison',
       'Furaiglon',
       'Gueriaigle',
       'Vostourno',
       'Vaututrice',
       'Aflamanoir',
       'Fermite',
       'Solochi',
       'Diamat',
       'Trioxhydre',
       'Pyronille',
       'Pyrax',
       'Cobaltium',
       'Terrakium',
       'Viridium',
       'Boréas',
       'Fulguris',
       'Reshiram',
       'Zekrom',
       'Démétéros',
       'Kyurem',
       'Keldeo',
       'Meloetta',
       'Genesect',
       'Marisson',
       'Boguérisse',
       'Blindépique',
       'Feunnec',
       'Roussil',
       'Goupelin',
       'Grenousse',
       'Croâporal',
       'Amphinobi',
       'Sapereau',
       'Excavarenne',
       'Passerouge',
       'Braisillon',
       'Flambusard',
       'Lépidonille',
       'Pérégrain',
       'Prismillon',
       'Hélionceau',
       'Némélios',
       'Flabébé',
       'Floette',
       'Florges',
       'Cabriolaine',
       'Chevroum',
       'Pandespiègle',
       'Pandarbare',
       'Couafarel',
       'Psystigri',
       'Mistigrix',
       'Monorpale',
       'Dimoclès',
       'Exagide',
       'Fluvetin',
       'Cocotine',
       'Sucroquin',
       'Cupcanaille',
       'Sepiatop',
       'Sepiatroce',
       'Opermine',
       'Golgopathe',
       'Venalgue',
       'Kravarech',
       'Flingouste',
       'Gamblast',
       'Galvaran',
       'Iguolta',
       'Ptyranidur',
       'Rexillius',
       'Amagara',
       'Dragmara',
       'Nymphali',
       'Brutalibré',
       'Dedenne',
       'Strassie',
       'Mucuscule',
       'Colimucus',
       'Muplodocus',
       'Trousselin',
       'Brocélôme',
       'Desséliande',
       'Pitrouille',
       'Banshitrouye',
       'Grelaçon',
       'Séracrawl',
       'Sonistrelle',
       'Bruyverne',
       'Xerneas',
       'Yveltal',
       'Zygarde',
       'Diancie',
       'Hoopa',
       'Volcanion',
       'Brindibou',
       'Efflèche',
       'Archéduc',
       'Flamiaou',
       'Matoufeu',
       'Félinferno',
       'Otaquin',
       'Otarlette',
       'Oratoria',
       'Picassaut',
       'Piclairon',
       'Bazoucan',
       'Manglouton',
       'Argouste',
       'Larvibule',
       'Chrysapile',
       'Lucanon',
       'Crabagarre',
       'Crabominable',
       'Plumeline',
       'Bombydou',
       'Rubombelle',
       'Rocabot',
       'Lougaroc',
       'Froussardine',
       'Vorastérie',
       'Prédastérie',
       'Tiboudet',
       'Bourrinos',
       'Araqua',
       'Tarenbulle',
       'Mimantis',
       'Floramantis',
       'Spododo',
       'Lampignon',
       'Tritox',
       'Malamandre',
       'Nounourson',
       'Chelours',
       'Croquine',
       'Candine',
       'Sucreine',
       'Guérilande',
       'Gouroutan',
       'Quartermac',
       'Sovkipou',
       'Sarmuraï',
       'Bacabouh',
       'Trépassable',
       'Concombaffe',
       'Type:0',
       'Silvallié',
       'Météno',
       'Dodoala',
       'Boumata',
       'Togedemaru',
       'Mimiqui',
       'Denticrisse',
       'Draïeul',
       'Sinistrail',
       'Bébécaille',
       'Écaïd',
       'Ékaïser',
       'Tokorico',
       'Tokopiyon',
       'Tokotoro',
       'Tokopisco',
       'Cosmog',
       'Cosmovum',
       'Solgaleo',
       'Lunala',
       'Zéroïd',
       'Mouscoto',
       'Cancrelove',
       'Câblifère',
       'Bamboiselle',
       'Katagami',
       'Engloutyran',
       'Necrozma',
       'Magearna',
       'Marshadow',
       'Vémini',
       'Mandrillon',
       'Ama-Ama',
       'Pierroteknik',
       'Zeraora',
       'Meltan',
       'Melmetal',
       'Ouistempo',
       'Badabouin',
       'Gorythmic',
       'Flambino',
       'Lapyro',
       'Pyrobut',
       'Larméléon',
       'Arrozard',
       'Lézargus',
       'Vinted',
       'Sheesh']

pokedex=[]


for i in range(0,len(pokede)):
    a=str('/'+pokede[i])
    pokedex.append(a)





class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            
            return
        
    
        #Commande  ->  /NomDuPokémon
        global list1
        list1=[]
        if message.content.startswith('/'):
            list1.append(message.content)
            
            if (str(list1[0])) in pokedex:
                a=str(list1[0])
                a="https://www.pokepedia.fr"+a
                await message.channel.send(a.format(message))    
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))
                
        #Commande -> champ/NomDuChampion
        if message.content.startswith('champ/'):
            list1.append(message.content)
            nomchampion=str(list1[0][5:(len(list1[0]))])

            if nomchampion in listechampion:
                champ="https://www.pokepedia.fr"+nomchampion
                await message.channel.send(champ.format(message))
            if nomchampion not in listechampion:
                await message.channel.send("Erreur : champion introuvable. ".format(message))
    


        #Commande -> v/NomDuChampion
        Or=["Albert", "Blanche", "Blue", "Chuck", "Auguste", "Erika","Frédo","Hector", "Jasmine", "Jeannine", "Majorbob", "Morgane", "Mortimer", "Ondine", "Pierre", "Sandra"]
        Argent=Or
        Cristal=Or
        Rouge=["Pierre","Ondine","Major Bob","Erika","Koga","Morgane","Auguste","Giovanni"]
        Bleu=Rouge
        Jaune=Rouge
        Rubis=['Roxanne','Bastien','Voltère','Adriane','Norman','Alizée','Lévy & Tatia','Marc']
        Saphir=Rubis
        Emeraude=Rubis
        Diamant=["Pierrick','Flo','Mélina","Lovis","Kiméra","Charles","Gladys","Tanguy"]
        Perle=Diamant
        Platine=Diamant
        Blanc=['Noa,Rachid,Armando','Aloé',"Artie","Inezia","Bardane","Carolina","Zhu","Iris"]
        Noir=["Noa,Rachid,Armando","Aloé","Artie","Inezia","Bardane","Carolina","Zhu","Watson"]
        Blanc2=["Tcheren","Strykna","Artie","Inezia","Bardane","Carolina","Watson","Armana"]
        Noir2=Blanc2
        X=["Violette","Lino","Cornélia","Amaro","Lem","Valériane","Astera","Urup"]
        Y=X
        if message.content.startswith('v/'):
            list1.append(message.content)
            nomchampax=str(list1[0][2:(len(list1[0]))])

        
            version=["versions : ---"]
            versionchampion="---"
            compto=0
            if nomchampax in Or:
                version.append("Or   ")
                compto+=1
            if nomchampax in Argent:
                version.append("Argent   ")
                compto+=1
            if nomchampax in Cristal:
                version.append("Cristal   ")
                compto+=1    
            if nomchampax in Rouge:
                version.append("Rouge   ")
                compto+=1
            if nomchampax in Bleu:
                version.append("Bleu   ")
                compto+=1
            if nomchampax in Jaune:
                version.append("Jaune   ")
                compto+=1
            if nomchampax in Emeraude:
                version.append("Emeraude   ")
                compto+=1
            if nomchampax in Rubis:
                version.append("Rubis   ")
                compto+=1
            if nomchampax in Saphir:
                version.append("Saphir   ")
                compto+=1
            if nomchampax in Diamant:
                version.append("Diamant   ")
                compto+=1
            if nomchampax in Perle:
                version.append("Perle   ")
                compto+=1
            if nomchampax in Platine:
                version.append("Platine   ")
                compto+=1
            if nomchampax in Noir:
                version.append("Noir   ")
                compto+=1
            if nomchampax in Blanc:
                version.append("Blanc   ")
                compto+=1
            if nomchampax in Blanc2:
                version.append("Blanc2   ")
                compto+=1
            if nomchampax in Noir2:
                version.append("Noir2   ")
                compto+=1
            if nomchampax in X:
                version.append("X   ")
                compto+=1
            if nomchampax in Y:
                version.append("Y   ")
                compto+=1
            
        
            for i in range(len(version)):
                versionchampion+=(version[i])
            await message.channel.send(versionchampion.format(message))

    
        #Commande -> liste/NomDeLaVersion
        if message.content.startswith('liste/Or') or message.content.startswith('liste/Argent') or message.content.startswith('liste/Cristal'):
            await message.channel.send(":military_medal:"+"**"+"Albert   " "Blanche   " "Blue   " "Chuck   " "Auguste   " "Erika   ""Frédo   ""Hector   ""Jasmine   " "Jeannine   " "Majorbob   " "Morgane   ""Mortimer   " "Ondine   ""Pierre   ""Sandra   "+"**".format(message))
        if message.content.startswith('liste/Rouge') or message.content.startswith('liste/Bleu') or message.content.startswith('liste/Jaune'):
            await message.channel.send(":military_medal:"+"**"+"Pierre   ""Ondine   ""Major Bob   ""Erika   ""Koga   ""Morgane   ""Auguste   ""Giovanni   "+"**".format(message))
        if message.content.startswith('liste/Diamant') or message.content.startswith('liste/Perle') or message.content.startswith('liste/Platine'):
            await message.channel.send(":military_medal:"+"**"+"Pierrick   ''Flo   ''Mélina   ""Lovis   ""Kiméra   ""Charles   ""Gladys   ""Tanguy   "+"**".format(message))
        if message.content.startswith('liste/Rubis') or message.content.startswith('liste/Saphir') or message.content.startswith('liste/Emeraude'):
            await message.channel.send(":military_medal:"+"**"+'Roxanne   ''Bastien   ''Voltère   ''Adriane   ''Norman   ''Alizée   ''Lévy & Tatia   ''Marc   '+"**".format(message))
        if message.content.startswith('liste/Noir'):
            await message.channel.send(":military_medal:"+"**"+"Noa,Rachid,Armando   ""Aloé   ""Artie   ""Inezia   ""Bardane   ""Carolina   ""Zhu   ""Watson   "+"**".format(message))
        if message.content.startswith('liste/Blanc'):
            await message.channel.send(":military_medal:"+"**"+"Noa,Rachid,Armando   ""Aloé   ""Artie   ""Inezia   ""Bardane   ""Carolina   ""Zhu   ""Iris   "+"**".format(message))
        if message.content.startswith('liste/Blanc2') or message.content.startswith('liste/Noir2'): 
            await message.channel.send(":military_medal:"+"**"+"Tcheren   ""Strykna   ""Artie   " "Inezia   ""Bardane   ""Carolina   ""Watson   ""Armana   "+"**".format(message))   
        if message.content.startswith('liste/X') or message.content.startswith('liste/Y'):        
            await message.channel.send(":military_medal:"+"**"+"Violette   ""Lino   ""Cornélia   ""Amaro   ""Lem   ""Valériane   ""Astera   ""Urup   "+"**".format(message))
                
            
        



        #Commande  ->  shiny/NomDuPokémon    
        if message.content.startswith('shiny/'):
            list1.append(message.content)
            nompoke=list1[0][5:(len(list1[0]))]

            if nompoke in pokedex:
                b=pokedex.index(nompoke)
                b+=1
                b="https://pokestrat.io/images/gif-animes/shiny/"+str(b)+".gif"
                await message.channel.send(b.format(message))   
            
            
                    
            elif nompoke in megaliste:
                nompoke=list1[0][5:(len(list1[0]))]
                mega=megaliste.index(nompoke)+10001
                mega="https://pokestrat.io/images/gif-animes/shiny/"+str(mega)+".gif"
                await message.channel.send(mega.format(message))
            
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))        
        
        #Commande  ->  gif/NomDuPokémon 
        if message.content.startswith('gif/'):
            list1.append(message.content)
            nompoke2=list1[0][3:(len(list1[0]))]

            if nompoke2 in pokedex:
                c=pokedex.index(nompoke2)
                c+=1
                c="https://pokestrat.io/images/gif-animes/"+str(c)+".gif"
                await message.channel.send(c.format(message))        
            
            elif nompoke2 in megaliste:
                mega=megaliste.index(nompoke2)+10001
                mega="https://pokestrat.io/images/gif-animes/"+str(mega)+".gif"
                await message.channel.send(mega.format(message))
                
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))
                
                
        ##Commande  ->  stats/NomDuPokémon   
        if message.content.startswith('stats/'):
            list1.append(message.content)
            nompoke3=list1[0][5:(len(list1[0]))]

            if nompoke3 in pokedex:
                nompoke4=nompoke3.lower()
                nompoke4=unidecode.unidecode(nompoke4)
                print(nompoke4)
                url = "https://pokestrat.io/fiche-pokemon/"+nompoke4

                response = requests.get(url)

                if response.ok:
                    soup=BeautifulSoup(response.text,"html.parser")
                    table = soup.findAll('table', class_='tableau-stat')
                    carac=[]
                    for tr in table:
                        for td in tr:
                            carac.append(td.text.strip())
                    
                    pv=carac[1]
                    attaque=carac[3]
                    defense=carac[5]
                    attspe=carac[7]
                    defspe=carac[9]
                    vitesse=carac[11]
                    
                    stat="   "+pv+"     "+attaque+"     "+defense+"     "+attspe+"     "+defspe+"     "+vitesse+"   "
                    stat='*'+":bar_chart:"+"**"+stat+"**"+':bar_chart:'+'*'
                    await message.channel.send(stat.format(message))        
            
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))  
                
                
        if message.content.startswith('strats/'):
            list1.append(message.content)
            nompoke7=list1[0][6:(len(list1[0]))]
            avantages=""

            if nompoke7 in pokedex:
                nompoke8=nompoke7.lower()
                nompoke8=unidecode.unidecode(nompoke8)
                print(nompoke8)
                url = "https://pokestrat.io/fiche-strategique/"+nompoke8

                response = requests.get(url)

                if response.ok:
                    soup=BeautifulSoup(response.text,"html.parser")
                    section = soup.findAll('section', class_='avantages')
                    carac1=[]
                    for div in section:
                        carac1.append(div.text.strip())
                    for i in range (0,(len(carac1))):
                        avantages+=" "+carac1[i]
                        print(avantages)
                    
                    print(avantages)
                    avantages='*'+":man_office_worker:"+"  "+avantages+"  "+':man_office_worker:'+'*'    
                    await message.channel.send(avantages.format(message))        
            
                else:
                    await message.channel.send("Erreur : Pokémon introuvable.".format(message))
                    
                    
        if message.content.startswith('partenaires/'):
            list1.append(message.content)
            nompoke9=list1[0][11:(len(list1[0]))]
            part=""

            if nompoke9 in pokedex:
                nompoke10=nompoke9.lower()
                nompoke10=unidecode.unidecode(nompoke10)
                print(nompoke10)
                url = "https://pokestrat.io/fiche-strategique/"+nompoke10

                response = requests.get(url)

                if response.ok:
                    soup=BeautifulSoup(response.text,"html.parser")
                    div = soup.findAll('div',class_='partenaire ombre')
                    print(div)
                    carac1=[]
                    for i in div:
                        carac1.append(i.text.strip())
                    for i in range (0,(len(carac1))):
                        part+=" "+carac1[i]
                        print(part)
                    
                    print(part)
                    part="*"+"**"+":man_office_worker:"+"  "+"Liste de(s) partenaire(s) possible(s) de "+nompoke9+"  "+':man_office_worker:'+"  "+" :\n\n"+"**"+part+'*'    
                    await message.channel.send(part.format(message))        
            
                else:
                    await message.channel.send("Erreur : Pokémon introuvable.".format(message))
            
            
        #Commandes  ->  maps
        
        if message.content.startswith('map/Kanto'):
            kanto="https://www.pokepedia.fr/images/4/44/Kanto_LGPE.png"
            await message.channel.send(kanto.format(message))

        if message.content.startswith('map/Johto'):
            johto="https://www.pokepedia.fr/images/f/f2/Johto_HGSS.jpg"
            await message.channel.send(johto.format(message))

        if message.content.startswith('map/Hoenn'):
            hoenn="https://www.pokepedia.fr/images/4/4c/Carte_de_Hoenn_ROSA.png"
            await message.channel.send(hoenn.format(message))

        if message.content.startswith('map/Sinnoh'):
            sinnoh="https://www.pokepedia.fr/images/9/99/Sinnoh-DEPS.png"
            await message.channel.send(sinnoh.format(message))

        if message.content.startswith('map/Unys'):
            unys="https://www.pokepedia.fr/images/a/ae/Unys_-_NB2.png"
            await message.channel.send(unys.format(message))

        if message.content.startswith('map/Kalos'):
            kalos="https://www.pokepedia.fr/images/a/ae/Unys_-_NB2.png"
            await message.channel.send(kalos.format(message))

        if message.content.startswith('map/Alola'):
            alola="https://www.pokepedia.fr/images/4/4d/Alola_-_USUL.png"
            await message.channel.send(alola.format(message))

        if message.content.startswith('map/Galar'):
            galar="https://www.pokepedia.fr/images/b/bc/Galar_-_EB.png"
            await message.channel.send(galar.format(message))   
            
            
        #Commande  ->  teams/NomDuPokémon
        
        if message.content.startswith('teams/'):
            list1.append(message.content)
            nompoke5=list1[0][5:(len(list1[0]))]
        
            if nompoke5 in pokedex:
                nompoke6=nompoke5.lower()
                nompoke6=unidecode.unidecode(nompoke6)
                e=pokedex.index(nompoke5)
                e+=1
                url="https://pokestrat.io/equipe"+nompoke6
                await message.channel.send(url.format(message))        
        
            else:
                await message.channel.send("Erreur : Pokémon introuvable.".format(message))  
                
        if message.content.startswith("!news"):
            await message.channel.send("https://www.pokemon.com/fr/actus-pokemon/".format(message))
        
        if message.content.startswith("!pokédex"):
            await message.channel.send("https://www.pokemon.com/fr/pokedex/".format(message))
            
        if message.content.startswith("!pokedex"):
            await message.channel.send("https://www.pokemon.com/fr/pokedex/".format(message))
        
            

        #Commande  ->  sheesh
        if message.content.startswith('!sheesh'):
            await message.channel.send(":loudspeaker:"+'*SHHHHEEEEESHHHH @everyone*'+":loudspeaker:".format(message))
            
            
        #Commande  ->  vinted    
        if message.content.startswith('!Vinted'):
            vinted="https://www.vinted.fr/member/34595386-nathangeck"
            await message.channel.send(vinted.format(message))
            
        if message.content.startswith('!Youtube'):
            ytb1="https://www.youtube.com/watch?v=AZSNu-V8CQw"
            ytb2="https://www.youtube.com/watch?v=1qyq9TZA5cQ"
            await message.channel.send(ytb1.format(message))
            await message.channel.send(ytb2.format(message))

        #Commande -> table des types
        if message.content.startswith('!tabletypes'):
            await message.channel.send("https://i.servimg.com/u/f58/13/25/12/23/tbtrs10.png".format(message))
            
        if message.content.startswith("!command"):    
            await message.channel.send('*voilà la liste des commandes ! Amuse toi bien ;)*', file=discord.File("/Users/bellou/Desktop/command.txt"))
        
        




       




 



client = MyClient()
client.run("OTE4MTYwNDkxMjU0Mjc2MTM3.YbDNlw.HeUQw7nq1Pcp-gM1rbyoyY8g-1U")