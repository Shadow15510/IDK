vanaheim = (r"""
                /  \          /  \     /\          /  \   /    \   /\   /  
          /\   /    \        /    \   /  \   /\   /    \ /      \ /  \ /   
         /  \ /      \   /\ /      \ /    \ /  \ /     /\        /    \    
        /    \   /\     /  \        / /\   /    \     /  \      /      \   
    /\ /      \ /  \   /    \        /  \ / /\   \ /\/    \                
   /  \        /    \ /      \ /\   /    \ /  \   /  \ /\                 /
  /    \      /      \        /  \ /      /    \ /    /  \  /\   /\      / 
 /      \ /\          /\     /    \      /      \    /    \/  \ /  \      /
         /  \        /  \   /      \        _       /     /    \    \ /\ / 
   /\   /    \      /    \                 / \_          /           /  \  
  /  \ /      \ /\ /      \        __      |_ o\                 /\ /    \ 
 /    \        /  \         _     /<>\     |^|_|                /  \       
/      \ /\   /    \       /o\ *  |__|                         /    \   /\ 
        /  \ /      \      |_|                            _   /      \ /  \
/\     /    \ /\      ###   .        ######  ######      /o\    /\    /    
  \   /      /  \    #####      ###  ######  ######      |_|   /  \  /     
   \   /\   /    \    ###   '. ##### #####    #####           /    \   /\  
    \ /  \ /      \   /|\    `  ###  ####      ####   ###    /      \ /  \ 
     /    \               __    /|\                  #####   /\      /    \
 /\ /      \ /\          /  \ .`'    ####      ####   ###   /  \    /      
/  \        /  \         |__|        #####?   #####   /|\  /    \          
    \      /    \         ,' . ``    ######  ######       /      \ /\      
     \ /\ /      \ /\         '`'.,  ######  ###### *  ###        /  \     
      /  \        /  \    ###     ``'                 #####      /    \   /
/\   /    \      /    \  #####   _        __           ###   /\ /      \ / 
  \ /      \ /\ /         ###   / \ '    /<>\   `      /|\  /  \        /  
   \        /  \          /|\   |_| .    |__|     .'       /    \   /\ /   
    \ /\   /    \              ` ``'         ###   ,  _   /      \ /  \    
     /  \ /      \ /\             _         ##### ', /o\          /    \   
    /    \        /  \         . / \         ### ,   |_|        /\      \ /
   /      \ /\   /    \          |_|         /|\ ,  * `        /  \      / 
           /  \ /      \       ,.     _            ',` ''     /    \   /\  
          /    \          ###       _/ \   ###    _____  '   /      \ /  \ 
         /      \ /\     #####     /o  |  #####  /_____\ `'     /\   /    \
     /\          /  \     ###   `'.|___|   ###   |<>_<>|       /  \ /      
    /  \        /    \    /|\     '',.,    /|\   |_|^|_|  ,   /    \       
   /    \   /\ /      \        __     `,'.``` .',  .``'   `  /      \ /\   
  /      \ /  \               /<>\  ###              ,,.'            /  \  
          /    \              |__| #####          ###               /    \ 
      /\ /      \ /\            '   ###      *   #####            /\      \
     /  \        /  \           `   /|\  _        ###   _        /  \      
    /    \      /    \   /\       ..    /o\      ./|\  /o\      /    \   /\
   /      \ /\ /      \ /  \       .''  |_|   ,'`' ',` |_|  /\ /      \ /  
           /  \        /    \         ,.,  .,`,  /\  ', ,` /  \        /   
     /\   /    \   /\ /      \ /\               /  \      /    \   /\ /    
    /  \ /      \ /  \        /  \   /\  *     /    \ /\ /      \ /  \     
   /    \        /    \      /    \ /  \   /\ /      /  \   /\   /    \    
  /      \      /      \ /\ /      /    \ /  \      /    \ /  \ /      \   
                        /  \      /      /    \    /      /    \           
                       /    \           /      \         /      \          """,
# Autres mondes (Vanaheim = 1)
    (28, 13, 2, 14, 68),  # Alfheim
    (54, 29, 3, 10, 58),  # Midgard
    (56, 42, 5, 11, 120), # Jotunheim
    
# Maisons
    (44, 11, 21, 5, 9), # Auberge
    (52, 35, 22, 20, 19),
)

# * : (31; 12)
# * : (52; 22)
# * : (52; 30)
# * : (45; 39)

