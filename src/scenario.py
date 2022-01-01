def shop_interaction(data, stat, nb_choice, *events):
    for choice in range(nb_choice):
        if data[0] == stat[9] + choice + 1:
            stat[9] = -1
            if stat[1] < events[choice][0]: return events[choice][2], choice + 1
            else: return events[choice][1], choice + 1


# - - - Asgard - - - #
def asgard_po(coords):
    if coords == (120, 26): return [0, "De hautes montagnes vous entourent de toutes part. Taillees dans la roche enneigee, les marches de l'escalier qui mene a Valaskjalf se decoupent nettement. La grande demeure d'Odin et son toit d'argent domine les environs."]
    elif coords == (51, 55): return [0, "Tout autour de vous s'etend un riche jardin soigneusement entretenu. Dans l'alignement de l'allee nord, une fontaine complete l'ensemble. Une douce odeur de verdure emplit vos narines, l'ambiance est calme."] 


def asgard_npc(data, stat):
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
        if stat[8] == 4:
            if xp == 20: return [5, 3, 10, 12, 70], "Hargduf", 10, 1
            elif xp == 21: return [0, "[VOUS REGARDEZ LE CADAVRE D'HARGDUF. UNE FLAQUE DE SANG NOIR S'ETEND DEJA SOUS LUI.]"]
    
    elif coords == (121, 21):
        if stat[8] == 3: return {
            21: [0, "Alors ?"],
            25: [1, "Je savais que je pouvais compter sur toi ! Cela n'a rien a voir, mais j'ai entendu dire que Freyr cherche un certain {}, tu le connais ? [+15 PO]".format(stat[5]), 0, (1, 15), (8, -3)]
        }
        
        else: return {
            "base": [0, "Daric, je peux vous aider ?"],
            16: [0, "J'ai besoin d'un coup de main.\n1. Je vous ecoute.\n2. Desole.", 2],
                17: [1, "Cela fait plusieurs fois deja qu'Egel, mon voisin, s'introduit dans mon jardin. Je n'arrive pas a lui faire entendre raison.\n1. Qu'attendez-vous de moi ?\n2. Cela ne m'interesse pas, bonne journee.", 2],
                    19: [2, "On m'a dit que le dieu de la Justice pouvait m'aider, mais il ne m'ecoutera jamais. Tu peux interceder en ma faveur ?", 0, (8, 3)],
                    20: [-4, "Dans ce cas..."],
                18: [-2, "Cela ne fait rien."],
        }

    elif coords == (117, 32):
        if stat[8] == 4: return {
            22: [4, "Je savais que je pouvais te faire confiance. Je n'ai pas beaucoup d'argent a te donner, mais si cela peut t'aider : Niflheim a une magicienne tres puissante qui vend des sorts. Avant que j'oublie, Freyr te demande.", 0, (8, -4)]
        }

        else: return {
            "base": [0, "Bonjour, je suis Theldis."],
            16: [0, "C'est un peu delicat... J'ai un different avec quelqu'un qui m'a fait une offense. Depuis je prie Vidar de me venir en aide, mais il ne semble pas tres concerne. Tu peux aller le voir pour moi ?\n1. Euh, non ?\n2. Je vais voir ce que je peux faire.", 2],
                17: [-1, "Je pense que tu devrais prier aussi. Pour que Vidar continue ne pas m'entendre !"],
                18: [1, "Ooh, merci beaucoup ! On peut le trouver autour de Landvidi", 0, (8, 4)],
            19: [0, "Alors ?"],
        }


# Forseti
def h_9_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    if coords == (19, 4):
        if stat[8] == 3: return {
            "base": [0, "Forseti, fils de Baldr et Nanna, dieu de la Justice. Tu as besoin de moi ?"],
            21: [0, "Oui, je suis bien Forseti, dieu de la Justice. Hum, je conscent a aider Daric. Mais en echange, j'ai une faveur a te demander. La guerre qui couve n'est pas fondee, il faut l'empecher. Je ne te demande rien de plus.\n1. D'accord mais comment faire ?\n2. Je ferais mon possible.\n3. J'ai d'autres engagements a tenir.", 3],
                22: [-1, "Eh bien, c'est la que commence ton travail je pense."],
                23: [2, "Merci ! Tu pourras dire a Daric que je m'occupe de son affaire de suite."],
                24: [1, "Je comprends."],
        }

        else: return {
            "base": [0, "Forseti, fils de Baldr et Nanna, dieu de la Justice. Tu as besoin de moi ?"]
        }


