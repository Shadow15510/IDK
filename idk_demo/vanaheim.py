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
    pass