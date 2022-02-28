from idk_lib import *

try:
    import dlc_idk as dlc
    spells = dlc.dlc_spells
    spells_level = dlc.dlc_spells_level
    spells_effect = dlc.dlc_spells_effect
    weapons = dlc.dlc_weapons
    armors = dlc.dlc_armors
    dlc_entities = dlc.dlc_entities
except:
    dlc = None
    dlc_entities = []



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
    h_45_npc, h_46_npc, h_47_npc, h_48_npc)


    if dlc:
        event = dlc.dlc_npc(data, stat, entities, identifiant)
        if event: return "dlc", event

    return npc_core(npc_data[data[1]], data, stat, entities, identifiant)


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
        svartalfheim_po
    )

    coords = data[2], data[3]
    event = po_data[data[1]](coords, identifiant)

    if not event: return [0, "Il n'y a rien à voir ici."]
    else: return event


entities = asgard_entities + vanaheim_entities + alfheim_entities + midgard_entities + niflheim_entities + jotunheim_entities + nidavellir_entities + muspellheim_entities + svartalfheim_entities + dlc_entities

print(center("Island of the Dead", 21, " "))
print(center("*  Kings  *", 21, " "))
print("---------------------")
if dlc: print(center("DLC : {}".format(dlc.dlc_title), 21, " "))
else: print()
print("Entrez 'idk()' pour\nune nouvelle partie.")
events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 8: misc_stat, 6: inventory, 9: sleep, "s": quick_save}


def idk(save_code=None):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - classe, 7 - sorts connus : (id, level), 8 - sous-quêtes terminées]
    if not save_code:
        stat = init_stat()
        name = stat[5]
        data = [{"main": 0}, 3, 44, 66]

        print_text("Au alentour du Ve siecle, quelque part en Scandinavie. La bataille prenait place dans un champ saccage, et la nuit etait tombee depuis quelques heures lorsque l'assaut debuta. Hache levee, a la seule lueur de la pleine lune, {0} et sa division se jeterent sur le camp adverse, mais, pris a revers, le combat tourna vite a la defaveur des assaillants qui furent reduit sans autres difficultes.\nBlesse a plusieurs endroit, {0} se trainait sur le sol, tentant de se refugier dans la nuit lorsqu'une forme humaine portant un espadon dans le dos et une lourde armure d'argent s'arreta silencieusement devant lui. La Valkyrie degaina son espadon et acheva {0} avant de l'emporter dans ses bras.\nMais Odin, septique des exploits au combat de {0}, lui refusa une retraite parmi les meilleurs guerriers, et il le renvoya dans le vaste monde avec cet ultimatum : s'il trouve la voie jusqu'a Asgard et le Valaskjalf, Odin conscent a revoir son jugement, sinon il sera condamne a errer dans le monde sans jamais trouver le repos.".format(name))

    else:
        stat, data = decode_save(save_code)

    idk_game = Asci(maps, entities, events, keys)
    stat, data = idk_game.mainloop(102, stat, data, routine=routine, door="^_", walkable=".,`' ", exit_key="q")
    if stat[9] != -1: data[0]["main"] -= stat[9]

    if data[0]["main"] == 102:
        print_text("Ainsi s'acheva la premiere guerre du monde. Les Ases garderent la tete de Mimir pour ses conseils avises, mais il n'y eu jamais de represailles. Les Ases et les Vanes se melerent ne formant ainsi qu'une seule et meme grande famille.")
    
    else:
        print("idk(\"{}\")".format(encode_save(data, stat[:-1])))


# Scenario
def shop_interaction(data, stat, nb_choice, *events):
    for choice in range(nb_choice):
        if data[0]["main"] == stat[9] + choice + 1:
            stat[9] = -1
            if stat[1] < events[choice][0]: return events[choice][2], choice + 1
            else: return events[choice][1], choice + 1


# - - - Asgard - - - #
def asgard_po(coords, identifiant):
    if coords == (120, 26): return [0, "De hautes montagnes vous entourent de toutes part. Taillees dans la roche enneigee, les marches de l'escalier qui mene a Valaskjalf se decoupent nettement. La grande demeure d'Odin et son toit d'argent domine les environs."]
    elif coords == (51, 55): return [0, "Tout autour de vous s'etend un riche jardin soigneusement entretenu. Dans l'alignement de l'allee nord, une fontaine complete l'ensemble. Une douce odeur de verdure emplit vos narines, l'ambiance est calme."] 


def asgard_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]
    # * : ( 34, 7)
    # * : ( 29, 13)
    # * : ( 19, 20)
    # * : (121, 21)
    # * : ( 28, 26)
    # * : (117, 32)
    # * : ( 46, 35)
    # * : ( 57, 38)
    # * : ( 82, 38)
    # * : ( 22, 39)
    # * : (  8, 44)
    # * : ( 58, 50)
    # * : ( 83, 51)
    # * : ( 32, 59)
    # * : (104, 63)
    # * : ( 46, 65)
    # * : ( 16, 71)
    # * : (138, 71)
    if coords == (34, 7):
        if "theldis" in data[0]:
            if data[0]["theldis"] == 4: return [5, 3, 7, 5, 70], "Hargduf", 10, 1, "theldis"
            elif data[0]["theldis"] == 5: return [0, "[VOUS REGARDEZ LE CADAVRE D'HARGDUF. UNE FLAQUE DE SANG NOIR S'ETEND DEJA SOUS LUI.]"]
    
    elif coords == (121, 21):
        if "daric" in data[0] and data[0]["daric"] == 10:
            stat[8] *= 7
            data[0].pop("daric")

        elif stat[8] % 7: return "daric", {
            0: [0, "J'ai besoin d'un coup de main.\n1. Je vous ecoute.\n2. Desole.", 2],
                1: [1, "Cela fait plusieurs fois deja qu'Egel, mon voisin, s'introduit dans mon jardin. Je n'arrive pas a lui faire entendre raison.\n1. Qu'attendez-vous de moi ?\n2. Cela ne m'interesse pas, bonne journee.", 2],
                    3: [2, "On m'a dit que le dieu de la Justice pouvait m'aider, mais il ne m'ecoutera jamais. Tu peux interceder en ma faveur ?"],
                    4: [-4, "Dans ce cas..."],
                2: [-2, "Cela ne fait rien."],
            5: [0, "Alors ?"],
            6: [0, "Alors ?"],
            8: [-2, "Ah ! Mais quel...! Bon, voici 12 pieces d'or, cela devrait suffire.", 0, (1, 12)],
            9: [1, "Je savais que je pouvais compter sur toi ! [+15 PO]", 0, (1, 15)],
        }

        else: return [0, "Daric, je peux vous aider ?"]

    elif coords == (117, 32):
        if "theldis" in data[0] and data[0]["theldis"] == 7:
            stat[8] *= 11
            data[0].pop("theldis")

        elif stat[8] % 11: return "theldis", {
            "base": [0, "Bonjour, je suis Theldis."],
            0: [0, "C'est un peu delicat... J'ai un different avec quelqu'un qui m'a fait une offense. Depuis je prie Vidar de me venir en aide, mais il ne semble pas tres concerne. Tu peux aller le voir pour moi ?\n1. Euh, non ?\n2. Je vais voir ce que je peux faire.", 2],
                1: [-1, "Je pense que tu devrais prier aussi. Pour que Vidar continue ne pas m'entendre !"],
                2: [1, "Ooh, merci beaucoup ! On peut le trouver autour de Landvidi"],
            3: [0, "Alors ?, Tu as reussi a le convaincre ?"],

            6: [1, "Je savais que je pouvais te faire confiance. Je n'ai pas beaucoup d'argent a te donner [+5 PO], mais si cela peut t'aider : Niflheim a une magicienne tres puissante qui vend des sorts.", 0, (1, 5)]
        }


# Forseti
def h_9_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]
    
    if coords == (19, 4):
        if "daric" in data[0]: return "daric", {
            "base": [0, "Forseti, fils de Baldr et Nanna, dieu de la Justice. Tu as besoin de moi ?"],
            5: [0, "Oui, je suis bien Forseti, dieu de la Justice. Hum, je conscent a aider Daric. Mais en echange, je prend une commission de 10 pieces d'or.\n1. Marche conclu ! [-10 PO]\n2. Hors de question", 2],
                6: [3, "Tu peux aller dire a Daric que je m'occupe de son cas. [-10 PO]", 0, (1, -10)],
                7: [1, "Reviens quand tu auras l'argent."],
        }

        else: return [0, "Forseti, fils de Baldr et Nanna, dieu de la Justice. Tu as besoin de moi ?"]