# Odin
def h_10_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    if coords == (25, 11):
        if stat[8]:
            return [0, "Fini ce que tu as a faire."]

        if xp == 0:
            stat[3][0] = 1
            return [1, "Je suis Odin, Roi des Ases. Actuellement nous avons quelques differents avec les Vanes. Vous irez donc porter cette dague a Freyja, a Vanaheim. Elle comprendra. [ODIN VOUS DONNE UNE DAGUE]"]

        else: return {
            "base": [0, "Je suis Odin, Roi des Ases, dieux de la Guerre."],
            1: [0, "Deja revenu !?"],
            3: [1, "Bon travail. Tu peux garder la dague, une guerre se prepare, ce serait bete de mourrir deux fois quand meme ? [UN SOURIRE PASSA SUR LES LEVRES D'ODIN] Jadis Freyja m'enseigna la magie et l'astrologie. [ODIN SE FIT PENSIF. IL SE RETROURNA VERS VOUS BRUTALEMENT] Je te ferais savoir mes instructions en temps voulu. Je crois qu'il te reste quelques mondes a decouvrir."],
            4: [3, "Deja revenu ?\n1. Euh, non, pas encore.\n2. Oui !", 2],
                8: [-4, "Reviens quand tu auras fini."],

            9: [0, "Bien. Les Vanes ont refuse ma treve, je vais frapper ! Et pour cela j'ai besoin de toi.\n1. Certainement pas !\n2. J'en suis.", 2],
                10: [-1, "[LE REGARD D'ODIN CHANGEA. VOUS FAITES UN PAS EN ARRIERE, MAIS IL EST TROP TARD : ODIN SE JETTE SUR VOUS ET VOUS DEPECE A MAINS NUES.]", 0, (0, -stat[0] * 2)],
                11: [0, "{}, tu vas trouver Gullveig, et tu vas la tuer.\n1. Pourquoi faire ?\n2. Je pars sur-le-champ.".format(stat[5]), 2],
                    12: [2, "Gullveig est une magicienne creee par les Vanes pour semer la decadence parmi nos rangs. Elle distille son poison dans les veines de mes guerriers, c'est une epine dans notre pied. Trouve-la, ou qu'elle se cache, et debarasse-nous de cette maudite creature."],
                    13: [1, "C'est ce que je voulais entendre."],
                14: [0, "Mes espions m'ont indique sa presence vers Jotunheim"],

            15: [1, "Morte !? Je ne te crois pas, mes informateurs l'ont vue, et elle va tres bien ! Mais cela ne fait rien : c'est symbolique. Je veux frapper les Vanes et maintenant ils veulent un tribut pour Gullveig. J'ai besoin de m'entretenir avec les Ases. Je te donne quartier libre jusqu'a la fin de nos discussions."],

            31: [0, "[A VOTRE ENTREE ODIN SE RETOURNA BRUTALEMENT] Ah ! {} ! Tu as fait le bon choix !\n1. Hum, je n'ai pas encore accepte.\n2. Je suis des votres !".format(stat[5]), 2],
                32: [-1, "Decide-toi vite ! Cette guerre ne t'attendra pas..."],
                33: [2, "Ca, c'est un choix strategique !"],

            90: [0, "Tient donc ! Cela fait longtemps que je n'avais pas vu ta face, traitre !\n1. Freyja m'a demande de vous transmettre ce message.\n2. Espece de vieux barbu borgne !", 2],
                91: [3, "[ODIN VOUS ARRACHA LE PARCHEMIN DES DOIGTS.] Ah ! Une treve ? Hum. Soit. [ODIN SE RETOURNA BRUTALEMENT VERS VOUS] Tu es encore la !? Hors de ma vue !"],
                92: [-2, "Que croyais-tu ? [ODIN S'AVANCE VERS VOUS CALMEMENT.] C'est moi qui t'ai redonne la vie... Et je peux la reprendre. [UN FROID IMMENSE EMPLIT VOTRE POITRINE, VOUS NE PARVENEZ PLUS A RESPIRER, VOUS VOUS EFFONDREZ, FACE CONTRE TERRE, MORT.]", 0, (0, -(2 * stat[0]))],
            
            100: [2, "[VOUS TENDEZ LA TETE A ODIN.] Les conseils de Mimir ne vous auront pas servit tres longtemps... [ODIN PRIT LA TETE DANS SES MAINS, UNE INTENSE LUMIERE LES PARCOURUS ET LORSQUE LA LUMINOSITE REVIENT A UN NIVEAU SOUTENABLE, LA TETE AVAIT RETROUVE LA VIE.]"]
        }


def h_11_npc(data, stat):
    pass


def h_12_npc(data, stat):
    pass


def h_13_npc(data, stat):
    pass


def h_14_npc(data, stat):
    pass


# Vidar
def h_15_npc(data, stat):
    coords = data[2], data[3]

    if coords == (10, 6):
        if stat[8] == 4: return {
            "base": [0, "Vidar, dieu de la vengeance et du silence. Besoin de faire taire quelqu'un ?"],
            19: [1, "Hum, j'accepte de réaliser votre vengeance, mais j'ai une condition : vous devrez vous charger d'une autre vengeance. Allez dans les montagnes au nord-est, trouvez Hargduf, c'est un orc, vous ne pouvez pas le louper. Eliminez-le."],
            20: [0, "Si tu veux que justice soit faite, va tuer cet orc."],
            21: [1, "Bon travail."]
        }
        else: return {
            "base": [0, "Les taillis croissent\nEt l'herbe haute\nDans la foret du pays de Vidarr\nEt la, le fils intrepide\nDescendra de cheval\nPour venger son pere."],
        }

def h_16_npc(data, stat):
    pass


def h_17_npc(data, stat):
    pass


def h_18_npc(data, stat):
    pass


def h_19_npc(data, stat):
    pass


def h_20_npc(data, stat):
    pass


# - - - Vanaheim - - - #
def vanaheim_po(coords):
    if coords == (42, 20): return [0, "Vous vous trouvez sur le bord d'une large place verdoyante et bien entretenue. Entoure de montagnes, Vanaheim semble hors d'atteinte du temps. Quelques maisons et arbres completent le decor."]


def vanaheim_npc(data, stat):
    # * : (31; 12)
    # * : (52; 22)
    # * : (52; 30)
    # * : (45; 39)
    coords = data[2], data[3]

    # Riethas
    if coords == (31, 12):
        if stat[8] == 5: return {
            82: [0, "Kamuel est au sud, a la limite des montagnes."],
            86: [2, "Parfait, merci beaucoup !", 0, (1, -25), (8, -5)],
        }

        else: return {
                "base": [0, "Riethas, simple paysan. Que Nerthus vous garde !"],
                78: [0, "Je suis Riethas. Kamuel me doit de l'argent. Si tu veux bien aller le chercher, je te laisserai une part.\n1. Je m'en charge.\n2. Hum, non.", 2],
                    79: [3, "Merci ! Tu le trouveras au sud de Vanaheim.", 0, (8, 5)],
                    80: [-2, "Cela ne fait rien."],
            }

    # Kamuel
    if coords == (41, 45):
        if stat[8] == 5:
            if data[0] == 84: return [20, 20, 20, 20, 100], "Kamuel", 50, 2
            else: return {
                "base": [0, "Kamuel, que puis-je pour vous ?"],
                82: [0, "Kamuel, que voulez-vous ?\n1. Tu dois de l'argent a Riethas.\n2. Vous tuer.", 2],
                83: [3, "Bien sur, voila. [+50 PO]", 0, (1, 50)],
            }

    # Charrette
    if coords == (45, 39):
        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Jotunheim\n3. Alfheim", 3]

        else:
            destinations = ("Midgard", "Jotunheim", "Alfheim")
            dest_coords = ((3, 10, 58), (5, 11, 120), (2, 14, 68))
            for i in range(1, 4):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]                     


def h_21_npc(data, stat):
    coords = data[2], data[3]

    if coords == (8, 1):
        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
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
            40: [2, "Ah, enfin ! D'apres nos informateurs, Odin va d'abord attaquer Midgard, et plus precisement le manoir au sud. On se retrouve dans le parc. Bon route, {} !".format(stat[5])],
            42: [0, "[UTARG EST DEJA EN ROUTE POUR MIDGARD.]"]
        }


