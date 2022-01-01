from asci_lib import Asci, print_text
from random import randint
from math import floor, ceil

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
    h_45, h_46, h_47, h_48)

# Asci functions
def npc(data, stat):
    from random import choice
    
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


    event = npc_data[data[1]](data, stat)

    if not event:    
        print("\nChoissez une action :\n1. Attaquer\n2. Voler\n3. Parler\n4. Ne rien faire")
        choice_sel = input(">")
        try: choice_sel = int(choice_sel)
        except: choice_sel = 3

        if choice_sel == 1:
            opponent_stat = [randint(5, stat[2][i] + 5) for i in range(4)]
            opponent_stat.append(randint(50, 150))
            return launch_fight(data, stat, [opponent_stat, "Ennemi"])

        elif choice_sel == 2:
            if stat_test(stat[2], 1)[0]:
                amount = randint(2, 20)
                return [0, "Vous avez reussi a voler {} PO.".format(amount), 0, (1, amount)]
            else:
                if stat[0] > 10: return [0, "Votre victime vous a vu et vous a mis une raclee.", 0, (0, -10)]
                else: return [0, "Votre victime vous a vu, et vous a mis une tellement grosse raclee que vous etes mort.", 0, (0, -10)]

        elif choice_sel == 3:
            msg = ("Hmm ?", "Besoin de quelque chose ?", "Vous cherchez quelqu'un ?", "Vous etes... ?", "Oui ?", "He ! Regarde ou tu vas.")
            return [0, choice(msg)]

        elif choice_sel == 4:
            return None

    elif type(event) == tuple:
        return launch_fight(data, stat, event)
    
    else:
        return event


def launch_fight(data, stat, event):
    issue = fight(stat, event[0], event[1])

    if issue == 0:
        stat[1] += event[2]
        if sum(stat[2][:-1]) >= 200: return [event[3], "Vous avez gagne le combat. [+{}PO]".format(event[2])]
        
        print_text("Vous avez gagne le combat. [+{}PO]".format(event[2]))
        data[0] += event[3]
        choice = 0
        while not choice:
            print("<o> Amelioration  <o>")
            print(" |1. Vitesse       |")
            print(" |2. Agilite       |")
            print(" |3. Attaque       |")
            print(" |4. Defense       |")
            print("<o> ============= <o>")
            choice = get_input()
            if (choice < 0 or choice > 4) and stat[2][choice - 1] >= 50: choice = 0

        print_text("Vous gagnez 2 points {}".format(("de vitesse", "d'agilite", "d'attaque", "de defense")[choice - 1]))
        stat[2][choice - 1] += 2
        if stat[2][choice -1] > 50: stat[2][choice - 1] = 50
        
        return None

    elif issue == 1: return [0, "Vous etes mort."]
    elif issue == 2: return [0, "Vous avez fuit."]


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


def routine(data, stat):
    stat[4] = (stat[4] + 1) % 1440

    # Mana regeneration
    if stat[2][4] < stat[0] // 2 and not (stat[4] % 60):
        stat[2][4] += 1


