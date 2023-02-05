import cv2

path = 'imageDataset/Ak/Ak (1).png'

img = cv2.imread(path)

# Output img with window name as 'image'
cv2.imshow('image', img)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()