from Options import Choice, Toggle, StartInventoryPool, PerGameCommonOptions, Range, OptionSet
from dataclasses import dataclass

# Additional Checks/Items #


class PlatinumBoltsItems(Toggle):
    """
    Add Platinum Bolts in the item pool. Adds 40 items.
    """
    display_name = "Platinum Bolts as items"
    default = 1


class NanotechPickupsItems(Toggle):
    """
    Add Nanotech Booster pickups in the item pool. Adds 10 items.
    """
    display_name = "Nanotech pickups as items"
    default = 1


class WeaponsBoughtItems(Toggle):
    """
    Make Weapons bought count from vendors as items in the item pool. Adds 21 items.
    """
    display_name = "Weapons bought as items"


class WeaponModsBoughtItems(Toggle):
    """
    Make Weapon mods bought from Slim's count as items in the item pool. Adds 24 items.
    """
    display_name = "Weapon Mods bought as items"


class ShipUpgradesItems(Toggle):
    """
    Make Ship upgrades count from Slim's as items in the item pool. Adds 11 items.
    Upgrades depending on another are progressive.
    """
    display_name = "Ship upgrades as items"


class ClankItem(Toggle):
    """
    Count Clank as an item in the item pool. Rescuing him in Megapolis will give an item instead.
    Once you receive him, you'll receive his appropriate equipment: Heli-Pack, Thruster-Pack and Hydro-Pack.
    """
    display_name = "Clank as an item"
    default = 1


# TODO See if story events can unlock a planet and go back to the first planet or stop after cutscene
class PlanetItems(Toggle):
    """
    Add Planet Coordinates in the item pool. Adds 18 items. Planet Unlocking must be on.
    Boldan and Aranos (2nd visit) and Siberius and Tabora count as one planet as they are connected by a story event.
    """
    display_name = "Planet Coordinates as items"
    default = 1


class SkillPointsLocations(Toggle):
    """
    Add Skill Points as locations. Adds 30 items.
    "Nano to the max!", "Weapons Envy" and "Nice Ride" will never count as progression.
    """
    display_name = "Skill Points as locations"


class ArenaLocations(Toggle):
    """
    Add Arena challenges as locations.
    Adds 11 checks for the Galactic Gladiators challenges and another 11 checks for the Megacorp Games Arena challenges.
    Required challenges (Electrolyzer, Gravity Boots and Infiltrator) are not added as they already are checks.
    Challenge Mode challenges are not included as they are not available.
    """
    display_name = "Arena Challenges as checks"


class RaceLocations(Toggle):
    """Add Race challenges as locations.
    Adds 4 checks for the Desert Riders challenges and another 4 checks for the Megacorp Games Race challenges.
    The Feltzin System Coordinates challenge is always considered a check as it is a main planet objective"""
    display_name = "Race Challenges as checks"


class SpaceLocations(Toggle):
    """Add Space challenges as locations.
    Adds 4 checks for the Desert Riders challenges and another 4 checks for the Megacorp Games Race challenges.
    The Feltzin System Coordinates challenge is always considered a check as it is a main planet objective"""
    display_name = "Race Challenges as checks"
    default = 1

# Randomizer #


class RandomWeaponStart(Toggle):
    """
    Start the game with 2 random weapons instead of the Lancer and Gravity Bomb.
    """
    display_name = "Start with random weapons"
    default = 1


class RandomWeaponMods(Toggle):
    """
    Randomize the mods a weapon can have, can switch up the Acid/Shock mods or give Lock-On to any weapon.
    """
    display_name = "Randomize mods"

#
# class RandomWeaponsVendors(Toggle):
#     """
#     Randomize the weapons you can acquire in vendors and their price.
#     """
#     display_name = "Randomize weapon vendors"


class RandomWeaponUpgrades(Toggle):
    """
    Randomize weapon upgrades, meaning a weapon could become another weapon once it upgrades.
    Ex: Lancer -> Mini-Nuke
    """
    display_name = "Randomize weapon upgrades"


