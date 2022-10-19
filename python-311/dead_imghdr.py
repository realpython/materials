import imghdr

import magic

print(imghdr.what("python-311.jpg"))

print(magic.from_file("python-311.jpg"))
