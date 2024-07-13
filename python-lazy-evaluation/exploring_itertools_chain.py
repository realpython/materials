"""
Exploring the itertools module
"""

import itertools
import sys

# Explore itertools.chain()
first_team = ["Sarah", "Matt", "Jim", "Denise", "Kate"]
second_team = ["Mark", "Zara", "Mo", "Jennifer", "Owen"]

for name in itertools.chain(first_team, second_team):
    print(name)

# Verify changes in reference counts
print(sys.getrefcount(first_team))

quiz_team = itertools.chain(first_team, second_team)
print(sys.getrefcount(first_team))

for name in quiz_team:
    print(name)

print(sys.getrefcount(first_team))
