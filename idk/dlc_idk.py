dlc_title = "Marchands"

dlc_spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
dlc_spells_level = ("I", "II", "III", "IV", "V")
dlc_spells_effect = ((0, 1, True), (4, -1, False), (4, -1, False), (4, -1, False), (0, -1, False))
dlc_weapons = ("<aucune>", "Dague", "Marteau", "Masse", "Fleau", "Hache", "Epee", "Espadon", "Hache double")
dlc_armors = ("<aucune>", "Rondache", "Pavois", "Cote de maille", "Broigne", "Harnois")

def dlc_npc(data, stat, entities, identifiant):
    if not "dlc" in data[0]: data[0]["dlc"] = 0
    if data[1] == 3: return dlc_midgard_npc(data, stat, entities, identifiant)


def dlc_midgard_npc(data, stat, entities, identifiant):
    coords = data[2], data[3]
    xp = data[0]["dlc"]
    if coords == (51, 60):
        if xp == 0: return [0, "Bonjour, je suis Khajit, marchand ambulant. Je suis a la recherche d'un partenaire d'affaire, partant ?\n1. J'ai besoin d'y reflechir.\n2. J'en suis !", 2]
        elif xp == 1: return [-1, "Je comprends, reviens quand tu veux : je pense rester quelques temps a Midgard."]
        elif xp == 2: return [1, "Parfait !"]
