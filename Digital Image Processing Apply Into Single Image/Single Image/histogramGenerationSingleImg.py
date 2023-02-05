import cv2
from matplotlib import pyplot as plt

path = 'imageDataset/github pp.jpg'

img = cv2.imread(path, 0)

plt.hist(img.ravel(),256,[0,256])
plt.show()
