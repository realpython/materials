UNSET = sentinel("UNSET")
INHERIT = sentinel("INHERITED")  # Name doesn't match the variable


class Config:
    AUTO = sentinel("Config.AUTO")
    # Some code here...
    NO_LIMIT = sentinel("NO_LIMIT")  # Forgot the qualified name
