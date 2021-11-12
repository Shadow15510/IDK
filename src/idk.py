from asci_lib import Asci, print_text

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


po_data = (
    asgard_po,
    vanaheim_po,
    alfheim_po,
    midgard_po,
    niflheim_po,
    jotunheim_po,
    nidavellir_po,
    muspellheim_po,
    helheim_po)


def npc(data, stat):
    event = npc_data[data[1]](data, stat)

    if not event: return [0, "Hmm ?"]
    else: return event


def point_of_interest(data, stat):
    coords = data[2], data[3]

    event = po_data[data[1]](coords)

    if not event: return [0, "Il n'y a rien à voir ici."]
    else: return event


def routine(data, stat):
    stat[4] = (stat[4] + 1) % 1440

    # Mana regeneration
    if stat[2][4] < stat[0] // 20 and not (stat[4] % 10):
        stat[2][4] += 1

    # Leave dialogue
    if stat[6][0] != -1 and stat[4] - stat[6][0] >= 2:
        stat[6] = (-1, -1)


def fight(player_stat, opponent_stat):
    pass


def display_stat(data, stat):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - (temps, xp), 7 - classe, 8 - sorts connus : (id, level)]
    if data[1] < 9: place = ("Asgard", "Vanaheim", "Alfheim", "Midgard", "Niflheim", "Jotunheim", "Nidavellir", "Muspellheim", "Helheim")[data[1]]
    else: place =  "Interieur"
    health, money, _, _, ticks, _, _, _, _ = stat
    
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

    health = " |Vie : {}/100".format(health)
    money = " |Argent : {} PO".format(money)

    print("<o> Statistiques <o>")
    print(" |" + place.center(16, " ") + "|")
    print(hours + " " * (18 - len(hours)) + "|")
    print(health + " " * (18 - len(health)) + "|")
    print(money + " " * (18 - len(money)) + "|")
    print("<o> ============ <o>")
    input()


def inventory(data, stat):
    weapon = ("<aucune>", "dague", "marteau", "masse", "fleau", "hache", "epee", "espadon", "hache double")[stat[3][0]]
    shield = ("<aucune>", "rondache", "pavois", "cote de maille", "broigne", "harnois")[stat[3][1]]

    weapon = " |" + weapon + " " * (16 - len(weapon)) + "|"
    shield = " |" + shield + " " * (16 - len(shield)) + "|"

    print("<o>  Inventaire  <o>")
    print(" |- Arme :        |\n{}".format(weapon))
    print(" |- Armure :      |\n{}".format(shield))
    print("<o> ============ <o>")
    input()


def sleep(data, stat):
    stat[4] = 360

    # If the player is at home
    if data[1] == 27:
        if stat[0] < 100: stat[0] += 10
        stat[2][4] += 2

    print("Vous vous reposez.")
    input()


def spell(data, stat):
    spell_data = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
    spell_level = ("I", "II", "III", "IV", "V")

    to_disp = "Magie : {}".format(stat[2][4])
    print("<o>    Sorts     <o>")
    print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")

    for i in range(3):
        if i < len(stat[8]):
            spell_id, level = stat[8]
            if spell_id >= 0:
                to_disp = "{0} {1}".format(spell_data[spell_id], spell_level[level - 1])
                print(" |" + to_disp + " " * (16 - len(to_disp)) + "|")
        else:
            print(" |<aucun>         |")

    print("<o> ============ <o>")
    input()


events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 6: inventory, 9: sleep}

def idk(stat=None, data=None):
    if not stat:
        name = input("Entrez votre nom : ")

        player_class = 0
        while(not player_class):
            print("Choisissez votre classe\n1. Guerrier\n2. Voleur\n3. Moine\n4. Mage")
            print()
            player_class = input(">")
            try: player_class = int(player_class)
            except: player_class = 0

            if player_class > 4: player_class = 0

        if player_class == 1:
            stat = [5, 5, 10, 5, 5]
        elif player_class == 2:
            stat = [5, 10, 5, 5, 5] 
        elif player_stat == 3:
            stat = [5, 5, 5, 10, 5]
        elif player_stat == 4:
            stat = [5, 5, 5, 5, 10]

        stat = [100, 10, stat, [0, 0], 1170, name, (-1, -1), player_class - 1, []]
        data = [0, 3, 44, 66]

        print_text("Au alentour du Ve siecle, quelque part en Scandinavie. La bataille prenait place dans un champ saccage, les arbres alentours avaient ete abbatus pour les besoins en bois, et la nuit etait tombe depuis quelques heures lorsque l'assaut debuta. Hache levee, a la seule lueur des torches, {0} et sa division se jeterent sur le camp adverse, mais, pris a revers, le combat tourna vite a la defaveur des assaillants qui furent reduit sans autres difficultes. Blesse a plusieurs endroit, {0} se trainait sur le sol, tentant de se refugier dans la nuit lorsqu'une forme humaine portant un espadon dans le dos et une lourde armure d'argent s'arrêta devant lui. La Valkyrie prit {0} dans ses bras. Il senti son ame se dissocier de son corps, il vit son cadavre, le champ de bataille, le pays entier lui apparut, un lueur aveuglante le forca a fermer les yeux et Vahalla lui apparu. Mais Odin avait d'autres plan pour {0} qu'une retraite parmi les meilleurs guerriers, et il renvoya {0} dans le vaste monde avec cet ultimatum : si {0} trouve la voie jusqu'a Asgard et le Valaskjalf, Odin conscent a le garder a son service, sinon il sera condamne a errer dans le monde sans jamais trouver le repos.".format(name))

    idk_game = Asci(maps, events, keys)
    stat, data = idk_game.mainloop(100, stat, data, routine=routine, door="^_", walkable=".,`' ", exit_key="q")

    print(f"idk({stat}, {data})")
