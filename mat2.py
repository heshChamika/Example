import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
image = img.imread('chamika.jpg')
plt.imshow(image)
print(image.shape)