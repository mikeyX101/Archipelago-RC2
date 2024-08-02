from typing import List

from BaseClasses import Tutorial, Region, ItemClassification
from worlds.AutoWorld import World, WebWorld

from .Items import get_rc2_items, RC2Item, get_rc2_item_groups
from .Locations import get_rc2_locations, RC2Location, RC2LocationData
from .Options import RC2Options
from .Regions import rc2_regions
from ..generic.Rules import add_rule, set_rule, add_item_rule, forbid_item


class RC2WebWorld(WebWorld):
    theme = "stone"
    rich_text_options_doc = True
    tutorials = [
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up Ratchet and Clank Going Commando for Archipelago.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["mikeyX"],
        )
    ]


class RC2World(World):
    """
    Ratchet and Clank returns in a new adventure to save the Bogon galaxy from the Protopet menace.
    """

    game = "Ratchet and Clank Going Commando"
    web = RC2WebWorld()
    options_dataclass = RC2Options
    options: RC2Options

    #settings: typing.ClassVar[RC2Settings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = {item.name: item.code for item in get_rc2_items()}
    location_name_to_id = {loc.name: loc.code for loc in get_rc2_locations()}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = get_rc2_item_groups()

    def generate_early(self) -> None:
        #self.multiworld.push_precollected(self.create_item("FPWC"))
        self.multiworld.push_precollected(self.create_item("DGC"))
        self.multiworld.push_precollected(self.create_item("Charge Tricks"))

        self.multiworld.push_precollected(self.create_item("Lancer"))

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        ship_region = Region("Ship", self.player, self.multiworld)
        menu_region.connect(ship_region, "Aranos1 Done", lambda state: (
            state.has_group("Planet Coordinates", self.player))
        )
        self.multiworld.regions.append(ship_region)

        all_locations: list[RC2LocationData] = get_rc2_locations(self)
        for region in rc2_regions:
            world_region = Region(region, self.player, self.multiworld)
            region_locations = list(loc for loc in all_locations if loc.planet == region)
            world_region.add_locations({loc.name: loc.code for loc in region_locations}, RC2Location)
            self.multiworld.regions.append(world_region)

            if region == "Aranos1":
                menu_region.connect(world_region)
                world_region.connect(ship_region, "Ship Access", lambda state: (
                    state.has_group("Planet Coordinates", self.player))
                )
            else:
                ship_region.connect(world_region, f"To {region}", lambda state: (
                    state.has(f"Planet Coordinates to {region}", self.player))
                )

        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "rc2_base_world.puml")

    def create_item(self, item: str) -> RC2Item:
        # this is called when AP wants to create an item by name (for plando) or when you call it from your own code
        rc2_item = next(rc2_item for rc2_item in get_rc2_items() if rc2_item.name == item)
        return RC2Item(rc2_item.name, rc2_item.classification, rc2_item.code, self.player)

    def create_event(self, event: str) -> RC2Item:
        return RC2Item(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player options, e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If an item can't have duplicates it has to be excluded manually.

        # List of items to exclude, as a copy since it will be destroyed below

        exclude = [item for item in self.multiworld.precollected_items[self.player]]

        rc2_item_names = [rc2_item.name for rc2_item in get_rc2_items()]
        for item in map(self.create_item, rc2_item_names):
            if item in exclude:
                exclude.remove(item)  # this is destructive. create unique list above
                #self.multiworld.itempool.append(self.create_item("nothing"))
            elif item.name != "Planet Coordinates to Feltzin":
                self.multiworld.itempool.append(item)

        # itempool and number of locations should match up.
        # If this is not the case we want to fill the itempool with junk.
        junk = 0  # calculate this based on player options
        self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]

    def set_rules(self) -> None:
        all_locations: list[RC2LocationData] = get_rc2_locations(self)
        for loc in all_locations:
            if loc.planet == "Aranos1":
                add_item_rule(self.multiworld.get_location(loc.name, self.player), lambda item: (
                    item.name in self.item_name_groups["Planet Coordinates"])
                )
            else:
                set_rule(self.multiworld.get_location(loc.name, self.player), loc.rule)

        # Stop planets from having their own coordinates
        for region in rc2_regions:
            region_locations = list(loc for loc in all_locations if loc.planet == region)
            coord = f"Planet Coordinates to {region}"
            for loc in region_locations:
                forbid_item(self.multiworld.get_location(loc.name, self.player), coord, self.player)
        #forbid_item(self.multiworld.get_location("Planet Coordinates to Oozla", self.player), "Planet Coordinates to Barlow", self.player)

        self.multiworld.get_location("Planet Coordinates to Feltzin", self.player).place_locked_item(self.create_item("Planet Coordinates to Feltzin"))
        self.multiworld.get_location("Victory", self.player).place_locked_item(self.create_event("Victory"))
        self.multiworld.g()
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def post_fill(self) -> None:
        print("holy damn")