# Game mecanics
def fight(stat, opponent_stat, opponent_name):

    def player_turn():
        end = False
        msg = "Tour de {}".format(stat[5])
        
        if choice == 1:
            damage = stat_test(player_stat, 2)[1] - opponent_stat[3]
            if damage < 0: damage = 0
            
            if damage == 0:
                msg += "\n{} bloque l'attaque.".format(opponent_name)
            elif stat_test(opponent_stat[:-1], 1)[0]:
                msg += "\n{} esquive le coup.".format(opponent_name)
            else:
                opponent_stat[4] -= damage
                msg += "\n{0} perd {1} PV.".format(opponent_name, damage)

        elif choice == 2:
            if len(stat[7]) == 0:
                msg += "\nVous ne connaissez pas de sort."
            else:
                spell_data = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
                spell_level = ("I", "II", "III", "IV", "V")

                spell_choice = 0
                while not spell_choice:
                    print("\n" * 6 + "Sort(s) connu(s) :")
                    count = 0
                    for spell_id, level in stat[7]:
                        print("{0}. {1} {2}".format(count + 1, spell_data[spell_id], spell_level[level - 1]))
                        count += 1
                    spell_choice = get_input()
                    if spell_choice < 0 or spell_choice > 3: spell_choice = 0

                spell_choice -= 1
                name, level = spell_data[stat[7][spell_choice][0]], stat[7][spell_choice][1]

                if stat[2][4] >= level * 10:
                    msg += "\nVous lancez {0} de niveau {1} [-{2} PM].".format(name, spell_level[level - 1], level * 10)
                    stat[2][4] -= level * 10
                    pts = 12 * level + randint(-5, 5)

                    if stat[7][spell_choice][0] == 0:
                        stat[0] += pts
                        msg += "\nVous gagnez {} PV".format(pts)
                    
                    elif stat[7][spell_choice][0] == 1:
                        opponent_stat[4] -= pts
                        msg += "\n{0} perd {1} PV".format(opponent_name, pts)
                    
                    elif stat[7][spell_choice][0] == 2:
                        opponent_stat[4] -= pts
                        msg += "\n{0} perd {1} PV".format(opponent_name, pts)
                    
                    elif stat[7][spell_choice][0] == 3:
                        opponent_stat[4] -= pts
                        msg += "\n{0} perd {1} PV".format(opponent_name, pts)
                    
                    elif stat[7][spell_choice][0] == 4:
                        opponent_stat[0] -= pts
                        msg += "\n{0} perd {1} points de vitesse".format(opponent_name, 12 * level)

                else:
                    msg += "\nVous ne parvenez pas a lancer le sort."

        elif choice == 3:
            if stat_test(player_stat, 1)[0] or stat_test(player_stat, 1)[0]:
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
            stat[0] -= damage
            msg += "\n{0} perd {1} PV.".format(stat[5], damage)

        print_text(msg)

    # opponent_stat = [vitesse, agilité, attaque, défense, vie]
    # player_stat = [vitesse, agilité, attaque, défense]
    player_stat = [stat[2][0], stat[2][1], stat[2][2] + stat[3][0] * 5, stat[2][3] + stat[3][1] * 5]

    end = False
    while not end:
        choice = 0
        while not choice:
            print("<o>    Combat     <o>")
            print(" | 1. Attaquer     |")
            print(" | 2. Ensorceler   |")
            print(" | 3. Fuir         |")
            print(" | 4. Statistiques |")
            print("<o> ============= <o>")
            choice = get_input()
            if choice < 0 or choice > 4: choice = 0

            if choice == 4:
                p_capacities = ["{} ".format(i) if i < 10 else str(i) for i in player_stat]
                o_capacities = ["{} ".format(i) if i < 10 else str(i) for i in opponent_stat[:-1]]

                p_health = str(stat[0]) + " " * (3 - len(str(stat[0])))
                o_health = str(opponent_stat[4]) + " " * (3 - len(str(opponent_stat[4])))

                print("  Joueur | Ennemi")
                print("Vit: {0}  | {1}".format(p_capacities[0], o_capacities[0]))
                print("Agi: {0}  | {1}".format(p_capacities[1], o_capacities[1]))
                print("Att: {0}  | {1}".format(p_capacities[2], o_capacities[2]))
                print("Def: {0}  | {1}".format(p_capacities[3], o_capacities[3]))
                print("Vie: {0} | {1}".format(p_health, o_health))
                input()
                choice = 0

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
            if opponent_stat[4] <= 0: return 0
            opponent_turn()
        
        else:
            opponent_turn()
            if stat[0] <= 0: return 1 
            end = player_turn()

        if opponent_stat[4] <= 0: return 0
        if stat[0] <= 0: return 1

    return 2


