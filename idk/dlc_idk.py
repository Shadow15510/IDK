title = "Marchands"

spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
spells_level = ("I", "II", "III", "IV", "V")
spells_effect = ((0, 1, True), (4, -1, False), (4, -1, False), (4, -1, False), (0, -1, False))
weapons = ("<aucune>", "Dague", "Marteau", "Masse", "Fleau", "Hache", "Epee", "Espadon", "Hache double")
armors = ("<aucune>", "Rondache", "Pavois", "Cote de maille", "Broigne", "Harnois")

def npc(data, stat, entites, identifiant):
    coords = data[2], data[3]
    pass