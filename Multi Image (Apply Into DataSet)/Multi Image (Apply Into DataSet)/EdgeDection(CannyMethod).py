import cv2
import os

filePath = "imageDataset/Ak"
for fileName in os.listdir(filePath):
    if fileName.endswith(".jpg") or fileName.endswith(".png"):
     file_path = os.path.join(filePath, fileName)
    im = cv2.imread(file_path)  # Read image

    img = cv2.resize(im, (400, 400))


    # Setting parameter values
    t_lower = 50 # Lower Threshold
    t_upper = 150 # Upper threshold

    # Applying the Canny Edge filter
    edge = cv2.Canny(img, t_lower, t_upper)

    cv2.imshow('original', img)
    cv2.imshow('Canny edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
