import cv2

import os

filePath = "imageDataset/Ak"
for fileName in os.listdir(filePath):
    if fileName.endswith(".jpg") or fileName.endswith(".png"):
        file_path = os.path.join(filePath, fileName)
        path = file_path

        img = cv2.imread(path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(gray, 200, 255, 0)

        cv2.imshow("Binary Image", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()