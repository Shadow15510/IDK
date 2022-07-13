from asci import Asci, print_text, center, enumerate
from random import randint, choice

from asgard import *
from vanaheim import *
from alfheim import *
from midgard import *
from niflheim import *
from jotunheim import *
from nidavellir import *
from muspellheim import *
from svartalfheim import *

maps = (
    asgard,
    vanaheim,
    alfheim,
    midgard,
    niflheim,
    jotunheim,
    nidavellir,
    muspellheim,
    svartalfheim,
    h_9, h_10, h_11, h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20,
    h_21, h_22,
    h_23, h_24,
    h_25, h_26, h_27, h_28,
    h_29, h_30,
    h_31, h_32, h_33, h_34, h_35, h_36,
    h_37, h_38, h_39, h_40, h_41,
    h_42, h_43, h_44,
    h_45, h_46, h_47, h_48
    )

spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
spells_level = ("I", "II", "III", "IV", "V")
spells_effect = ((4, 1, True), (4, -1, False), (4, -1, False), (4, -1, False), (0, -1, False)) # (capacity, factor, True on player; False on opponent)
weapons = ("<aucune>", "Dague", "Marteau", "Masse", "Fleau", "Hache", "Epee", "Espadon", "Hache double")
armors = ("<aucune>", "Rondache", "Pavois", "Cote de maille", "Broigne", "Harnois")


# Shop functions
def inn_interaction(data, stat, nb_choice, text, *events):
    choice = print_text(text, 1, nb_choice, 0) - 1
    if choice == -1: return [0, None], choice
    if stat[1] < events[choice][0]: return events[choice][2], choice + 1
    else: return events[choice][1], choice + 1


def spell_selection(text, spells_to_display):
    message = text + "\n" + "\n".join(["{0}. {1} {2}".format(nb + 1, spells[spells_to_display[nb][0]], spells_level[spells_to_display[nb][1] - 1]) for nb in range(len(spells_to_display))])
    return print_text(message, 1, len(spells_to_display), 0) - 1


def spell_purchase(data, stat, text, spell_purchased, already_known, not_enough_money, too_many_spell):
    spells_sale = []
    while len(spells_sale) < 3:
        sp_id = randint(0, len(spells) - 1)
        sp_lvl = randint(1, len(spells_level))

        check = True
        for sp in spells_sale:
            if sp == (sp_id, sp_lvl):
                check = False
                break

        if check: spells_sale.append((sp_id, sp_lvl))

    choice = spell_selection(text, spells_sale)
    if choice == -1: return [0, ""]
    spell_selected = spells_sale[choice]

    if stat[1] < 10 * spell_selected[1]: return [0, not_enough_money]

    for spell in stat[7]:
        if spell_selected[0] == spell[0]:
            if spell_selected[1] <= spell[1]: return [0, already_known]
            else: stat[7].remove(spell)

    if len(stat[7]) >= 3: return [0, too_many_spell] 
    
    stat[7].append(spell_selected)
    return [0, spell_purchased, 0, (1, -10 * spell_selected[1])]


def spell_deletion(data, stat, text, spell_deleted, no_spell_known, health_cost, not_enough_health=""):
    if not stat[7]: return [0, no_spell_known]
    choice = spell_selection(text, stat[7])
    if choice == -1: return [0, ""]

    if stat[0] <= health_cost: return [0, not_enough_health]
    stat[7].remove(stat[7][choice])
    return [0, spell_deleted, 0, (0, -health_cost)]


def weapon_selection(text, weapons_to_display):
    message = text + "\n" + "\n".join(["{0}. {1} [-{2} PO]".format(i + 1, weapons[wpn_index], 10 * wpn_index) for i, wpn_index in enumerate(weapons_to_display)])
    return print_text(message, 1, len(weapons_to_display), 0) - 1


