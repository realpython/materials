##
## Code for the interactions in town
##

## Backgrounds
image path = "1_forest_a.jpg"
image wizard hut = "BG600a_1280.jpg"

# Characters
image wizard greeting = "wizard1.png"
image wizard happy = "wizard2.png"
image wizard confused = "wizard3.png"
image wizard shocked = "wizard4.png"

label path:

    scene path
    with fade

    show expression current_weapon at left

    "You pick up the tracks as you follow the path through the woods."

    jump giant_battle