# Odin
def h_10_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]
    
    if coords == (25, 11):
        if data[0]["main"] == 0:
            stat[3][0] = 1
            return [1, "Je suis Odin, Roi des Ases. Actuellement nous avons quelques differents avec les Vanes. Vous irez donc porter cette dague a Freyja, a Vanaheim. Elle comprendra. [ODIN VOUS DONNE UNE DAGUE]"]

        else: return {
            "base": [0, "Je suis Odin, Roi des Ases, dieux de la Guerre."],
            1: [0, "Deja revenu !?"],
            3: [1, "Bon travail. Tu peux garder la dague, une guerre se prepare, ce serait bete de mourrir deux fois quand meme ? [UN SOURIRE PASSA SUR LES LEVRES D'ODIN] Jadis Freyja m'enseigna la magie et l'astrologie. [ODIN SE FIT PENSIF. IL SE RETROURNA VERS VOUS BRUTALEMENT] Je te ferais savoir mes instructions en temps voulu. Je crois qu'il te reste quelques mondes a decouvrir."],
            4: [3, "Deja revenu ?\n1. Euh, non, pas encore.\n2. Oui !", 2],
                8: [-4, "Reviens quand tu peux, j'ai quelques missions pour toi."],

            9: [0, "Bien. Les Vanes ont refuse ma treve, je vais frapper ! Et pour cela j'ai besoin de toi.\n1. Certainement pas !\n2. J'en suis.", 2],
                10: [-1, "[LE REGARD D'ODIN CHANGEA. VOUS FAITES UN PAS EN ARRIERE, MAIS IL EST TROP TARD : ODIN SE JETTE SUR VOUS ET VOUS DEPECE A MAINS NUES.]", 0, (0, -stat[0] * 2)],
                11: [0, "{}, tu vas trouver Gullveig, et tu vas la tuer.\n1. Pourquoi faire ?\n2. Je pars sur-le-champ.".format(stat[5]), 2],
                    12: [2, "Gullveig est une magicienne creee par les Vanes pour semer la decadence parmi nos rangs. Elle distille son poison dans les veines de mes guerriers, c'est une epine dans notre pied. Trouve-la, ou qu'elle se cache, et debarasse-nous de cette maudite creature."],
                    13: [1, "C'est ce que je voulais entendre."],
                14: [0, "Mes espions m'ont indique sa presence vers Jotunheim"],

            15: [12, "Morte !? Je ne te crois pas, mes informateurs l'ont vue, et elle va tres bien ! Mais cela ne fait rien : c'est symbolique. Je veux frapper les Vanes et maintenant ils veulent un tribut pour Gullveig. J'ai besoin de m'entretenir avec les Ases. Avant que tu ne partes, rejoint Lithy, tu la trouveras au sud du Palais de Midgard. Elle t'expliquera la suite."],
            27: [0, "{}, ta position entre Ases et Vanes derange, il faut que tu choisisse un camp.".format(stat[5])],

            31: [0, "[A VOTRE ENTREE ODIN SE RETOURNA BRUTALEMENT] Ah ! {} ! Tu as fait le bon choix !\n1. Hum, je n'ai pas encore accepte.\n2. Je suis des votres !".format(stat[5]), 2],
                32: [-1, "Decide-toi vite ! Cette guerre ne t'attendra pas..."],
                33: [2, "Ca, c'est un choix strategique ! [ODIN SAISIT SA LONGUE LANCE ET LA JETA EN L'AIR. LE TRAIT DE FEU TRAVERSA LE CIEL EN DIRECTION DE VANAHEIM, SEMANT LA GUERRE DANS SON SILLAGE.]\nMaintenant que la guerre est declaree, tu es requisitionne ! Reviens me voir quand tu seras pret a commencer."],

            35: [0, "Va querrir la deesse de la mort, Hel. Tu la trouveras dans dans son palais, a Niflheim. Annonce-lui qu'une guerre se prepare."],
            37: [2, "Ainsi, Hel s'occupe de preparer les soldats du Valhalla ? Nous allons ecraser les Vanes... Va espionner du cote du Folkvangr, reviens me voir quand tu auras des informations."],
            39: [0, "Alors, des nouvelles ?"],

            47: [0, "Alors, des nouvelles ?\n1. Les guerriers du Folkvangr sont mobilises en vue d'un assault.", 1],
                48: [0, "Quel assault ?\n1. Je n'ai pas pu le savoir.", 1],
                49: [2, "Cela ne fait rien, nous attaquerons les premiers ! Rejoint nos troupes stationne au Manoir de Midgard, au sud. J'enverrais Skirnir vous porter votre ordre de mission. Va d'abord trouver Irob, le mot de passe est 'Essa'."],
                51: [0, "Aller, va !"],

            65: [0, "Enfin ! [ODIN VOUS LANCA UN REGARD FURIEUX] Pourquoi avez-vous attaquez Svartalfheim ??\n1. C'etait vos ordres.", 1],
                66: [0, "Mais non ! Je vous ai demande d'attaquer Muspellheim ! [ODIN S'ARRETA BRUTALEMENT DE HURLER.] Rhaa Skirnir ! Il modifie le contenu des messages.\n1. Vous voulez que le l'elimine ?\n2. Qu'attendez-vous de moi ?", 2],
                67: [2, "Hum... Non, il doit etre loin a present. Va plutot porter ce message a Muspellheim. Nos troupes occupent le palais au sud. Avant que tu ne partes, prend ces pieces. [+20 PO]", 0, (1, 20)],
                68: [1, "Puisque nous n'avons plus de messager, tu remplira ce role. Va porter ce message a Muspellheim. Nos troupes occupent le palais au sud. Avant que tu ne partes, prend ces pieces [+20 PO]", 0, (1, 20)],
            69: [0, "Il faut transite par Nidavellir. Bonne route."],

            73: [0, "Bon travail : Muspellheim est nettoye, je n'y ai laisse qu'une garnison reduite, le gros de nos troupes etant repliee ici.\n1. Allons-nous attaquer Vanaheim ?\n2. Peut-etre devrions proposer une treve, cette guerre n'a pas de sens.", 2],
                74: [9, "Hum, j'hesite... [UN MESSAGER ENTRA DANS LA GRANDE SALLE DU VALASKJALF ET TENDIT UN PARCHEMIN SELLE A ODIN QUI LUI ARRACHA LA MISSIVE DES MAINS] Aha ! Nous en parlions : les Vanes proposent une treve. Elle me donne rendez-vous entre les colonnes du palais de Midgard. On s'y retrouve."],
                75: [6, "Aucune guerre n'a de sens. Celle-ci pas plus qu'une autre... Tu as raison, proposons une treve. [ODIN GRIFONNA QUELQUES MOTS SUR UN VELIN ET VOUS TENDIT LE PLI.] Portez cela a Freyja. Si elle accepte on se retrouve directement sous les colonnes du palais de Midgard."],

            85: [17, "Bien, Freyja a juge l'echange d'otage inegal, je l'ai vu dans ses yeux. Je m'attend au pire... [UN MESSAGER ENTRA DANS LA SALLE, PORTANT A BOUT DE BRAS LA TETE DE MIMIR. IL SE PROSTERNA DEVANT ODIN ET RECULA. ODIN S'ADRESSA AU MESSAGER] Les conseils de Mimir ne vous auront pas servi tres longtemps... [ODIN PRIT LA TETE DANS SES MAINS, UNE INTENSE LUMIERE LES PARCOURUS ET LORSQUE LA LUMINOSITE REVIENT A UN NIVEAU SOUTENABLE, LA TETE AVAIT RETROUVE LA VIE.]"],

            90: [0, "Tient donc ! Cela fait longtemps que je n'avais pas vu ta face, traitre !\n1. Freyja m'a demande de vous transmettre ce message.\n2. Espece de vieux barbu borgne !", 2],
                91: [3, "[ODIN VOUS ARRACHA LE PARCHEMIN DES DOIGTS.] Ah ! Une treve ? Hum. Soit. [ODIN SE RETOURNA BRUTALEMENT VERS VOUS] Tu es encore la !? Hors de ma vue !"],
                92: [-2, "Que croyais-tu ? [ODIN S'AVANCE VERS VOUS CALMEMENT.] C'est moi qui t'ai redonne la vie... Et je peux la reprendre. [UN FROID IMMENSE EMPLIT VOTRE POITRINE, VOUS NE PARVENEZ PLUS A RESPIRER, VOUS VOUS EFFONDREZ, FACE CONTRE TERRE, MORT.]", 0, (0, -(2 * stat[0]))],
            
            100: [2, "[VOUS TENDEZ LA TETE A ODIN.] Les conseils de Mimir ne vous auront pas servi tres longtemps... [ODIN PRIT LA TETE DANS SES MAINS, UNE INTENSE LUMIERE LES PARCOURUS ET LORSQUE LA LUMINOSITE REVIENT A UN NIVEAU SOUTENABLE, LA TETE AVAIT RETROUVE LA VIE.]"]
        }


def h_11_npc(data, stat, entites, identifiant):
    pass


def h_12_npc(data, stat, entites, identifiant):
    pass


