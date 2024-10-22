import glob
import re
from pathlib import Path

print('\nUsing glob("*"):\n')
for path in Path("music").glob("*"):
    print("    ", path)

print('\nUsing glob("**"):\n')
for path in Path("music").glob("**"):
    print("    ", path)

print('\nUsing glob("**/*"):\n')
for path in Path("music").glob("**/*"):
    print("    ", path)

print('\nUsing glob("**/"):\n')
for path in Path("music").glob("**/"):
    print("    ", path)

print("\nglob.translate()\n")
pattern = glob.translate("music/**/*.txt")
print(pattern)

print(re.match(pattern, "music/opera/flower_duet.txt"))
print(re.match(pattern, "music/progressive_rock/"))
print(re.match(pattern, "music/progressive_rock/fandango.txt"))
