# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kevin = Character("Kevin", color="#c8ffc8")
define mom = Character("Mom", color="#c8ffff")
define me = Character("Me", color="#c8c8ff")

# The game starts here.

label start:

    # Some basic narration to start the game

    "You hear your alarm going off, and your mother calling to you."

    mom "It's time to wake up. If I can hear your alarm,
    you can hear it to - let's go!"

    "Reluctantly you open your eyes."

    # Show a background.

    scene bedroom day

    # This shows the basic narration

    "You awaken in your bedroom after a good night's rest. 
    Laying there sleepily, your eyes wander to the clock on your phone."

    me "Yoinks! I'm gonna be late!"

    "You leap out of bed and quickly put on some clothes.
    Grabbing your book bag, you sprint for the door to the living room."

    scene hallway day

    "Your brother is waiting for you in the hall."

    show kevin normal

    kevin "Let's go, loser! We're gonna be late!"

    mom "Got everything, honey?"

    menu:
        "Yes, I've got everything.":
            jump follow_kevin

        "Wait, I forgot my phone!":
            jump check_room

label check_room:

    me "Wait! My phone!"

    kevin "Whatever. See you outside!"

    "You sprint back to your room to get your phone."

    scene bedroom day

    "You grab the phone from the nightstand and sprint back to the hall."

    scene hallway day

    "True to his word, Kevin is already outside."

    jump outside

label follow_kevin:

    kevin "Then let's go!"

    "You follow Kevin out to the street."

label outside:

    scene street

    show kevin normal

    kevin "About time you got here. Let's Go!"

    # This ends the game
    return
