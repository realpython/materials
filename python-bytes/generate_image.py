import numpy as np
from PIL import Image

pixels = np.random.default_rng().random((1080, 1920, 3)) * 255
image = Image.fromarray(pixels.astype("uint8"))
image.save("image.png")
