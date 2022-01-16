from idk_lib import *


# Game
def npc(data, stat):    
    npc_data = (
    asgard_npc,
    vanaheim_npc,
    alfheim_npc,
    midgard_npc,
    niflheim_npc,
    jotunheim_npc,
    nidavellir_npc,
    muspellheim_npc,
    svartalfheim_npc,
    h_9_npc, h_10_npc, h_11_npc, h_12_npc, h_13_npc, h_14_npc, h_15_npc, h_16_npc, h_17_npc, h_18_npc, h_19_npc, h_20_npc,
    h_21_npc, h_22_npc,
    h_23_npc, h_24_npc,
    h_25_npc, h_26_npc, h_27_npc, h_28_npc,
    h_29_npc, h_30_npc,
    h_31_npc, h_32_npc, h_33_npc, h_34_npc, h_35_npc, h_36_npc,
    h_37_npc, h_38_npc, h_39_npc, h_40_npc, h_41_npc,
    h_42_npc, h_43_npc, h_44_npc,
    h_45_npc, h_46_npc, h_47_npc, h_48_npc)


    return npc_core(npc_data[data[1]], data, stat)


def point_of_interest(data, stat):
    po_data = (
        asgard_po,
        vanaheim_po,
        alfheim_po,
        midgard_po,
        niflheim_po,
        jotunheim_po,
        nidavellir_po,
        muspellheim_po,
        svartalfheim_po
    )

    coords = data[2], data[3]
    event = po_data[data[1]](coords)

    if not event: return [0, "Il n'y a rien à voir ici."]
    else: return event


print("<scenario>")
events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 8: misc_stat, 6: inventory, 9: sleep, "s": quick_save}


def scenario(save_code=None):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - classe, 7 - sorts connus : (id, level), 8 - sous-quêtes terminées]
    if not save_code:
        stat = init_stat()
        name = stat[5]
        data = [{"main": 0}, 3, 44, 66]

        print_text("<intro>")
    else:
        stat, data = decode_save(save_code)

    idk_game = Asci(maps, events, keys)
    stat, data = idk_game.mainloop(10, stat, data, routine=routine, door="^_", walkable=".,`' ", exit_key="q")
    if stat[9] != -1: data[0]["main"] -= stat[9]

    if data[0]["main"] == 10:
        print_text("<conclusion>")
    else:
        print("Pour continuer :\nscenario(\"{}\")".format(encode_save(data, stat[:-1])))


# Scenario
def shop_interaction(data, stat, nb_choice, *events):
    for choice in range(nb_choice):
        if data[0]["main"] == stat[9] + choice + 1:
            stat[9] = -1
            if stat[1] < events[choice][0]: return events[choice][2], choice + 1
            else: return events[choice][1], choice + 1


# - - - Asgard - - - #
def asgard_po(coords):
    # ? : (120, 26)
    # ? : (51, 55)
    pass

def asgard_npc(data, stat):
    coords = data[2], data[3]
    # * : ( 34, 7)
    # * : ( 29, 13)
    # * : ( 19, 20)
    # * : (121, 21)
    # * : ( 28, 26)
    # * : (117, 32)
    # * : ( 46, 35)
    # * : ( 57, 38)
    # * : ( 82, 38)
    # * : ( 22, 39)
    # * : (  8, 44)
    # * : ( 58, 50)
    # * : ( 83, 51)
    # * : ( 32, 59)
    # * : (104, 63)
    # * : ( 46, 65)
    # * : ( 16, 71)
    # * : (138, 71)
    pass


# Forseti
def h_9_npc(data, stat):
    # * : (19, 4)
    pass

# Odin
def h_10_npc(data, stat):
    # * : (25, 11)
    pass


def h_11_npc(data, stat):
    # * : (34, 7)
    pass


def h_12_npc(data, stat):
    # * : (19, 4)
    pass


# Folkvangr
def h_13_npc(data, stat):
    # * : (21, 8)
    pass


