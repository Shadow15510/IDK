def generateur_scenario(nom):
    functions = (
        "asgard_po",
        "asgard_npc",
        "h_9_npc",
        "h_10_npc",
        "h_11_npc",
        "h_12_npc",
        "h_13_npc",
        "h_14_npc",
        "h_15_npc",
        "h_16_npc",
        "h_17_npc",
        "h_18_npc",
        "h_19_npc",
        "h_20_npc",
        "vanaheim_po",
        "vanaheim_npc",
        "h_22_npc",
        "alfheim_po",
        "alfheim_npc",
        "h_23_npc",
        "h_24_npc",
        "midgard_po",
        "midgard_npc",
        "h_25_npc",
        "h_26_npc",
        "h_27_npc",
        "h_28_npc",
        "niflheim_po",
        "niflheim_npc",
        "h_29_npc",
        "h_30_npc",
        "jotunheim_po",
        "jotunheim_npc",
        "h_31_npc",
        "h_32_npc",
        "h_33_npc",
        "h_34_npc",
        "h_35_npc",
        "h_36_npc",
        "nidavellir_po",
        "nidavellir_npc",
        "h_37_npc",
        "h_38_npc",
        "h_39_npc",
        "h_40_npc",
        "h_41_npc",
        "muspellheim_po",
        "muspellheim_npc",
        "h_42_npc",
        "h_43_npc",
        "h_44_npc",
        "svartalfheim_po",
        "svartalfheim_npc",
        "h_45_npc",
        "h_46_npc",
        "h_47_npc",
        "h_48_npc")

    default_content = f"""
try:
    import dlc_{nom} as dlc
    spells = dlc.dlc_spells
    spells_level = dlc.dlc_spells_level
    spells_effect = dlc.dlc_spells_effect
    weapons = dlc.dlc_weapons
    armors = dlc.dlc_armors
    dlc_entities = dlc.dlc_entities
except:
    dlc = None
    dlc_entities = ()



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

print(center("{nom}", 21, " "))
print("Entrez '' pour\nune nouvelle partie.")
events = {"*": npc, "?": point_of_interest}
keys = {4: display_stat, 7: spell, 8: misc_stat, 6: inventory, 9: sleep, "s": quick_save}


def {nom}(save_code=None):
    # stat = [0 - PV, 1 - pièces d'or, 2 - [vitesse, agilité, attaque, defense, magie], 3 - [arme, armure], 4 - ticks, 5 - nom, 6 - classe, 7 - sorts connus : (id, level), 8 - sous-quêtes terminées]
    if not save_code:
        stat = init_stat()
        name = stat[5]
        data = [{"main": 0}, 3, 44, 66]

        print_text("introduction")
    else:
        stat, data = decode_save(save_code)

    idk_game = Asci(maps, entities, events, keys)
    stat, data = idk_game.mainloop(1, stat, data, routine=routine, door="^_", walkable=".,`' ", exit_key="q")
    if stat[9] != -1: data[0]["main"] -= stat[9]

    if data[0]["main"] == 1:
        print_text("conclusion")
    else:
        print("{nom}(\"\{\}\")".format(encode_save(data, stat[:-1])))


# Scenario
def shop_interaction(data, stat, nb_choice, *events):
    for choice in range(nb_choice):
        if data[0]["main"] == stat[9] + choice + 1:
            stat[9] = -1
            if stat[1] < events[choice][0]: return events[choice][2], choice + 1
            else: return events[choice][1], choice + 1
            """