def h_22_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    # Freyja
    if coords == (2, 8):
        if xp == 45 and stat[8] == 0:
            stat[8] = 1

        if not (360 <= stat[4] <= 1200):
            return [0, "Revenez plus tard s'il vous plait : il fait nuit."]

        else: return {
            "base": [0, "Bonjour, je suis Freyja, deesse de la beaute et de l'erotisme."],
            1: [1, "Hum. [FREYJA REGARDE LA DAGUE] Odin me propose la paix... Mais cela ne se passera pas comme ca. [ELLE VOUS REND LA DAGUE]. Rendez sa dague a Odin. Avant que vous ne partiez pour Asgard, allez voir Freyr, il est dans la piece adjacente, il te renverra directement a Asgard."],

            14: [1, "Hum, merci de m'avoir prevenue. Tu peux aller dire a Odin que tu as tue Gullveig, Odin lui-meme ne peut pas la tuer [FREYJA A UN PETIT RIRE.] {}, il sera bientot temps de choisir un camp songes-y.".format(stat[5])],
            31: [0, "{} ! J'ai rarement ete aussi heureuse de te voir mon cher. Tu viens joindre tes forces a notre cause ?\n1. J'y reflechis encore.\n2. Je vous suis !".format(stat[5]), 2],
                32: [-1, "Bien, bien, mais depeche-toi !"],
                33: [1, "Voila une heureuse nouvelle !\n[FREYJA AVAIT A PEINE FINI SA PHRASE QU'UN TRAIT DE FEU TRAVERSA LE CIEL.]\nOdin nous declare la guerre ! Nous devons rassembler nos forces. Va a Jotunheim, et previent Thrym."],
            
            44: [0, "Ah, {} !\n1. Nous avons pris le manoir de Midgard.\n2. Quels liens vous unissent aux Geants ?\n3. Savez-vous ou je peux trouver une bibliotheque ?".format(stat[5]), 3],
                45: [-1, "Parfait ! Vois avec Freyr pour ta recompense."],
                46: [-2, "A l'origine des Vanes est Thjazi, un Geant, il enleva Idunn, une Asyne, ce qui signa le debut de nos conflits avec les Ases. Ces differents n'ont cesses de s'amplifier avec le temps, les Ases ne perdant pas une occasion de tuer un Geant. Finalement, les Geants et nous ne formons qu'une seule et meme famille, ces liens sont encore plus forts depuis que Freyr, mon frere, s'est marie avec Gerd, une Geante. Leur monde est Jotunheim, tu peux y acceder uniquement par Vanaheim."],
                47: [-3, "Hmm, je crois qu'il y en a une vers Alfheim."],

            56: [0, "Tu as trouve quelque chose ?\n1. Les runes signifient 'kvasir'.", 1, (8, -2)],
            57: [3, "'kvasir' ? Cela ne me dit rien... Laissons cela de cote, Va voir Freyr, il te precisera ta prochaine mission."],

            74: [0, "Te voila enfin !\n1. C'est un succes.\n2. Ou en est la guerre ?", 2],
                75: [3, "Bien joue {} ! Tu as merite un peu de repos. Reviens me voir quand tu sera repose.".format(stat[5])],
                76: [-2, "Hum... Nous ne parvenons pas a sortir du statu quo. Chez les Ases comme chez nous, les troupes sont fatiguees. Ce ne sont que des rumeurs, mais une treve pourrait se profiler."],

            78: [0, "Riethas cherche quelqu'un pour un service... Tu le trouveras a Vanaheim, dans la direction de Nordri."],

            88: [2, "Apres avoir convoque les autres Vanes nous avons conclu qu'il faut cesser cette guerre. Tu iras donc porter ce message a Odin. [FREYJA VOUS TEND UN PARCHEMIN SELLE.]"],

            94: [0, "Alors ?\n1. Odin a accepte la treve.", 1],
                95: [1, "Parfait ! J'ai dit a Odin treve se deroulera a Midgard, sous les colonnes du palais. On se retrouve la-bas."],

            98: [2, "L'echange d'otage a ete tres inegal, j'ai ordonne l'execution de Mimir ! [FREYJA VOUS TENDIT LA TETE DE MIMIR.] Va donc porter cela a Odin."]
        }

    # Freyr
    elif coords == (36, 3):
        if (not 360 <= stat[4] <= 1200):
            return [0, "He ! Il fait nuit !"]

        if xp == 2:
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
        
        elif xp == 44:
            if stat[8] == 0: return [0, "Va donc annoncer la nouvelle a Freyja !"]
            if stat[8] == 2: return [0, "Tsst, tu as deja eu ta recompense. Essaye plutot de comprendre ce que signifie ces runes."]
            check = True
            for spell_id, spell_level in stat[7]:
                if spell_id == 2: check = False
            
            if check:
                stat[7].append((2, 2))
                return [0, "En remerciement je vais t'apprendre le sort Givre de niveau II. [FREYR COMMENCA A CHANTER UNE MELODIE, VOTRE VISION DEVINT FLOUE. LORSQUE VOUS REPRENEZ VOS ESPRITS, VOUS LE SORT EST GRAVE DANS VOTRE MEMOIRE.]", 0, (8, 1)]
            else:
                return [0, "Je vois que tu connais deja le sort Givre, voila la somme equivalente. [+20 PO]", 0, (1, 20), (8, 1)]

        if xp == 64:
            message = input("Parfait ! (ecrivez le message dechiffre) :\n")
            if message.lower() == "prenez alfheim": return [2, "Ah ! Parfait, montre-moi ca ! [VOUS TENDEZ LE MESSAGE DECHIFFRE A FREYR.]"]
            else: return [-2, "Ca n'a aucun sens... cherche encore."]

        if xp == 66:
            data[1], data[2], data[3] = 6, 93, 8
            return [2, "Bien, j'ai modifie le contenu du message pour attire les soldats Ases dans un piege, tu vas donne ce parchemin a Skirnir qui le portera aux Ases. Tu le trouveras vers Nidavellir. [UNE TERRIBLE FATIGUE S'ABATTIT SUR VOUS, UNE SENSATION DE CHUTE ACCOMPAGNA VOTRE PERTE DE CONSCIENCE. LE DUR CHOC CONTRE LE SOL VOUS REVEILLA.]"]

        else: return {
            "base": [0, "Freyr, dieu de la vie. Bienvenue a Vanaheim"],
            16: [8, "J'aurais besoin de ton aide...\n1. Peut-etre plus tard ?\n2. Oui ?", 2],
                25: [-9, "Si tu es toujours interesse..."],
            26: [1, "Votre situation, entre Vanes et Ases nous derange. Je suis desole de ne pas etre plus explicite. Allez voir Lithy, elle se trouve a Midgard, vers le centre, dans l'alignement du grand palais. Elle vous expliquera la suite."],

            60: [2, "Ah {} ! Mon messager, Skirnir, en se faisant passer pour un Ase, a intercepte un message; mais il est chiffre. [FREYR VOUS TEND UN PARCHEMIN PLIE.] Le message est : 'zmefmq kgfzmzw'. Reviens me voir quand tu auras termine.".format(stat[5])],
            62: [0, "Deja fini ?\n1. Pas encore...\n2. Oui !", 2],
                63: [-1, "Reviens me voir quand tu auras avance, le message est : 'zmefmq kgfzmzw'."],
        }


