from asci_lib import Asci, text_formater

from asgard import *
from vanaheim import *
from alfheim import *
from midgard import *
from niflheim import *
from jotunheim import *
from nidavellir import *
from muspellheim import *
from helheim import *


# maps = (
#     asgard,
#     vanaheim,
#     alfheim,
#     midgard,
#     niflheim,
#     jotunheim,
#     nidavellir,
#     muspellheim,
#     helheim,
#     h_9, h_10, h_11, h_12, h_13, h_14, h_15, h_16, h_17, h_18, h_19, h_20,
#     h_21, h_22,
#     h_23, h_24,
#     h_25, h_26, h_27, h_28,
#     h_29, h_30, h_31, h_32,
#     h_33, h_34, h_35, h_36, h_37, h_38, h_39,
#     h_40, h_41, h_42, h_43, h_44,
#     h_45, h_46, h_47, h_48,
#     h_49, h_50)


# npc = (
#     asgard_npc,
#     vanaheim_npc,
#     alfheim_npc,
#     midgard_npc,
#     niflheim_npc,
#     jotunheim_npc,
#     nidavellir_npc,
#     muspellheim_npc,
#     helheim_npc,
#     h_9_npc, h_10_npc, h_11_npc, h_12_npc, h_13_npc, h_14_npc, h_15_npc, h_16_npc, h_17_npc, h_18_npc, h_19_npc, h_20_npc,
#     h_21_npc, h_22_npc,
#     h_23_npc, h_24_npc,
#     h_25_npc, h_26_npc, h_27_npc, h_28_npc,
#     h_29_npc, h_30_npc, h_31_npc, h_32_npc,
#     h_33_npc, h_34_npc, h_35_npc, h_36_npc, h_37_npc, h_38_npc, h_39_npc,
#     h_40_npc, h_41_npc, h_42_npc, h_43_npc, h_44_npc,
#     h_45_npc, h_46_npc, h_47_npc, h_48_npc,
#     h_49_npc, h_50_npc,)


# po = (
#     asgard_po,
#     vanaheim_po,
#     alfheim_po,
#     midgard_po,
#     niflheim_po,
#     jotunheim_po,
#     nidavellir_po,
#     muspellheim_po,
#     helheim_po)


def npc(data, stat):
    npc = ()

    event = png[data[1]](data, stat)

    if not event: return [0, "Hmm ?"]
    else: return event


def point_of_interest(data, stat):
    coords = data[2], data[3]

    po = ()

    event = po[data[1]](coords)

    if not event: return [0, "Il n'y a rien à voir ici."]
    else: return event


def routine(data, stat):
    stat[4] = (stat[4] + 1) % 1440

    if stat[6][0] != -1 and stat[6][0] - stat[4] >= 5:
        stat[6] = (-1, -1)


def sleep(data, stat):
    stat[4] = 360

    # If the player is at home
    if data[1] == 27:
        stat[0] += 10
        if stat[0] > 100: stat[0] = 100

    print("Vous vous reposez.")
    input()


def display_stat(data, stat):
    # stat = [0 - PV, 1 - pièces d'or, 2 - arme, 3 - armure, 4 - ticks, 5 - nom, 6 - (temps, xp)]
    place = ("Asgard", "Vanaheim", "Alfheim", "Midgard", "Niflheim", "Jotunheim", "Nidavellir", "Muspellheim", "Helheim")[data[1]]
    health, money, _, _, ticks, _, _ = stat
    
    hours = ticks // 60
    if 4 <= hours <= 5:
        hours = "aube"
    elif 6 <= hours <= 12:
        hours = "matin"
    elif 13 <= hours <= 18:
        house = "apres-midi"
    elif 19 <= hours <= 20:
        hours = "crepuscule"
    else:
        hours = "nuit"

    print("<*> Statistiques <*>")
    print("Lieu : {}".format(place))
    print("Heure : {}".format(hours))
    print("Vie : {}/100".format(health))
    print("Argent : {} PO".format(money))
    print("<*>              <*>")
    input()


def inventory(data, stat):
    weapons = ("<aucune>", "dague", "marteau", "masse", "fleau", "hache", "epee", "espadon", "hache double")
    shields = ("<aucune>", "rondache", "pavois", "cote de maille", "broigne", "harnois")

    print("<*>  Inventaire  <*>")
    print("  Arme :\n{}".format(weapons[stat[2]]))
    print("  Armure :\n{}".format(shields[stat[3]]))
    print()
    print("<*>              <*>")
    input()


events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 6: inventory, 7: sleep}

def idk(stat=None, data=None):
    if not stat:
        name = input("Entrez votre nom : ")
        stat = [100, 10, 0, 0, 360, name, (-1, -1)]
        data = [0, 3, 44, 65]

        paragraphs = text_formater("Au alentour du Ve siecle. Quelque part en Scandinavie. La bataille prenait place dans un champ saccage, les arbres alentours avaient ete abbatus pour les besoins en bois, et la nuit etait tombe depuis quelques heures. Une brusque douleur reveilla {0} et lui arracha un hurlement : les ennemis attaquaient, mais le jeune soldat ne put rien faire... Les reins pulverises par le violent coup de hache, il se traina sur quelques metres. L'assaut fut vite termine faute de combattants. A travers une brume de larmes et de douleur il entendit un homme se pencher sur lui, un infirmier peut-etre ? Mais ce dernier s'en alla vers un autre blesse. Ainsi se termina la courte vie de {0}.".format(name))
        for i in paragraphs:
            print("\n" * 7)
            print(i)
            input()

    # idk_game = Asci(maps, events, keys)
    # idk_game.mainloop(100, stat, data, routine=routine, door="^_", walkable=".,`' ")
