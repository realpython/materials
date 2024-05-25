"""
Rooms for the adventurelib game
"""

# Import the library contents
import adventurelib as adv

# And your characters
import adventurelib_game_characters

# Import your items as well
import adventurelib_game_items


# Create a subclass of Rooms to track some custom properties
class GameArea(adv.Room):
    def __init__(self, description: str):

        super().__init__(description)

        # All areas can have locked exits
        self.locked_exits = {
            "north": False,
            "south": False,
            "east": False,
            "west": False,
        }
        # All areas can have items in them
        self.items = adv.Bag()

        # All areas can have characters in them
        self.characters = adv.Bag()

        # All areas may have been visited already
        # If so, you can print a shorter description
        self.visited = False

        # Which means each area needs a shorter description
        self.short_desc = ""

        # Each area also has a very short title for the prompt
        self.title = ""


# Your home
home = GameArea(
    """
You wake as the sun streams in through the single
window into your small room. You lie on your feather bed which
hugs the north wall, while the remains of last night's
fire smolders in the center of the room.

Remembering last night's discussion with the council, you
throw back your blanket and rise from your comfortable
bed. Cold water awaits you as you splash away the night's
sleep, grab an apple to eat, and prepare for the day.
"""
)
home.title = "Home"
home.short_desc = "This is your home."


# Hamlet
hamlet = GameArea(
    """
From the center of your small hamlet, you can see every other
home. It doesn't really even have an official name --- folks
around here just call it Home.

The council awaits you as you approach. Elder Barron beckons you
as you exit your home.
"""
)
hamlet.title = "Hamlet"
hamlet.short_desc = "You are in the hamlet."

# Fork in road
fork = GameArea(
    """
As you leave your hamlet, you think about how unprepared you
really are. Your lack of experience and pitiful equipment
are certainly no match for whatever has been stealing
the villages livestock.

As you travel, you come across a fork in the path. The path of
the livestock thief continues east. However, you know
the village of Dunhaven lies to the west, where you may
get some additional help.
"""
)
fork.title = "Fork in road"
fork.short_desc = "You are at a fork in the road."

# Village of Dunhaven
village = GameArea(
    """
A short trek up the well-worn path brings you the village
of Dunhaven. Larger than your humble Home, Dunhaven sits at
the end of a supply route from the capitol. As such, it has
amenities and capabilities not found in the smaller farming
communities.

As you approach, you hear the clang-clang of hammer on anvil,
and inhale the unmistakable smell of the coal-fed fire of a
blacksmith shop to your south.
"""
)
village.title = "Village of Dunhaven"
village.short_desc = "You are in the village of Dunhaven."

# Blacksmith shop
blacksmith_shop = GameArea(
    """
As you approach the blacksmith, the sounds of the hammer become
clearer and clearer. Passing the front door, you head towards
the sound of the blacksmith, and find her busy at the furnace.
"""
)
blacksmith_shop.title = "Blacksmith Shop"
blacksmith_shop.short_desc = "You are in the blacksmith shop."

# Side path away from fork
side_path = GameArea(
    """
The path leads away from the fork to Dunhaven. Fresh tracks of
something big, dragging something behind it, lead away to the south.
"""
)
side_path.title = "Side path"
side_path.short_desc = "You are standing on a side path."

# Wizard's Hut
wizard_hut = GameArea(
    """
The path opens into a shaded glen. A small stream wanders down the
hills to the east and past an unassuming hut. In front of the hut,
the local wizard Trent sits smoking a long clay pipe.
"""
)
wizard_hut.title = "Wizard's Hut"
wizard_hut.short_desc = "You are at the wizard's hut."

# Cave mouth
cave_mouth = GameArea(
    """
The path from Trent's hut follows the stream for a while before
turning south away from the water. The trees begin closing overhead,
blocking the sun and lending a chill to the air as you continue.

The path finally terminates at the opening of a large cave. The
tracks you have been following mix and mingle with others, both
coming and going, but all the same. Whatever has been stealing
your neighbor's livestock lives here, and comes and goes frequently.
"""
)
cave_mouth.title = "Cave Mouth"
cave_mouth.short_desc = "You are at the mouth of large cave."

# Cave of the Giant
giant_cave = GameArea(
    """
You take a few tentative steps into the cave. It feels much warmer
and more humid than the cold sunless forest air outside. A steady
drip of water from the rocks is the only sound for a while.

You begin to make out a faint light ahead. You hug the wall and
press on, as the light becomes brighter. You finally enter a
chamber at least 20 meters across, with a fire blazing in the center.
Cages line one wall, some empty, but others containing cows and
sheep stolen from you neighbors. Opposite them are piles of the bones
of the creatures unlucky enough to have already been devoured.

As you look around, you become aware of another presence in the room.
"""
)
giant_cave.title = "Cave of the Giant"
giant_cave.short_desc = "You are in the giant's cave."

# Set up the paths between areas
home.south = hamlet
hamlet.south = fork
fork.west = village
fork.east = side_path
village.south = blacksmith_shop
side_path.south = wizard_hut
wizard_hut.west = cave_mouth
cave_mouth.south = giant_cave

# Lock some exits, since you can't leave until something else happens
hamlet.locked_exits["south"] = True
wizard_hut.locked_exits["west"] = True

# Place items in different areas
# These are just for flavor
home.items.add(adventurelib_game_items.apple)
fork.items.add(adventurelib_game_items.cloak)
cave_mouth.items.add(adventurelib_game_items.slug)

# Place characters where they should be
hamlet.characters.add(adventurelib_game_characters.elder_barron)
blacksmith_shop.characters.add(adventurelib_game_characters.blacksmith)
wizard_hut.characters.add(adventurelib_game_characters.wizard_trent)
giant_cave.characters.add(adventurelib_game_characters.giant)
