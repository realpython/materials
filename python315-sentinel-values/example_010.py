MISSING = sentinel("MISSING")
print(bool(MISSING))
print(hash(MISSING))
config = {MISSING: "unset", "timeout": 30}
print(config[MISSING])
print(MISSING in {MISSING, 1, 2})
print(MISSING == sentinel("MISSING"))
