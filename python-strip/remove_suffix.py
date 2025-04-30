from pathlib import Path

filename = "txt_transcript.txt"

# Incorrect: .strip() doesn't remove sequences
print(filename.strip(".txt"))
# Correct: Use .removesuffix() for this task
print(filename.removesuffix(".txt"))

# If the suffix isn't found, it returns the original string
print(filename.removesuffix(".mp3"))

# Better to use pathlib.Path for file operations
print(Path(filename).stem)
