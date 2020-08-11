"""
Items for the AdventureLib Game
"""

# Import the AdventureLib library
from adventurelib import *

# All items have some basic properties
Item.color = "undistiguished"
Item.description = "a generic thing"
Item.edible = False
Item.wearable = False

# Create our "flavor" items
# Apple
apple = Item("small red apple", "apple")
apple.color = "red"
apple.description = "a small ripe red apple"
apple.edible = True
apple.wearable = False

cloak = Item("wool cloak", "cloak")
cloak.color = "grey tweed"
cloak.description = (
    "a grey tweed cloak, heavy enough to keep the wind and rain at bay"
)
cloak.edible = False
cloak.wearable = True

slug = Item("slimy brown slug", "slug")
slug.color = "slimy brown"
slug.description = "a fat, slimy, brown slug"
slug.edible = True
slug.wearable = False

# Create the real items we need
wooden_sword = Item("wooden sword", "sword")
wooden_sword.color = "brown"
wooden_sword.description = (
    "a small wooden practice sword, not even sharp enough to cut milk"
)
wooden_sword.edible = False
wooden_sword.wearable = False
wooden_sword.damage = 4
wooden_sword.bonus = 0

steel_sword = Item("steel sword", "sword")
steel_sword.color = "steely grey"
steel_sword.description = (
    "a finely made steel sword, honed to a razor edge, ready for blood"
)
steel_sword.edible = False
steel_sword.wearable = False
steel_sword.damage = 10
steel_sword.bonus = 0