def h_14_npc(data, stat):
    # * : (26, 2)
    pass


# Vidar
def h_15_npc(data, stat):
    # * : (10, 6)
    pass

def h_16_npc(data, stat):
    # * : (50, 14)
    pass


def h_17_npc(data, stat):
    # * : (36, 14)
    pass


def h_18_npc(data, stat):
    # * : (30, 9)
    pass


def h_19_npc(data, stat):
    # * : (28, 7)
    pass


def h_20_npc(data, stat):
    # * : (39, 9)
    pass


# - - - Vanaheim - - - #
def vanaheim_po(coords):
    # ? : (42, 20)
    pass


def vanaheim_npc(data, stat):
    # * : (31; 12)
    # * : (52; 22)
    # * : (52; 30)
    # * : (45; 39)

    # Charrette
    if coords == (45, 39):
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Jotunheim\n3. Alfheim", 3]

        else:
            destinations = ("Midgard", "Jotunheim", "Alfheim")
            dest_coords = ((3, 10, 58), (5, 11, 120), (2, 14, 68))
            for i in range(1, 4):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]                     


def h_21_npc(data, stat):
    # * : (8, 1)
    # * : (21, 6)
    coords = data[2], data[3]

    if coords == (8, 1):
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Cher client bonjour ! Que puis-je faire pour vous ?\n1. Manger [5 PO]\n2. Boire [2 PO]\n3. Dormir [10 PO]", 3]
        else:
            event, _ = shop_interaction(data, stat, 3,
                (5, [-1, "Et un plat chaud, un ! [VOUS VOUS ASSEYEZ DEVANT UN TRANCHOIR DE PAIN ET UNE ASSIETTE DE SOUPE EPAISSE.]", 0, (0, 5), (1, -5)], [-1, "Tsst, quand on ne peut pas payer, on ne rentre pas."]),
                (2, [-2, "Et voila ! [L'AUBERGISTE PLACA DEVANT VOUS UNE CHOPE DE BIERE]", 0, (0, 2), (1, -2)], [-2, "La maison ne fait pas credit."]),
                (10, [-3, "Votre chambre est a l'etage.\n[VOUS MONTEZ A L'ETAGE ET VOUS ENDORMEZ SANS DIFFICULTES.]", 0, (0, 10), (1, -10), (4, 480)], [-3, "Allez donc voir ailleurs."]))

            return event


def h_22_npc(data, stat):
    # * : (36, 3)
    # * : (2, 8)
    pass


# - - - Alfheim - - - #
def alfheim_po(coords):
    # ? : (34, 20)
    pass

def alfheim_npc(data, stat):
    # * : (11; 4)
    # * : (46; 6)
    # * : (23; 17)
    # * : (27; 54)
    coords = data[2], data[3]

    # Charrette
    if coords == (23, 17):
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Asgard\n3. Vanaheim\n4. Svartalfheim", 4]

        else:
            destinations = ("Midgard", "Asgard", "Vanaheim", "Svartalfheim")
            dest_coords = ((3, 10, 58), (0, 126, 71), (1, 28, 13), (8, 109, 66))
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)] 


def h_23_npc(data, stat):
    # * : (23, 5)
    pass


