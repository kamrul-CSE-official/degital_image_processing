import cv2
import os

filePath = "imageDataset/Ak"
for fileName in os.listdir(filePath):
    if fileName.endswith(".jpg") or fileName.endswith(".png"):
        file_path = os.path.join(filePath, fileName)
    im = cv2.imread(file_path, 0)
    img = cv2.resize(im, (400, 400))
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()