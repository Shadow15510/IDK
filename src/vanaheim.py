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
    /  \ /      \ /  \        /  \   /\        /    \ /\ /      \ /  \     
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
    xp = data[0]

    if coords == (31, 12): return {
            "base": [0, "Riethas, simple paysan. Que Nerthus vous garde !"],
        }

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
            return [-2, "Et voila ! [L'AUBERGISTE PLACA DEVANT VOUS UNE CHOPPE DE BIERE]", 0, (0, 2), (1, -2)]

        elif data[0] == stat[9] + 3:
            stat[9] = -1
            if stat[1] < 10: return [-3, "Allez donc voir ailleurs."]
            stat[4] = 360
            return [-3, "Votre chambre est a l'etage.\n[VOUS MONTEZ A L'ETAGE ET VOUS ENDORMEZ SANS DIFFICULTES.]", 0, (0, 10), (1, -10)]

    return [0, "Ch'rois hips qu'j'ais hips trop buu'hips."]




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
        if not (360 <= stat[4] <= 1200):
            return [0, "Revenez plus tard s'il vous plait : il fait nuit."]

        else: return {
            "base": [0, "Bonjour, je suis Freyja, deesse de la beaute et de l'erotisme."],
            1: [1, "Hum. [FREYJA REGARDE LA DAGUE] Odin me propose la paix... Mais cela ne se passera pas comme ca. [ELLE VOUS REND LA DAGUE]. Rendez sa dague a Odin. Avant que vous ne partiez pour Asgard, allez voir Freyr, il est dans la piece adjacente, il te renverra directement a Asgard."],

            14: [1, "Hum, merci de m'avoir prevenue. Tu peux aller dire a Odin que tu as tue Gullveig, Odin lui-meme ne peut pas la tuer [FREYJA A UN PETIT RIRE.] {}, il sera bientot temps de choisir un camp songes-y.".format(stat[5])],
            31: [0, "{} ! J'ai rarement ete aussi heureuse de te voir mon cher. Tu viens joindre tes forces a notre cause ?\n1. J'y reflechis encore.\n2. Je vous suis !".format(stat[5]), 2],
                32: [-1, "Bien, bien, mais depeche-toi !"],
                33: [1, "Voila une heureuse nouvelle !"]
        }

    # Freyr
    elif coords == (36, 3):
        if (not 360 <= stat[4] <= 1200):
            return [0, "Hein ? Quoi ? Ca va pas non ? Qu'est-ce qu'il vous a pris de me reveiller comme ca ?"]

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



        else: return {
            "base": [0, "Freyr, dieu de la vie. Bienvenue a Vanaheim"],
            16: [8, "J'aurais besoin de ton aide...\n1. Peut-etre plus tard ?\n2. Oui ?", 2],
                25: [-9, "Si tu es toujours interesse..."],
            26: [1, "Votre situation, entre Vanes et Ases nous derange. Je suis desole de ne pas etre plus explicite. Allez voir Lithy, elle se trouve a Midgard, vers le centre, dans l'alignement du grand palais. Elle vous expliquera la suite."],
        }
