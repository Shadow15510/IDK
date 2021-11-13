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
from helheim import *


maps = (
    asgard,
    vanaheim,
    alfheim,
    midgard,
    niflheim,
    jotunheim,
    nidavellir,
    muspellheim,
    helheim,
    h_9, h_10, h_11, h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20,
    h_21, h_22,
    h_23, h_24,
    h_25, h_26, h_27, h_28,
    h_29, h_30, h_31, h_32,)
#     h_33, h_34, h_35, h_36, h_37, h_38, h_39,
#     h_40, h_41, h_42, h_43, h_44,
#     h_45, h_46, h_47, h_48,
#     h_49, h_50)

# Asci functions
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
    helheim_npc,
    h_9_npc, h_10_npc, h_11_npc, h_12_npc, h_13_npc, h_14_npc, h_15_npc, h_16_npc, h_17_npc, h_18_npc, h_19_npc, h_20_npc,
    h_21_npc, h_22_npc,
    h_23_npc, h_24_npc,
    h_25_npc, h_26_npc, h_27_npc, h_28_npc,
    h_29_npc, h_30_npc, h_31_npc, h_32_npc,)
#     h_33_npc, h_34_npc, h_35_npc, h_36_npc, h_37_npc, h_38_npc, h_39_npc,
#     h_40_npc, h_41_npc, h_42_npc, h_43_npc, h_44_npc,
#     h_45_npc, h_46_npc, h_47_npc, h_48_npc,
#     h_49_npc, h_50_npc,)


    event = npc_data[data[1]](data, stat)

    if not event:
        return [0, "Hmm ?"]

    elif type(event) == tuple:
        issue = fight(stat, event[0], event[1])
        if issue == 0:
            stat[1] += event[2]
            return [1, "Vous avez gagne le combat. [+{}PO]".format(event[2])]
        elif issue == 1: return [0, "Vous etes mort."]
        elif issue == 2: return [0, "Vous avez fuit."]
    
    else:
        return event


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
        helheim_po
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

    # Leave dialogue
    if stat[6][0] != -1 and stat[4] - stat[6][0] >= 2:
        stat[6] = (-1, -1)


# Game mecanics
def fight(stat, opponent_stat, opponent_name):

    def player_turn():
        end = False
        print_text("Tour de {}".format(stat[5]))
        if choice == 1:
            damage = 2 * stat_test(player_stat, 2)[2] - opponent_stat[3]
            if damage < 0: damage = 0
            
            if damage == 0:
                print_text("{} bloque l'attaque.".format(opponent_name))
            elif stat_test(opponent_stat[:-1], 1)[0]:
                print_text("{} esquive le coup.".format(opponent_name))
            else:
                opponent_stat[4] -= damage
                print_text("{0} perd {1} PV.".format(opponent_name, damage))

        elif choice == 2:
            if len(stat[8]) == 0:
                print_text("Vous ne connaissez pas de sort.")
            else:
                spell_data = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
                spell_level = ("I", "II", "III", "IV", "V")

                spell_choice = 0
                while not spell_choice:
                    count = 0
                    for spell_id, level in stat[8]:
                        print("{0}. {1} {2}".format(count + 1, spell_data[spell_id], spell_level[level]))
                        count += 1
                    spell_choice = get_input()
                    if spell_choice < 0 or spell_choice > 3: spell_choice = 0

                spell_choice -= 1
                spell_name, level = spell_data[stat[8][spell_choice][0]], stat[8][spell_choice][1] + 1

                if stat[2][4] >= level * 10:
                    print_text("Vous lancez {0} de niveau {1} [-{2} PM].".format(name, spell_level[level - 1]))
                    stat[2][4] -= level * 10

                    if stat[8][spell_choice][0] == 0:
                        stat[0] += 12 * level
                    elif stat[8][spell_choice][0] == 1:
                        opponent_stat[4] -= 12 * level
                    elif stat[8][spell_choice][0] == 2:
                        opponent_stat[4] -= 12 * level
                    elif stat[8][spell_choice][0] == 3:
                        opponent_stat[4] -= 12 * level
                    elif stat[8][spell_choice][0] == 4:
                        opponent_stat[0] -= 12 * level

                else:
                    print_text("Vous ne parvenez pas a lancer le sort.")

        elif choice == 3:
            if stat_test(player_stat, 1)[0]:
                end = True
            else:
                print_text("Votre tentative de fuite echoue.")

        return end

    def opponent_turn():
        print_text("Tour de {}".format(opponent_name))
        damage = 2 * stat_test(opponent_stat, 2)[2] - player_stat[3]
        if damage < 0: damage = 0

        if damage == 0:
            print_text("{} bloque l'attaque.".format(stat[5]))
        elif stat_test(player_stat, 1)[0]:
            print_text("{} esquive le coup.".format(stat[5]))
        else:
            stat[0] -= damage
            print_text("{0} perd {1} PV.".format(stat[5], damage))

    # opponent_stat = [vitesse, agilité, attaque, défense, vie]
    # player_stat = [vitesse, agilité, attaque, défense]
    player_stat = [stat[2][0], stat[2][1], stat[2][2] + stat[3][0] * 10, stat[2][3] + stat[3][1] * 10]

    player, opponent = 0, 0

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
        while player == opponent:
            player = stat_test(player_stat, 0)[1]
            opponent = stat_test(opponent_stat[:-1], 0)[1]

        # Fight
        if player > opponent:
            end = player_turn()
            if end: return 2

            if opponent_stat[4] > 0: opponent_turn()
            else: return 0
        else:
            opponent_turn()
            if stat[0] > 0: end = player_turn()
            else: return 1

    return 2