def misc_stat(data, stat):
    if data[1] < 9: place = ("Asgard", "Vanaheim", "Alfheim", "Midgard", "Niflheim", "Jotunheim", "Nidavellir", "Muspellheim", "Svartalfheim")[data[1]]
    elif data[1] == 27: place = "chez vous"
    else: place =  "interieur"
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
    weapon = ("<aucune>", "Dague", "Marteau", "Masse", "Fleau", "Hache", "Epee", "Espadon", "Hache double")[stat[3][0]]
    shield = ("<aucune>", "Rondache", "Pavois", "Cote de maille", "Broigne", "Harnois")[stat[3][1]]

    weapon = " |" + weapon + " " * (17 - len(weapon)) + "|"
    shield = " |" + shield + " " * (17 - len(shield)) + "|"

    print("<o>  Inventaire   <o>")
    print(" |- Arme :         |\n{}".format(weapon))
    print(" |- Armure :       |\n{}".format(shield))
    print("<o> ============= <o>")
    input()


def sleep(data, stat):
    sleep_hours = 0
    while not sleep_hours:
        print("Combien d'heures\nvoulez-vous dormir ?")
        sleep_hours = get_input() % 25
        if sleep_hours < 0: sleep_hours = 0

    stat[4] += sleep_hours * 60
    if stat[0] < 100: stat[0] += sleep_hours
    if stat[2][4] < 50: stat[2][4] += sleep_hours // 2


    # If the player is at home
    if data[1] == 27:
        if stat[0] < 100: stat[0] += 5 * sleep_hours
        if stat[2][4] < 50: stat[2][4] += sleep_hours // 2

    print_text("Vous vous reposez {0} heure{1}.".format(sleep_hours, ("", "s")[sleep_hours > 1]))


def spell(data, stat):
    spell_data = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
    spell_level = ("I", "II", "III", "IV", "V")

    to_disp = "Magie : {} PM".format(stat[2][4])
    print("<o>    Sorts     <o>")
    print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")

    for i in range(3):
        if i < len(stat[7]):
            spell_id, level = stat[7][i]
            if spell_id >= 0:
                to_disp = "{0} {1}".format(spell_data[spell_id], spell_level[level - 1])
                print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")
        else:
            print(" |<aucun>         |")

    print("<o> ============ <o>")
    input()


def quick_save(data, stat):
    data_copy = data[:]
    data_copy[2] += 10
    data_copy[3] += 3
    print("idk({0}, {1})".format(stat[:-1], data_copy))
    input()


events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 8: misc_stat, 6: inventory, 9: sleep, "s": quick_save}


# Main function
def idk(stat=None, data=None):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - classe, 7 - sorts connus : (id, level), 8 - sous-quête en cours]
    if not stat:
        name = ""
        while len(name) == 0 or len(name) > 13:
            name = input("Entrez votre nom :\n>")

        player_class = 0
        while(not player_class):
            print("Choisissez une classe\n1. Guerrier\n2. Voleur\n3. Moine\n4. Mage\n5. Assassin")
            player_class = get_input()
            if player_class < 0 or player_class > 5: player_class = 0

        if player_class == 1:
            stat = [5, 5, 10, 5, 5]
        elif player_class == 2:
            stat = [5, 10, 5, 5, 5] 
        elif player_class == 3:
            stat = [5, 5, 5, 10, 5]
        elif player_class == 4:
            stat = [5, 5, 5, 5, 20]
        elif player_class == 5:
            stat = [10, 5, 5, 5, 5]

        stat = [100, 1000, stat, [0, 0], 360, name, player_class - 1, [], 0, -1]
        if player_class == 4:
            stat[7].append((1, 1))
        data = [0, 3, 44, 66]

    else:
        stat.append(-1)

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

        if len(stat[5]) > 13:
            raise ValueError("nom du joueur invalide")

    idk_game = Asci(maps, events, keys)
    stat, data = idk_game.mainloop(102, stat, data, routine=routine, door="^_", walkable=".,`' ", exit_key="q")


    print("idk({0}, {1})".format(stat[:-1], data))


# Misc functions
def get_input():
    string = input(">")
    try:
        return int(string)
    except:
        return 0


def center(string, total_length, symbol):
    left = floor((total_length - len(string)) / 2)
    right = ceil((total_length - len(string)) / 2)

    return left * symbol + string + right * symbol


def stat_test(stat, test_id):
    score = (80 + randint(-20, 20)) * stat[test_id] / 50
    return randint(1, 100) <= score, floor(score)

