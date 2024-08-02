from BaseClasses import CollectionState

# General


def can_decoy_clip(state: CollectionState, player: int) -> bool:
    return state.has_all({"Decoy Glove", "DGC"}, player)


def can_charge_boot_trick(state: CollectionState, player: int) -> bool:
    return state.has_all({"Charge Boots", "Charge Tricks"}, player)

# Oozla


def oozla_swamp_monster_1(state: CollectionState, player: int) -> bool:
    return state.has_group("Weapon", player) or state.has_any({"AW", "FPWC"}, player)


def oozla_megacorp_shop(state: CollectionState, player: int) -> bool:
    return (
            (state.has("Dynamo", player) or (state.has("Clank", player) and can_decoy_clip(state, player)))
            and oozla_swamp_monster_1(state, player)
    )


def platinum_bolt_1(state: CollectionState, player: int) -> bool:
    return state.has_any({"Tractor Beam", "FPWC"}, player)


# TODO Event/Hint that you need to complete other mission too?
def platinum_bolt_2(state: CollectionState, player: int) -> bool:
    return oozla_megacorp_shop(state, player)


def skill_point_prehistoric_rampage(state: CollectionState, player: int) -> bool:
    return True


# TODO Complete
def skill_point_smash_and_grab(state: CollectionState, player: int) -> bool:
    return oozla_megacorp_shop(state, player) and state.has_group("Weapon", player)

# Maktar


def maktar_photo_booth(state: CollectionState, player: int) -> bool:
    return state.has("Electrolyzer", player) and state.has_group("Weapon", player)


def maktar_jamming_array(state: CollectionState, player: int) -> bool:
    return ((state.has("Tractor Beam", player) or can_charge_boot_trick(state, player))
            and state.has_group("Weapon", player))


def platinum_bolt_3(state: CollectionState, player: int) -> bool:
    return True


def platinum_bolt_4(state: CollectionState, player: int) -> bool:
    return maktar_jamming_array(state, player)


def skill_point_blade_to_blade(state: CollectionState, player: int) -> bool:
    return True


# TODO Complete
def skill_point_vandalize(state: CollectionState, player: int) -> bool:
    return True

# Endako


def endako_clank(state: CollectionState, player: int) -> bool:
    return state.has("Electrolyzer", player)


# TODO Complete
def endako_appartment(state: CollectionState, player: int) -> bool:
    return True


def platinum_bolt_5(state: CollectionState, player: int) -> bool:
    return state.has("Electrolyzer", player) or can_decoy_clip(state, player)


def platinum_bolt_6(state: CollectionState, player: int) -> bool:
    return True


# TODO Complete
def skill_point_destroy_all_breakables(state: CollectionState, player: int) -> bool:
    return True


# TODO Complete
def skill_point_operate_heavy_machinery(state: CollectionState, player: int) -> bool:
    return state.has("Electrolyzer", player)


# TODO Complete
def endako_nanotech_boost(state: CollectionState, player: int) -> bool:
    return (
        state.has_any({"Electrolyzer", "FPWC"})
        and state.has("Infiltrator", player) or can_decoy_clip(state, player)
    )

# Barlow


def barlow_race_access(state: CollectionState, player: int) -> bool:
    test = state.has_any({"Clank", "FPWC"}, player)
    return state.has_any({"Clank", "FPWC"}, player)


def barlow_thermanator(state: CollectionState, player: int) -> bool:
    return state.has_any({"Swingshot", "FPWC"}, player)


def platinum_bolt_7(state: CollectionState, player: int) -> bool:
    return state.has("Swingshot", player)


def platinum_bolt_8(state: CollectionState, player: int) -> bool:
    return barlow_race_access(state, player)


def skill_point_speed_demon(state: CollectionState, player: int) -> bool:
    return barlow_race_access(state, player)