# Folkvangr
def h_13_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if coords == (21, 8): return {
        "base": [0, "Bienvenue au Folkvangr, la demeure des soldats de Freyja."],
        39: [0, "Que veux-tu l'ami ?\n1. Vous parler.\n2. Des informations sur vos mouvements de troupes.", 2],
            40: [1, "Soit, mais vite, je suis presse.\n1. Des ennuis ?\n2. Je serais bref.", 2],
            41: [-2, "Gaarrrdees ! [UNE DIZAINE DE FANTASSINS SE PLACERENT EN CERCLE AUTOUR DE VOUS, VOUS EMPOIGNERENT ET VOUS JETERENT SANS MENAGEMENT DANS UNE GEOLE HUMIDE ET SOMBRE.] Ici, les espions, nous les faisons parler... [VOUS MOURREZ SOUS LA TORTURE APRES AVOIR DONNE TOUTES LES INFORMATIONS EN VOTRE POSSESSION.]", 0, (0, - 2 * stat[0])],
        42: [3, "Pas a proprement parler, on nous a demande de rassembler nos guerriers et de les tenir pret pour un eventuel combat.\n1. Oh, dans ce cas, je ne vous derange pas plus.", 1],
        43: [0, "Je vous ecoute.\n1. Freyja m'envoie pour prendre des nouvelles des preparatifs.\n2. Je viens pour l'inspection annuelle de vos troupes.", 2],
            44: [3, "Nos troupes sont en cours de preparation, conformement aux ordres de Freyja, nous avons rassemble les guerriers, ils seront pret d'ici quelques heures."],
            45: [-6, "Bien essaye l'ami, mais il n'y a pas d'inspection de ce genre par ici. Gaarrddes ! [UNE DIZAINE DE GARDES SE JETTENT SUR VOUS, VOUS EN BLESSEZ UN, PEUT-ETRE DEUX, MAIS VOUS SUCCOMBEZ SOUS LE NOMBRE ET MOURREZ DE VOS BLESSURES.]", 0, (0, -2 * stat[0])],
        46: [1, "Bonne journee."],
    }


def h_14_npc(data, stat, entites, identifiant):
    pass


# Vidar
def h_15_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if coords == (10, 6):
        if "theldis" in data[0]: return "theldis", {
            "base": [0, "Vidar, dieu de la vengeance et du silence. Besoin de faire taire quelqu'un ?"],
            3: [1, "Hum, j'accepte de réaliser votre vengeance, mais j'ai une condition : vous devrez vous charger d'une autre vengeance. Allez dans les montagnes au nord-est, trouvez Hargduf, c'est un orc, vous ne pouvez pas le louper. Eliminez-le."],
            4: [0, "Si tu veux que justice soit faite, va tuer cet orc."],
            5: [1, "Bon travail. Je m'occupe de ton affaire des que possible."]
        }

        else: return {
            "base": [0, "Les taillis croissent\nEt l'herbe haute\nDans la foret du pays de Vidarr\nEt la, le fils intrepide\nDescendra de cheval\nPour venger son pere."],
        }

def h_16_npc(data, stat, entites, identifiant):
    pass


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
    if coords == (42, 20): return [0, "Vous vous trouvez sur le bord d'une large place verdoyante et bien entretenue. Entoure de montagnes, Vanaheim semble hors d'atteinte du temps. Quelques maisons et arbres completent le decor."]


def vanaheim_npc(data, stat, entites, identifiant):
    # * : (31; 12)
    # * : (52; 22)
    # * : (52; 30)
    # * : (45; 39)
    coords = data[2], data[3]

    if coords == (31, 12):
        if "riethas" in data[0] and data[0]["riethas"] == 7:
            stat[8] *= 5            
            data[0].pop("riethas")

        elif stat[8] % 5: return "riethas", {
            0: [0, "Je suis Riethas. Kamuel me doit de l'argent. Si tu veux bien aller le chercher, je te laisserai une part.\n1. Je m'en charge.\n2. Hum, non.", 2],
                1: [2, "Merci ! Tu le trouveras au sud de Vanaheim."],
                2: [-2, "Cela ne fait rien."],
            3: [0, "Kamuel est au sud, a la limite des montagnes."],
            6: [1, "Parfait, merci beaucoup !", 0, (1, -25)],
        }

        else: return [0, "Riethas, simple paysan. Que Nerthus vous garde !"]

    if coords == (41, 45):
        if "riethas" in data[0]:
            if data[0]["riethas"] == 5: return [20, 20, 20, 20, 100], "Kamuel", 50, 1, "riethas"
            else: return "riethas", {
                "base": [0, "Bonjour... ?"],
                3: [0, "Kamuel, que voulez-vous ?\n1. Tu dois de l'argent a Riethas.\n2. Vous tuer.", 2],
                4: [2, "Bien sur, voila. [+50 PO]", 0, (1, 50)],
            }

    if identifiant == "vanaheim_charretier":
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Jotunheim\n3. Alfheim", 3]

        else:
            destinations = ("Midgard", "Jotunheim", "Alfheim")
            dest_coords = ((3, 10, 58), (5, 11, 120), (2, 14, 68))
            for i in range(1, 4):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]                     


def h_21_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if identifiant == "vanaheim_aubergiste":
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Cher client bonjour ! Que puis-je faire pour vous ?\n1. Manger [5 PO]\n2. Boire [2 PO]\n3. Dormir [10 PO]", 3]
        else:
            event, _ = shop_interaction(data, stat, 3,
                (5, [-1, "Et un plat chaud, un ! [VOUS VOUS ASSEYEZ DEVANT UN TRANCHOIR DE PAIN ET UNE ASSIETTE DE SOUPE EPAISSE.]", 0, (0, 5), (1, -5)], [-1, "Tsst, quand on ne peut pas payer, on ne rentre pas."]),
                (2, [-2, "Et voila ! [L'AUBERGISTE PLACA DEVANT VOUS UNE CHOPE DE BIERE]", 0, (0, 2), (1, -2)], [-2, "La maison ne fait pas credit."]),
                (10, [-3, "Votre chambre est a l'etage.\n[VOUS MONTEZ A L'ETAGE ET VOUS ENDORMEZ SANS DIFFICULTES.]", 0, (0, 10), (1, -10), (4, 480)], [-3, "Allez donc voir ailleurs."]))

            return event
    
    # Utarg
    elif coords == (21, 6): return {
            "base": [0, "Uiiips ?"],
            40: [2, "Ah, enfin ! D'apres nos informateurs, Odin va d'abord attaquer Midgard, et plus precisement le manoir au sud. On se retrouve dans le parc. Bonne route, {} !".format(stat[5])],
            42: [0, "[UTARG EST DEJA EN ROUTE POUR MIDGARD.]"]
        }