def weapon_purchase(data, stat, text, weapon_purchased, already_have_one, not_enough_money):
    if stat[3][0]: return [0, already_have_one]

    weapons_sale = []
    while len(weapons_sale) < 3:
        wpn_id = randint(1, len(weapons) - 1)
        if not wpn_id in weapons_sale: weapons_sale.append(wpn_id)

    choice = weapon_selection(text, weapons_sale)
    if choice == -1: return [0, ""]

    weapon_selected = weapons_sale[choice]
    if stat[1] < 10 * weapon_selected: return [0, not_enough_money]
    stat[3][0] = weapon_selected
    return [0, weapon_purchased, 0, (1, -10 * weapon_selected)]
    

def weapon_sale(data, stat, text, weapon_sold, sale_aborted, no_weapon_owned, price):
    if not stat[3][0]: return [0, no_weapon_owned]

    choice = print_text(text + "\n1. Oui\n2. Non", 1, 2, 0)
    
    if choice == 0: return [0, ""]
    elif choice == 1:
        stat[3][0] = 0
        return [0, weapon_sold, 0, (1, price)]
    else: return [0, sale_aborted]


def armor_selection(text, armors_to_display):
    message = text + "\n" + "\n".join(["{0}. {1} [-{2} PO]".format(i + 1, armors[arm_index], 10 * arm_index) for i, arm_index in enumerate(armors_to_display)])
    return print_text(message, 1, len(armors_to_display), 0) - 1


def armor_purchase(data, stat, text, armor_purchased, already_have_one, not_enough_money):
    if stat[3][1]: return [0, already_have_one]

    armors_sale = []
    while len(armors_sale) < 3:
        arm_id = randint(1, len(armors) - 1)
        if not arm_id in armors_sale: armors_sale.append(arm_id)

    choice = armor_selection(text, armors_sale)
    if choice == -1: return [0, ""]

    armor_selected = armors_sale[choice]
    if stat[1] < 10 * armor_selected: return [0, not_enough_money]
    stat[3][1] = armor_selected
    return [0, armor_purchased, 0, (1, -10 * armor_selected)]


def armor_sale(data, stat, text, armor_sold, sale_aborted, no_armor_owned, price):
    if not stat[3][1]: return [0, no_armor_owned]

    choice = print_text(text + "\n1. Oui\n2. Non", 1, 2, 0)
    
    if choice == 0: return [0, ""]
    elif choice == 1:
        stat[3][1] = 0
        return [0, armor_sold, 0, (1, price)]
    else: return [0, sale_aborted]


# Asci functions
def npc_core(event_fn, data, stat, entities, identifiant):
    event = event_fn(data, stat, entities, identifiant)

    if not event:
        msg = ("Hmm ?", "Besoin de quelque chose ?", "Vous cherchez quelqu'un ?", "Vous etes... ?", "Oui ?", "He ! Regarde ou tu vas.")
        sel_choice = print_text("{0}\n1. Attaquer\n2. Voler\n3. Ne rien faire".format(choice(msg)), 1, 3, 3)

        if sel_choice == 1:
            opponent_stat = [randint(5, stat[2][i] + 5) for i in range(4)]
            opponent_stat.append(randint(50, 150))
            return launch_fight(data, stat, (opponent_stat, "Ennemi", randint(10, 30), 0))

        elif sel_choice == 2:
            if stat_test(stat[2], 1)[0]:
                amount = randint(5, 25)
                return [0, "Vous avez reussi a voler {} PO.".format(amount), 0, (1, amount)]
            else:
                return [0, "Votre victime vous a vu et vous a mis une raclee.", 0, (0, -10)]

        elif sel_choice == 3:
            return None

    elif type(event) == tuple and len(event) > 2:
        if len(event) == 4: quest = "main"
        else: event, quest = event[:-1], event[-1]
        return launch_fight(data, stat, event, quest)
    
    else:
        return event


