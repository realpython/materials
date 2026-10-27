import pickle
from config import Config, INHERIT, UNSET

print(pickle.loads(pickle.dumps(UNSET)) is UNSET)
print(pickle.loads(pickle.dumps(Config.AUTO)) is Config.AUTO)
# These names intentionally don't match their module/class bindings.
for value in (INHERIT, Config.NO_LIMIT):
    try:
        pickle.dumps(value)
    except pickle.PicklingError as error:
        print(f"Expected PicklingError: {error}")
