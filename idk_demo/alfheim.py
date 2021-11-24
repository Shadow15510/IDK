alfheim = (r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~         ~~~~      ~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~     *  ~~~~~~   ##    ~~~~~~~~~~~~    ~~~~~~~~       ~~~~~~~~~~~~~~~
~~~~~        ~~~~~~~  ####        ~~~~~~~        ##                ~~~~~~~~
~~~         ~~~~~      ||         ~~~~~~~     * ####    __   ##     ~~~~~~~
~~~         ~~~~~~~~       ##      ~~~~~  ##     ||    /[]\ ####      ~~~~~
~~~      ~~~~~~~~~~~~     ####  ##   ##  ####  `    '  |__|  ||  __     ~~~
~~~      ~~~~~~~~~~~~ ##   ||  #### ####  ||   ,'    '.'        /  \    ~~~
~~~      ~~~~~  ~~~~ ####       ||   ||      ` '  __   '`' . `  |__|     ~~
~~~  ##         ~~~   ||                    ''   /[]\        ' .     ##  ~~
~~  ####  ##   _          _________________      |__|   ##     `.`  #### ~~
~~   ||  #### / \        /  |]O[|   |]O[|  \           ####  __      ||  ~~
~~~~      ||  |_|       /___________________\  ##  ##   ||  /[]\         ~~
~~~~  ##           _    |_/   \_/ _ \_/   \_|  ##  ##       |__|  ##   ~~~~
~~~~ ####         / \   |_|   |_|/^\|_|   |_|          __        ####  ~~~~
~~~~  ||      _   |_|  *                       ##  ## /  \    `'  ||   ~~~~
~~~~         /-\         ###             ###   ##  ## |__|  .  ,       ~~~~
~~~~~~~~~    |_|   _    #####           #####            `' `_ ,,  ,    ~~~
~~~~~~~~~         /o\    ###      ?      ### '   _     ``'  / \         ~~~
~~~~~~~~~~~       |_|    /-\             /-\ ,  / \         |_|  ~~~~   ~~~
~~~~~~~~~~~~                 ###     ###     ' ,|_|  .'   _      ~~~~~  ~~~
~~~~~~ ~~~~~~~      ###     ##### ` #####  .   `  .,.    /-\     ~~~~~  ~~~
~~~~~  ~~~~~~~     #####     ###  '  ###      _ ` , _    |_| _   ~~~~~~ ~~~
~~~~~   __  ~~      ###      /-\     /-\  `  / \ , /o\      / \  ~~~~~~~~~~
~~~~~~ /  \         /-\          ' .  '``,'' |_|`  |_|      |_|  ~~~~~~~~~~
~~~~~~ |__|                      ,.   '     .`  ',               ~~~~~~~~~~
~~~~~~        __       ###         .,    _    .  ,  _       ,.   ~~~~~~~~~~
~~~~~~~~     /  \     #####  ###        / \   ` '  /o\__    `.    ~~~~~~~~~
~~~~~~~~~    |__|      ###  #####  ###  |_|    .   |_ o \==| .'`.   ~~~~~~~
~~~~~~~~~~~~       ### /-\   ###  #####      ,.`  ||^|__|  | .  .   ~~~~~~~
~~~~~~~~~~~~      #####      /-\   ###            |           .'     ~~~~~~
~~~~~~~~~~~~~     #####  ###       /-\ ###   ###  | ,`','` '',,      ~~~~~~
~~~~~~~~~~~        ###  #####  ###    ##### ##### |==|==|==|          ~~~~~
~~~~~~~~~~ ###     |_|  ##### #####    ###   ###               _      ~~~~~
~~~~~~~~~ #####          ###  #####    /-\   /-\  ###      _  / \  _   ~~~~
~~~~~~~~~ #####          |_|   ###   ###         #####    /-\ |_| / \  ~~~~
~~~~~~~~~  ###                 |_|  #####   ###   ###     |_|     |_|  ~~~~
~~~~~~~    |_|     ~~~~~~~          #####  #####  /-\   _              ~~~~
~~~~~~~        ~~~~~~~~~~~~~~~~~~    ###   #####       / \     _       ~~~~
~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~   |_|    ###        |_|    / \  _   ~~~~
~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~~         |_|               |_| / \  ~~~~
~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~~~          ~~~~~~~~~           |_|  ~~~~
~~~~~~~~     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      ~~~~~~~~           ~~~
~~~~~~~~~    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~              ~~~~~~~      ~~~~~~
~~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~~~~~~                      ~~~~~~~~~~~~~
~~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~~~~~             ####  #### ~~~~~~~~~~~~
~~~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~~~~             ###    ### ~~~~~~~~~~~~
~~~~~~~~~~   __  ~~~~~~~~~~~~~~~~~~~~  __    ###    ##      ## ~~~~~~~~~~~~
~~~~~~~~~~  /  \ ~~~~~~~~~~~~~~~~~~~~ /  \  #####              ~~~~~~  ~~~~
~~~~~~~~~~  |__|        ~~~~~~~~~~~~~ |__|  #####   ##      ## ~~~~~   ~~~~
~~~~~~~~~~     ###        ~~~~~~~~           ###    ###    ###   ~~    ~~~~
~~~~~~~~~     #####                   ,''    |_|    ####  ####          ~~~
~~~~~~~~      ##### '      *  ###    ,,,.                       ###     ~~~
~~~~~~~~       ###     ###   #####    `,,                      #####    ~~~
~~~~~~~        |_| .  #####  ##### ',,    __             ###   #####    ~~~
~~~~~~    ###        ,#####   ###  `     /  \  ###      #####   ###     ~~~
~~~~~~   #####   ### , ###    |_|`' ###  |__| #####     #####   |_|     ~~~
~~~~~~   #####  #####``|_| ###   ` #####      #####      ###            ~~~
~~~~~~    ###   ##### '   #####    #####       ###       |_|       ###  ~~~
~~~~~~    |_|    ### ,'   #####     ###        |_|                ##### ~~~
~~~~~~       ##  |_| `     ###      |_|                      ~~   ##### ~~~
~~~~~    ## ####     `     |_|                   ~~~~      ~~~~    ###  ~~~
~~~~    #### ||    .          ~~~~~~~          ~~~~~~    ~~~~~~~~  |_|  ~~~
~~~~~ ## ||     ,` '      ~~~~~~~~~~~~~~~      ~~~~~~    ~~~~~~~~       ~~~
~~~~ ####     _     ~~~~~~~~~~~~~~~~~~~~~~   ~~~~~~     ~~~~~~~~~~~     ~~~
~~~~~ ||     /-\  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      ~~~~~~~~~~~~   ~~~~
~~~~~~  ~    |_|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      ~~~~~~~~~~~~ ~~~~~
~~~~~~~~~~~      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""",
# Autres mondes (Alfheim = 2)
    (14, 68, 1, 28, 13), # Vanaheim

# Maisons
	(34, 16, 23, 25, 19),
	(52, 31, 24, 20, 19), # Librairie
)

# * : (11; 4)
# * : (46; 6)
# * : (23; 17)
# * : (27; 54)

def alfheim_po(coords):
	if coords == (34, 20): return [0, "Quelques arbres au sud vous masque la vue. Au nord, l'imposant palais des Elfes et ses quatres colonnes finement travaillee s'offre a vous. La lourde porte a deux battants en bois massif et fer forge vous fait face. Au sud est, les bruits d'un bourg en pleine activite montent a vos oreilles."]

def alfheim_npc(data, stat):
    pass





h_23 = (r"""
               |==================|               
               |                  |               
               |   _          _   |               
               |  / \        / \  |               
               |  \_/        \_/  |               
               |  |_|  *     |_|  |               
               |                  |               
               |   _          _   |               
               |  / \        / \  |               
               |  \_/        \_/  |               
   |===========|  |_|        |_|  |===========|   
   |                                          |   
   |                                          |   
   |               _          _               |   
   |__        __  / \        / \  __        __|   
   /  \      /  \ \_/        \_/ /  \      /  \   
   \__/      \__/ |_|        |_| \__/      \__/   
   |  |      |  |                |  |      |  |   
   |  |      |  |                |  |      |  |   
   /  \______/  \_______|^|______/  \______/  \   """,
	(25, 19, 2, 34, 16)) # * : (23, 5)

def h_23_npc(data, stat):
	pass





h_24 = (r"""
|====|_|======|           |=====|_|====|
|   /___\     |           |    /___\   |
|   |===|     |===========|    |===|   |
|           * |           |            |
|   +---+     |  _     _  |    +---+   |
|   |   |     | (~)   (~) |    |   |   |
|   |   |     | |_|   |_| |    |   |   |
|   |   |                      |   |   |
|   +---+                      +---+   |
|             |  _     _  |            |
|=============| (~)   (~) |============|
|             | |_|   |_| |            |
|                                   *  |
|                                      |
|             |  _     _  |            |
|=============| (~)   (~) |============|
|=============| |_|   |_| |============|
              |           |             
              |====| |====|             
              |====|^|====|             """,
	(20, 19, 2, 52, 31)) # * : (12, 3) * : (36, 12)

def h_24_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
    levels = ("I", "II", "III", "IV", "V")

    if not (480 <= stat[4] <= 1140): return [0, "Excusez-moi, nous sommes fermes."]

    if coords == (12, 3):
        if not stat[7]: return [0, "Je ne peux pas vous faire oublier ce que vous ne connaissez pas."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Quel sort souhaitez-vous oublier ?\n" + "\n".join(["{0}. {1} {2}".format(nb + 1, spells[stat[7][nb][0]], levels[stat[7][nb][1] - 1]) for nb in range(len(stat[7]))]), len(stat[7])]

        else:
            for i in range(1, len(stat[7]) + 1):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    stat[7].pop(i - 1)
                    return [-i, "Asseyez-vous, je vais vous faire oublier ce sort. [UN PUISSANT MAL DE TETE VOUS PRIT, LES MURS SEMBLERENT TANGUER TANDIS QUE VOTRE VUE DEVINT FLOUE. LE VERTIGE S'ESTOMPA PROGRESSIVEMENT.] Et voila !"]

    if coords == (36, 12):
        spells_sale = ((0, 2), (1, 2), (2, 4), (4, 1))

        if len(stat[7]) >= 3: return [0, "Je suis desole, vous ne pouvez pas apprendre plus de trois sorts."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Diomwar, pour vous servir. Quel sort voulez-vous acheter ?\n1. Soin II\n2. Flammes II\n3. Givre IV\n4. Fatigue I", 4]

        else:
            for i in range(1, 5):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < spells_sale[i - 1][1] * 10: return [-i, "Vous n'avez pas les moyens, desole."]

                    spell_id = -1
                    for sp_id in range(len(stat[7])):
                        sp = stat[7][sp_id]
                        if spells_sale[i - 1][0] == sp[0]:
                            if spells_sale[i - 1][1] <= sp[1]: return [-i, "Vous connaissez deja ce sort."]
                            else:
                                spell_id = sp_id
                                break

                    if spell_id == -1:
                        stat[7].append(spells_sale[i - 1])
                    else:
                        stat[7][spell_id] = spells_sale[i - 1]

                    return [-i, "[DIOMWAR OUVRIT UN LIVRE RELIE DE CUIR NOIR, ET TRACA DU DOIGT DES SIGNES CABALISTIQUES SUR LE SOL. LES RUNES BRILLERENT PUISSAMMENT AVANT DE S'ETEINDRE.]", 0, (1, -spells_sale[i - 1][1] * 10)]


                    
        