def launch_fight(data, stat, event, quest="main"):
    issue, stat[0] = fight(stat, event[0], event[1])

    if issue == 0:
        stat[1] += event[2]
        if sum(stat[2][:-1]) >= 200: return [event[3], "Vous avez gagne le combat. [+{}PO]".format(event[2])]
        
        print_text("Vous avez gagne le combat. [+{}PO]".format(event[2]))
        data[0][quest] += event[3]
        sel_choice = 0
        while not sel_choice:
            print("<o> Amelioration  <o>")
            print(" |1. Vitesse       |")
            print(" |2. Agilite       |")
            print(" |3. Attaque       |")
            print(" |4. Defense       |")
            print("<o> ============= <o>")
            sel_choice = get_input()
            if (sel_choice < 0 or sel_choice > 4) and stat[2][sel_choice - 1] >= 50: sel_choice = 0

        print_text("Vous gagnez 2 points {}".format(("de vitesse", "d'agilite", "d'attaque", "de defense")[sel_choice - 1]))
        stat[2][sel_choice - 1] += 2
        if stat[2][sel_choice -1] > 50: stat[2][sel_choice - 1] = 50
        
        return None

    elif issue == 1: return [0, "Vous etes mort."]
    elif issue == 2: return [0, "Vous avez fuit."]


def routine(data, stat):
    stat[4] = (stat[4] + 1) % 1440

    # Health regeneration
    if stat[0] < 100 and not (stat[4] % 60):
        stat[0] += 1
    if stat[0] > 999: stat[0] = 999

    # Mana regeneration
    if stat[2][4] < stat[0] // 2 and not (stat[4] % 30):
        stat[2][4] += 1
    if stat[2][4] > 99: stat[2][4] = 99 




def low_bar(data, stat):
    h = stat[4] // 60
    m = stat[4] % 60
    if m < 10: m = "0" + str(m)
    return "{0}h|{2}PV|{3}PM ".format(h, m, stat[0], stat[2][4])