# - - - Alfheim - - - #
def alfheim_po(coords):
    coords = data[2], data[3]
    if coords == (34, 20): return [0, "Quelques arbres au sud vous masque la vue. Au nord, l'imposant palais des Elfes et ses quatres colonnes finement travaillee s'offrent a vous. La lourde porte a deux battants en bois massif et fer forge vous fait face. Au sud est, les bruits d'un bourg en pleine activite montent a vos oreilles."]


def alfheim_npc(data, stat):
    # * : (11; 4)
    # * : (46; 6)
    # * : (23; 17)
    # * : (27; 54)
    coords = data[2], data[3]

    if coords == (23, 17):
        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Midgard\n2. Asgard\n3. Vanaheim\n4. Svartalfheim", 4]

        else:
            destinations = ("Midgard", "Asgard", "Vanaheim", "Svartalfheim")
            dest_coords = ((3, 10, 58), (0, 126, 71), (1, 28, 13), (8, 109, 66))
            for i in range(1, 5):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)] 


def h_23_npc(data, stat):
    coords = data[2], data[3]

    if coords == (23, 5):
        return {
            "base": [0, "Bonjour... ?"],
            44: [0, "Je suis Sagriel, alfe claire. Je peux t'aider ?\n1. Oui, je voulais connaitre la signification de ces runes.\n2. Non, rien, excusez-moi...", 2],
                45: [1, "[VOUS TENDEZ LE CROQUIS D'UTARG À SAGRIEL] Hum, ces runes sont celles d'Odin. Il s'interesse de tres pres a cela. Je peux vous les traduire contre un service.\n1. Lequel ?\n2. Je trouverais quelqu'un d'autre.", 2],
                46: [-2, "Eh bien revenez quand vous vous serez decide alors..."],

            47: [3, "J'ai besoin d'une potion d'eternelle jeunesse, Gullveig en vend pour 10 pieces d'or. [+10 PO]", 0, (1, 10)],
            48: [-4, "A bientot alors."],

            54: [2, "Si j'en crois ce qui est note, cela veut dire : 'kvasir'."]
        }


