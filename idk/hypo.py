from idk_lib import *


# Game
def npc(data, stat, entities, identifiant):    
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
        h_45_npc, h_46_npc, h_47_npc, h_48_npc,
    )

    if identifiant == "Kvasir": return kvasir(data, stat, entities)
    elif identifiant == 12: return frigg(data, stat, entities)
    elif identifiant == "Freyja": return freyja(data, stat, entities)
    else: return npc_core(npc_data[data[1]], data, stat, entities, identifiant)


def point_of_interest(data, stat, entities, identifiant):
    po_data = (
        asgard_po,
        vanaheim_po,
        alfheim_po,
        midgard_po,
        niflheim_po,
        jotunheim_po,
        nidavellir_po,
        muspellheim_po,
        svartalfheim_po,
    )

    coords = data[2], data[3]
    event = po_data[data[1]](coords, identifiant)

    if not event: return [0, "Il n'y a rien à voir ici."]
    else: return event


entities = asgard_entities + vanaheim_entities + alfheim_entities + midgard_entities + niflheim_entities + jotunheim_entities + nidavellir_entities + muspellheim_entities + svartalfheim_entities + dlc_entities + (["Kvasir", "*", 3, 46, 66, "stand by"], )

print(center("L'Hydromel poetique", 21, " "))
print("---------------------")
print()
print("Entrez 'hypo()' pour\nune nouvelle partie.")
events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 8: misc_stat, 6: inventory, 9: sleep, "s": quick_save}


def hypo(save_code=None):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - classe, 7 - sorts connus : (id, level), 8 - sous-quêtes terminées, 9 - misc]
    if not save_code:
        stat = init_stat()
        name = stat[5]
        data = [{"main": 0}, 3, 44, 66]

        print_text("A l'issue de la guerre qui opposa Ases et Vanes, Odin et Freyja conclurent un accord de paix durant lequel ils cracherent dans une meme cuve. De cette cuve naquit Kvasir, l'etre le plus sage qui soit. Venere par tous, Kvasir est tres souvent appelle au chevet des Dieux pour prodiguer ses precieux conseils. Odin et Freyja vous ont missionne pour escorter et assister Kvasir dans ses deplacements.")
    else:
        stat, data = decode_save(save_code)

    idk_game = Asci(maps, entities, events, keys)
    npc_init_position(idk_game.entities, data[0]["main"])
    
    stat, data = idk_game.mainloop(100, stat, data, routine=routine, low_bar=low_bar, door="^_", walkable=".,`' ", exit_key="q")

    if data[0]["main"] == 100:
        print_text("conclusion")
    else:
        print("hypo(\"{}\")".format(encode_save(data, stat)))


def npc_init_position(entites, xp):
    if xp < 2: entites["Kvasir"].change_behavior("follow")
    elif xp < 11: entites["Kvasir"].teleport(16, 50, 16)
    elif xp < 13: entites["Kvasir"].teleport(16, 29, 28)
    elif xp < 24: entites["Kvasir"].teleport(16, 30, 28)
    else:
        entites["Kvasir"].teleport(16, 50, 16)
        entites["Freyja"].teleport(16, 48, 14)

    if 16 < xp < 17: entites[12].teleport(4, 79, 20)
    elif 17 <= xp < 21: entites[12].teleport(4, 71, 32)



def kvasir(data, stat, entites):
    if data[0]["main"] == 13: entites["Kvasir"].teleport(16, 30, 28)
    
    return {
        "base": [0, "Je suis Kvasir."],
        0: [1, "Baldr m'a confie etre preoccupe par de recents reves premonitoires. Nous devrions aller le voir."],
        1: [0, "Nous devrions aller voir Baldr. Il habite dans le Breidablik, a Asgard."],
        2: [0, "Je vais rester ici pour veiller sur Baldr, va chercher Freyja et reviens vite !"],

        13: [1, "En partant, pense a prevenir la mere de Baldr. [KVASIR SE DECALA POUR VOUS CEDER LE PASSAGE.]"],

        25: [0, "Grace a toi et a Hel, Baldr est maintenant invincible ! [POUR APPUYER SES PROPOS, KVASIR DEGAINA UNE PETITE DAGUE QU'IL PORTAIT A LA TAILLE ET L'ENFONCA DANS LE VENTRE DE BALDR. LA BLESSURE NE SEMBLAIT PAS LE FAIRE SOUFFRIR LE MOINDRE DU MONDE ET CICATRISA AU FUR ET A MESURE QUE KVASIR RECUPERAIT SON ARME.]"],
        28: [0, "Il me semble que Baldr a une petite commission a te demander."]
    }


