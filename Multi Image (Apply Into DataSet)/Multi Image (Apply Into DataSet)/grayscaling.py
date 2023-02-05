import cv2
import os


filePath = "imageDataset/Ak"
for fileName in os.listdir(filePath):
    if fileName.endswith(".jpg") or fileName.endswith(".png"):
        file_path = os.path.join(filePath, fileName)
    im = cv2.imread(file_path)  # Read image
    image = cv2.resize(im, (400, 400))

    cv2.imshow('Original', image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Grayscale', gray_image)
    cv2.waitKey(0)

    rgb_img = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
    cv2.imshow('GGB', rgb_img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