def h_22_npc(data, stat, entites, identifiant):    
    if identifiant == "Freyja":
        if data[0]["main"] == 44:
            check = True
            for spell_id, spell_level in stat[7]:
                if spell_id == 2: check = False
            
            if check:
                stat[7].append((2, 2))
                return [1, "Belle victoire a Midgard, bravo ! En remerciement je vais t'apprendre le sort Givre de niveau II. [FREYJA COMMENCA A CHANTER UNE MELODIE, VOTRE VISION DEVINT FLOUE. LORSQUE VOUS REPRENEZ VOS ESPRITS, VOUS LE SORT EST GRAVE DANS VOTRE MEMOIRE.]"]
            else:
                return [1, "Belle victoire a Midgard, bravo ! Je vois que tu connais deja le sort Givre, voila la somme equivalente. [+20 PO]", 0, (1, 20)]

        if not (360 <= stat[4] <= 1200):
            return [0, "Revenez plus tard s'il vous plait : il fait nuit."]

        else: return {
            "base": [0, "Bonjour, je suis Freyja, deesse de la beaute et de l'erotisme."],
            1: [1, "Hum. [FREYJA REGARDE LA DAGUE] Odin me propose la paix... Mais cela ne se passera pas comme ca. [ELLE VOUS REND LA DAGUE]. Rendez sa dague a Odin. Avant que vous ne partiez pour Asgard, allez voir Freyr, il est dans la piece adjacente, il te renverra directement a Asgard."],

            14: [1, "Hum, merci de m'avoir prevenue. Tu peux aller dire a Odin que tu as tue Gullveig, Odin lui-meme ne peut pas la tuer [FREYJA A UN PETIT RIRE.] {}, il sera bientot temps de choisir un camp songes-y.".format(stat[5])],
            31: [0, "{} ! J'ai rarement ete aussi heureuse de te voir mon cher. Tu viens joindre tes forces a notre cause ?\n1. J'y reflechis encore.\n2. Je vous suis !".format(stat[5]), 2],
                32: [-1, "Bien, bien, mais depeche-toi !"],
                33: [1, "Voila une heureuse nouvelle !\n[FREYJA AVAIT A PEINE FINI SA PHRASE QU'UN TRAIT DE FEU TRAVERSA LE CIEL.]\nOdin nous declare la guerre ! Nous devons rassembler nos forces. Va a Jotunheim, et previent Thrym."],
            
            45: [0, "Ah, {} !\n1. Quels liens vous unissent aux Geants ?\n2. Savez-vous ou je peux trouver une bibliotheque ?".format(stat[5]), 2],
                46: [-1, "A l'origine des Vanes est Thjazi, un Geant, il enleva Idunn, une Asyne, ce qui signa le debut de nos conflits avec les Ases. Ces differents n'ont cesses de s'amplifier avec le temps, les Ases ne perdant pas une occasion de tuer un Geant. Finalement, les Geants et nous ne formons qu'une seule et meme famille, ces liens sont encore plus forts depuis que Freyr, mon frere, s'est marie avec Gerd, une Geante. Leur monde est Jotunheim, tu peux y acceder uniquement par Vanaheim."],
                47: [-2, "Hmm, je crois qu'il y en a une vers Alfheim."],

            56: [0, "Tu as trouve quelque chose ?\n1. Les runes signifient 'kvasir'.", 1],
            57: [3, "'kvasir' ? Cela ne me dit rien... Laissons cela de cote, Va voir Freyr, il te precisera ta prochaine mission."],

            74: [0, "Te voila enfin !\n1. C'est un succes.\n2. Ou en est la guerre ?", 2],
                75: [3, "Bien joue {} ! Tu as merite un peu de repos. Reviens me voir quand tu sera repose.".format(stat[5])],
                76: [-2, "Hum... Nous ne parvenons pas a sortir du statu quo. Chez les Ases comme chez nous, les troupes sont fatiguees. Ce ne sont que des rumeurs, mais une treve pourrait se profiler."],

            78: [0, "Pret a reprendre du service ?\n1. Oui !\n2. Pas encore.", 2],
                79: [11, "Parfait ! Apres avoir convoque les autres Vanes nous avons conclu qu'il faut cesser cette guerre. Tu iras donc porter ce message a Odin. [FREYJA VOUS TEND UN PARCHEMIN SELLE.]"],
                80: [-2, "Bon bon, mais ne tarde pas trop non plus."],

            81: [0, "Oh {} ! La traitrise conserve dirait-on... Que veux-tu ?\n1. Odin vous propose une treve.".format(stat[5]), 1],
                82: [1, "Une treve... Bien... J'accepte de me rendre a Midgard pour discuter."],

            94: [0, "Alors ?\n1. Odin a accepte la treve.", 1],
                95: [1, "Parfait ! Si Odin respecte ma demande, la treve se deroulera a Midgard, sous les colonnes du palais. On se retrouve la-bas."],

            98: [2, "L'echange d'otage a ete tres inegal, j'ai ordonne l'execution de Mimir pour montrer que nous ne nous laissons pas faire. [FREYJA VOUS TENDIT LA TETE DE MIMIR.] Va donc porter cela a Odin."]
        }

    elif identifiant == "Freyr":
        if (not 360 <= stat[4] <= 1200):
            return [0, "He ! Il fait nuit !"]

        if data[0]["main"] == 2:
            check = True
            for spell_id, spell_level in stat[7]:
                if spell_id == 0: check = False

            data[1] = 0
            data[2], data[3] = 126, 71
            
            if check:
                stat[7].append((0, 1))
                return [1, "Chez les Vanes, nous rendons hommage aux messagers, en guise de remerciement, je vais vous apprendre le sort de Soin [FREYR DESSINA DANS L'AIR DES RUNES VIOLETTE QUI TOURNOYERENT UN INSTANT AVANT DE S'ESTOMPER PEU A PEU.]\nEt maintenant : direction Asgard !\n[UNE LOURDE TORPEUR S'ABATTIT SUR VOUS. VOUS VOUS SENTEZ LEGER. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]"]
            else:
                return [1, "Chez les Vanes, nous rendons hommage aux messagers, voici quelques pieces d'or, faites en bon usage ! [UNE LOURDE TORPEUR S'ABATTIT SUR VOUS. VOUS VOUS SENTEZ LEGER. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]", 0, (1, 5)]
        
        if data[0]["main"] == 64:
            message = input("Parfait ! (ecrivez le message dechiffre) :\n")
            if message.lower() == "prenez muspellheim": return [2, "Ah ! Parfait, montre-moi ca ! [VOUS TENDEZ LE MESSAGE DECHIFFRE A FREYR.]"]
            else: return [-2, "Ca n'a aucun sens... cherche encore."]

        if data[0]["main"] == 66:
            data[1], data[2], data[3] = 6, 93, 8
            return [2, "Bien, j'ai modifie le contenu du message pour attire les soldats Ases dans un piege, tu vas donne ce parchemin a Skirnir qui le portera aux Ases. Tu le trouveras vers Nidavellir. [UNE TERRIBLE FATIGUE S'ABATTIT SUR VOUS, UNE SENSATION DE CHUTE ACCOMPAGNA VOTRE PERTE DE CONSCIENCE. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]"]

        else: return {
            "base": [0, "Freyr, dieu de la vie. Bienvenue a Vanaheim"],
            16: [8, "{}, il faut que nous parlions.\n1. Peut-etre plus tard ?\n2. Oui ?".format(stat[5]), 2],
                25: [-9, "Reviens me voir des que possible.."],
            26: [1, "Votre situation, entre Vanes et Ases nous derange. Je suis desole de ne pas etre plus explicite. Allez voir Lithy, elle se trouve a Midgard, vers le centre, dans l'alignement du grand palais. Elle vous expliquera la suite."],

            44: [0, "Ooh, bien joue pour Midgard ! Va donc en informer Freyja."],
            45: [0, "Ces runes doivent bien avoir une signification..."],

            60: [2, "Ah {} ! Mon messager, Skirnir, en se faisant passer pour un Ase, a intercepte un message; mais il est chiffre. [FREYR VOUS TEND UN PARCHEMIN PLIE.] Le message est : 'zmefmq kgfzmzw'. Reviens me voir quand tu auras termine.".format(stat[5])],
            62: [0, "Deja fini ?\n1. Pas encore...\n2. Oui !", 2],
                63: [-1, "Reviens me voir quand tu auras avance, le message est : 'zmefmq wpshmcvceau'."],
        }


# - - - Alfheim - - - #
def alfheim_po(coords, identifiant):
    if coords == (34, 20): return [0, "Quelques arbres au sud vous masque la vue. Au nord, l'imposant palais des Elfes et ses quatres colonnes finement travaillee s'offrent a vous. La lourde porte a deux battants en bois massif et fer forge vous fait face. Au sud est, les bruits d'un bourg en pleine activite montent a vos oreilles."]


def alfheim_npc(data, stat, entites, identifiant):
    # * : (11; 4)
    # * : (46; 6)
    # * : (23; 17)
    # * : (27; 54)
    if identifiant == "alfheim_charretier":
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Asgard\n3. Vanaheim\n4. Svartalfheim", 4]

        else:
            destinations = ("Midgard", "Asgard", "Vanaheim", "Svartalfheim")
            dest_coords = ((3, 10, 58), (0, 126, 71), (1, 28, 13), (8, 109, 66))
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)] 


def h_23_npc(data, stat, entites, identifiant):
    if identifiant == "Sagriel":
        return {
            "base": [0, "Bonjour... ?"],
            44: [0, "Je suis Sagriel, alfe claire. Je peux t'aider ?\n1. Oui, je voulais connaitre la signification de ces runes.\n2. Non, rien, excusez-moi...", 2],
                45: [1, "[VOUS TENDEZ LE CROQUIS D'UTARG À SAGRIEL] Hum, ces runes sont celles d'Odin. Il s'interesse de tres pres a cela. Je peux vous les traduire contre un service.\n1. Lequel ?\n2. Je trouverais quelqu'un d'autre.", 2],
                46: [-2, "Eh bien revenez quand vous vous serez decide alors..."],

            47: [3, "J'ai besoin d'une potion d'eternelle jeunesse, Gullveig en vend pour 10 pieces d'or. [+10 PO]", 0, (1, 10)],
            48: [-4, "A bientot alors."],

            54: [2, "Si j'en crois ce qui est note, cela veut dire : 'kvasir'."]
        }

