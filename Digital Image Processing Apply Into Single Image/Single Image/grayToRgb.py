import cv2

path = 'imageDataset/github pp.jpg'

im = cv2.imread(path)

image = cv2.resize(im, (440, 440))

cv2.imshow('Original', image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

rgb_img = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
cv2.imshow('GGB', rgb_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
