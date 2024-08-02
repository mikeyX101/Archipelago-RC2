from typing import NamedTuple, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.rc2 import RC2World

from BaseClasses import Location
from worlds.generic.Rules import CollectionRule
from worlds.rc2.Rules import *


class RC2Location(Location):
    game: str = "Ratchet & Clank Going Commando"


class RC2LocationData(NamedTuple):
    planet: str
    name: str
    code: Optional[int]
    rule: CollectionRule = lambda state: True


def get_rc2_locations(world: Optional["RC2World"] = None) -> list[RC2LocationData]:
    p = 0
    if world is not None:
        p = world.player

    rc2_victory = RC2LocationData("Yeedil", "Mutant Protopet Defeated", None)
    rc2_test_victory = RC2LocationData("Feltzin", "Victory", None,
                                       lambda s: s.has("Planet Coordinates to Feltzin", p))

    rc2_gadgets = [
        RC2LocationData("Oozla", "Dynamo", 0x1D059,
                        lambda s: oozla_swamp_monster_1(s, p)),
        RC2LocationData("Oozla", "Tractor Beam", 0x1D05B),

        RC2LocationData("Maktar", "Electrolyzer", 0x1D060,
                        lambda s: maktar_photo_booth(s, p)),

        RC2LocationData("Endako", "Swingshot", 0x1D058,
                        lambda s: endako_appartment(s, p)),
        RC2LocationData("Endako", "Grind Boots", 0x1D05D,
                        lambda s: endako_appartment(s, p)),

        RC2LocationData("Barlow", "Thermanator", 0x1D05A,
                        lambda s: barlow_thermanator(s, p)),

        RC2LocationData("Endako", "Clank", 0x1D06A,
                        lambda s: endako_clank(s, p)),
    ]

    rc2_planet_coordinates = [
        RC2LocationData("Aranos1", "Planet Coordinates to Oozla", 0x1D070),
        RC2LocationData("Oozla", "Planet Coordinates to Maktar", 0x1D071,
                        lambda s: oozla_megacorp_shop(s, p)),
        RC2LocationData("Maktar", "Planet Coordinates to Endako", 0x1D072,
                        lambda s: maktar_photo_booth(s, p)),
        RC2LocationData("Maktar", "Planet Coordinates to Barlow", 0x1D073,
                        lambda s: maktar_jamming_array(s, p)),
        RC2LocationData("Barlow", "Planet Coordinates to Feltzin", 0x1D074,
                        lambda s: barlow_race_access(s, p)),
    ]

    rc2_platinum_bolts = [
        RC2LocationData("Oozla", "Oozla - Tractor Beam Platinum Bolt", 0x1D000,
                        lambda s: platinum_bolt_1(s, p)),
        RC2LocationData("Oozla", "Oozla - Cave Platinum Bolt", 0x1D001,
                        lambda s: platinum_bolt_2(s, p)),
        RC2LocationData("Maktar", "Maktar - Path to the Arena Platinum Bolt", 0x1D002,
                        lambda s: platinum_bolt_3(s, p)),
        RC2LocationData("Maktar", "Maktar - Jamming Array Platinum Bolt", 0x1D003,
                        lambda s: platinum_bolt_4(s, p)),
        RC2LocationData("Endako", "Endako - Move the crates Platinum Bolt", 0x1D004,
                        lambda s: platinum_bolt_5(s, p)),
        RC2LocationData("Endako", "Endako - Down the ladder Platinum Bolt", 0x1D005,
                        lambda s: platinum_bolt_6(s, p)),
        RC2LocationData("Barlow", "Barlow - Swingshot Platinum Bolt", 0x1D006,
                        lambda s: platinum_bolt_7(s, p)),
        RC2LocationData("Barlow", "Barlow - Race Platinum Bolt", 0x1D007,
                        lambda s: platinum_bolt_8(s, p)),
    ]

    rc2_skill_points = [

    ]

    return [rc2_test_victory] + rc2_gadgets + rc2_planet_coordinates + rc2_platinum_bolts
