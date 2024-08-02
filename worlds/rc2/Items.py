from typing import NamedTuple, Optional


from BaseClasses import Item, ItemClassification

PROGRESSION = ItemClassification.progression
FILLER = ItemClassification.filler
USEFUL = ItemClassification.useful
TRAP = ItemClassification.trap
SKIP_BALANCING = ItemClassification.skip_balancing
PROGRESSION_SKIP_BALANCING = ItemClassification.progression_skip_balancing


class RC2Item(Item):
    game: str = "Ratchet and Clank Going Commando"


class RC2ItemData(NamedTuple):
    name: str
    code: Optional[int]
    classification: ItemClassification
    categories: set[str] = {}
    amount: Optional[int] = 1


def get_platinum_bolt_items(are_mods_items: bool) -> list[RC2ItemData]:
    classification = PROGRESSION if are_mods_items else USEFUL
    return [
        RC2ItemData("Oozla - Tractor Beam Platinum Bolt", 0x1D000, classification, {"Platinum Bolt"}),
        RC2ItemData("Oozla - Cave Platinum Bolt", 0x1D001, classification, {"Platinum Bolt"}),
        RC2ItemData("Maktar - Path to the Arena Platinum Bolt", 0x1D002, classification, {"Platinum Bolt"}),
        RC2ItemData("Maktar - Jamming Array Platinum Bolt", 0x1D003, classification, {"Platinum Bolt"}),
        RC2ItemData("Endako - Move the crates Platinum Bolt", 0x1D004, classification, {"Platinum Bolt"}),
        RC2ItemData("Endako - Down the ladder Platinum Bolt", 0x1D005, classification, {"Platinum Bolt"}),
        RC2ItemData("Barlow - Swingshot Platinum Bolt", 0x1D006, classification, {"Platinum Bolt"}),
        RC2ItemData("Barlow - Race Platinum Bolt", 0x1D007, classification, {"Platinum Bolt"}),
        # RC2ItemData("Feltzin - Race Rings Platinum Bolt", 0x1D008, classification, {"Platinum Bolt"}),
        # RC2ItemData("Notak - Near Ship Platinum Bolt", 0x1D009, classification, {"Platinum Bolt"}),
        # RC2ItemData("Notak - Promenade Platinum Bolt", 0x1D00A, classification, {"Platinum Bolt"}),
        # RC2ItemData("Notak - Dynamo Door Platinum Bolt", 0x1D00B, classification, {"Platinum Bolt"}),
        # RC2ItemData("Siberius - Tractor Beam Platinum Bolt", 0x1D00C, classification, {"Platinum Bolt"}),
        # RC2ItemData("Siberius - Gliding Platinum Bolt", 0x1D00D, classification, {"Platinum Bolt"}),
        # RC2ItemData("Tabora - Desert Platinum Bolt", 0x1D00E, classification, {"Platinum Bolt"}),
        # RC2ItemData("Tabora - Thermanator Platinum Bolt", 0x1D00F, classification, {"Platinum Bolt"}),
        # RC2ItemData("Tabora - Glider Platinum Bolt", 0x1D010, classification, {"Platinum Bolt"}),
        # RC2ItemData("Dobbo - Spiderbot Platinum Bolt", 0x1D011, classification, {"Platinum Bolt"}),
        # RC2ItemData("Dobbo - Glider Platinum Bolt", 0x1D012, classification, {"Platinum Bolt"}),
        # RC2ItemData("Hrugis - Race Rings Platinum Bolt", 0x1D013, classification, {"Platinum Bolt"}),
        # RC2ItemData("Joba - Swingshot Platinum Bolt", 0x1D014, classification, {"Platinum Bolt"}),
        # RC2ItemData("Joba - Levitator Platinum Bolt", 0x1D015, classification, {"Platinum Bolt"}),
        # RC2ItemData("Todano - Fizzwidget Platinum Bolt", 0x1D016, classification, {"Platinum Bolt"}),
        # RC2ItemData("Todano - Employee Platinum Bolt", 0x1D017, classification, {"Platinum Bolt"}),
        # RC2ItemData("Todano - Conveyor Belts Platinum Bolt", 0x1D018, classification, {"Platinum Bolt"}),
        # RC2ItemData("Boldan - Spiderbot Platinum Bolt", 0x1D019, classification, {"Platinum Bolt"}),
        # RC2ItemData("Boldan - Platform Platinum Bolt", 0x1D01A, classification, {"Platinum Bolt"}),
        # RC2ItemData("Boldan - Post-Fizzwidget Platinum Bolt", 0x1D01B, classification, {"Platinum Bolt"}),
        # RC2ItemData("Aranos - Under Ship Platinum Bolt", 0x1D01C, classification, {"Platinum Bolt"}),
        # RC2ItemData("Gorn - Race Rings Platinum Bolt", 0x1D01D, classification, {"Platinum Bolt"}),
        # RC2ItemData("Snivelak - Dynamo Platinum Bolt", 0x1D01E, classification, {"Platinum Bolt"}),
        # RC2ItemData("Smolg - Levitator Platinum Bolt", 0x1D01F, classification, {"Platinum Bolt"}),
        # RC2ItemData("Smolg - Warehouse Platinum Bolt", 0x1D020, classification, {"Platinum Bolt"}),
        # RC2ItemData("Damosel - Fountain Platinum Bolt", 0x1D021, classification, {"Platinum Bolt"}),
        # RC2ItemData("Damosel - Pyramid Platinum Bolt", 0x1D022, classification, {"Platinum Bolt"}),
        # RC2ItemData("Grelbin - Ice Plains Platinum Bolt", 0x1D023, classification, {"Platinum Bolt"}),
        # RC2ItemData("Grelbin - Water Platinum Bolt", 0x1D024, classification, {"Platinum Bolt"}),
        # RC2ItemData("Grelbin - Cave Platinum Bolt", 0x1D025, classification, {"Platinum Bolt"}),
        # RC2ItemData("Yeedil - Bridge Platinum Bolt", 0x1D026, classification, {"Platinum Bolt"}),
        # RC2ItemData("Yeedil - Rails Platinum Bolt", 0x1D027, classification, {"Platinum Bolt"}),
    ]


