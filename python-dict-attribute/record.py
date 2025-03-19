import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


class Record:
    def __init__(self, **fields):
        logging.info(f"[INIT] Creating record with fields: {fields}")
        self.__dict__.update(fields)

    def __getattribute__(self, key):
        if key == "__dict__":
            return super().__getattribute__(key)
        value = super().__getattribute__(key)
        logging.info(f"[GET] Accessing '{key}' → {value}")
        return value

    def __setattr__(self, key, value):
        if key in self.__dict__:
            logging.info(f"[UPDATE] Modifying '{key}' → {value}")
        else:
            logging.info(f"[SET] Creating '{key}' → {value}")
        self.__dict__[key] = value

    def __delattr__(self, key):
        if key in self.__dict__:
            logging.info(f"[DEL] Deleting '{key}'")
            del self.__dict__[key]
        else:
            logging.warning(
                f"[DEL] Attempted to delete non-existent field '{key}'"
            )


jane = Record(first_name="Jane", last_name="Doe", age=25)

# Access
print(jane.first_name)
print(jane.age)

# Mutations
jane.age = 26
jane.job = "Software Engineer"
print(jane.__dict__)

# Deletion
del jane.age
print(jane.__dict__)