def frigg(data, stat, entites):
    if data[0]["main"] == 16: entites[12].teleport(4, 79, 20)
    elif data[0]["main"] == 17: entites[12].change_behavior("follow by player", 0, ((82, 20), (82, 32), (71, 32)))
    elif data[0]["main"] == 18:
        if stat[9] == -1: return [0, "[FRIGG SE TOURNA, VERS VOUS, UNE POINTE D'EMOTION DANS LA VOIX.] Nous voila devant le palais de Hel.\n1. Mais pourquoi sommes nous ici ?\n2. Que faisons-nous maintenant ?", 2]
        else: return [0, "[FRIGG SE TOURNA, VERS VOUS, UNE POINTE D'EMOTION DANS LA VOIX.] Nous voila devant le palais de Hel.\n1. Mais pourquoi sommes nous ici ?\n2. Que faisons-nous maintenant ?\n3. Souhaitez-moi bonne chance !", 3]
    elif data[0]["main"] == 21:
        stat[9] = -1
        entites[12].teleport(0, 8, 44)

    return {
        "base": [0, "Je suis Frigg, deesse du mariage et de la maternite."],
        14: [0, "Frigg, deesse du mariage et de la maternite, que puis-je pour toi ?\n1. Pour moi rien, c'est votre fils, Baldr.", 1],
            15: [0, "Que lui arrive-t-il ?\n1. Il reve de sa mort. Freyja va tenter de voir son avenir grace au Seidr.", 1],
            16: [1, "Le Seidr ne fait pas tout, c'est Hel qu'il faut aller voir. On se retrouve a Helheim."],
            17: [1, "Je savais que tu viendrais, suis-moi."],
            19: [-1, "Les reves premonitoires ne sont jamais bon signe. Si Baldr reve de sa mort, le meilleur moyen de l'empecher de passer de l'autre cote est encore de convaincre Hel de le rendre immortel."],
            20: [-2, "Il va te falloir convaincre Hel pour qu'elle rende Baldr immortel. Aucun Dieu, aucun humain, aucun animal, aucune plante ni aucune chose ne doit pouvoir le blesser ni le tuer.", 0, (9, 1)],       
            21: [1, "Bon courage {}. Et merci ! Pour ma part je vais retourner au chevet de mon fils.".format(stat[5])],
        }


def freyja(data, stat, entites):
    if data[0]["main"] == 10: data[1], data[2], data[3] = 16, 29, 28

    return {
        "base": [0, "Je suis Freyja, la reine des Vanes."],
        7: [0, "Tu n'as pas l'air tres frais {}...\n1. Desole, je viens d'Asgard, le voyage a ete... brutal.\n2. Baldr m'envoie requerir votre aide.".format(stat[5]), 2],
            8: [-1, "C'est Freyr qui t'as teleporte ? Pourtant je lui ai fait repeter le sort des dizaines de fois..."],
            9: [0, "Baldr ?! Que lui arrive-t-il ?\n1. Il reve de sa propre mort, et voudrais que le Seidr eclaire son avenir.", 1],
                10: [1, "Hmm... Je vais voir ce que je peux faire. As-tu prevenu Frigg, sa mere ? Tu la trouveras non loin du Breidablik. [UNE DOUCE CHALEUR VOUS ENVELOPPA, VOUS FERMEZ LES YEUX ET TOMBEZ DANS UN SOMMEIL PROFOND.]"],
        
        25: [0, "Baldr savoure sa jeune immortalite, et ignore les avertissements du Seidr.\n1. Comment cela ?\n2. Cela n'a guere d'importance : il est immortel.", 2],
            26: [2, "Il m'accuse de jouer les rabas-joie, mais je sais ce que j'ai vu, et Baldr est aussi immortel et toi et moi... enfin... surtout toi."],
            27: [1, "Tu seras moins sur de toi quand il mourra."],
        28: [0, "Baldr mourra. Et plus tot qu'on ne le pense."],
    }


