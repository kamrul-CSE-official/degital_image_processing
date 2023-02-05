# import required libraries
import cv2

path = 'imageDataset/Ak/Ak (10).png'

img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 200, 255, 0)

cv2.imshow("Binary Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()