def h_24_npc(data, stat):
    # * : (12, 3)
    # * : (36, 12)
    coords = data[2], data[3]
    

    spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
    levels = ("I", "II", "III", "IV", "V")

    if not (480 <= stat[4] <= 1140): return [0, "Excusez-moi, nous sommes fermes."]

    if coords == (12, 3):
        if not stat[7]: return [0, "Je ne peux pas vous faire oublier ce que vous ne connaissez pas."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Quel sort souhaitez-vous oublier ?\n" + "\n".join(["{0}. {1} {2}".format(nb + 1, spells[stat[7][nb][0]], levels[stat[7][nb][1] - 1]) for nb in range(len(stat[7]))]), len(stat[7])]

        else:
            for i in range(1, len(stat[7]) + 1):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    stat[7].pop(i - 1)
                    return [-i, "Asseyez-vous, je vais vous faire oublier ce sort. [UN PUISSANT MAL DE TETE VOUS PRIT, LES MURS SEMBLERENT TANGUER TANDIS QUE VOTRE VUE DEVINT FLOUE. LE VERTIGE S'ESTOMPA PROGRESSIVEMENT.] Et voila !"]

    if coords == (36, 12):
        spells_sale = ((0, 2), (1, 2), (2, 4), (4, 1))

        if len(stat[7]) >= 3: return [0, "Je suis desole, vous ne pouvez pas apprendre plus de trois sorts."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Diomwar, pour vous servir. Quel sort voulez-vous acheter ?\n1. Soin II\n2. Flammes II\n3. Givre IV\n4. Fatigue I", 4]

        else:
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
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


# - - - Midgard - - - #
def midgard_po(coords):
    # ? : (29, 9)
    # ? : (53, 24)
    # ? : (66, 45)
    # ? : (52, 79)
    pass

def midgard_npc(data, stat):
    # * : (67, 46)
    # * : (39, 49)
    # * : (66, 56)
    # * : (68, 71)
    # * : (8, 59)
    # * : (94, 85)
    # * : (51, 60)
    coords = data[2], data[3]
    
    # Charrette
    elif coords == (39, 49):
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Vanaheim\n2. Asgard\n3. Nidavellir\n4. Niflheim", 4]

        else:
            destinations = ("Vanaheim", "Asgard", "Nidavellir", "Niflheim")
            dest_coords = ((1, 54, 29), (0, 126, 71), (6, 93, 8), (4, 78, 19))
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]  


def h_25_npc(data, stat):
    pass


def h_26_npc(data, stat):
    # * : (17, 7)
    # * : (22, 7)
    # * : (17, 8)
    # * : (27, 8)
    # * : (27, 6)
    coords = data[2], data[3]
    

    # Rosahil Green
    if coords == (27, 6):
        if stat[4] >= 1320 or stat[4] <= 340: return [0, "Je suis desolee, nous sommes fermes. Revenez plus tard !"]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Rosahil Green, tenanciere de cette auberge. Vous desirez quelque chose ?\n1.De quoi manger s'il vous plait. [-5 PO]\n2.Je voudrais une chambre pour la nuit. [-10 PO]", 2]
        else:
            event, choice = shop_interaction(data, stat, 2,
                (5, [-1, "Et voila pour vous ! [ROSAHIL POSA UNE ASSIETTE DE RAGOUT CHAUD DEVANT VOUS.]", 0, (0, 5), (1, -5)], [-1, "Reviens quand tu auras assez de pieces d'or."]),
                (10, [-2, "Suivez-moi, je vais vous montrer votre chambre. [VOUS SUIVEZ ROSAHIL DANS L'AUBERGE, LA NUIT PASSA.]", 0, (0, 10), (1, -10), (4, 480)], [-2, "Je suis desolee, tu n'as pas assez !"]))

            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Il est trop tot, revenez vers 19h."]
            else: return event

    else: return [0, "Ui hips ?"]


def h_27_npc(data, stat):
    pass


def h_28_npc(data, stat):
    # * : (27, 6)
    pass

# - - - Niflheim - - - #
def niflheim_po(coords):
    # ? : (88, 32)
    pass

def niflheim_npc(data, stat):
    # * : (95, 30)
    # * : (57, 31)
    # * : (39, 60)
    # * : (108, 67)
    pass


def h_29_npc(data, stat):
    # * : (5, 5)

    coords = data[2], data[3]

    spells_sale = ((0, 5), (1, 5), (2, 5), (3, 5), (4, 5))

    if not (480 <= stat[4] <= 1140): return [0, "Je suis desolee, nous sommes fermes."]

    if coords == (5, 5):
        if len(stat[7]) >= 3: return [0, "Vous ne pouvez pas apprendre plus de sort, et je ne pratique pas les sorts d'oubli. Je crois qu'une librairie vers Alfheim le fait gratuitement."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Merath, je vend les sorts les plus puissants de tout l'Yggdrasil ! Quel sort voulez-vous ?\n1. Soin V\n2. Flammes V\n3. Givre V\n4. Etincelles V\n4. Fatigue V", 4]

        else:
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 50: return [-i, "Vous n'avez pas les moyens, desolee."]

                    spell_id = -1
                    for sp_id, sp in range(len(stat[7])):
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

                    return [-i, "[MERATH SE RETOURNA ET S'EMPARA D'UN GRIMOIRE. ELLE L'OUVRIT ET LUT A HAUTE VOIX. UNE LOURDE TORPEUR S'ABBATIT SUR VOUS. QUAND VOUS REPRENEZ PLEINEMENT CONSCIENCE, LE SORT EST GRAVE DANS VOTRE MEMOIRE.]", 0, (1, -50)]


def h_30_npc(data, stat):
    # * : (37, 4)
    # * : (17, 6)
    pass


# - - - Jotunheim - - - #
def jotunheim_po(coords):
    # ? : (60, 57)
    # ? : (23, 70)
    # ? : (60, 86)
    pass

def jotunheim_npc(data, stat):
    # * : (25; 10)
    # * : (39; 20)
    # * : (3; 28)
    # * : (34; 45)
    # * : (53; 49)
    # * : (19; 51)
    # * : (34; 56)
    # * : (64; 64)
    # * : (54; 70)
    # * : (8; 72)
    # * : (40; 75)
    # * : (72; 87)
    # * : (6; 98)
    pass


def h_31_npc(data, stat):
    # * : (28, 4)
    pass


def h_32_npc(data, stat):
    # * : (28, 6)
    pass


def h_33_npc(data, stat):
    # * : (48, 5)
    # * : (24, 7)
    pass


def h_34_npc(data, stat):
    # * : (26, 6)
    pass


def h_35_npc(data, stat):
    # * : (17, 5)
    pass


def h_36_npc(data, stat):
    # * : (11, 3)
    # * : (27, 10)
    # * : (9, 12)
    coords = data[2], data[3]
    
    if coords == (27, 10):
        if not (300 <= stat[4] <= 1380): return [0, "Je suis desole, nous somme ferme la nuit."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Vous voulez quelque-chose ?\n1. Je mangerai bien un truc [-4 PO]\n2. Il vous reste une chambre ? [-12 PO]", 2]

        else:
            event, choice = shop_interaction(data, stat, 2,
                (4, [-1, "Et voila ! [LE TAVERNIER POSA UNE ASSIETTE FUMANTE DEVANT VOUS ET UN VERRE DE VIN]", 0, (0, 5), (1, -4)], [-1, "Reviens quand tu auras de quoi me payer."]),
                (12, [-2, "Oui, au premier etage, au bout du couloir sur votre droite. [VOUS SUIVEZ LES INDICATIONS DU TAVERNIER ET TROUVEZ VOTRE CHAMBRE. VOUS SOMBREZ DANS LES BRAS DE NOTT.]", 0, (0, 15), (1, -12), (4, 480)], [-2, "Tu n'as pas assez."]))
        
            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Il est trop tot, reviens vers 19h."]
            else: return event


# - - - Nidavellir - - - #
def nidavellir_po(coords):
    # ? : (65, 7)
    # ? : (66, 58)
    pass

def nidavellir_npc(data, stat):
    # * : (49, 21)
    # * : (25, 31)
    # * : (74, 46)
    # * : (16, 55)
    # * : (77, 61)
    pass


def h_37_npc(data, stat):
    # * : (2, 1)
    # * : (26, 1)
    # * : (10, 5)
    # * : (27, 8)
    # * : (3, 10)
    coords = data[2], data[3]

    if coords == (2, 1):
        if not (340 <= stat[4] <= 1380): return [0, "Nous sommes ouverts de 5 heures a 23."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bonjour, Muin pour vous servir.\n1. Bonjour je voudrais manger. [-5 PO]\n2. Vous reste-t-il des chambres ? [-15 PO]\n3. A boire ! [-3 PO]", 3]

        else:
            event, choice = shop_interaction(data, stat, 3,
                (5, [-1, "Pas de probleme ! [MUIN REVINT QUELQUES MINUTES PLUS TARD, ET POSA UNE ASSIETTE FUMANTE DEVANT VOUS.]", 0, (0, 5), (1, -5)], [-1, "Hey la ! Reviens quand tu pourras me payer."]),
                (15, [-2, "Bien sur ! Suivez-moi. [VOUS SUIVEZ MUIN DANS UNE PIECE TROGLODYTE MUNIE D'UN LIT ET D'UN COFFRE. VOUS VOUS ENDORMEZ RAPIDEMENT.]", 0, (0, 15), (1, -15), (4, 480)], [-2, "Desole, je n'ai plus une seule chambre de libre."]),
                (3, [-3, "[MUIN POSA UNE CHOPPE DE BIERE MOUSSEUSE DEVANT VOUS.]", 0, (0, 3), (1, -3)], [-3, "Allez donc voir un autre etablissement, nous ne servons pas gratuitement."]))
            
            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Une chambre !? Il n'est que {} heures. Reviens dans la soiree.".format(stat[4] // 60)]
            else: return event

    return [0, "Hmm ?"]


def h_38_npc(data, stat):
    # * : (12, 3)
    # * : (19, 7)
    pass


def h_39_npc(data, stat):
    # * : (9, 2)
    # * : (9, 4)
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "La forge de Nivallir est ouverte de 8 heures a 18 heures."]

    if coords == (9, 2):

        if stat[3][0]: return [0, "Vous avez deja une arme. Allez voir mon confrere si vous voulez la vendre et revenez me voir."]

        elif stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bienvenue a la forge de Nidavellir ! Vous desirez une piece particulière ?\n1. Un marteau [-20 PO]\n2. Une masse [-30 PO]\n3. Un fleau [-40 PO]\n4. Une hache [-50 PO]", 4]

        else:
            weapons = ("UN MARTEAU", "UNE MASSE", "UN FLEAU", "UNE HACHE")
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < (i+1) * 10: return [-i, "Vous n'avez pas assez."]
                    stat[3][0] = i + 1
                    return [-i, "Tres bon choix ! [LE NAIN DECROCHA {} DU RATELIER ET VOUS TENDIT L'ARME.]".format(weapons[i - 1]), 0, (1, -(i+1) * 10)]

    if coords == (9, 4):
        if stat[3][0] == 0: return [0, "Vous n'avez pas d'arme a me vendre. Allez voir mon collegue pour en acheter une."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bienvenue dans notre forge. Vous souhaitez me vendre votre arme ?\n1. Oui\n2. Non", 2]

        elif data[0]["main"] == stat[9] + 1:
            stat[9] = -1
            cost = stat[3][0] * 8
            stat[3][0] = 0
            return [-1, "Marche conclu ! [+{} PO]".format(cost), 0, (1, cost)]

        elif data[0]["main"] == stat[9] + 2:
            stat[9] = -1
            return [-2, "A votre guise, revenez quand vous voulez !"]


def h_40_npc(data, stat):
    # * : (14, 5)
    pass


def h_41_npc(data, stat):
    # * : (12, 2)
    # * : (10, 8)
    pass


# - - - Muspellheim - - - #
def muspellheim_po(coords):
    # ? (66, 8)
    # ? : (64, 97)
    pass


def muspellheim_npc(data, stat):
    # * : (20, 12)
    # * : (78, 14)
    # * : (54, 80)
    # * : (59, 91)
    # * : (39, 94)
    # * : (29, 113)
    pass


def h_42_npc(data, stat):
    # * : (11, 5)
    # * : (6, 7)
    # * : (31, 9)
    # * : (2, 11)
    coords = data[2], data[3]

    if coords == (6, 7):
        if not (300 <= stat[4] <= 1380): return [0, "Nous sommes ouverts de 5 a 23 heures."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Besoin de quelque chose messire ?\n1. Hum, oui, j'aimerais manger. [-5 PO]\n2. Je voudrais dormir [-10 PO]", 2]

        else:
            event, _ = shop_interaction(data, stat, 2, 
                (5, [-1, "Et voila pour vous !", 0, (0, 5), (1, -5)], [-1, "Je regrette, vous n'avez pas assez."]),
                (10, [-2, "Bien sur, si vous voulez bien me suivre. [VOUS VOUS ALLONGEZ SUR LE LIT ET VOUS ENDORMEZ RAPIDEMENT.]", 0, (0, 10), (1, -10), (4, 480)], [-2, "Nous ne pouvons pas nous permettre de faire credit."]))
        
            return event

def h_43_npc(data, stat):
    # * : (24, 4)
    # * : (6, 5) 
    # * : (13, 9)
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "L'armurerie est ouverte de 8 heures a 18 heures."]

    if coords == (24, 4):
        if stat[3][1]: return [0, "Vous portez deja une armure, allez voir mon confrere."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bienvenue, dans mon armurerie ! Je suis Bertfrid, besoin d'une armure ?\n1. Oui, d'une rondache. [-10 PO]\n2. d'un pavois [-20 PO]\n3. d'une cotte de mailles [-30 PO]\n4. d'une broigne [-40 PO]\n5. d'un harnois [-50 PO]", 5]

        else:
            shields = ("UNE RONDACHE", "UN PAVOIS", "UNE COTTE DE MAILLES", "UNE BROIGNE", "UN HARNOIS")
            for i in range(1, 6):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < i * 10: return [-i, "Vous n'avez pas assez."]
                    stat[3][1] = i
                    return [-i, "C'est un bon achat. [BERTFRID DECROCHA {}]".format(shields[i - 1]), 0, (1, -i * 10)]

    elif coords == (13, 9):
        if stat[3][1] == 0: return [0, "J'achete, je ne vend pas ! Allez voir Bertfrid du cote du four a metaux, elle vous renseignera"]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Vous voulez vendre votre piece d'armure ?\n1. Oui\n2. Non", 2]

        elif data[0]["main"] == stat[9] + 1:
            stat[9] = -1
            cost = stat[3][1] * 8
            return [-1, "C'est une affaire ! [+{} PO]".format(cost), 0, (1, cost)]

        elif data[0]["main"] == stat[9] + 2:
            stat[9] = -1
            return [-2, "Revenez quand vous voulez !"]

    elif coords == (6, 5):
        return [0, "Je ne suis qu'apprenti monseigneur. Adressez-vous plutot a Bertfrid."]


def h_44_npc(data, stat):
    # * : (13, 2)
    # * : (13, 20)
    pass


# - - - Svartalfheim - - - #
def svartalfheim_po(coords):
    # ? : (113, 37)
    pass


def svartalfheim_npc(data, stat):
    # * : (10; 24)
    # * : (105; 46)
    # * : (22; 50)
    # * : (15; 54)
    # * : (25; 61)
    # * : (121; 68)
    pass

def h_45_npc(data, stat):
    # * : (15, 4)
    pass


def h_46_npc(data, stat):
    # * : (13, 2)
    # * : (13, 4)
    pass

def h_47_npc(data, stat):
    # * : (3, 4)
    # * : (15, 8)
    pass


def h_48_npc(data, stat):
    # * : (34, 5)
    # * : (29, 6)
    pass