def vanaheim_npc(data, stat):
    coords = data[2], data[3]

    # Riethas
    if coords == (31, 12):
        if stat[8] == 5: return {
            82: [0, "Kamuel est au sud, a la limite des montagnes."],
            86: [2, "Parfait, merci beaucoup !", 0, (1, -25), (8, -5)],
        }

        else: return {
                "base": [0, "Riethas, simple paysan. Que Nerthus vous garde !"],
                78: [0, "Je suis Riethas. Kamuel me doit de l'argent. Si tu veux bien aller le chercher, je te laisserai une part.\n1. Je m'en charge.\n2. Hum, non.", 2],
                    79: [3, "Merci ! Tu le trouveras au sud de Vanaheim.", 0, (8, 5)],
                    80: [-2, "Cela ne fait rien."],
            }

    # Kamuel
    if coords == (41, 45):
        if stat[8] == 5:
            if data[0] == 84: return [20, 20, 20, 20, 100], "Kamuel", 50, 2
            else: return {
                "base": [0, "Kamuel, que puis-je pour vous ?"],
                82: [0, "Kamuel, que voulez-vous ?\n1. Tu dois de l'argent a Riethas.\n2. Vous tuer.", 2],
                83: [3, "Bien sur, voila. [+50 PO]", 0, (1, 50)],
            }

    # Charrette
    if coords == (45, 39):
        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Jotunheim\n3. Alfheim", 3]

        else:
            destinations = ("Midgard", "Jotunheim", "Alfheim")
            dest_coords = ((3, 10, 58), (5, 11, 120), (2, 14, 68))
            for i in range(1, 4):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]                     

def vanaheim_po(coords):
    if coords == (42, 20): return [0, "Vous vous trouvez sur le bord d'une large place verdoyante et bien entretenue. Entoure de montagnes, Vanaheim semble hors d'atteinte du temps. Quelques maisons et arbres completent le decor."]





h_21 = (r"""
|=======================|
|       * |             |
|         |-------------|
|                       |
|  +--+   +--+   +--+   |
|  |  |   |  |   |  |   |
|  +--+   +--+   +--+*  |
|                       |
|                       |
|===|^|=================|""",
    (5, 9, 1, 44, 11)) # * : (8, 1) * : (21, 6)

def h_21_npc(data, stat):
    coords = data[2], data[3]

    if coords == (8, 1):
        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Cher client bonjour ! Que puis-je faire pour vous ?\n1. Manger [5 PO]\n2. Boire [2 PO]\n3. Dormir [10 PO]", 3]
        
        elif data[0] == stat[9] + 1:
            stat[9] = -1
            if stat[1] < 5: return [-1, "Tsst, quand on ne peut pas payer, on ne rentre pas."]
            return [-1, "Et un plat chaud, un ! [VOUS VOUS ASSEYEZ DEVANT UN TRANCHOIR DE PAIN ET UNE ASSIETTE DE SOUPE EPAISSE.]", 0, (0, 5), (1, -5)]
        
        elif data[0] == stat[9] + 2:
            stat[9] = -1
            if stat[1] < 2: return [0, "La maison ne fait pas credit."]
            return [-2, "Et voila ! [L'AUBERGISTE PLACA DEVANT VOUS UNE CHOPE DE BIERE]", 0, (0, 2), (1, -2)]

        elif data[0] == stat[9] + 3:
            stat[9] = -1
            if stat[1] < 10: return [-3, "Allez donc voir ailleurs."]
            stat[4] = 360
            return [-3, "Votre chambre est a l'etage.\n[VOUS MONTEZ A L'ETAGE ET VOUS ENDORMEZ SANS DIFFICULTES.]", 0, (0, 10), (1, -10)]

    # Utarg
    elif coords == (21, 6): return {
            "base": [0, "Uiiips ?"],
            40: [2, "Ah, enfin ! D'apres nos informateurs, Odin va d'abord attaquer Midgard, et plus precisement le manoir au sud. On se retrouve dans le parc. Bon route, {} !".format(stat[5])],
            42: [0, "[UTARG EST DEJA EN ROUTE POUR MIDGARD.]"]
        }