def h_24_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    spells = ("Soin", "Flammes", "Givre", "Etincelles", "Fatigue")
    levels = ("I", "II", "III", "IV", "V")

    if not (480 <= stat[4] <= 1140): return [0, "Excusez-moi, nous sommes fermes."]

    if coords == (12, 3):
        if not stat[7]: return [0, "Je ne peux pas vous faire oublier ce que vous ne connaissez pas."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Quel sort souhaitez-vous oublier ?\n" + "\n".join(["{0}. {1} {2}".format(nb + 1, spells[stat[7][nb][0]], levels[stat[7][nb][1] - 1]) for nb in range(len(stat[7]))]), len(stat[7])]

        else:
            for i in range(1, len(stat[7]) + 1):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    stat[7].pop(i - 1)
                    return [-i, "Asseyez-vous, je vais vous faire oublier ce sort. [UN PUISSANT MAL DE TETE VOUS PRIT, LES MURS SEMBLERENT TANGUER TANDIS QUE VOTRE VUE DEVINT FLOUE. LE VERTIGE S'ESTOMPA PROGRESSIVEMENT.] Et voila !"]

    if coords == (36, 12):
        spells_sale = ((0, 2), (1, 2), (2, 4), (4, 1))

        if len(stat[7]) >= 3: return [0, "Je suis desole, vous ne pouvez pas apprendre plus de trois sorts."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Diomwar, pour vous servir. Quel sort voulez-vous acheter ?\n1. Soin II\n2. Flammes II\n3. Givre IV\n4. Fatigue I", 4]

        else:
            for i in range(1, 5):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < spells_sale[i - 1][1] * 10: return [-i, "Vous n'avez pas les moyens, desole."]

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

                    return [-i, "[DIOMWAR OUVRIT UN LIVRE RELIE DE CUIR NOIR, ET TRACA DU DOIGT DES SIGNES CABALISTIQUES SUR LE SOL. LES RUNES BRILLERENT PUISSAMMENT AVANT DE S'ETEINDRE.]", 0, (1, -spells_sale[i - 1][1] * 10)]


# - - - Midgard - - - #
def midgard_po(coords):
    if coords == (29, 9): return [0, "Du haut des falaises, vous regardez vers le nord. La mer s'etale, infinie. Le vent porte des embruns a votre visage. 30 metres plus bas, les vagues se dechainent contre le calcaire de la roche dans un fracas assourdissant."]
    elif coords == (53, 24): return [0, "Vous regardez la clairiere autour de vous, l'endroit est agreable. Une douce chaleur traine dans l'air sec. Au dela des grands pins qui vous entourent, vous parvenez a voir quelques sommets de montagnes."]
    elif coords == (66, 45): return [0, "Les imposantes colonnes du palais de Midgard vous entourent. Un peu au sud, le bourg est actif : marchands de toutes sortent deambulent, entoures d'une population dense et bruyante."]
    elif coords == (52, 79): return [0, "Tournant le dos a l'epais mur qui delimite la propriete, vous observez le manoir. Le corps du batiment etait clairement une ancienne ferme a laquelle deux tours on ete rajoute a posteriori. L'ensemble garde un aspect massif et froid. Neanmoins, le reste de la propriete a fait l'objet d'un certain soin, en particulier le jardin en 4 parties dans lequel un vieux jardinier s'affaire."]


def midgard_npc(data, stat):
    # (67, 46)
    # (39, 49)
    # (66, 56)
    # (68, 71)
    coords = data[2], data[3]
    xp = data[0]

    if coords == (67, 46):
        return {
            "base": [0, "Hmm ?"],
            96: [2, "[ODIN ET FREYJA S'AVANCERENT SOUS LES COLONNES ET CRACHERENT DANS UNE CUVE. UNE EPAISSE FUMMEE S'ELEVA DE CETTE DERNIERE ET LAISSA APPARAITRE UN CORPS EN DISPARAISSANT, 'KVASIR' DIT FREYJA EN MONTRANT LE NOUVEAU DIEU. EN GUISE D'ACCORD DE PAIX, LES ASES DONNERENT MIMIR ET HOENIR TANDIS QUE LES VANES CEDERNT NJORD, FREYR ET KVASIR. FRYEYJA SE PENCHA VERS VOUS.] {}, je te rejoint a Vanaheim.".format(stat[5])]
        }

    # Laard
    if coords == (8, 59):
        if stat[8] == 1: return {
                7: [0, "En clair, j'aimerais que tu elimines Gardim. La paye sera bonne."],
                8: [1, "C'est un grand service que tu m'a rendu l'ami, je ne l'oublierai pas ! [+5 PO] Un courrier est passe, je crois qu'Odin requiert ta presence au plus vite.", 0, (1, 5), (8, -1)]
            }

        else: return {
                "base": [0, "Laard, je suis marin de mon etat."],
                4: [0, "Laard, marin. Vous cherchez un engagement ?\n1. Hmm ? Proposez toujours ?\n2. Désolé, j'ai d'autres affaires a regler.", 2],
                    5: [2, "Voila, il y a quelques temps j'ai embarque dans un navire. Malheureusement, Njord ne nous a pas ete favorable et la tempete fut rude. La situation a bord est devenue tendue, nous nous sommes mutines. En represailles, Gardim, le capitaine, a fait passer quelques matelots par dessus bord. J'ai jure de les venger, mais je ne connais rien aux armes. Tu peux t'en charger pour moi ?", 0, (8, 1)],
                    6: [-2, "Je comprends."],
            }

    # Gardim
    elif coords == (94, 85):
        if stat[8] == 1:
            if xp < 7: 
                return [0, "Gardim, capitaine du Mantree [IL DESIGNA UN DRAKKAR]"]
            elif xp == 7:
                return [5, 2, 7, 7, 30], "Gardim", 3, 1
            else: return {
                    "base": [0, "[A VOS PIEDS S'ETEND LE CORPS FROID DE GARDIM.]"]
                }

    elif coords == (51, 60):
        return {
                "base": [0, "Hmm ?"],
                0: [0, "Vous cherchez quelque chose ?\n1. Oui : Asgard.\n2. Je cherche Vanaheim.\n3. Non, tout va bien.", 3],
                    1: [-1, "Vous devriez essayer au nord, en passant par la foret, a l'est."],
                    2: [-2, "Hum, vous avez regarde du cote de la petite maison tout a l'ouest ? Un bon ami a moi, Laard est souvent a cote."],
                    3: [-3, "Dans ce cas... Bonne journee !"],
            }

    # Lithy
    elif coords == (66, 56):
        return {
            "base": [0, "Bonjour, je suis Lithy."],
            27: [0, "Je suis Lithy. Les morts au combat sont repartis entre les Ases et les Vanes. Tot ou tard tu devras choisir ton camp et renier l'autre.\n1. Sur quel critere les morts sont-ils repartis ?\n2. Freyr m'a dit que je derangeais... ?", 2],
                28: [-1, "Les combattans morts lors d'attaques reviennent en general a Odin alors que ceux qui sont morts pour defendre leurs biens sont plutot l'apanage des Vanes."],
            29: [0, "Votre position vous situe entre Ases et Vanes, a la veille d'une guerre comme celle-ci, les Vanes comme les Ases redoutent les informateurs caches. Vous allez devoir afficher clairement votre camp.\n1. Je suis oblige de choisir ?\n2. Comment je peux choisir ?", 2],
                30: [-1, "Oui, ne serait-ce que parce qu'Odin n'acceptera jamais le doute : il vous fera tuer."],
                31: [0, "Allez voir Freyja ou Odin. C'est aussi simple. Et ne vous retournez pas."]
        }

    elif coords == (68, 71):
        return {
            "base": [0, "Hmm ?"],
            42: [0, "Occupez-vous de l'interieur, je me charge du parc !"],
            44: [0, "[UTARG SE RETOURNA VERS VOUS, SA DIVSION DERRIERE LUI.] Allez voir Freyja pour lui annoncer la nouvelle. Mes hommes, et moi restons ici en garnison. Avant que vous ne partiez... J'ai trouve des runes graves dans la parois. [UTARG VOUS TENDIT UN CROQUIS DES RUNES]"]
        }

    # Charrette
    elif coords == (39, 49):
        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "[LE CONDUCTEUR DE LA CHARRETTE SE TOURNA VERS VOUS] Ou voulez-vous aller ? Je vous emmene pour 5 pieces.\n1. Vanaheim\n2. Asgard\n3. Nidavellir\n4. Niflheim", 4]

        else:
            destinations = ("Vanaheim", "Asgard", "Nidavellir", "Niflheim")
            dest_coords = ((1, 54, 29), (0, 126, 71), (6, 93, 8), (4, 78, 19))
            for i in range(1, 5):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 5: return [-i, "Je ne travaille pas gratuitement."]
                    else:
                        data[1], data[2], data[3] = dest_coords[i - 1][0], dest_coords[i - 1][1], dest_coords[i - 1][2]
                        return [-i, "C'est parti pour {} !".format(destinations[i - 1]), 0, (1, -5), (4, 60)]  


def h_25_npc(data, stat):
    pass


def h_26_npc(data, stat):
    # * : (17, 7)
    # * : (22, 7)
    # * : (17, 8)
    # * : (27, 8)
    coords = data[2], data[3]
    xp = data[0]

    # Rosahil Green
    if coords == (27, 6):
        if stat[4] >= 1320 or stat[4] <= 340: return [0, "Je suis desolee, nous sommes fermes. Revenez plus tard !"]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Rosahil Green, tenanciere de cette auberge. Vous desirez quelque chose ?\n1.De quoi manger s'il vous plait. [-5 PO]\n2.Je voudrais une chambre pour la nuit. [-10 PO]", 2]
        else:
            event, choice = shop_interaction(data, stat, 2,
                (5, [-1, "Et voila pour vous ! [ROSAHIL POSA UNE ASSIETTE DE RAGOUT CHAUD DEVANT VOUS.]", 0, (0, 5), (1, -5)], [-1, "Reviens quand tu auras assez de pieces d'or."]),
                (10, [-2, "Suivez-moi, je vais vous montrer votre chambre. [VOUS SUIVEZ ROSAHIL DANS L'AUBERGE, LA NUIT PASSA.]", 0, (0, 10), (1, -10), (4, 480)], [-2, "Je suis desolee, tu n'as pas assez !"]))

            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Il est trop tot, revenez vers 19h."]
            else: return event

    elif coords == (17, 7):
        if stat[8] == 2: return {
                7: [0, "Aller, file !"],
                8: [1, "Merci de ton aide, voila quelques pieces. [+10 PO], un messager est passe, Odin te demande.", 0, (1, 10), (8, -2)],
            }

        else: return {
                "base": [0, "Ui hips ?"],
                4: [0, "Hey toi ! J'ai besoin de toi.\n1. Je ne crois pas, bonne journee.\n2. Je vous ecoute.", 2],
                    5: [-1, "Tu ne sais pas ce que tu rates l'ami."],
                    6: [1, "Bien. Tu vas aller au sud ouest, au fond d'un bois, il y a trois maisons. Je sais que l'une d'elle mene a Niflheim. Trouve un esprit du nom d'Asufaith et donne-lui ce mot. [L'HOMME VOUS DONNE UNE LETTRE CACHETEE D'UN SCEAU DE CIRE NOIRE.].", 0, (8, 2)],
            }
    
    else: return [0, "Ui hips ?"]


def h_27_npc(data, stat):
    pass


def h_28_npc(data, stat):
    coords = data[2], data[3]

    if coords == (27, 6):
        if data[0] == 42: return [10, 10, 10, 10, 100], "Targ", 40, 2
        elif data[0] == 44: return [0, "[ENCORE SUANT DU COMBAT, VOUS REGARDEZ AVEC UNE CERTAINE SATISFACTION LE TAS DE CHAIR QUI FUT VOTRE ADVERSAIRE.]"]


# - - - Niflheim - - - #
def niflheim_po(coords):
    if coords == (88, 32): return [0, "Entoure de pierre tombales, de nombreux chemins serpentent. De lourd nuages fonces entretiennent une atmosphere pesante et une brume noiratres flotte dans l'air. Dans la penombre ambiante, une haute maison se detache, masse plus sombre encore que le reste, percee de fines fenetres et encadree de deux tours."]


def niflheim_npc(data, stat):
    # * : (95, 30)
    # * : (57, 31)
    # * : (39, 60)
    # * : (108, 67)
    coords = data[2], data[3]
    xp = data[0]

    if coords == (57, 31):
        if stat[8] == 2: return {
            "base": [0, "[VOUS REGARDEZ LE SOL SANS COMPRENDRE.]"],
                7: [1, "Asufaith, besoin de quelque chose ? [VOUS LUI DONNEZ LA LETTRE, L'ESPRIT VOUS REGARDA SANS PARAITRE ETONNE ET S'EN EMPARA.] Notre... Ami commun vous envoie de loin. [SUR CES MOTS L'ESPRIT SE RETOURNA ET TRAVERSA LE SOL DE TERRE, VOUS LAISSANT DESEMPARE.]"],
        }


def h_29_npc(data, stat):
    coords = data[2], data[3]

    spells_sale = ((0, 5), (1, 5), (2, 5), (3, 5), (4, 5))

    if not (480 <= stat[4] <= 1140): return [0, "Je suis desolee, nous sommes fermes."]

    if coords == (5, 5):
        if len(stat[7]) >= 3: return [0, "Vous ne pouvez pas apprendre plus de sort, et je ne pratique pas les sorts d'oubli. Je crois qu'une librairie vers Alfheim le fait gratuitement."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Merath, je vend les sorts les plus puissants de tout l'Yggdrasil ! Quel sort voulez-vous ?\n1. Soin V\n2. Flammes V\n3. Givre V\n4. Etincelles V\n4. Fatigue V", 4]

        else:
            for i in range(1, 5):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < 50: return [-i, "Vous n'avez pas les moyens, desolee."]

                    spell_id = -1
                    for sp_id, sp in range(len(stat[7])):
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


def h_30_npc(data, stat):
    pass


# - - - Jotunheim - - - #
def jotunheim_po(coords):
    if coords == (60, 57): return [0, "Un bruit de fontaine monte a vos oreilles. A travers les arbres, l'immense palais de Thrym se dresse. Les enormes colonnes qui entourent le batiments sont a elles seules des symboles de demesures. Aux alentours se dresse quelques maisons tout aussi imposantes et enorme, mais moins travaillee."]
    elif coords == (23, 70): return [0, "Face a la mer, sur une langue de terre, le phare se dresse, eclairant puissemment le large pour signaler l'estuaire."]
    elif coords == (60, 86): return [0, "Un imposant manoir se tient devant vous, flanque de deux tours surmontees de domes en ardoise brillantes, l'ensemble est perce de multiples et larges ouvertures. Le parc autour se compose de quelques arbres et est delimite au nord par le fleuve."]


def jotunheim_npc(data, stat):
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

    # Utarg
    if coords == (34, 56): return {
        "base": [0, "Utarg, pour vous servir."],
        36: [0, "Utarg, vous me cherchiez ?\n1. Oui, Thrym m'a demande de vous donner ceci [VOUS LUI DONNEZ LA LETTRE].\n2. Quelles sont les relations entre les Geants et les Ases ?", 2],
            37: [3, "[UTARG LIT LE BILLET.] Hum. Thrym me demande de detacher une garnison et de me rendre a Vanaheim. On se retrouve a l'auberge, au nord de Vanaheim."],
            38: [-2, "Plusieurs differents ont eloignes les Ases des Geants : meutres, enlevements, traitrises... Ce serait long a expliquer."]
    }


def h_31_npc(data, stat):
    pass


def h_32_npc(data, stat):
    pass


def h_33_npc(data, stat):
    pass


def h_34_npc(data, stat):
    coords = data[2], data[3]

    if coords == (26, 6):
        if not (360 <= stat[4] <= 1200):
            return [0, "Reviens quand il fera jour s'il te plait."]
        else: return {
            "base": [0, "Thyrm, roi des Geants. Bienvenue a Utgard."],
            34: [0, "Bonjour, je suis Thyrm, bienvenue a Utgard.\n1. Freyja m'a charge de vous dire qu'Odin a declare la guerre aux Vanes.", 1],
            35: [1, "De part le mariage entre Gerd et Freyr, nos liens avec les Vanes sont forts. Par respect pour eux et en souvenir de notre histoire mouvemente avec les Ases, j'accepte d'aider Freyja et les siens. [THRYM SAISIT UNE LETTRE ET GRIFONNA QUELQUES MOTS AVANT DE VOUS LA TENDRE.] En sortant dirige-toi vers Westri, vers la jetee, tu trouveras Utarg. Donne-lui ce mot."]
        }


def h_35_npc(data, stat):
    coords = data[2], data[3]
    xp = data[0]

    if coords == (17, 5):
        if xp == 14: return [8, 8, 5, 5, 80], "Gullveig", 15, 1
        elif xp == 15: return [0, "[VOUS REGARDEZ LA DEPOUILLE DESARTICULEE DE LA MAGICIENNE, ODIN SERA CONTENT.]"]
        else: return {
                "base": [0, "Gullveig, magicienne Vane, pour te servir."],
                44: [0, "Gullveig, magicienne Vane, besoin de quelque chose ?\n1. Pouvez-vous dechiffre ces runes pour moi ?\n2. Non, excusez-moi.", 2],
                    45: [11, "Bien sur. [GULLVEIG REGARDA LE CROQUIS DES RUNES] Hum... je ne suis pas sure de ce que cela veut dire, si je traduit dans notre alphabet cela donne 'kvasir'."],
                    46: [-2, "Reviens quand tu veux !"],
                50: [0, "Ah {} ! Besoin de quelque chose ?\n1.C'est Sagriel qui m'envoie, elle a besoin d'une potion d'eternelle jeunesse.\n2. Non, rien, merci.".format(stat[5]), 2],
                    51: [3, "Oui, bien sur ! [GULLVEIG VOUS TEND UNE FIOLE REMPLIE D'UN LIQUIDE AMBRE.]", 0, (1, -10)],
                    52: [-2, "Reviens quand tu veux !"],
            }


def h_36_npc(data, stat):
    coords = data[2], data[3]
    
    if coords == (27, 10):
        if not (300 <= stat[4] <= 1380): return [0, "Je suis desole, nous somme ferme la nuit."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Vous voulez quelque-chose ?\n1. Je mangerai bien un truc [-4 PO]\n2. Il vous reste une chambre ? [-12 PO]", 2]

        else:
            event, choice = shop_interaction(data, stat, 2,
                (4, [-1, "Et voila ! [LE TAVERNIER POSA UNE ASSIETTE FUMANTE DEVANT VOUS ET UN VERRE DE VIN]", 0, (0, 5), (1, -4)], [-1, "Reviens quand tu auras de quoi me payer."]),
                (12, [-2, "Oui, au premier etage, au bout du couloir sur votre droite. [VOUS SUIVEZ LES INDICATIONS DU TAVERNIER ET TROUVEZ VOTRE CHAMBRE. VOUS SOMBREZ DANS LES BRAS DE NOTT.]", 0, (0, 15), (1, -12), (4, 480)], [-2, "Tu n'as pas assez."]))
        
            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Il est trop tot, reviens vers 19h."]
            else: return event


# - - - Nidavellir - - - #
def nidavellir_po(coords):
    if coords == (65, 7): return [0, "La mer etendait ses rouleaux sur le sable noir. Au sud s'etend le rocheux royaume de Nidavellir. Le monde des nains a pour seul maison les montagnes. D'ancienne legendes racontent que certaines communiquent entre elles par des passages oublies."]
    elif coords == (66, 58): return [0, "Coupee en deux par le fleuve, la chaine de montagne semble s'etendre a l'infini. De toute part le meme paysage rocailleux. Le terrain est si inhospitalier que les nains eux-meme restent dans leurs mines."]


def nidavellir_npc(data, stat):
    # * : (49, 21)
    # * : (25, 31)
    # * : (74, 46)
    # * : (16, 55)
    # * : (77, 61)
    coords = data[2], data[3]

    if coords == (25, 31):
        return {
            "base": [0, "Skirnir, messager de Freyr..."],
            68: [0, "Skirnir, messager de Freyr...\n1. J'ai un message pour vous", 1],
            69: [1, "[VOUS TENDEZ LE PARCHEMIN MODIFIE A SKIRNIR] Je vais de ce pas transmettre ce message aux Ases. Nous allons attirer les Ases dans un piege dans une tour de guet de Svartalfheim. Il ne doit pas y avoir beaucoup de soldats Ases present. Tu rendras directement compte a Freyja. Avant que tu ne partes, achetes-toi un equimement digne de ce nom. [+30 PO]", 0, (1, 30)],
        }


def h_37_npc(data, stat):
    coords = data[2], data[3]

    if coords == (2, 1):
        if not (340 <= stat[4] <= 1380): return [0, "Nous sommes ouverts de 5 heures a 23."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Bonjour, Muin pour vous servir.\n1. Bonjour je voudrais manger. [-5 PO]\n2. Vous reste-t-il des chambres ? [-15 PO]\n3. A boire ! [-3 PO]", 3]

        else:
            event, choice = shop_interaction(data, stat, 3,
                (5, [-1, "Pas de probleme ! [MUIN REVINT QUELQUES MINUTES PLUS TARD, ET POSA UNE ASSIETTE FUMANTE DEVANT VOUS.]", 0, (0, 5), (1, -5)], [-1, "Hey la ! Reviens quand tu pourras me payer."]),
                (15, [-2, "Bien sur ! Suivez-moi. [VOUS SUIVEZ MUIN DANS UNE PIECE TROGLODYTE MUNIE D'UN LIT ET D'UN COFFRE. VOUS VOUS ENDORMEZ RAPIDEMENT.]", 0, (0, 15), (1, -15), (4, 480)], [-2, "Desole, je n'ai plus une seule chambre de libre."]),
                (3, [-3, "[MUIN POSA UNE CHOPPE DE BIERE MOUSSEUSE DEVANT VOUS.]", 0, (0, 3), (1, -3)], [-3, "Allez donc voir un autre etablissement, nous ne servons pas gratuitement."]))
            
            if choice == 2 and 360 < stat[4] < 1140: return [-2, "Une chambre !? Il n'est que {} heures. Reviens dans la soiree.".format(stat[4] // 60)]
            else: return event

    return [0, "Hmm ?"]


def h_38_npc(data, stat):
    pass


def h_39_npc(data, stat):
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "La forge de Nivallir est ouverte de 8 heures a 18 heures."]

    if coords == (9, 2):

        if stat[3][0]: return [0, "Vous avez deja une arme. Allez voir mon confrere si vous voulez la vendre et revenez me voir."]

        elif stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Bienvenue a la forge de Nidavellir ! Vous desirez une piece particulière ?\n1. Un marteau [-20 PO]\n2. Une masse [-30 PO]\n3. Un fleau [-40 PO]\n4. Une hache [-50 PO]", 4]

        else:
            weapons = ("UN MARTEAU", "UNE MASSE", "UN FLEAU", "UNE HACHE")
            for i in range(1, 5):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < (i+1) * 10: return [-i, "Vous n'avez pas assez."]
                    stat[3][0] = i + 1
                    return [-i, "Tres bon choix ! [LE NAIN DECROCHA {} DU RATELIER ET VOUS TENDIT L'ARME.]".format(weapons[i - 1]), 0, (1, -(i+1) * 10)]

    if coords == (9, 4):
        if stat[3][0] == 0: return [0, "Vous n'avez pas d'arme a me vendre. Allez voir mon collegue pour en acheter une."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Bienvenue dans notre forge. Vous souhaitez me vendre votre arme ?\n1. Oui\n2. Non", 2]

        elif data[0] == stat[9] + 1:
            stat[9] = -1
            cost = stat[3][0] * 8
            stat[3][0] = 0
            return [-1, "Marche conclu ! [+{} PO]".format(cost), 0, (1, cost)]

        elif data[0] == stat[9] + 2:
            stat[9] = -1
            return [-2, "A votre guise, revenez quand vous voulez !"]


def h_40_npc(data, stat):
    pass


def h_41_npc(data, stat):
    pass


# - - - Muspellheim - - - #
def muspellheim_po(coords):
    if coords == (66, 8): return [0, "La mer s'etendait, calme. Bosquets et maisons peuplaient la cote, dont plusieurs petite tentes."]
    elif coords == (64, 97): return [0, "La cloture de la propriete etait ouvragee, le manoir aussi. Constitue d'un corps de ferme rehabilite et entoure de deux tours decoratives, l'ensemble conservait un air propre et entretenu. Le jardin taille en temoigne."]


def muspellheim_npc(data, stat):
    # * : (20, 12)
    # * : (78, 14)
    # * : (54, 80)
    # * : (59, 91)
    # * : (39, 94)
    # * : (29, 113)
    pass


def h_42_npc(data, stat):
    coords = data[2], data[3]

    if coords == (6, 7):
        if not (300 <= stat[4] <= 1380): return [0, "Nous sommes ouverts de 5 a 23 heures."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Besoin de quelque chose messire ?\n1. Hum, oui, j'aimerais manger. [-5 PO]\n2. Je voudrais dormir [-10 PO]", 2]

        else:
            event, _ = shop_interaction(data, stat, 2, 
                (5, [-1, "Et voila pour vous !", 0, (0, 5), (1, -5)], [-1, "Je regrette, vous n'avez pas assez."]),
                (10, [-2, "Bien sur, si vous voulez bien me suivre. [VOUS VOUS ALLONGEZ SUR LE LIT ET VOUS ENDORMEZ RAPIDEMENT.]", 0, (0, 10), (1, -10), (4, 480)], [-2, "Nous ne pouvons pas nous permettre de faire credit."]))
        
            return event

def h_43_npc(data, stat):
    coords = data[2], data[3]

    if not (480 <= stat[4] <= 1140): return [0, "L'armurerie est ouverte de 8 heures a 18 heures."]

    if coords == (24, 4):
        if stat[3][1]: return [0, "Vous portez deja une armure, allez voir mon confrere."]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Bienvenue, dans mon armurerie ! Je suis Bertfrid, besoin d'une armure ?\n1. Oui, d'une rondache. [-10 PO]\n2. d'un pavois [-20 PO]\n3. d'une cotte de mailles [-30 PO]\n4. d'une broigne [-40 PO]\n5. d'un harnois [-50 PO]", 5]

        else:
            shields = ("UNE RONDACHE", "UN PAVOIS", "UNE COTTE DE MAILLES", "UNE BROIGNE", "UN HARNOIS")
            for i in range(1, 6):
                if data[0] == stat[9] + i:
                    stat[9] = -1
                    if stat[1] < i * 10: return [-i, "Vous n'avez pas assez."]
                    stat[3][1] = i
                    return [-i, "C'est un bon achat. [BERTFRID DECROCHA {}]".format(shields[i - 1]), 0, (1, -i * 10)]

    elif coords == (13, 9):
        if stat[3][1] == 0: return [0, "J'achete, je ne vend pas ! Allez voir Bertfrid du cote du four a metaux, elle vous renseignera"]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Vous voulez vendre votre piece d'armure ?\n1. Oui\n2. Non", 2]

        elif data[0] == stat[9] + 1:
            stat[9] = -1
            cost = stat[3][1] * 8
            return [-1, "C'est une affaire ! [+{} PO]".format(cost), 0, (1, cost)]

        elif data[0] == stat[9] + 2:
            stat[9] = -1
            return [-2, "Revenez quand vous voulez !"]

    elif coords == (6, 5):
        return [0, "Je ne suis qu'apprenti monseigneur. Adressez-vous plutot a Bertfrid."]


def h_44_npc(data, stat):
    pass


# - - - Svartalfheim - - - #
def svartalfheim_po(coords):
    if coords == (113, 37): return [0, "Des tours de guets parsement la cote, plus loin, a l'ouest, une chaine de petites montagnes s'etend, coupant Svartalfheim en deux. Mais la partie est du monde est plus habitee et plus animee que la partie ouest qui reste majoritairement consitituee de denses forets."]


def svartalfheim_npc(data, stat):
    # * : (105; 46)
    # * : (22; 50)
    # * : (15; 54)
    # * : (25; 61)
    # * : (121; 68)
    coords = data[2], data[3]

    if coords == (120, 49) or coords == (104, 30):
        if not (360 <= stat[4] <= 1200): return [0, "Hmm, hein ? Quoi ? Zavez pas vu l'heure ??"]

        if stat[9] == -1 or data[0] == stat[9]:
            stat[9] = data[0]
            return [0, "Hey, toi ! Tu veux traverser ?\n1. Traverser [2 PO]\n2. Ne pas traverser", 2]
        
        elif data[0] == stat[9] + 1:
            stat[9] = -1
            if stat[1] < 2: return [-1, "Reviens quand tu auras de quoi me payer."]
            
            if coords == (104, 30): data[2], data[3] = 119, 49
            else: data[2], data[3] = 103, 30
            
            return [-1, "C'est parti !", 0, (1, -2)]

        elif data[0] == stat[9] + 2:
            stat[9] = -1
            return [0, "Reviens quand tu voudras traverser."]


def h_45_npc(data, stat):
    # * : (15, 4)
    pass


def h_46_npc(data, stat):
    # * : (13, 2)
    # * : (13, 4)
    coords = data[2], data[3]

    if coords == (13, 2):
        if data[0] in (70, 72): return [12, 10, 15, 15, 100], "Soldat Ase", 10, 2
        elif data[0] == 74: return [0, "[LA DEPOUILLE SANGLANTE DU SOLDAT EST AFFALLEE SUR LE BANC. UNE MARE DE SANG COAGULE DEJA A SES PIEDS.]"]

    if coords == (13, 4):
        if data[0] in (70, 72): return [12, 10, 20, 15, 100], "Soldat Ase", 10, 2
        elif data[0] == 74: return [0, "[DES MORCEAUX DE CORPS JONCHENT LE SOL ET LA TABLE.]"]


def h_47_npc(data, stat):
    # * : (3, 4)
    # * : (15, 8)
    pass


def h_48_npc(data, stat):
    # * : (34, 5)
    # * : (29, 6)
    pass