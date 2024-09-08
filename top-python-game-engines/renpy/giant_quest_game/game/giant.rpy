##
## Code for the giant battle
##

## Backgrounds
image forest = "forest_hill_night.jpg"

# Characters
image giant greeting = "giant1.png"
image giant unhappy = "giant2.png"
image giant angry = "giant3.png"
image giant hurt = "giant4.png"

# Text of the giant encounter
label giant_battle:

    scene forest
    with fade

    show expression current_weapon at left

    "As you follow the tracks down the path, night falls.
    You hear sounds in the distance:
    cows, goats, sheep. You've found the livestock!"

    show giant greeting

    "As you approach the clearing and see your villages livestock,
    a giant appears."

    giant "Who are you?"

    player "I've come to get our livestock back."

    giant "You and which army, little ... whatever you are?"

    show giant unhappy

    "The giant bears down on you - the battle is joined!"

python:

    def show_giant_condition(giant_hp):
        if giant_hp < 10:
            renpy.say(None, "The giant staggers, his eyes unfocused.")
        elif giant_hp < 20:
            renpy.say(None, "The giant's steps become more unsteady.")
        elif giant_hp < 30:
            renpy.say(
                None, "The giant sweats and wipes the blood from his brow."
            )
        elif giant_hp < 40:
            renpy.say(
                None,
                "The giant snorts and grits his teeth against the pain.",
            )
        else:
            renpy.say(
                None,
                "The giant smiles and readies himself for the attack.",
            )

    def show_player_condition(player_hp):
        if player_hp < 4:
            renpy.say(
                None,
                "Your eyes lose focus on the giant as you sway unsteadily.",
            )
        elif player_hp < 8:
            renpy.say(
                None,
                "Your footing becomes less steady as you swing your sword sloppily.",
            )
        elif player_hp < 12:
            renpy.say(
                None,
                "Blood mixes with sweat on your face as you wipe it from your eyes.",
            )
        elif player_hp < 16:
            renpy.say(
                None,
                "You bite down as the pain begins to make itself felt.",
            )
        else:
            renpy.say(None, "You charge into the fray valiantly!")

    def fight_giant():

        # Default values
        giant_hp = 50
        player_hp = 20
        giant_damage = 4

        battle_over = False
        player_wins = False

        # Keep swinging until something happens
        while not battle_over:

            renpy.say(
                None,
                "You have {0} hit points. Do you want to fight or flee?".format(
                    player_hp
                ),
                interact=False,
            )
            battle_over = renpy.display_menu(
                [("Fight!", False), ("Flee!", True)]
            )

            if battle_over:
                player_wins = False
                break

            # The player gets a swing
            player_attack = (
                randint(1, base_damage + 1) * multiplier + additional
            )
            renpy.say(
                None,
                "You swing your {0}, doing {1} damage!".format(
                    current_weapon, player_attack
                ),
            )
            giant_hp -= player_attack

            # Is the giant dead?
            if giant_hp <= 0:
                battle_over = True
                player_wins = True
                break

            show_giant_condition(giant_hp)

            # Then the giant tries
            giant_attack = randint(0, giant_damage)
            if giant_attack == 0:
                renpy.say(
                    None,
                    "The giant's arm whistles harmlessly over your head!",
                )
            else:
                renpy.say(
                    None,
                    "The giant swings his mighty fist, and does {0} damage!".format(
                        giant_attack
                    ),
                )
                player_hp -= giant_attack

            # Is the player dead?
            if player_hp <= 0:
                battle_over = True
                player_wins = False

            show_player_condition(player_hp)

        # Return who died
        return player_wins

    # fight_giant returns True if the player wins.
    if fight_giant():
        renpy.jump("player_wins")
    else:
        renpy.jump("giant_wins")

label player_wins:

    "The giant's eyes glaze over as he falls heavily to the ground.
    The earth shakes as his bulk lands face down,
    and his death rattle fills the air."

    hide giant

    "You are victorious! The land is safe from the giant!"

    return

label giant_wins:

    "The giant takes one last swing, knocking you down.
    Your vision clouds, and you see the ground rising to meet you.
    As you slowly lose consciousness, your last vision is
    the smiling figure of the giant as he advances on you."

    "You have lost!"

    return
