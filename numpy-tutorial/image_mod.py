import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitten.png")
print(type(img))
print(img.shape)

# => numpy.ndarray
# => (866, 1280, 3)

output = img.copy()  # The original image is read-only!
output[:, :, :2] = 0  # Drop out Red and Green channels
mpimg.imsave("blue.jpg", output)

averages = img.mean(axis=2)  # Take the average of each R, G, and B
mpimg.imsave("bad-gray.jpg", averages, cmap="gray")

weights = np.array([0.3, 0.59, 0.11])
greyscale = np.dot(img, weights)
mpimg.imsave("good-gray.jpg", greyscale, cmap="gray")
