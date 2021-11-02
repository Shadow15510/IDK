from asci_lib import Asci


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
    h_9,
    h_10,
    h_11,
    h_12,
    h_13,
    h_14,
    h_15,
    h_16,
    h_17, 
    h_18,
    h_19,
    h_20,
    h_21,
    h_22,
    h_23,
    h_24,
    h_25,
    h_26,
    h_27,
    h_28)


def pnj(data, stat):
    pnj = [
        asgard_pnj,
        vanaheim_pnj,
        alfheim_pnj,
        midgard_pnj,
        niflheim_pnj,
        jotunheim_pnj,
        nidavellir_pnj,
        muspellheim_pnj,
        helheim_pnj,
        h_9_pnj,
        h_10_pnj,
        h_11_pnj,
        h_12_pnj,
        h_13_pnj,
        h_14_pnj,
        h_15_pnj,
        h_16_pnj,
        h_17_pnj, 
        h_18_pnj,
        h_19_pnj,
        h_20_pnj,
        h_21_pnj,
        h_22_pnj,
        h_23_pnj,
        h_24_pnj,
        h_25_pnj,
        h_26_pnj,
        h_27_pnj,
        h_28_pnj,
    ]

    event = png[data[1]](data, stat)

    if not event: return [0, "Hmm ?"]
    else: return event


def point_of_interest(data, stat):
    coords = data[2], data[3]

    po = [
        asgard_po,
        vanaheim_po,
        alfheim_po,
        midgard_po,
        niflheim_po,
        jotunheim_po,
        nidavellir_po,
        muspellheim_po,
        helheim_po,
    ]

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


def idk(stat=None, data=None):
    if not stat:
        name = input("Entrez votre nom : ")
        stat = [100, 10, 0, 0, 360, name, (-1, -1)]
        data = [0, 3, 44, 65]

    display_stat(data, stat)
    inventory(data, stat)
