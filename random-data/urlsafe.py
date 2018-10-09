import binascii
import math
import os

# binascii.b2a_base64(data, *, newline=True)
#     Convert binary data to a line of ASCII characters in base64 coding.
#     The return value is the converted line, including a newline char if
#     newline is true. The output of this function conforms to RFC 3548.


_urlsafe_encode_translation = bytes.maketrans(b"+/", b"-_")  # bitwise mapping


def token_urlsafe(nbytes):
    tok = os.urandom(nbytes)

    # this mimics the steps in `base64.urlsafe_b64encode()`
    encoded = binascii.b2a_base64(tok, newline=False)
    translated = encoded.translate(_urlsafe_encode_translation)
    res = translated.rstrip(b"=").decode("ascii")
    return tok, encoded, translated, res


def tok_to_trans(length):
    return math.ceil(length * 8 / 6)


if __name__ == "__main__":
    for nbytes in range(10):
        d = dict(zip(("tok", "enc", "trans", "res"), token_urlsafe(nbytes)))
        print(d)
        print("\tlengths:", {k: len(v) for k, v in d.items()})

    print()
    print("Mapping of original `nbytes` to token length:")
    for j in range(10):
        print(j, tok_to_trans(j), sep="\t")
