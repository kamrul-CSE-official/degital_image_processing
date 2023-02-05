import cv2
from matplotlib import pyplot as plt
import os

filePath = "imageDataset/Ak"
for fileName in os.listdir(filePath):
    if fileName.endswith(".jpg") or fileName.endswith(".png"):
        file_path = os.path.join(filePath, fileName)
    im = cv2.imread(file_path, 0)  # Read image

    img = cv2.resize(im, (400, 400))

    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