def h_24_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "Excusez-moi, nous sommes fermes."]

    if coords == (12, 3):
        if not stat[7]: return [0, "Je ne peux pas vous faire oublier ce que vous ne connaissez pas."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Quel sort souhaitez-vous oublier ?\n" + "\n".join(["{0}. {1} {2}".format(nb + 1, spells[stat[7][nb][0]], spells_level[stat[7][nb][1] - 1]) for nb in range(len(stat[7]))]), len(stat[7])]

        else:
            for i in range(1, len(stat[7]) + 1):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    stat[7].pop(i - 1)
                    pts = (20 * stat[0]) // 100
                    return [-i, "Asseyez-vous, je vais vous faire oublier ce sort. [UN PUISSANT MAL DE TETE VOUS PRIT, LES MURS SEMBLERENT TANGUER TANDIS QUE VOTRE VUE DEVINT FLOUE. LE VERTIGE S'ESTOMPA PROGRESSIVEMENT.] Et voila ! [-{} PV]".format(pts), 0, (0, -pts)]

    if coords == (36, 12):         
        if len(stat[7]) >= 3: return [0, "Je suis desole, vous ne pouvez pas apprendre plus de trois sorts."]

        spells_sale = []
        formated_spells = ""
        while len(spells_sale) < 3:
            sp_id = randint(0, len(spells) - 1)
            sp_lvl = randint(1, len(spells_level))

            check = True
            for sp in spells_sale:
                if sp[0] == sp_id and sp[1] == sp_lvl:
                    check = False
                    break

            if check:
                spells_sale.append((sp_id, sp_lvl))
                formated_spells += "{0}. {1} {2}\n".format(len(spells_sale), spells[sp_id], spells_level[sp_lvl - 1])

        spell_choice = print_text("Diomwar, pour vous servir. Quel sort voulez-vous acheter ?\n{}".format(formated_spells), 1, 3, 0)

        if not spell_choice: return [0, "Hmm ?"]

        spell_sel = spells_sale[spell_choice - 1]
        if stat[1] < 10 * spell_sel[1]: return [0, "Vous n'avez pas les moyens, desole."]

        spell_id = -1
        for sp_id in range(len(stat[7])):
            sp = stat[7][sp_id]
            if spell_sel[0] == sp[0]:
                if spells_sel[1] <= sp[1]: return [0, "Vous connaissez deja ce sort."]
                else:
                    spell_id = sp_id
                    break

        if spell_id == -1:
            stat[7].append(spells_sale[i])
        else:
            stat[7][spell_id] = spells_sale[i]

        return [0, "[DIOMWAR OUVRIT UN LIVRE RELIE DE CUIR NOIR, ET TRACA DU DOIGT DES SIGNES CABALISTIQUES SUR LE SOL. LES RUNES BRILLERENT PUISSAMMENT AVANT DE S'ETEINDRE.]", 0, (1, -10 * spells_sel[1])]                


# - - - Midgard - - - #
def midgard_po(coords, identifiant):
    if coords == (29, 9): return [0, "Du haut des falaises, vous regardez vers le nord. La mer s'etale, infinie. Le vent porte des embruns a votre visage. 30 metres plus bas, les vagues se dechainent contre le calcaire de la roche dans un fracas assourdissant."]
    elif coords == (53, 24): return [0, "Vous regardez la clairiere autour de vous, l'endroit est agreable. Une douce chaleur traine dans l'air sec. Au dela des grands pins qui vous entourent, vous parvenez a voir quelques sommets de montagnes."]
    elif coords == (66, 45): return [0, "Les imposantes colonnes du palais de Midgard vous entourent. Un peu au sud, le bourg est actif : marchands de toutes sortent deambulent, entoures d'une population dense et bruyante."]
    elif coords == (52, 79): return [0, "Tournant le dos a l'epais mur qui delimite la propriete, vous observez le manoir. Le corps du batiment etait clairement une ancienne ferme a laquelle deux tours on ete rajoute a posteriori. L'ensemble garde un aspect massif et froid. Neanmoins, le reste de la propriete a fait l'objet d'un certain soin, en particulier le jardin en 4 parties dans lequel un vieux jardinier s'affaire."]


def midgard_npc(data, stat, entites, identifiant):
    # (67, 46)
    # (39, 49)
    # (66, 56)
    # (68, 71)
    coords = data[2], data[3]
    

    if coords == (67, 46):
        return {
            "base": [0, "Hmm ?"],
            83: [2, "[ODIN ET FREYJA S'AVANCERENT SOUS LES COLONNES DU PALAIS. MELANT LEURS SALIVES DANS LE CALICE, ILS CREERENT L'ETRE LE PLUS SAGE : KVASIR. LA TREVE SE CONCLUA SUR UN ECHANGE DE DIVINITES. LES VANES CEDERENT KVASIR, FREYR ET NJORD ALORS QUE LES ASES DONNERENT MIMIR ET HOENIR. LA TREVE TERMINEE, ODIN SE PENCHA VERS VOUS] {}, retourne a Asgard, j'ai l'impression que cette guerre n'est pas terminee.".format(stat[5])],
            96: [2, "[ODIN ET FREYJA S'AVANCERENT SOUS LES COLONNES ET CRACHERENT DANS UNE CUVE. UNE EPAISSE FUMMEE S'ELEVA DE CETTE DERNIERE ET LAISSA APPARAITRE UN CORPS EN SE DISSIPANT, 'KVASIR' DIT FREYJA EN MONTRANT LE NOUVEAU DIEU. EN GUISE D'ACCORD DE PAIX, LES ASES DONNERENT MIMIR ET HOENIR TANDIS QUE LES VANES CEDERNT NJORD, FREYR ET KVASIR. FRYEYJA SE PENCHA VERS VOUS.] {}, je te rejoint a Vanaheim.".format(stat[5])]
        }

    # Laard
    if coords == (8, 59):
        if "laard" in data[0] and data[0]["laard"] == 5:
            stat[8] *= 3
            data[0].pop("laard")

        if stat[8] % 3: return "laard", {
                "base": [0, "Laard, je suis marin de mon etat."],
                0: [0, "Laard, marin. Vous cherchez un engagement ?\n1. Hmm ? Proposez toujours ?\n2. Désolé, j'ai d'autres affaires a regler.", 2],
                    1: [2, "Voila, il y a quelques temps j'ai embarque dans un navire. Malheureusement, Njord ne nous a pas ete favorable et la tempete fut rude. La situation a bord est devenue tendue, nous nous sommes mutines. En represailles, Gardim, le capitaine, a fait passer quelques matelots par dessus bord. J'ai jure de les venger, mais je ne connais rien aux armes. Tu peux t'en charger pour moi ?"],
                    2: [-2, "Je comprends."],
                3: [0, "En clair, j'aimerais que tu elimines Gardim. La paye sera bonne."],
                4: [1, "C'est un grand service que tu m'a rendu l'ami, je ne l'oublierai pas ! [+5 PO]", 0, (1, 5)]
            }

    # Gardim / Marli
    elif coords == (94, 85):
        if "laard" in data[0]:
            if data[0]["laard"] < 3: return "laard", [0, "Gardim, capitaine du Mantree [IL DESIGNA UN DRAKKAR]"]
            elif data[0]["laard"] == 3: return [5, 2, 7, 7, 30], "Gardim", 3, 1, "laard"
            else: return "laard", [0, "[A VOS PIEDS S'ETEND LE CORPS FROID DE GARDIM.]"]
        else:
            if stat[8] % 3: return [0, "Gardim, capitaine du Mantree [IL DESIGNA UN DRAKKAR]"]
            else: return [0, "Marli, assistant de feu Gardim, je peux vous renseigner ?"]

    # Lithy
    elif coords == (66, 56):
        if data[0]["main"] == 0:
            stat[9] = 0
            return [0, "Vous cherchez quelque chose ?\n1. Oui : Asgard.\n2. Je cherche Vanaheim.\n3. Non, tout va bien.", 3]
        
        elif stat[9] == 0:
            stat[9] = -1
            if data[0]["main"] == 1:
                return [-1, "Vous devriez essayer au nord, en passant par la foret, a l'est."]
            elif data[0]["main"] == 2:
                return [-2, "Hum, vous avez regarde du cote de la petite maison tout a l'ouest ? Un bon ami a moi, Laard est souvent a cote."]
            elif data[0]["main"] == 3:
                return [-3, "Dans ce cas... Bonne journee !"]

        else: return {
            "base": [0, "Bonjour, je suis Lithy."],
            
            27: [0, "Je suis Lithy. Les morts au combat sont repartis entre les Ases et les Vanes. Tot ou tard tu devras choisir ton camp et renier l'autre.\n1. Sur quel critere les morts sont-ils repartis ?\n2. On m'a dit que je derangeais... ?", 2],
                28: [-1, "Les combattans morts lors d'attaques reviennent en general a Odin alors que ceux qui sont morts pour defendre leurs biens sont plutot l'apanage des Vanes."],
            29: [0, "Votre position vous situe entre Ases et Vanes, a la veille d'une guerre comme celle-ci, les Vanes comme les Ases redoutent les informateurs caches. Vous allez devoir afficher clairement votre camp.\n1. Je suis oblige de choisir ?\n2. Comment je peux choisir ?", 2],
                30: [-1, "Oui, ne serait-ce que parce qu'Odin n'acceptera jamais le doute : il vous fera tuer."],
                31: [0, "Allez voir Freyja ou Odin. C'est aussi simple. Et ne vous retournez pas."]
            }

    elif coords == (68, 71):
        return {
            "base": [0, "Hmm ?"],
            42: [0, "Occupez-vous de l'interieur, je me charge du parc !"],
            44: [0, "[UTARG SE RETOURNA VERS VOUS, SA DIVSION DERRIERE LUI.] Allez voir Freyja pour lui annoncer la nouvelle. Mes hommes, et moi restons ici en garnison. Avant que vous ne partiez... J'ai trouve des runes graves dans la parois. [UTARG VOUS TENDIT UN CROQUIS DES RUNES]"],
        
            51: [0, "Je suis Irob, quel est le mot de passe ?\n1. Ases.\n2. Essa\n3. Sase\n4. Sesa", 4],
                52: [-1, "Hum... [AVANT QUE N'AYEZ PU CORRIGER VOTRE ERREUR, IROB VOUS A DEJA TUE.]", 0, (0, -2 * stat[0])],
                53: [4, "C'est bien, passez."],
                54: [-3, "Vous aviez un doute ? Oui, moi aussi. [VOUS SENTEZ VOTRE TETE SE DECOLLER DU RESTE DE VOTRE CORPS.]", 0, (0, -2 * stat[0])],
                55: [-4, "C'est bien, passez. [ALORS QUE VOUS PASSIEZ A COTE DE IROB, UNE VIVE DOULEUR VOUS PRIT L'ABDOMEN, LE SANG ET LES CHAIRS SE REPANDIRENT SUR VOS MAINS ET VOTRE INCOMPREHENSION.]"],
        }

    elif identifiant == "midgard_charretier":
        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Vanaheim\n2. Asgard\n3. Nidavellir\n4. Niflheim", 4]

        else:
            destinations = ("Vanaheim", "Asgard", "Nidavellir", "Niflheim")
            dest_coords = ((1, 54, 29), (0, 126, 71), (6, 93, 8), (4, 78, 19))
            for i in range(1, 5):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]  