# - - - Asgard - - - #
def asgard_po(coords, identifiant):
    pass


def asgard_npc(data, stat, entites, identifiant):
    pass        


def h_9_npc(data, stat, entites, identifiant):
    pass


def h_10_npc(data, stat, entites, identifiant):
    if identifiant == "Odin":
        return {
            "base": [0, "Je suis Odin, le plus puissant des Ases."],
            29: [],
        }


def h_11_npc(data, stat, entites, identifiant):
    pass


def h_12_npc(data, stat, entites, identifiant):
    pass


def h_13_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if coords == (21, 8):
        if data[0]["main"] == 6: data[1], data[2], data[3] = 1, 54, 29

        return {
            "base": [0, "Freyr, pour te servir."],
            2: [0, "[FREYR SE RETOURNE VERS VOUS.] Oh, bonjour {}. Que puis-je faire pour toi ?\n1. Baldr reve de sa mort et aimerait en savoir plus sur son destin.\n2. Je cherche Freyja.\n3. Que faites-vous ici ?\n4. Pouvez-vous m'envoyer a Vanaheim s'il vous plait ?".format(stat[5]), 4],
                3: [-1, "Hum, je comprends... Pour ce genre de question, Freyja est plus douee que moi."],
                4: [-2, "La derniere fois que je l'ai vue elle etait a Vanaheim."],
                5: [-3, "Depuis la fin de la Premiere Guerre, Ases et Vanes ont echanges des Dieux en signe d'appaisement. Je suis ainsi arrive chez les Ases. Freyja vient de temps en temps me rendre visite."],
                6: [1, "Mais bien sur {} ! [L'HABITUELLE TORPEUR VOUS PRIT, VOTRE VISION D'ESTOMPA DANS UNE SENSATION NAUSEEUSE DE FLOTTEMENT. LE CHOC BRUTAL CONTRE LA TERRE VOUS REVEILLA COMME D'UN MAUVAIS REVE.]".format(stat[5])],
        }


def h_14_npc(data, stat, entites, identifiant):
    pass


def h_15_npc(data, stat, entites, identifiant):
    pass


def h_16_npc(data, stat, entites, identifiant):
    if identifiant == "Baldr":
        
        if data[0]["main"] == 1:
            entites["Kvasir"].change_behavior("stand by")
            entites["Kvasir"].teleport(16, 50, 16)
        elif data[0]["main"] == 11:
            entites["Kvasir"].change_behavior("walk to", 0, ((50, 25), (29, 25), (29, 28)))
        
        return {
            "base": [0, "Baldr, fils d'Odin et de Frigg. Dieu de la lumiere, de la jeunesse, de l'amour et de la beaute."],
            1: [0, "Ah ! Vous voila enfin ! Depuis quelques temps, je fais des reves etranges dans lesquels je me vois mourir. Maintenant, j'ai meme peur de sortir du Breidablik !\n1. Nous pouvons vous aider ?", 1],
            2: [0, "Si vous pouviez demander de l'aide à Freyja, je vous en serais reconnaissant.\n1. En quoi Freyja peut vous aider ?\n2. Ou pouvons-nous la trouver ?", 2],
                3: [-1, "Freyja pratique le Seidr, et, avec Odin, elle est la meilleure seidr de tout l'Yggdrasil. Avant que tu ne me demandes, le Seidr est une forme de magie divinatoire. Nous autres, Dieux, la pratiquons et pour certains avec beaucoup de puissance. Mais les humains peuvent aussi en faire."],
                4: [-2, "Habituellement, elle reside dans son palais a Vanaheim, mais depuis la treve et en signe de paix, elle se rend regulierement au Folkvangr."],
            
            11: [0, "Ah {} deja de retour !\n1. Freyja m'a dit qu'elle allait faire son possible.".format(stat[5]), 1],
                12: [1, "Très bien ! Merci beaucoup de ton aide ! Voici quelques pieces. [+15 PO]", 0, (1, 15)],

            25: [0, "Ah merci {} ! Grace a toi je ne crains plus la mort ! Odin, mon pere, n'a plus besoin de s'inquieter de rien !".format(stat[5])],
            28: [1, "{}, mon ami ! Va porter ce plis a mon pere, Odin.".format(stat[5])],

        }