rc2_weapon_lancer = RC2ItemData("Lancer", 0x1D040, PROGRESSION, {"Weapon"})
rc2_weapon_items = [
    RC2ItemData("Lancer", 0x1D040, PROGRESSION, {"Weapon"}),
    RC2ItemData("Gravity Bomb", 0x1D041, PROGRESSION, {"Weapon"}),
    RC2ItemData("Chopper", 0x1D042, PROGRESSION, {"Weapon"}),
    RC2ItemData("Blitz Gun", 0x1D043, PROGRESSION, {"Weapon"}),
    RC2ItemData("Pulse Rifle", 0x1D044, PROGRESSION, {"Weapon"}),
    RC2ItemData("Miniturret Glove", 0x1D045, PROGRESSION, {"Weapon"}),
    RC2ItemData("Seeker Gun", 0x1D046, PROGRESSION, {"Weapon"}),
    RC2ItemData("Synthenoids", 0x1D047, PROGRESSION, {"Weapon"}),
    RC2ItemData("Lava Gun", 0x1D048, PROGRESSION, {"Weapon"}),
    RC2ItemData("Bouncer", 0x1D049, PROGRESSION, {"Weapon"}),
    RC2ItemData("Minirocket Tube", 0x1D04A, PROGRESSION, {"Weapon"}),
    RC2ItemData("Spiderbot Glove", 0x1D04B, PROGRESSION, {"Weapon"}),
    RC2ItemData("Plasma Coil", 0x1D04C, PROGRESSION, {"Weapon"}),
    RC2ItemData("Hoverbomb Gun", 0x1D04E, PROGRESSION, {"Weapon"}),
    RC2ItemData("Shield Charger", 0x1D04D, PROGRESSION, {"Weapon"}),
    RC2ItemData("Zodiac", 0x1D04F, USEFUL, {"Weapon"}),
    RC2ItemData("RYNO II", 0x1D051, PROGRESSION, {"Weapon"}),
    RC2ItemData("Clank Zapper", 0x1D052, USEFUL, {"Weapon"}),
    RC2ItemData("Bomb Glove", 0x1D053, PROGRESSION, {"Weapon"}),
    RC2ItemData("Walloper", 0x1D054, USEFUL, {"Weapon"}),
    RC2ItemData("Decoy Glove", 0x1D055, PROGRESSION, {"Weapon"}),
    RC2ItemData("Tesla Coil", 0x1D056, PROGRESSION, {"Weapon"}),
    RC2ItemData("Visibomb Gun", 0x1D057, PROGRESSION, {"Weapon"}),
]