def h_25_npc(data, stat, entites, identifiant):
    pass


def h_26_npc(data, stat, entites, identifiant):
    # * : (17, 7)
    # * : (22, 7)
    # * : (17, 8)
    # * : (27, 8)
    coords = data[2], data[3]
    
    if identifiant == "Rosahil Green":
        if stat[4] >= 1320 or stat[4] <= 340: return [0, "Je suis desolee, nous sommes fermes. Revenez plus tard !"]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Rosahil Green, tenanciere de cette auberge. Vous desirez quelque chose ?\n1.De quoi manger s'il vous plait. [-5 PO]\n2.Je voudrais une chambre pour la nuit. [-10 PO]", 2]
        else:
            event, choice = shop_interaction(data, stat, 2,
                (5, [-1, "Et voila pour vous ! [ROSAHIL POSA UNE ASSIETTE DE RAGOUT CHAUD DEVANT VOUS.]", 0, (0, 5), (1, -5)], [-1, "Reviens quand tu auras assez de pieces d'or."]),
                (10, [-2, "Suivez-moi, je vais vous montrer votre chambre. [VOUS SUIVEZ ROSAHIL DANS L'AUBERGE, LA NUIT PASSA.]", 0, (0, 10), (1, -10), (4, 480)], [-2, "Je suis desolee, tu n'as pas assez !"]))

            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Il est trop tot, revenez vers 19h."]
            else: return event

    elif coords == (17, 7):
        if "asufaith" in data[0] and data[0]["asufaith"] == 5:
            stat[8] *= 2
            data[0].pop("asufaith")

        elif stat[8] % 2: return "asufaith", {
                0: [0, "Hey toi ! J'ai besoin de toi.\n1. Je ne crois pas, bonne journee.\n2. Je vous ecoute.", 2],
                    1: [-1, "Tu ne sais pas ce que tu rates l'ami."],
                    2: [1, "Bien. Tu vas aller au sud ouest, au fond d'un bois, il y a trois maisons. Je sais que l'une d'elle mene a Niflheim. Trouve un esprit du nom d'Asufaith et donne-lui ce mot. [L'HOMME VOUS DONNE UNE LETTRE CACHETEE D'UN SCEAU DE CIRE NOIRE.].", 0],
                3: [0, "Aller, file !"],
                4: [1, "Merci de ton aide, voila quelques pieces. [+10 PO]", 0, (1, 10)],
            }
    
    else: return [0, "Ui hips ?"]


def h_27_npc(data, stat, entites, identifiant):
    pass


def h_28_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if coords == (27, 6):
        if data[0]["main"] == 42: return [10, 10, 10, 10, 100], "Targ", 40, 2
        elif data[0]["main"] == 44: return [0, "[ENCORE SUANT DU COMBAT, VOUS REGARDEZ AVEC UNE CERTAINE SATISFACTION LE TAS DE CHAIR QUI FUT VOTRE ADVERSAIRE.]"]

        else: return {
            "base": [0, "Hmm ?"],
            57: [2, "Ah voila {} ! Skirnir vient de repartir, nous devons prendre une tour de guet de Svartalfheim. Nous passerons par Nidavellir. On se retrouve au pied de la tour.".format(stat[5])]
        }


# - - - Niflheim - - - #
def niflheim_po(coords, identifiant):
    if coords == (88, 32): return [0, "Entoure de pierre tombales, de nombreux chemins serpentent. De lourd nuages fonces entretiennent une atmosphere pesante et une brume noiratres flotte dans l'air. Dans la penombre ambiante, une haute maison se detache, masse plus sombre encore que le reste, percee de fines fenetres et encadree de deux tours."]


def niflheim_npc(data, stat, entites, identifiant):
    # * : (95, 30)
    # * : (57, 31)
    # * : (39, 60)
    # * : (108, 67)
    coords = data[2], data[3]
    

    if coords == (57, 31):
        if "asufaith" in data[0]: return "asufaith", {
            3: [1, "Asufaith, besoin de quelque chose ? [VOUS LUI DONNEZ LA LETTRE, L'ESPRIT VOUS REGARDA SANS PARAITRE ETONNE ET S'EN EMPARA.] Notre... Ami commun vous envoie de loin. [SUR CES MOTS L'ESPRIT SE RETOURNA ET TRAVERSA LE SOL DE TERRE, VOUS LAISSANT DESEMPARE.]"],
            4: [0, "[VOUS REGARDEZ LE SOL SANS COMPRENDRE.]"],
        }


