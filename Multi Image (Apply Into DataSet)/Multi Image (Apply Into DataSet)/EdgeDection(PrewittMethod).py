import cv2
import numpy as np
import os

filePath = "imageDataset/Ak"
for fileName in os.listdir(filePath):
    if fileName.endswith(".jpg") or fileName.endswith(".png"):
        file_path = os.path.join(filePath, fileName)
        im = cv2.imread(file_path)  # Read image

        img = cv2.resize(im, (400, 400))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)



        # prewitt
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
        img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

        cv2.imshow("Original Image", img)

        cv2.imshow("Prewitt X", img_prewittx)
        cv2.imshow("Prewitt Y", img_prewitty)
        cv2.imshow("Prewitt", img_prewittx + img_prewitty)

        cv2.waitKey(0)
        cv2.destroyAllWindows()