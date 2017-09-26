from skimage import io
import matplotlib.pyplot as plt

image = io.imread("C:\\Users\\blthr\\PycharmProjects\\seed-detector\\img\\IMG_20170906_190232691_HDR.jpg")
i2 = image[:][1600:4600]
#io.imshow(image)
f1 = plt.figure()
plt.imshow(i2)
plt.show()