def h_29_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    n = len(spells)
    spells_sale = [(i, len(spells_level)) for i in range(n)]
    formated_spells = ""
    for sp in range(n):
        formated_spells += "{0}. {1} {2}\n".format(sp + 1, spells[spells_sale[sp][0]], spells_level[spells_sale[sp][1] - 1])

    if not (480 <= stat[4] <= 1140): return [0, "Je suis desolee, nous sommes fermes."]

    if coords == (5, 5):
        if len(stat[7]) >= 3: return [0, "Vous ne pouvez pas apprendre plus de sort, et je ne pratique pas les sorts d'oubli. Je crois qu'une librairie vers Alfheim le fait gratuitement."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Merath, je vend les sorts les plus puissants de tout l'Yggdrasil ! Quel sort voulez-vous ?\n{}".format(formated_spells), n]

        else:
            for i in range(1, n + 1):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 50: return [-i, "Vous n'avez pas les moyens, desolee."]

                    spell_id = -1
                    for sp_id in range(len(stat[7])):
                        sp = stat[7][sp_id]
                        if spells_sale[i - 1][0] == sp[0]:
                            if spells_sale[i - 1][1] <= sp[1]: return [-i, "Vous connaissez deja ce sort."]
                            else:
                                spell_id = sp_id
                                break

                    if spell_id == -1:
                        stat[7].append(spells_sale[i - 1])
                    else:
                        stat[7][spell_id] = spells_sale[i - 1]

                    return [-i, "[MERATH SE RETOURNA ET S'EMPARA D'UN GRIMOIRE. ELLE L'OUVRIT ET LUT A HAUTE VOIX. UNE LOURDE TORPEUR S'ABBATIT SUR VOUS. QUAND VOUS REPRENEZ PLEINEMENT CONSCIENCE, LE SORT EST GRAVE DANS VOTRE MEMOIRE.]", 0, (1, -50)]


def h_30_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    # Hel
    if identifiant == "Hel": return {
        "base": [0, "Hel, deesse de la mort, tu veux quelque chose ?"],

        35: [2, "Une guerre contre les Vanes ? Les guerriers du Valhalla vont enfin sortir affronter ceux du Folkvangr. Je m'occupe du Valhalla, retourne voir Odin. Voici quelques pieces pour ta commission. [+10 PO]", 0, (1, 10)],
    }


# - - - Jotunheim - - - #
def jotunheim_po(coords, identifiant):
    if coords == (60, 57): return [0, "Un bruit de fontaine monte a vos oreilles. A travers les arbres, l'immense palais de Thrym se dresse. Les enormes colonnes qui entourent le batiments sont a elles seules des symboles de demesures. Aux alentours se dresse quelques maisons tout aussi imposantes et enorme, mais moins travaillee."]
    elif coords == (23, 70): return [0, "Face a la mer, sur une langue de terre, le phare se dresse, eclairant puissemment le large pour signaler l'estuaire."]
    elif coords == (60, 86): return [0, "Un imposant manoir se tient devant vous, flanque de deux tours surmontees de domes en ardoise brillantes, l'ensemble est perce de multiples et larges ouvertures. Le parc autour se compose de quelques arbres et est delimite au nord par le fleuve."]


def jotunheim_npc(data, stat, entites, identifiant):
    # * : (25; 10)
    # * : (39; 20)
    # * : (3; 28)
    # * : (34; 45)
    # * : (53; 49)
    # * : (19; 51)
    # * : (34; 56)
    # * : (64; 64)
    # * : (54; 70)
    # * : (8; 72)
    # * : (40; 75)
    # * : (72; 87)
    # * : (6; 98)
    coords = data[2], data[3]

    if identifiant == "Utarg": return {
        "base": [0, "Utarg, pour vous servir."],
        36: [0, "Utarg, vous me cherchiez ?\n1. Oui, Thrym m'a demande de vous donner ceci [VOUS LUI DONNEZ LA LETTRE].\n2. Quelles sont les relations entre les Geants et les Ases ?", 2],
            37: [3, "[UTARG LIT LE BILLET.] Hum. Thrym me demande de detacher une garnison et de me rendre a Vanaheim. On se retrouve a l'auberge, au nord de Vanaheim."],
            38: [-2, "Plusieurs differents ont eloignes les Ases des Geants : meutres, enlevements, traitrises... Ce serait long a expliquer."]
    }


def h_31_npc(data, stat, entites, identifiant):
    pass


def h_32_npc(data, stat, entites, identifiant):
    pass


def h_33_npc(data, stat, entites, identifiant):
    pass


def h_34_npc(data, stat, entites, identifiant):
    if identifiant == "Thrym":
        if not (360 <= stat[4] <= 1200):
            return [0, "Reviens quand il fera jour s'il te plait."]
        else: return {
            "base": [0, "Thyrm, roi des Geants. Bienvenue a Utgard."],
            34: [0, "Bonjour, je suis Thyrm, bienvenue a Utgard.\n1. Freyja m'a charge de vous dire qu'Odin a declare la guerre aux Vanes.", 1],
            35: [1, "De part le mariage entre Gerd et Freyr, nos liens avec les Vanes sont forts. Par respect pour eux et en souvenir de notre histoire mouvemente avec les Ases, j'accepte d'aider Freyja et les siens. [THRYM SAISIT UNE LETTRE ET GRIFONNA QUELQUES MOTS AVANT DE VOUS LA TENDRE.] En sortant dirige-toi vers Westri, vers la jetee, tu trouveras Utarg. Donne-lui ce mot."]
        }


def h_35_npc(data, stat, entites, identifiant):
    if identifiant == "Gullveig":
        if data[0]["main"] == 14: return [8, 8, 5, 5, 80], "Gullveig", 15, 1
        elif data[0]["main"] == 15: return [0, "[VOUS REGARDEZ LA DEPOUILLE DESARTICULEE DE LA MAGICIENNE, ODIN SERA CONTENT.]"]
        else: return {
                "base": [0, "Gullveig, magicienne Vane, pour te servir."],
                44: [0, "Gullveig, magicienne Vane, besoin de quelque chose ?\n1. Pouvez-vous dechiffre ces runes pour moi ?\n2. Non, excusez-moi.", 2],
                    45: [11, "Bien sur. [GULLVEIG REGARDA LE CROQUIS DES RUNES] Hum... je ne suis pas sure de ce que cela veut dire, si je traduit dans notre alphabet cela donne 'kvasir'."],
                    46: [-2, "Reviens quand tu veux !"],
                50: [0, "Ah {} ! Besoin de quelque chose ?\n1.C'est Sagriel qui m'envoie, elle a besoin d'une potion d'eternelle jeunesse.\n2. Non, rien, merci.".format(stat[5]), 2],
                    51: [3, "Oui, bien sur ! [GULLVEIG VOUS TEND UNE FIOLE REMPLIE D'UN LIQUIDE AMBRE.]", 0, (1, -10)],
                    52: [-2, "Reviens quand tu veux !"],
            }


def h_36_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]
    
    if identifiant == "jotunheim_aubergiste":
        if not (300 <= stat[4] <= 1380): return [0, "Je suis desole, nous somme ferme la nuit."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Vous voulez quelque-chose ?\n1. Je mangerai bien un truc [-4 PO]\n2. Il vous reste une chambre ? [-12 PO]", 2]

        else:
            event, choice = shop_interaction(data, stat, 2,
                (4, [-1, "Et voila ! [LE TAVERNIER POSA UNE ASSIETTE FUMANTE DEVANT VOUS ET UN VERRE DE VIN]", 0, (0, 5), (1, -4)], [-1, "Reviens quand tu auras de quoi me payer."]),
                (12, [-2, "Oui, au premier etage, au bout du couloir sur votre droite. [VOUS SUIVEZ LES INDICATIONS DU TAVERNIER ET TROUVEZ VOTRE CHAMBRE. VOUS SOMBREZ DANS LES BRAS DE NOTT.]", 0, (0, 15), (1, -12), (4, 480)], [-2, "Tu n'as pas assez."]))
        
            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Il est trop tot, reviens vers 19h."]
            else: return event


# - - - Nidavellir - - - #
def nidavellir_po(coords, identifiant):
    if coords == (65, 7): return [0, "La mer etendait ses rouleaux sur le sable noir. Au sud s'etend le rocheux royaume de Nidavellir. Le monde des nains a pour seul maison les montagnes. D'ancienne legendes racontent que certaines communiquent entre elles par des passages oublies."]
    elif coords == (66, 58): return [0, "Coupee en deux par le fleuve, la chaine de montagne semble s'etendre a l'infini. De toute part le meme paysage rocailleux. Le terrain est si inhospitalier que les nains eux-meme restent dans leurs mines."]


def nidavellir_npc(data, stat, entites, identifiant):
    # * : (49, 21)
    # * : (25, 31)
    # * : (74, 46)
    # * : (16, 55)
    # * : (77, 61)
    coords = data[2], data[3]

    if coords == (25, 31):
        return {
            "base": [0, "Skirnir, messager de mon etat."],
            68: [0, "Skirnir, messager de Freyr...\n1. J'ai un message pour vous", 1],
            69: [1, "[VOUS TENDEZ LE PARCHEMIN MODIFIE A SKIRNIR] Je vais de ce pas transmettre ce message aux Ases. Nous allons attirer les Ases dans un piege dans une tour de guet de Svartalfheim. Il ne doit pas y avoir beaucoup de soldats Ases present. Tu rendras directement compte a Freyja. Avant que tu ne partes, achetes-toi un equimement digne de ce nom. [+30 PO]", 0, (1, 30)],
        }


def h_37_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if identifiant == "Muin":
        if not (340 <= stat[4] <= 1380): return [0, "Nous sommes ouverts de 5 heures a 23."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bonjour, Muin pour vous servir.\n1. Bonjour je voudrais manger. [-5 PO]\n2. Vous reste-t-il des chambres ? [-15 PO]\n3. A boire ! [-3 PO]", 3]

        else:
            event, choice = shop_interaction(data, stat, 3,
                (5, [-1, "Pas de probleme ! [MUIN REVINT QUELQUES MINUTES PLUS TARD, ET POSA UNE ASSIETTE FUMANTE DEVANT VOUS.]", 0, (0, 5), (1, -5)], [-1, "Hey la ! Reviens quand tu pourras me payer."]),
                (15, [-2, "Bien sur ! Suivez-moi. [VOUS SUIVEZ MUIN DANS UNE PIECE TROGLODYTE MUNIE D'UN LIT ET D'UN COFFRE. VOUS VOUS ENDORMEZ RAPIDEMENT.]", 0, (0, 15), (1, -15), (4, 480)], [-2, "Desole, je n'ai plus une seule chambre de libre."]),
                (3, [-3, "[MUIN POSA UNE CHOPPE DE BIERE MOUSSEUSE DEVANT VOUS.]", 0, (0, 3), (1, -3)], [-3, "Allez donc voir un autre etablissement, nous ne servons pas gratuitement."]))
            
            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Une chambre !? Il n'est que {} heures. Reviens dans la soiree.".format(stat[4] // 60)]
            else: return event

    return [0, "Hmm ?"]


def h_38_npc(data, stat, entites, identifiant):
    pass


def h_39_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "La forge de Nidavellir est ouverte de 8 heures a 18 heures."]

    if coords == (9, 2):
        if stat[3][0]: return [0, "Vous avez deja une arme. Allez voir mon confrere si vous voulez la vendre et revenez me voir."]

        weapons_sale = []
        formated_wpn = ""
        while len(weapons_sale) < 4:
            wpn = randint(1, len(weapons) - 1)
            if not wpn in weapons_sale:
                weapons_sale.append(wpn)
                formated_wpn += "{0}. {1} [-{2} PO]\n".format(len(weapons_sale), weapons[wpn], 10 * wpn)

        wpn_choice = print_text("Bienvenue a la forge de Nidavellir ! Vous desirez une piece particulière ?\n{}".format(formated_wpn), 1, 4, 0)
        if not wpn_choice: return [0, "Hmm ?"]
    
        wpn = weapons_sale[wpn_choice - 1]
        if stat[1] < 10 * wpn: return [0, "Vous n'avez pas assez."]
        stat[3][0] = wpn
        return [0, "Tres bon choix ! [LE NAIN DECROCHA L'ARME DU RATELIER ET VOUS LA TENDIT.]", 0, (1, -10 * wpn)]

    if coords == (9, 4):
        if stat[3][0] == 0: return [0, "Vous n'avez pas d'arme a me vendre. Allez voir mon collegue pour en acheter une."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bienvenue dans notre forge. Vous souhaitez me vendre votre arme ?\n1. Oui\n2. Non", 2]

        elif data[0]["main"] == stat[9] + 1:
            stat[9] = -1
            cost = stat[3][0] * 8
            stat[3][0] = 0
            return [-1, "Marche conclu ! [+{} PO]".format(cost), 0, (1, cost)]

        elif data[0]["main"] == stat[9] + 2:
            stat[9] = -1
            return [-2, "A votre guise, revenez quand vous voulez !"]


def h_40_npc(data, stat, entites, identifiant):
    pass


def h_41_npc(data, stat, entites, identifiant):
    pass


# - - - Muspellheim - - - #
def muspellheim_po(coords, identifiant):
    if coords == (66, 8): return [0, "La mer s'etendait, calme. Bosquets et maisons peuplaient la cote. Quelques petites tentes pointues ponctuaient le tout, bravant la brise marine par une fine enveloppe de cuir tanne."]
    elif coords == (64, 97): return [0, "La cloture de la propriete etait ouvragee, le manoir aussi. Constitue d'un corps de ferme rehabilite et entoure de deux tours decoratives, l'ensemble conservait un air propre et entretenu. Le jardin taille en temoigne."]


def muspellheim_npc(data, stat, entites, identifiant):
    # * : (20, 12)
    # * : (78, 14)
    # * : (54, 80)
    # * : (59, 91)
    # * : (39, 94)
    # * : (29, 113)
    
    coords = data[2], data[3]

    if coords == (39, 94):
        if data[0]["main"] == 71: return [15, 20, 20, 15, 100], "Soldat Vane", 20, 2


def h_42_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if identifiant == "muspellheim_aubergiste":
        if not (300 <= stat[4] <= 1380): return [0, "Nous sommes ouverts de 5 a 23 heures."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Besoin de quelque chose messire ?\n1. Hum, oui, j'aimerais manger. [-5 PO]\n2. Je voudrais dormir [-10 PO]", 2]

        else:
            event, _ = shop_interaction(data, stat, 2, 
                (5, [-1, "Et voila pour vous !", 0, (0, 5), (1, -5)], [-1, "Je regrette, vous n'avez pas assez."]),
                (10, [-2, "Bien sur, si vous voulez bien me suivre. [VOUS VOUS ALLONGEZ SUR LE LIT ET VOUS ENDORMEZ RAPIDEMENT.]", 0, (0, 10), (1, -10), (4, 480)], [-2, "Nous ne pouvons pas nous permettre de faire credit."]))
        
            return event

def h_43_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "L'armurerie est ouverte de 8 heures a 18 heures."]

    if identifiant == "Bertfrid":
        if stat[3][1]: return [0, "Vous portez deja une armure, allez voir mon confrere."]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Bienvenue, dans mon armurerie ! Je suis Bertfrid, besoin d'une armure ?\n1. Oui, d'une rondache. [-10 PO]\n2. d'un pavois [-20 PO]\n3. d'une cotte de mailles [-30 PO]\n4. d'une broigne [-40 PO]\n5. d'un harnois [-50 PO]", 5]

        else:
            shields = ("UNE RONDACHE", "UN PAVOIS", "UNE COTTE DE MAILLES", "UNE BROIGNE", "UN HARNOIS")
            for i in range(1, 6):
                if data[0]["main"] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < i * 10: return [-i, "Vous n'avez pas assez."]
                    stat[3][1] = i
                    return [-i, "C'est un bon achat. [BERTFRID DECROCHA {}]".format(shields[i - 1]), 0, (1, -i * 10)]

    elif coords == (13, 9):
        if stat[3][1] == 0: return [0, "J'achete, je ne vend pas ! Allez voir Bertfrid du cote du four a metaux, elle vous renseignera"]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Vous voulez vendre votre piece d'armure ?\n1. Oui\n2. Non", 2]

        elif data[0]["main"] == stat[9] + 1:
            stat[9] = -1
            cost = stat[3][1] * 8
            return [-1, "C'est une affaire ! [+{} PO]".format(cost), 0, (1, cost)]

        elif data[0]["main"] == stat[9] + 2:
            stat[9] = -1
            return [-2, "Revenez quand vous voulez !"]

    elif coords == (6, 5):
        return [0, "Je ne suis qu'apprenti monseigneur. Adressez-vous plutot a Bertfrid. Vous la trouverez pres du four."]


def h_44_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if coords == (13, 20): return {
        "base": [0, "Frealas, capitaine d'Odin."],
        69: [0, "Frealas, capitaine d'Odin.\n1. J'ai un message de sa part.", 1],
            70: [1, "[VOUS TENDEZ LE PLIS A FREALAS] Hum... Odin nous demande de reduire les derniers Vanes present avant de nous replier. Les rapports indiquent la presence de deux ou trois groupuscules. Vous vous chargerez de celui situe a Westri, dans le village. Retournez directement voir Odin quand vous aurez termine."],
    }


# - - - Svartalfheim - - - #
def svartalfheim_po(coords, identifiant):
    if coords == (113, 37): return [0, "Des tours de guets parsement la cote, plus loin, a l'ouest, une chaine de petites montagnes s'etend, coupant Svartalfheim en deux. Mais la partie est du monde est plus habitee et plus animee que la partie ouest qui reste majoritairement consitituee de denses forets."]


def svartalfheim_npc(data, stat, entites, identifiant):
    # * : (10; 24)
    # * : (105; 46)
    # * : (22; 50)
    # * : (15; 54)
    # * : (25; 61)
    # * : (121; 68)
    coords = data[2], data[3]

    if coords == (120, 49) or coords == (104, 30):
        if not (360 <= stat[4] <= 1200): return [0, "Hmm, hein ? Quoi ? Zavez pas vu l'heure ??"]

        if stat[9] == -1 or data[0]["main"] == stat[9]:
            stat[9] = data[0]["main"]
            return [0, "Hey, toi ! Tu veux traverser ?\n1. Traverser [2 PO]\n2. Ne pas traverser", 2]
        
        elif data[0]["main"] == stat[9] + 1:
            stat[9] = -1
            if stat[1] < 2: return [-1, "Reviens quand tu auras de quoi me payer."]
            
            if coords == (104, 30): data[2], data[3] = 119, 49
            else: data[2], data[3] = 103, 30
            
            return [-1, "C'est parti !", 0, (1, -2)]

        elif data[0]["main"] == stat[9] + 2:
            stat[9] = -1
            return [0, "Reviens quand tu voudras traverser."]

    elif coords == (10, 24):
        if data[0]["main"] == 59:
            if stat[3][0] == 8 and stat[3][1] == 5: return [2, "Voici un peu d'argent [+20 PO]. Selon nos espions, la tour est vide ou presque. Tu rentres, tu elemines les Vanes, pendant ce temps, on surveille les alentours.", 0, (1, 20)]
            else:
                if stat[3][0] < 8: stat[3][0] += 1
                if stat[3][1] < 5: stat[3][1] += 1
                return [2, "Voici un equipement de meilleure qualite, avec ca, tu ne peux pas perdre le combat ! Selon nos espions, la tour est vide ou presque. Tu rentres, tu elemines les Vanes, pendant ce temps, on surveille les alentours."]


def h_45_npc(data, stat, entites, identifiant):
    pass


def h_46_npc(data, stat, entites, identifiant):
    coords = data[2], data[3]

    if coords == (13, 2):
        if data[0]["main"] == 61: return [12, 10, 15, 15, 100], "Soldat Vane", 10, 2
        elif data[0]["main"] == 63:
            data[1], data[2], data[3] = 27, 4, 11
            return [2, "[UN PUISSANT BRUIT DE COR RETENTI, DES SOLDATS VANES SURGISSAIENT DE PARTOUT. SUBMERGE PAR LE NOMBRE ET LES COUPS, VOUS TOMBEZ AU SOL. VOUS AVEZ LA SENTATION CONFUSE QUE L'ON VOUS PORTE. LORSQUE VOUS VOUS REPRENEZ VOS ESPRITS, VOUS ETES CHEZ VOUS, A MIDGARD, VOS MULTIPLES CONTUSIONS SONT PANSEES ET LA DOULEUR EST LARGEMENT SUPPORTABLE. LE BILLET POSE SUR VOTRE TABLE VOUS INDIQUE QU'ODIN VOUS ATTEND.]", 0, (0, -stat[0] // 2)]

        if data[0]["main"] in (70, 72): return [12, 10, 15, 15, 100], "Soldat Ase", 10, 2
        elif data[0]["main"] == 74: return [0, "[LA DEPOUILLE SANGLANTE DU SOLDAT EST AFFALLEE SUR LE BANC. UNE MARE DE SANG COAGULE DEJA A SES PIEDS.]"]

    if coords == (13, 4):
        if data[0]["main"] == 61: return [12, 10, 15, 15, 100], "Soldat Vane", 10, 2
        elif data[0]["main"] == 63:
            data[1], data[2], data[3] = 27, 4, 11
            return [2, "[UN PUISSANT BRUIT DE COR RETENTI, DES SOLDATS VANES SURGISSAIENT DE PARTOUT. SUBMERGE PAR LE NOMBRE ET LES COUPS, VOUS TOMBEZ AU SOL. VOUS AVEZ LA SENTATION CONFUSE QUE L'ON VOUS PORTE. LORSQUE VOUS VOUS REPRENEZ VOS ESPRITS, VOUS ETES CHEZ VOUS, A MIDGARD, VOS MULTIPLES CONTUSIONS SONT PANSEES ET LA DOULEUR EST LARGEMENT SUPPORTABLE. LE BILLET POSE SUR VOTRE TABLE VOUS INDIQUE QU'ODIN VOUS ATTEND.]", 0, (0, -stat[0] // 2)]

        if data[0]["main"] in (70, 72): return [12, 10, 20, 15, 100], "Soldat Ase", 10, 2
        elif data[0]["main"] == 74: return [0, "[DES MORCEAUX DE CORPS JONCHENT LE SOL ET LA TABLE.]"]


def h_47_npc(data, stat, entites, identifiant):
    pass


def h_48_npc(data, stat, entites, identifiant):
    pass
