import imghdr

import magic

print(imghdr.what("python-311.png"))

print(magic.from_file("python-311.png"))