def h_17_npc(data, stat, entites, identifiant):
    pass


def h_18_npc(data, stat, entites, identifiant):
    pass


def h_19_npc(data, stat, entites, identifiant):
    pass


def h_20_npc(data, stat, entites, identifiant):
    pass


# - - - Vanaheim - - - #
def vanaheim_po(coords, identifiant):
    pass


def vanaheim_npc(data, stat, entites, identifiant):
    pass


def h_21_npc(data, stat, entites, identifiant):
    pass


def h_22_npc(data, stat, entites, identifiant):
    pass


# - - - Alfheim - - - #
def alfheim_po(coords, identifiant):
    pass


def alfheim_npc(data, stat, entites, identifiant):
    pass


def h_23_npc(data, stat, entites, identifiant):
    pass


def h_24_npc(data, stat, entites, identifiant):
    pass


# - - - Midgard - - - #
def midgard_po(coords, identifiant):
    pass


def midgard_npc(data, stat, entites, identifiant):
    pass


def h_25_npc(data, stat, entites, identifiant):
    pass


def h_26_npc(data, stat, entites, identifiant):
    pass


def h_27_npc(data, stat, entites, identifiant):
    pass


def h_28_npc(data, stat, entites, identifiant):
    pass


# - - - Niflheim - - - #
def niflheim_po(coords, identifiant):
    pass


def niflheim_npc(data, stat, entites, identifiant):
    pass


def h_29_npc(data, stat, entites, identifiant):
    pass


def h_30_npc(data, stat, entites, identifiant):
    if identifiant == "Hel":
        if data[0]["main"] == 24:
            entites["Kvasir"].teleport(16, 50, 16)
            entites["Freyja"].teleport(16, 48, 14)

        return {
            "base": [0, "Je suis Hel, deesse de la mort et reine de Niflheim"],
            22: [0, "Un humain !? C'est chose rare ici... surtout vivant.\n1. Je viens de la part de Frigg", 1],
            23: [0, "[HEL LEVA LES YEUX D'UN AIR EXASPÉRÉ.] Que veux-t-elle ?\n1. Baldr reve de sa mort et Frigg aimerait lui garantir la vie eternelle.", 1],
            24: [1, "Encore !? Bon d'accord, cette fois-ci je le ferai."],
            25: [0, "Oui, oui c'est bon je m'en occupe !"],
        }


# - - - Jotunheim - - - #
def jotunheim_po(coords, identifiant):
    pass


def jotunheim_npc(data, stat, entites, identifiant):
    pass


def h_31_npc(data, stat, entites, identifiant):
    pass


def h_32_npc(data, stat, entites, identifiant):
    pass


def h_33_npc(data, stat, entites, identifiant):
    pass


def h_34_npc(data, stat, entites, identifiant):
    pass


def h_35_npc(data, stat, entites, identifiant):
    pass


def h_36_npc(data, stat, entites, identifiant):
    pass


# - - - Nidavellir - - - #
def nidavellir_po(coords, identifiant):
    pass


def nidavellir_npc(data, stat, entites, identifiant):
    pass


def h_37_npc(data, stat, entites, identifiant):
    pass


def h_38_npc(data, stat, entites, identifiant):
    pass


def h_39_npc(data, stat, entites, identifiant):
    pass


def h_40_npc(data, stat, entites, identifiant):
    pass


def h_41_npc(data, stat, entites, identifiant):
    pass


# - - - Muspellheim - - - #
def muspellheim_po(coords, identifiant):
    pass


def muspellheim_npc(data, stat, entites, identifiant):
    pass


def h_42_npc(data, stat, entites, identifiant):
    pass


def h_43_npc(data, stat, entites, identifiant):
    pass


def h_44_npc(data, stat, entites, identifiant):
    pass


# - - - Svartalfheim - - - #
def svartalfheim_po(coords, identifiant):
    pass


def svartalfheim_npc(data, stat, entites, identifiant):
    pass


def h_45_npc(data, stat, entites, identifiant):
    pass


def h_46_npc(data, stat, entites, identifiant):
    pass


def h_47_npc(data, stat, entites, identifiant):
    pass


def h_48_npc(data, stat, entites, identifiant):
    pass