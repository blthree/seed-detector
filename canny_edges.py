import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage import feature
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte
from skimage.color import rgb2gray
from skimage import io

image = io.imread("C:\\Users\\blthr\\PycharmProjects\\seed-detector\\img\\IMG_20170906_190232691_HDR.jpg")
im = rgb2gray(image[:][1600:4600])

# Compute the Canny filter for two values of sigma
#edges1 = feature.canny(im, sigma=1, low_threshold=10, high_threshold=50)
edges1 = feature.canny(im, sigma=2, low_threshold=0.1, high_threshold=0.4)
#edges2 = feature.canny(im, sigma=3, low_threshold=10, high_threshold=50)
edges2 = feature.canny(im, sigma=2, low_threshold=0.05, high_threshold=0.4)#, high_threshold=50)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)

ax1.imshow(im, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()