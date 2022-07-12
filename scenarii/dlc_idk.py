dlc_title = "Marchands"

dlc_spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
dlc_spells_level = ("I", "II", "III", "IV", "V")
dlc_spells_effect = ((0, 1, True), (4, -1, False), (4, -1, False), (4, -1, False), (0, -1, False))
dlc_weapons = ("<aucune>", "Dague", "Marteau", "Masse", "Fleau", "Hache", "Epee", "Espadon", "Hache double")
dlc_armors = ("<aucune>", "Rondache", "Pavois", "Cote de maille", "Broigne", "Harnois")

dlc_entities = (
    ["Khajit", '*', 3, 51, 60, 'stand by'],
)

def dlc_npc(data, stat, entities, identifiant):
    if not "dlc" in data[0]: data[0]["dlc"] = 0
    coords = data[2], data[3]
    xp = data[0]["dlc"]
    main = data[0]["main"]

    if identifiant == "Khajit":
        if xp == 0: return [0, "Bonjour {}, je suis Khajit, marchand ambulant. Je suis a la recherche d'un partenaire d'affaire, partant ?\n1.J'ai besoin d'y reflechir.\n2.J'en suis !\n3.On se connait ?".format(stat[5]), 3]
        elif xp == 1: return [-1, "Je comprends, reviens quand tu veux : je pense rester quelques temps a Midgard."]
        elif xp == 2: return [2, "Excellente idee ! Un riche client m'a demande la dague d'Odin. Si tu arrives a te la procurer, cela serait un bon debut."]
        elif xp == 3: return [-3, "Hum, non. Mais les nouvelles vont vites et ceux qui peuvent voyager dans tous l'Yggdrasil sont rares."]
        elif xp == 4:
            if main == 0: return [0, "Alors ?"]
            elif main <= 3: return [0, "Oh ! [KHAJIT VOUS PRIS LA DAGUE DES MAINS] Elle est superbe ! Mais je crois que tu en as encore besoin. [KHAJIT VOUS RENDIT LA DAGUE]"]
            elif stat[3][0] == 1:
                stat[3][0] = 2
                return [1, "Magnifique ! [KHAJIT PRIT LA DAGUE ET LA RANGEA] Voici un marteau en echange et quelques pieces ! Revient me voir bientot, j'aurais du travail pour toi. [+10 PO]", 0, (1, 10)]
            else: return [1, "Hum, tu n'as plus la dague... Ce n'est pas grave, nous trouveront bien un autre client. Revient me voir bientot, j'aurais du travail pour toi."]