h_22 = (r"""
|=======================|==============|
|=======================|==============|
|                       |              |
|   _         _         |     __    *  |
|  (_)       (_)        |    |__|      |
|  |=|       |=|        |    |__|      |
|  |_|       |_|        |    |__|      |
|                       |              |
| *                     |              |
|                 |=]  [|]  [==========|
|   _         _   |                    |
|  (_)       (_)  |                    |
|  |=|       |=|  |   |=======[]=======|
|  |_|       |_|  |   |                |
|                 |   |                |
|                 |   |                |
|                 |   |                |
|                 |   |                |
|/\=/\=/\=/\=/\=/\=| |=/\=/\=/\=/\=/\==|
|\/=\/=\/=\/=\/=\/=]^[=\/=\/=\/=\/=\/==|""",
    (20, 19, 1, 52, 35)) # * : (36, 3) * : (2, 8)

def h_22_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    # Freyja
    if coords == (2, 8):
        if xp == 45 and stat[8] == 0:
            stat[8] = 1

        if not (360 <= stat[4] <= 1200):
            return [0, "Revenez plus tard s'il vous plait : il fait nuit."]

        else: return {
            "base": [0, "Bonjour, je suis Freyja, deesse de la beaute et de l'erotisme."],
            1: [1, "Hum. [FREYJA REGARDE LA DAGUE] Odin me propose la paix... Mais cela ne se passera pas comme ca. [ELLE VOUS REND LA DAGUE]. Rendez sa dague a Odin. Avant que vous ne partiez pour Asgard, allez voir Freyr, il est dans la piece adjacente, il te renverra directement a Asgard."],

            14: [1, "Hum, merci de m'avoir prevenue. Tu peux aller dire a Odin que tu as tue Gullveig, Odin lui-meme ne peut pas la tuer [FREYJA A UN PETIT RIRE.] {}, il sera bientot temps de choisir un camp songes-y.".format(stat[5])],
            31: [0, "{} ! J'ai rarement ete aussi heureuse de te voir mon cher. Tu viens joindre tes forces a notre cause ?\n1. J'y reflechis encore.\n2. Je vous suis !".format(stat[5]), 2],
                32: [-1, "Bien, bien, mais depeche-toi !"],
                33: [1, "Voila une heureuse nouvelle !\n[FREYJA AVAIT A PEINE FINI SA PHRASE QU'UN TRAIT DE FEU TRAVERSA LE CIEL.]\nOdin nous declare la guerre ! Nous devons rassembler nos forces. Va a Jotunheim, et previent Thrym."],
            
            44: [0, "Ah, {} !\n1. Nous avons pris le manoir de Midgard.\n2. Quels liens vous unissent aux Geants ?\n3. Savez-vous ou je peux trouver une bibliotheque ?".format(stat[5]), 3],
                45: [-1, "Parfait ! Vois avec Freyr pour ta recompense."],
                46: [-2, "A l'origine des Vanes est Thjazi, un Geant, il enleva Idunn, une Asyne, ce qui signa le debut de nos conflits avec les Ases. Ces differents n'ont cesses de s'amplifier avec le temps, les Ases ne perdant pas une occasion de tuer un Geant. Finalement, les Geants et nous ne formons qu'une seule et meme famille, ces liens sont encore plus forts depuis que Freyr, mon frere, s'est marie avec Gerd, une Geante. Leur monde est Jotunheim, tu peux y acceder uniquement par Vanaheim."],
                47: [-3, "Hmm, je crois qu'il y en a une vers Alfheim."],

            56: [0, "Tu as trouve quelque chose ?\n1. Les runes signifient 'kvasir'.", 1, (8, -2)],
            57: [3, "'kvasir' ? Cela ne me dit rien... Laissons cela de cote, Va voir Freyr, il te precisera ta prochaine mission."],

            74: [0, "Te voila enfin !\n1. C'est un succes.\n2. Ou en est la guerre ?", 2],
                75: [3, "Bien joue {} ! Tu as merite un peu de repos. Reviens me voir quand tu sera repose.".format(stat[5])],
                76: [-2, "Hum... Nous ne parvenons pas a sortir du statu quo. Chez les Ases comme chez nous, les troupes sont fatiguees. Ce ne sont que des rumeurs, mais une treve pourrait se profiler."],

            78: [0, "Riethas cherche quelqu'un pour un service... Tu le trouveras a Vanaheim, dans la direction de Nordri."],

            88: [2, "Apres avoir convoque les autres Vanes nous avons conclu qu'il faut cesser cette guerre. Tu iras donc porter ce message a Odin. [FREYJA VOUS TEND UN PARCHEMIN SELLE.]"],

            94: [0, "Alors ?\n1. Odin a accepte la treve.", 1],
                95: [1, "Parfait ! J'ai dit a Odin treve se deroulera a Midgard, sous les colonnes du palais. On se retrouve la-bas."],

            98: [2, "L'echange d'otage a ete tres inegal, j'ai ordonne l'execution de Mimir ! [FREYJA VOUS TENDIT LA TETE DE MIMIR.] Va donc porter cela a Odin."]
        }

    # Freyr
    elif coords == (36, 3):
        if (not 360 <= stat[4] <= 1200):
            return [0, "He ! Il fait nuit !"]

        if xp == 2:
            check = True
            for spell_id, spell_level in stat[7]:
                if spell_id == 0: check = False

            data[1] = 0
            data[2], data[3] = 126, 71
            
            if check:
                stat[7].append((0, 1))
                return [1, "Chez les Vanes, nous rendons hommage aux messagers, en guise de remerciement, je vais vous apprendre le sort de Soin [FREYR DESSINA DANS L'AIR DES RUNES VIOLETTE QUI TOURNOYERENT UN INSTANT AVANT DE S'ESTOMPER PEU A PEU.]\nEt maintenant : direction Asgard !\n[UNE LOURDE TORPEUR S'ABATTIT SUR VOUS. VOUS VOUS SENTEZ LEGER. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]"]
            else:
                return [1, "Chez les Vanes, nous rendons hommage aux messagers, voici quelques pieces d'or, faites en bon usage ! [UNE LOURDE TORPEUR S'ABATTIT SUR VOUS. VOUS VOUS SENTEZ LEGER. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]", 0, (1, 5)]
        
        elif xp == 44:
            if stat[8] == 0: return [0, "Va donc annoncer la nouvelle a Freyja !"]
            if stat[8] == 2: return [0, "Tsst, tu as deja eu ta recompense. Essaye plutot de comprendre ce que signifie ces runes."]
            check = True
            for spell_id, spell_level in stat[7]:
                if spell_id == 2: check = False
            
            if check:
                stat[7].append((2, 2))
                return [0, "En remerciement je vais t'apprendre le sort Givre de niveau II. [FREYR COMMENCA A CHANTER UNE MELODIE, VOTRE VISION DEVINT FLOUE. LORSQUE VOUS REPRENEZ VOS ESPRITS, VOUS LE SORT EST GRAVE DANS VOTRE MEMOIRE.]", 0, (8, 1)]
            else:
                return [0, "Je vois que tu connais deja le sort Givre, voila la somme equivalente. [+20 PO]", 0, (1, 20), (8, 1)]

        if xp == 64:
            message = input("Parfait ! (ecrivez le message dechiffre) :\n")
            if message.lower() == "prenez alfheim": return [2, "Ah ! Parfait, montre-moi ca ! [VOUS TENDEZ LE MESSAGE DECHIFFRE A FREYR.]"]
            else: return [-2, "Ca n'a aucun sens... cherche encore."]

        if xp == 66:
            data[1], data[2], data[3] = 6, 93, 8
            return [2, "Bien, j'ai modifie le contenu du message pour attire les soldats Ases dans un piege, tu vas donne ce parchemin a Skirnir qui le portera aux Ases. Tu le trouveras vers Nidavellir. [UNE TERRIBLE FATIGUE S'ABATTIT SUR VOUS, UNE SENSATION DE CHUTE ACCOMPAGNA VOTRE PERTE DE CONSCIENCE. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]"]

        else: return {
            "base": [0, "Freyr, dieu de la vie. Bienvenue a Vanaheim"],
            16: [8, "J'aurais besoin de ton aide...\n1. Peut-etre plus tard ?\n2. Oui ?", 2],
                25: [-9, "Si tu es toujours interesse..."],
            26: [1, "Votre situation, entre Vanes et Ases nous derange. Je suis desole de ne pas etre plus explicite. Allez voir Lithy, elle se trouve a Midgard, vers le centre, dans l'alignement du grand palais. Elle vous expliquera la suite."],

            60: [2, "Ah {} ! Mon messager, Skirnir, en se faisant passer pour un Ase, a intercepte un message; mais il est chiffre. [FREYR VOUS TEND UN PARCHEMIN PLIE.] Le message est : 'zmefmq kgfzmzw'. Reviens me voir quand tu auras termine.".format(stat[5])],
            62: [0, "Deja fini ?\n1. Pas encore...\n2. Oui !", 2],
                63: [-1, "Reviens me voir quand tu auras avance, le message est : 'zmefmq kgfzmzw'."],
        }
