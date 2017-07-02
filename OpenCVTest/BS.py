import numpy
import cv2

back_ground = cv2.imread('BS_1.jpg', 0)

fore_ground = cv2.imread('BS_2.jpg', 0)

result = back_ground ^ fore_ground

cv2.imshow('frame', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
