import hashlib
import hmac

import dill


def safe_dump(obj, file, secret_key):
    serialized_data = dill.dumps(obj)
    signature = sign(serialized_data, secret_key)
    dill.dump(signature, file)
    file.write(serialized_data)


def safe_load(file, secret_key):
    signature = dill.load(file)
    serialized_data = file.read()
    if signature == sign(serialized_data, secret_key):
        return dill.loads(serialized_data)
    raise dill.UnpicklingError("invalid digital signature")


def sign(message, secret_key, algorithm=hashlib.sha256):
    return hmac.new(secret_key, message, algorithm).digest()
