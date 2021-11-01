from asci_lib import Asci


def pnj(data, stat):
    xp, current_map, x, y = data
    coords = x, y

    # Asgard
    if current_map == 0:
        pass

    # Vanaheim
    elif current_map == 1:
        pass

    # Alfheim
    elif current_map == 2:
        pass

    # Midgard
    elif current_map == 3: return midgard_pnj(coords)

    # Niflheim
    elif current_map == 4:
        pass

    # Jotunheim
    elif current_map == 5:
        pass

    # Nidavellir
    elif current_map == 6:
        pass

    # Muspellheim
    elif current_map == 7:
        pass

    # Helheim
    elif current_map == 8:
        pass

    return [0, "Hmm ?"]


def point_of_interest(data, stat):
    xp, current_map, x, y = data
    coords = x, y

    # Asgard
    if current_map == 0:
        pass

    # Vanaheim
    elif current_map == 1:
        pass

    # Alfheim
    elif current_map == 2:
        pass

    # Midgard
    elif current_map == 3: return midgard_po(coords)
        
    # Niflheim
    elif current_map == 4:
        pass

    # Jotunheim
    elif current_map == 5:
        pass

    # Nidavellir
    elif current_map == 6:
        pass

    # Muspellheim
    elif current_map == 7:
        pass

    # Helheim
    elif current_map == 8:
        pass


def routine(data, stat):
    stat[4] = (stat[4] + 1) % 1440


def sleep(data, stat):
    stat[4] = 360

def display_stat(data, stat):
    # stat = [PV, pièces d'or, arme, armure, ticks, nom]
    place = ("Asgard", "Vanaheim", "Alfheim", "Midgard", "Niflheim", "Jotunheim", "Nidavellir", "Muspellheim", "Helheim")[data[1]]
    health, money, _, _, ticks, _ = stat
    
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
    print("Arme :\n{}".format(weapons[stat[2]]))
    print("Armure :\n{}".format(shields[stat[3]]))
    print()
    print("<*>              <*>")
    input()


def idk(stat=None, data=None):
    if not stat:
        name = input("Entrez votre nom : ")
        stat = [100, 10, 0, 0, 360, name]
        data = [0, 3, 44, 65]

    display_stat(data, stat)
    inventory(data, stat)
