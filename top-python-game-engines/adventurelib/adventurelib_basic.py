"""
Basic "Hello, World!" program in adventurelib

This program is designed to demonstrate the basic capabilities
of adventurelib. It will:
- Create a simple three-room world
- Add a single inventory item
- Require that inventory item to move to the final room
"""

# Import the library contents
import adventurelib as adv

# Define your rooms
bedroom = adv.Room(
    """
You are in your bedroom. The bed is unmade, but otherwise
it's clean. Your dresser is in the corner, and a desk is
under the window.
"""
)

living_room = adv.Room(
    """
The living room stands bright and empty. The TV is off,
and the sun shines brightly through the curtains.
"""
)

front_porch = adv.Room(
    """
The creaky boards of your front porch welcome you as an
old friend. Your front door mat reads 'Welcome'.
"""
)

# Define the connections between the rooms
bedroom.south = living_room
living_room.east = front_porch

# Define a constraint to move from the bedroom to the living room
# If the door between the living room and front porch door is locked,
# you can't exit
living_room.locked = {"east": True}

# None of the other rooms have any locked doors
bedroom.locked = dict()
front_porch.locked = dict()

# Set the starting room as the current room
current_room = bedroom


# Define functions to use items
def unlock_living_room(current_room):

    if current_room == living_room:
        print("You unlock the door.")
        current_room.locked["east"] = False
    else:
        print("There is nothing to unlock here.")


# Create your items
key = adv.Item("a front door key", "key")
key.use_item = unlock_living_room

# Create empty Bags for room contents
bedroom.contents = adv.Bag()
living_room.contents = adv.Bag()
front_porch.contents = adv.Bag()

# Put the key in the bedroom
bedroom.contents.add(key)

# Set up your current empty inventory
inventory = adv.Bag()


# Define your movement commands
@adv.when("go DIRECTION")
@adv.when("north", direction="north")
@adv.when("south", direction="south")
@adv.when("east", direction="east")
@adv.when("west", direction="west")
@adv.when("n", direction="north")
@adv.when("s", direction="south")
@adv.when("e", direction="east")
@adv.when("w", direction="west")
def go(direction: str):
    """Processes your moving direction

    Arguments:
        direction {str} -- which direction does the player want to move
    """

    # What is your current room?
    global current_room

    # Is there an exit in that direction?
    next_room = current_room.exit(direction)
    if next_room:
        # Is the door locked?
        if direction in current_room.locked and current_room.locked[direction]:
            print(f"You can't go {direction} --- the door is locked.")
        else:
            current_room = next_room
            print(f"You go {direction}.")
            look()

    # No exit that way
    else:
        print(f"You can't go {direction}.")


# How do you look at the room?
@adv.when("look")
def look():
    """Looks at the current room"""

    # Describe the room
    adv.say(current_room)

    # List the contents
    for item in current_room.contents:
        print(f"There is {item} here.")

    # List the exits
    print(f"The following exits are present: {current_room.exits()}")


# How do you look at items?
@adv.when("look at ITEM")
@adv.when("inspect ITEM")
def look_at(item: str):

    # Check if the item is in your inventory or not
    obj = inventory.find(item)
    if not obj:
        print(f"You don't have {item}.")
    else:
        print(f"It's an {obj}.")


# How do you pick up items?
@adv.when("take ITEM")
@adv.when("get ITEM")
@adv.when("pickup ITEM")
def get(item: str):
    """Get the item if it exists

    Arguments:
        item {str} -- The name of the item to get
    """
    global current_room

    obj = current_room.contents.take(item)
    if not obj:
        print(f"There is no {item} here.")
    else:
        print(f"You now have {item}.")
        inventory.add(obj)


# How do you use an item?
@adv.when("unlock door", item="key")
@adv.when("use ITEM")
def use(item: str):
    """Use an item, consumes it if used

    Arguments:
        item {str} -- Which item to use
    """

    # First, do you have the item?
    obj = inventory.take(item)
    if not obj:
        print(f"You don't have {item}")

    # Try to use the item
    else:
        obj.use_item(current_room)


if __name__ == "__main__":
    # Look at the starting room
    look()

    adv.start()
