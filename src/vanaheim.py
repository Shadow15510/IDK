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
     /  \ /      \ /\             _         ##### ', /-\          /    \   
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
    pass

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
        if stat[6][0] == -1:
            stat[6] = stat[4], data[0]
            return [0, "Cher client bonjour ! Que puis-je faire pour vous ?\n1. Manger [5 PO]\n2. Boire [2 PO]\n3. Dormir [10 PO]", 3]
        
        elif data[0] == stat[6][1] + 1:
            stat[6] = (-1, -1)
            if stat[1] < 5: return [-1, "Tsst, quand on ne peut pas payer, on ne rentre pas."]
            return [-1, "Et un plat chaud, un !", 0, (0, 5), (1, -5)]
        
        elif data[0] == stat[6][1] + 2:
            stat[6] = (-1, -1)
            if stat[1] < 2: return [0, "La maison ne fait pas credit."]
            return [-2, "Et voila !", 0, (0, 2), (1, -2)]

        elif data[0] == stat[6][1] + 3:
            stat[6] = (-1, -1)
            if stat[1] < 10: return [-3, "Allez donc voir ailleurs."]
            stat[4] = 360
            return [-3, "Votre chambre est a l'etage.\n[LA NUIT PASSE]", 0, (0, 10), (1, -10)]

    return [0, "Je grois qu'j'ais trop buurrps."]




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
    if coords == (36, 3):
        if not (360 <= stat[4] <= 1200):
            return [0, "Revenez plus tard s'il vous plait."]

        if xp == 1:
            stat[8].append((0, 1))
            return [1, "Hum. [FREYJA REGARDE LA HACHE] Odin me propose la paix... Mais ca ne se passera pas comme ca. [ELLE VOUS REND LA HACHE]. Allez voir Odin, et rendez-lui sa hache. En remerciement de vos services, je vous apprend le sort de Soin. [FREYJA DESSINA DU DOIGT DES RUNES VIOLETTE DANS L'AIR. LES LETTRES LUMINEUSES BRILLERENT UN INSTANT AVANT DE S'ESTOMPER PROGRESSIVEMENT.]"]

        else: return {
            "base": [0, "Bonjour, je suis Freyja, deesse de la beaute et de l'erotisme."]
        }

    # Freyr
    elif coords == (2, 8):
        if (not 360 <= stat[4] <= 1200):
            return [0, "Hein ? Quoi ? Ca va pas non ? Qu'est-ce qu'il vous a pris de me reveiller comme ca ?"]

        else: return {
            "base": [0, "Freyr, dieu de la vie. Bienvenue a Vanaheim"]
        }