rc2_gadgets_items = [
    RC2ItemData("Swingshot", 0x1D058, PROGRESSION, {"Gadget"}),
    RC2ItemData("Dynamo", 0x1D059, PROGRESSION, {"Gadget"}),
    RC2ItemData("Thermanator", 0x1D05A, USEFUL, {"Gadget"}),
    RC2ItemData("Tractor Beam", 0x1D05B, PROGRESSION, {"Gadget"}),
    # RC2ItemData("Hypnomatic", 0x1D05C, PROGRESSION, {"Gadget"}),

    RC2ItemData("Grind Boots", 0x1D05D, USEFUL, {"Gadget"}),
    # RC2ItemData("Gravity Boots", 0x1D05E, PROGRESSION, {"Gadget"}),
    # RC2ItemData("Charge Boots", 0x1D05F, PROGRESSION, {"Gadget"}),

    RC2ItemData("Electrolyzer", 0x1D060, PROGRESSION, {"Gadget"})
]

rc2_clank_item = RC2ItemData("Clank", 0x1D06A, PROGRESSION, {"Gadget"})

rc2_planet_coordinate_items = [
    RC2ItemData("Planet Coordinates to Oozla", 0x1D070, PROGRESSION, {"Planet Coordinates"}),
    RC2ItemData("Planet Coordinates to Maktar", 0x1D071, PROGRESSION, {"Planet Coordinates"}),
    RC2ItemData("Planet Coordinates to Endako", 0x1D072, PROGRESSION, {"Planet Coordinates"}),
    RC2ItemData("Planet Coordinates to Barlow", 0x1D073, PROGRESSION, {"Planet Coordinates"}),
    RC2ItemData("Planet Coordinates to Feltzin", 0x1D074, PROGRESSION, {"Planet Coordinates"}),
]

# Tricks
rc2_fpwc_item = RC2ItemData("FPWC", 0x1D0A0, FILLER)
rc2_dgc_item = RC2ItemData("DGC", 0x1D0A1, FILLER)
rc2_charge_tricks_item = RC2ItemData("Charge Tricks", 0x1D0A2, FILLER)


# Filler
rc2_1bolt_item = RC2ItemData("1 Bolt", 0x1D0B0, FILLER)


rc2_event_victory = RC2ItemData("Victory", None, PROGRESSION)


def get_rc2_items(are_mods_items: bool = False) -> list[RC2ItemData]:
    return (get_platinum_bolt_items(are_mods_items) + rc2_gadgets_items +
            rc2_planet_coordinate_items +
            [rc2_charge_tricks_item, rc2_dgc_item, rc2_clank_item, rc2_weapon_lancer])


def get_rc2_item_groups() -> dict[str, set[str]]:
    rc2_items = get_rc2_items()
    item_groups: dict[str, set[str]] = {}
    for rc2_item in rc2_items:
        for category in rc2_item.categories:
            if category not in item_groups.keys():
                item_groups[category] = set()
            item_groups[category].add(rc2_item.name)

    return item_groups
