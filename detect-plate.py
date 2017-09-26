from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage import io

import matplotlib.pyplot as plt
image = io.imread("C:\\Users\\blthr\\PycharmProjects\\seed-detector\\img\\IMG_20170906_190232691_HDR.jpg")
image = image[:][1600:4600]
print('loaded')
#image = data.hubble_deep_field()[0:500, 0:500]
image_gray = rgb2gray(image)

blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
print('log step 1 done')
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
print('log done')
blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.1)
print('dog step 1 done')
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
print('dog done')
blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)
print('doh done')
blobs_list = [blobs_log, blobs_dog, blobs_doh]
colors = ['yellow', 'lime', 'red']
titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
sequence = zip(blobs_list, colors, titles)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True,
                         subplot_kw={'adjustable': 'box-forced'})
ax = axes.ravel()

for idx, (blobs, color, title) in enumerate(sequence):
    ax[idx].set_title(title)
    ax[idx].imshow(image, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()
print("showing plot")
plt.tight_layout()
plt.show()