def misc_stat(data, stat):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - (temps, xp), 7 - classe, 8 - sorts connus : (id, level)]
    if data[1] < 9: place = ("Asgard", "Vanaheim", "Alfheim", "Midgard", "Niflheim", "Jotunheim", "Nidavellir", "Muspellheim", "Helheim")[data[1]]
    else: place =  "interieur"
    money, ticks, player_class = stat[1], stat[4], stat[7]
    
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

    if 360 < stat[4] < 1140:
        print_text("Vous ne pouvez pas dormir de jour.")
        return

    stat[4] = 360

    # If the player is at home
    if data[1] == 27:
        if stat[0] < 100: stat[0] += 10
        stat[2][4] += 2

    print_text("Vous vous reposez.")


def spell(data, stat):
    spell_data = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
    spell_level = ("I", "II", "III", "IV", "V")

    to_disp = "Magie : {} PM".format(stat[2][4])
    print("<o>    Sorts     <o>")
    print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")

    for i in range(3):
        if i < len(stat[8]):
            spell_id, level = stat[8][i]
            if spell_id >= 0:
                to_disp = "{0} {1}".format(spell_data[spell_id], spell_level[level - 1])
                print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")
        else:
            print(" |<aucun>         |")

    print("<o> ============ <o>")
    input()


events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 8:misc_stat, 6: inventory, 9: sleep}

# Main function
def idk(stat=None, data=None):
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
            stat = [5, 5, 5, 5, 10]
        elif player_class == 5:
            stat = [10, 5, 5, 5, 5]

        stat = [100, 10, stat, [0, 0], 360, name, (-1, -1), player_class - 1, []]
        data = [0, 3, 44, 66]

        print_text("Au alentour du Ve siecle, quelque part en Scandinavie. La bataille prenait place dans un champ saccage, et la nuit etait tombe depuis quelques heures lorsque l'assaut debuta.")
        print_text("Hache levee, a la seule lueur des torches, {0} et sa division se jeterent sur le camp adverse, mais, pris a revers, le combat tourna vite a la defaveur des assaillants qui furent reduit sans autres difficultes.".format(name))
        print_text("Blesse a plusieurs endroit, {0} se trainait sur le sol, tentant de se refugier dans la nuit lorsqu'une forme humaine portant un espadon dans le dos et une lourde armure d'argent s'arreta devant lui. La Valkyrie prit {0} dans ses bras. Une lueur aveuglante le forca a fermer les yeux et Vahalla lui apparu.".format(name))
        print_text("Mais Odin avait d'autres plan pour {0} qu'une retraite parmi les meilleurs guerriers, et il le renvoya dans le vaste monde avec cet ultimatum : si il trouve la voie jusqu'a Asgard et le Valaskjalf, Odin conscent a le garder a son service, sinon il sera condamne a errer dans le monde sans jamais trouver le repos.".format(name))

    idk_game = Asci(maps, events, keys)
    stat, data = idk_game.mainloop(100, stat, data, routine=routine, door="^_", walkable=".,`' ", exit_key="q")

    print("idk({0}, {1})".format(stat, data))


# Misc function
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
    avg = sum(stat) / len(stat)

    score = stat[test_id] + randint(0, ceil(avg / 2))
    return score >= avg, score / avg, score


