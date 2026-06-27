"""Reshape a 3D color image into a 2D triptych of its color channels.

Run this script from the folder that contains poppy.jpg. Each reshaped
image opens in your default image viewer.
"""

import numpy as np
from PIL import Image

with Image.open("poppy.jpg") as photo:
    image_array = np.array(photo)

print(f"Image shape: {image_array.shape}")
height, width, _ = image_array.shape

# The default order="C" interleaves each pixel's color channels
triptych_c = image_array.reshape((height, 3 * width))
print(f"Reshaped shape: {triptych_c.shape}")
Image.fromarray(triptych_c).show()

# order="F" places the red, green, and blue channels side by side
triptych_f = image_array.reshape((height, 3 * width), order="F")
Image.fromarray(triptych_f).show()