class AllowMegaUpgrading(Toggle):
    """
    Allow 2nd upgrades to upgrade to their Mega/Ultra variant. These offer more damage and ammo.
    """
    display_name = "Allow Mega/Ultra upgrades"


class RandomizeWeaponAttributes(Choice):
    """
    Randomize weapon attributes like damage, fire rate, ammo capacity, ammo price and projectile speeds.
    No: Keep vanilla weapon attributes.
    Presets: Use tested presets for weapon attributes.
    These are fair changes, but changes the feel of the weapon and how you play with it.
    One weapon can have multiple presets, so a weapon can still be different between runs.
    Fair Random: Weapon attributes will be completely random, but kept fair to not be overpowered/underpowered.
    Mayhem Random: Weapon attributes will be completely random
    with the possibility of being insanely overpowered or insanely underpowered. Total Mayhem!
    """
    display_name = "Randomize Weapon Attributes"
    option_no = 0
    options_presets = 1
    options_fair = 2
    options_mayhem = 3
    default = 0


class PlanetUnlocking(Toggle):
    """
    Determines if planets are unlocked through the vanilla way/coordinate items (if active) or are all unlocked.
    This means you'll need the items to go through Yeedil to complete the game and won't need to find the planet itself.
    """
    display_name = "Planet Unlocking"
    default = 1

# Quality of Life #


class EnableBoltMultiplier(Toggle):
    """
    Enable the Challenge Mode bolt multiplier.
    """
    display_name = "Enable Bolt Multiplier"
    default = 1


class BoltMaxMultiplier(Range):
    """
    Max multiplier possible for the bolt multiplier.
    """
    display_name = "Bolt Max Multiplier"
    range_start = 2
    range_end = 255
    default = 5


class SkipClankSections(Toggle):
    """
    Skip Clank sections entirely. When a Clank section starts, you'll be teleported to the end of it.
    """
    display_name = "Skip Clank Sections"


class RemoveFlashing(Toggle):
    """
    Remove flashing that occurs in the game. Helps with photosensitivity.
    """
    display_name = "Remove Flashing"
    default = 1


# TODO Always on? This is only to enable the possibility to skip, cutscenes are always shown at first.
class SkipCutscenes(Toggle):
    """
    Allow cutscenes to be skipped like in Challenge Mode.
    """
    display_name = "Allow Cutscene Skip"
    default = 1

# Glitches/Tricks #


class ConsiderTricks(OptionSet):
    """Allow these tricks and glitches to be considered for logic."""
    display_name = "Tricks and glitches"
    valid_keys = {
        "First-Person Wall Climbs",
        "Out-of-bounds First Person Wall Climbs",
        "Decoy Glove Clips",
        "Insane Decoy Glove Clips",
        "Hard/Annoying Wrench-Only tricks",
        "Charge Boots tricks"
    }

@dataclass
class RC2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    platinum_bolts_items: PlatinumBoltsItems
    nanotech_pickups_items: NanotechPickupsItems
    weapons_bought_items: WeaponsBoughtItems
    weapon_mods_bought_items: WeaponModsBoughtItems
    ship_upgrades_items: ShipUpgradesItems
    clank_item: ClankItem
    planet_items: PlanetItems

    skill_points_locations: SkillPointsLocations
    arena_locations: ArenaLocations
    race_locations: RaceLocations
    space_locations: SpaceLocations

    random_weapon_start: RandomWeaponStart
    random_weapon_mods: RandomWeaponMods
    random_weapon_upgrades: RandomWeaponUpgrades
    allow_mega_upgrading: AllowMegaUpgrading
    randomize_weapon_attributes: RandomizeWeaponAttributes
    planet_unlocking: PlanetUnlocking

    enable_bolt_multiplier: EnableBoltMultiplier
    bolt_max_multiplier: BoltMaxMultiplier
    skip_clank_sections: SkipClankSections
    remove_flashing: RemoveFlashing
    skip_cutscenes: SkipCutscenes

    consider_tricks: ConsiderTricks
