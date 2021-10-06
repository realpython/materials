"""
Characters for the AdventureLib Game
"""

# Import the AdventureLib library
import adventurelib as adv

# All characters have some properties
adv.Item.greeting = ""
adv.Item.context = ""

# Our characters
elder_barron = adv.Item("Elder Barron", "elder", "barron")
elder_barron.description = """Elder Barron, a tall distinguished member
of the community. His steely grey hair and stiff beard inspire confidence."""
elder_barron.greeting = "I have some information for you. Would you like to hear it?"
elder_barron.context = "elder"

blacksmith = adv.Item("Alanna Smith", "Alanna", "blacksmith", "smith")
blacksmith.description = """Alanna the blacksmith stands just 1.5m tall,
and her strength lies in her arms and heart"""
blacksmith.greeting = "Oh, hi! I've got some stuff for sale. Do you want to see it?"
blacksmith.context = "blacksmith"

wizard_trent = adv.Item("Trent the Wizard", "Trent", "wizard")
wizard_trent.description = """Trent's wizardly studies have apparently
aged him past his years, but they have also preserved his life longer than
expected."""
wizard_trent.greeting = (
    "It's been a long time since I've had a visitor? Do you seek wisdom?"
)
wizard_trent.context = "wizard"

giant = adv.Item("hungry giant", "giant")
giant.description = """Almost four meters of hulking brutish strength
stands before you, his breath rank with rotten meat, his mangy hair
tangled and matted"""
giant.greeting = "Argh! Who dares invade my home? Prepare to defend yourself!"
giant.context = "giant"
