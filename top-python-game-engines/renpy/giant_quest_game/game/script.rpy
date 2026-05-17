#
# Complete game in Ren'Py
# 
# This game demonstrates some of the more advanced features of
# Ren'Py, including:
# - Multiple sprites
# - Handling user input
# - Selecting alternate outcomes
# - Tracking score and inventory
# 

## Declare characters used by this game. The color argument colorizes the
## name of the character.
define player = Character("Me", color="#c8ffff")
define smith = Character("Miranda, village blacksmith", color="#99ff9c")
define wizard = Character("Endeavor, cryptic wizard", color="#f4d3ff")
define giant = Character("Maull, terrifying giant", color="#ff8c8c")

## Images used in the game
# Backgrounds
image starting path = "BG10a_1280.jpg"
image crossroads = "BG19a01_1280.jpg"

# Items
image wooden sword = "SwordWood.png"
image steel sword = "Sword.png"
image enchanted sword = "SwordT2.png"

## Default settings
# What is the current weapon?
default current_weapon = "wooden sword"

# What is the weapon damage?
# These change when the weapon is upgraded or enchanted
default base_damage = 4
default multiplier = 1
default additional = 0

# Did they cross the bridge to town?
default cross_bridge = False

# You need this for the giant battle later

init python:
    from random import randint

# The game starts here.

label start:

    # Show the initial background.

    scene starting path
    with fade

    # Begin narration

    "Growing up in a small hamlet was boring, but reliable and safe. 
    At least, it was until the neighbors began complaining of missing
    livestock. That's when the evening patrols began."

    "While on patrol just before dawn, your group noticed broken fence
    around a cattle paddock. Beyond the broken fence,
    a crude trail had been blazed to a road leading away from town."

    # Show the current weapon
    show expression current_weapon at left
    with moveinleft

    "After reporting back to the town council, it was decided that you
    should follow the tracks to discover the fate of the livestock.
    You picked up your only weapon, a simple wooden practice sword,
    and set off."

    scene crossroads
    with fade

    show expression current_weapon at left

    "Following the path, you come to a bridge across the river."

    "Crossing the bridge will take you to the county seat,
    where you may hear some news or get supplies.
    The tracks, however, continue straight on the path."

    menu optional_name:
        "Which direction will you travel?"

        "Cross the bridge":
            $ cross_bridge = True
            jump town
        "Continue on the path":
            jump path

    "Your quest is ended!"

    return