# Game mecanics
def fight(stat, opponent_stat, opponent_name):

    def player_turn():
        end = False
        msg = "Tour de {}".format(stat[5])
        
        if sel_choice == 1:
            damage = stat_test(player_stat, 2)[1] - opponent_stat[3]
            if damage < 0: damage = 0
            
            if damage == 0:
                msg += "\n{} bloque l'attaque.".format(opponent_name)
            elif stat_test(opponent_stat[:-1], 1)[0]:
                msg += "\n{} esquive le coup.".format(opponent_name)
            else:
                opponent_stat[4] -= damage
                msg += "\n{0} perd {1} PV.".format(opponent_name, damage)

        elif sel_choice == 2:
            if len(stat[7]) == 0:
                msg += "\nVous ne connaissez pas de sort."
            else:
                spell_choice = 0
                while not spell_choice:
                    print("\n" * 6 + "Sort(s) connu(s) :")
                    count = 0
                    for spell_id, level in stat[7]:
                        print("{0}. {1} {2}".format(count + 1, spells[spell_id], spells_level[level - 1]))
                        count += 1
                    spell_choice = get_input()
                    if spell_choice < 0 or spell_choice > len(stat[7]): spell_choice = 0

                spell_choice -= 1
                spell_id, level = stat[7][spell_choice][0], stat[7][spell_choice][1]

                if stat[2][4] >= level * 10:
                    msg += "\nVous lancez {0} de niveau {1} [-{2} PM].".format(spells[spell_id], spells_level[level - 1], level * 10)
                    stat[2][4] -= level * 10
                    pts = 12 * level + randint(-5, 5)

                    capacity, factor, apply_on_player = spells_effect[spell_id]

                    if apply_on_player:
                        player_stat[capacity] += factor * pts
                        msg += "\nVous {0} {1} points de {2}".format(("perdez", "gagnez")[factor > 0], pts, ("vitesse", "agilité", "attaque", "défense", "vie")[capacity])
                    else:
                        opponent_stat[capacity] += factor * pts
                        msg += "\n{0} {1} {2} points de {3}".format(opponent_name, ("perd", "gagne")[factor > 0], pts, ("vitesse", "agilité", "attaque", "défense", "vie")[capacity])

                else:
                    msg += "\nVous ne parvenez pas a lancer le sort."

        elif sel_choice == 3:
            if stat_test(player_stat, 1)[0] or not stat_test(opponent_stat, 1)[1]:
                end = True
            else:
                msg += "\nVotre tentative de fuite echoue."

        print_text(msg)
        return end

    def opponent_turn():
        msg = "Tour de {}".format(opponent_name)
        damage = stat_test(opponent_stat, 2)[1] - player_stat[3]
        if damage < 0: damage = 0

        if damage == 0:
            msg += "\n{} bloque l'attaque.".format(stat[5])
        elif stat_test(player_stat, 1)[0]:
            msg += "\n{} esquive le coup.".format(stat[5])
        else:
            player_stat[4] -= damage
            msg += "\n{0} perd {1} PV.".format(stat[5], damage)

        print_text(msg)

    # opponent_stat = [vitesse, agilité, attaque, défense, vie]
    # player_stat = [vitesse, agilité, attaque, défense, vie]
    player_stat = [stat[2][0], stat[2][1], stat[2][2] + stat[3][0] * 5, stat[2][3] + stat[3][1] * 5, stat[0]]

    end = False
    while not end:
        sel_choice = 0
        while not sel_choice:
            print("<o>    Combat     <o>")
            print(" | 1. Attaquer     |")
            print(" | 2. Ensorceler   |")
            print(" | 3. Fuir         |")
            print(" | 4. Statistiques |")
            print("<o> ============= <o>")
            sel_choice = get_input()
            if sel_choice < 0 or sel_choice > 4: sel_choice = 0

            if sel_choice == 4:
                p_capacities = ["{} ".format(i) if i < 10 else str(i) for i in player_stat]
                o_capacities = ["{} ".format(i) if i < 10 else str(i) for i in opponent_stat[:-1]]

                p_health = str(player_stat[4]) + " " * (3 - len(str(player_stat[4])))
                o_health = str(opponent_stat[4]) + " " * (3 - len(str(opponent_stat[4])))

                print("  Joueur | Ennemi")
                print("Vit: {0}  | {1}".format(p_capacities[0], o_capacities[0]))
                print("Agi: {0}  | {1}".format(p_capacities[1], o_capacities[1]))
                print("Att: {0}  | {1}".format(p_capacities[2], o_capacities[2]))
                print("Def: {0}  | {1}".format(p_capacities[3], o_capacities[3]))
                print("Vie: {0} | {1}".format(p_health, o_health))
                input()
                sel_choice = 0

        # Who start
        player = opponent = False
        while player == False and opponent == False:
            player = stat_test(player_stat, 0)[0]
            opponent = stat_test(opponent_stat[:-1], 0)[0]

            if player == True and opponent == True:
                if player_stat[0] < opponent_stat[0]: opponent = False
                else: player = False

        # Fight
        if player > opponent:
            end = player_turn()
            if end: return 2
            if opponent_stat[4] <= 0: return 0, player_stat[4]
            opponent_turn()
        
        else:
            opponent_turn()
            if player_stat[4] <= 0: return 1, player_stat[4]
            end = player_turn()

        if opponent_stat[4] <= 0: return 0, player_stat[4]
        if player_stat[4] <= 0: return 1, player_stat[4]

    return 2, player_stat[4]


def misc_stat(data, stat):
    if data[1] < 9: place = ("Asgard", "Vanaheim", "Alfheim", "Midgard", "Niflheim", "Jotunheim", "Nidavellir", "Muspellheim", "Svartalfheim")[data[1]]
    elif data[1] == 27: place = "chez vous"
    else: place = "interieur"
    money, ticks, player_class = stat[1], stat[4], stat[6]
    
    hours = ticks // 60
    if 4 <= hours <= 5:
        hours = " |aube - {}h".format(hours)
    elif 6 <= hours <= 12:
        hours = " |matin - {}h".format(hours)
    elif 13 <= hours <= 18:
        hours = " |apres-midi - {}h".format(hours)
    elif 19 <= hours <= 20:
        hours = " |crepuscule - {}h".format(hours)
    else:
        hours = " |nuit - {}h".format(hours)

    player_class = (" |Guerrier", " |Voleur", " |Moine", " |Mage", " |Assassin")[player_class]

    money = " |Argent: {} PO".format(money)

    print("<o> Informations  <o>")
    print(" |" + center(place, 17, " ") + "|")
    print(player_class + " " * (19 - len(player_class)) + "|")
    print(hours + " " * (19 - len(hours)) + "|")
    print(money + " " * (19 - len(money)) + "|")
    print("<o> ============= <o>")
    input()


