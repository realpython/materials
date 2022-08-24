err = ValueError(678)
err.add_note("Enriching Exceptions with Notes")
err.add_note("Python 3.11")

print(f"{err.__notes__ = }")

print("", " Loop over notes ".center(60, "-"), sep="\n")
for note in err.__notes__:
    print(note)

print("", " Notes are added to traceback ".center(60, "-"), sep="\n")
raise err
