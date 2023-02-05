import os
import cv2


path = "imageDataset/Ak"
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        file_path = os.path.join(path, filename)
        # Load the image using any image processing library such as OpenCV, PIL, etc.
        image = cv2.imread(file_path)
        print(file_path)
        k = cv2.imread(file_path)
        cv2.imshow("Prewitt Y", k)
        cv2.waitKey(0)

        # Do something with the image
        # ...