def display_stat(data, stat):
        capacities = ["{} ".format(i) if i < 10 else str(i) for i in stat[2]]

        first_line = " |Vit : {0} Agi : {1}|".format(capacities[0], capacities[1])
        second_line = " |Att : {0} Def : {1}|".format(capacities[2], capacities[3])
        health = " |Vie : {} PV".format(stat[0])
        mana = " |Magie : {} PM".format(stat[2][4])

        print("<o> {} <o>".format(center(stat[5], 13, " ")))
        print(first_line)
        print(second_line)
        print(mana + " " * (19 - len(mana)) + "|")
        print(health + " " * (19 - len(health)) + "|")
        print("<o> ============= <o>")
        input()


def inventory(data, stat):
    weapon = weapons[stat[3][0]]
    armor = armors[stat[3][1]]

    weapon = " |" + weapon + " " * (17 - len(weapon)) + "|"
    armor = " |" + armor + " " * (17 - len(armor)) + "|"

    print("<o>  Inventaire   <o>")
    print(" |- Arme :         |\n{}".format(weapon))
    print(" |- Armure :       |\n{}".format(armor))
    print("<o> ============= <o>")
    input()


def sleep(data, stat):
    sleep_hours = 0
    hours = "= {0} h ".format(stat[4] // 60)
    if stat[4] % 60 < 10: hours += "0{1} ="
    else: hours += "{1} ="

    hours = center(hours.format(stat[4] // 60, stat[4] % 60), 21, " ")
    
    while not sleep_hours:
        print(hours)
        print("Combien d'heures\nvoulez-vous dormir ?")
        sleep_hours = get_input() % 25
        if not sleep_hours or sleep_hours < 0: return

    stat[4] += sleep_hours * 60
    if stat[0] < 100: stat[0] += sleep_hours // 2
    if stat[2][4] < 50: stat[2][4] += sleep_hours


    # If the player is at home
    if data[1] == 27:
        if stat[0] < 100: stat[0] += sleep_hours
        if stat[2][4] < 50: stat[2][4] += sleep_hours * 2

    print_text("Vous vous reposez {0} heure{1}.".format(sleep_hours, ("", "s")[sleep_hours > 1]))


def spell(data, stat):
    to_disp = "Magie : {} PM".format(stat[2][4])
    print("<o>    Sorts     <o>")
    print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")
    for i in range(3):
        if i < len(stat[7]):
            spell_id, level = stat[7][i]
            if spell_id >= 0:
                to_disp = "{0} {1}".format(spells[spell_id], spells_level[level - 1])
                print(" |{}.".format(i + 1) + to_disp + " " * (14 - len(to_disp)) + "|")
        else:
            print(" |<aucun>         |")

    print("<o> ============ <o>")
    spell_choice = get_input()
    if not (1 <= spell_choice <= len(stat[7])): spell_choice = 0
    if spell_choice:
        spell_choice -= 1
        spell_id, level = stat[7][spell_choice][0], stat[7][spell_choice][1]
        capacity, factor, apply_on_player = spells_effect[spell_id]

        if not apply_on_player:
            print_text("Vous ne pouvez pas lancer ce sort.")

        elif stat[2][4] >= level * 10:
            msg = "".format()
            stat[2][4] -= level * 10
            pts = 12 * level + randint(-5, 5)
            
            if capacity == 4:
                stat[0] += factor * pts
            else:
                stat[2][capacity] += factor * pts
            print_text("Vous lancez {0} de niveau {1} [-{2} PM] et {3} {4} points de {5}".format(spells[spell_id], spells_level[level - 1], level * 10, ("perdez", "gagnez")[factor > 0], pts, ("vitesse", "agilité", "attaque", "défense", "vie")[capacity]))
            
        else:
            print_text("Vous n'avez plus assez de points de Magie.")

def quick_save(data, stat):
    data_copy = data[:]
    stat_copy = stat[:-1]
    print_text("\"{}\"".format(encode_save(data_copy, stat_copy)))


# Misc functions
def get_input(string=">"):
    string = input(string)
    try:
        return int(string)
    except:
        return 0


def stat_test(stat, test_id):
    score = (80 + randint(-20, 20)) * stat[test_id] / 50
    return randint(1, 100) <= score, floor(score)


def init_stat():
    name = input("Entrez votre nom :\n>")
    while len(name) == 0 or len(name) > 13:
        print("Erreur : nom invalide.")
        name = input("Entrez votre nom :\n>")

    player_class = 0
    while(not player_class):
        print("Choisissez une classe\n1. Guerrier\n2. Voleur\n3. Moine\n4. Mage\n5. Assassin")
        player_class = get_input()
        if player_class < 0 or player_class > 5: player_class = 0

    if player_class == 1:
        stat = [6, 6, 10, 6, 6]
    elif player_class == 2:
        stat = [6, 10, 6, 6, 6] 
    elif player_class == 3:
        stat = [6, 6, 6, 10, 6]
    elif player_class == 4:
        stat = [6, 6, 6, 6, 20]
    elif player_class == 5:
        stat = [10, 6, 6, 6, 6]

    stat = [100, 10, stat, [0, 0], 360, name, player_class - 1, [], 1, -1]
    if player_class == 4:
        stat[7].append((1, 1))

    return stat


def encode_save(data, stat):
    xp = ["{0}-{1}".format(key, data[0][key]) for key in data[0] if key == "main" or data[0][key]]
    data = "{0},{1},{2},{3}".format(data[1], data[2], data[3], ",".join(xp))

    stat[5] = 0
    if not stat[7]: stat[7] = 0
    else: stat[7] = ",".join(["{0}-{1}".format(i[0], i[1]) for i in stat[7]])

    save_code = []
    for i in stat:
        if type(i) == list:
            for j in i: save_code.append(str(j))
        else: save_code.append(str(i))

    return ",".join(save_code) + ".{}".format(data)


def decode_save(save_code):
    stat, data = save_code.split(".")
    encoded_stat = stat.split(",")
    encoded_data = data.split(",")

    encoded_stat = [encoded_stat[0], encoded_stat[1], encoded_stat[2: 7], encoded_stat[7: 9], encoded_stat[9], 0, encoded_stat[11], encoded_stat[12: -1], encoded_stat[-1], -1]
    
    if encoded_stat[7] == ["0"]:
        encoded_stat[7] = []
    else:
        spells = []
        for spell in encoded_stat[7]:
            s_id, s_lv = spell.split("-")
            spells.append((s_id, s_lv))
        encoded_stat[7] = spells

    stat = str_to_int(encoded_stat)

    for i in range(len(stat[7])):
        stat[7][i] = tuple(stat[7][i])
    
    # Money check
    if stat[1] < 0: stat[1] = 0
    if stat[1] > 100000: stat[1] = 100000

    # Stat check
    for i in range(len(stat[2])):
        if stat[2][i] > 50: stat[2][i] = 50
        if stat[2][i] < 0: stat[2][i] = 0

    # Player's class check
    if not (0 <= stat[6] <= 5):
        raise ValueError("classe du joueur inconnue")

    # PLayer's name check
    name = input("Entrez votre nom :\n>")
    while len(name) == 0 or len(name) > 13:
        print("Erreur : Nom invalide")
        name = input("Entrez votre nom :\n>")
    stat[5] = name

    xp = {}
    for quest in encoded_data[3:]:
        q_id, q_xp = quest.split("-")
        xp[q_id] = int(q_xp)
    data = [xp, int(encoded_data[0]), int(encoded_data[1]), int(encoded_data[2])]

    return stat, data


def str_to_int(data):
    result = []
    for i in data:
        if isinstance(i, (list, tuple)):
            result.append(str_to_int(i))
        else:
            result.append(int(i))
    return result
