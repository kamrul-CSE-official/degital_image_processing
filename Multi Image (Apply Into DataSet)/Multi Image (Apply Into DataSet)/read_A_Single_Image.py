import cv2

path = 'imageDataset/Ak/Ak (45).png'

image = cv2.imread(path)

cv2.imshow("Single Image Read", image)

cv2.waitKey(0)