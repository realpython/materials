##
## Code for the interactions in town
##

## Backgrounds
image distant town = "4_road_a.jpg"
image within town = "3_blacksmith_a.jpg"

# Characters
image blacksmith greeting = "blacksmith1.png"
image blacksmith confused = "blacksmith2.png"
image blacksmith happy = "blacksmith3.png"
image blacksmith shocked = "blacksmith4.png"

label town:

    scene distant town
    with fade

    show expression current_weapon at left

    "Crossing the bridge, you stride away from the river along a
    well worn path. The way is pleasant, and you find yourself humming
    a tune as you break into a small clearing."

    "From here, you can make out the county seat of Fetheron.
    You feel confident you can find help for your quest here."

    scene within town
    with fade

    show expression current_weapon at left

    "As you enter town, you immediately begin seeking the local blacksmith.
    After asking one of the townsfolk, you find the smithy on the far
    south end of town. You approach the smithy,
    smelling the smoke of the furnace long before you hear
    the pounding of hammer on steel."

    player "Hello! Is the smith in?"

    smith "Who wants to know?"

    show blacksmith greeting

    "The blacksmith appears from her bellows.
    She greets you with a warm smile."

    smith "Oh, hello! You're from the next town over, right?"

    menu:
        "Yes, from the other side of the river.":
            show blacksmith happy

            smith "I thought I recognized you. Nice to see you!"

        "Look, I don't have time for pleasantries, can we get to business?":
            show blacksmith shocked

            smith "Hey, just trying to make conversation"

    smith "So, what can I do for you?"

    player "I need a better weapon than this wooden thing."

    show blacksmith confused

    smith "Are you going to be doing something dangerous?"

    player "Have you heard about the missing livestock in town?"

    smith "Of course. Everyone has. What do you know about it?"

    player "Well, I'm tracking whatever took them from our town."

    smith "Oh, I see. So you want something better to fight with!"

    player "Exactly! Can you help?"

    smith "I've got just the thing. Been working on it for a while,
    but didn't know what to do with it. Now I know."

    "Miranda walks back past the furnace to a small rack.
    On it, a gleaming steel sword rests.
    She picks it up and walks back to you."

    smith "Will this do?"

    menu:
        "It's perfect!":
            show blacksmith happy

            smith "Wonderful! Give me the wooden one -
            I can use it in the furnace!"

            $ current_weapon = "steel sword"
            $ base_damage = 6
            $ multiplier = 2

        "Is that piece of junk it?":
            show blacksmith confused

            smith "I worked on this for weeks.
            If you don't want it, then don't take it."

    # Show the current weapon
    show expression current_weapon at left

    smith "Anything else?"

    player "Nope, that's all."

    smith "Alright. Good luck!"

    scene distant town
    with fade

    show expression current_weapon at left

    "You make your way back through town.
    Glancing back at the town, you wonder if
    you can keep them safe too."

    jump path
