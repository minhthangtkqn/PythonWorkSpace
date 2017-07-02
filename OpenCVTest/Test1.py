import numpy as np
import cv2

back = cv2.imread('image.jpg')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

ret, frame = back.read()

fgmask = fgbg.apply(frame)

cv2.imshow('frame', fgmask)
k = cv2.waitKey(30) & 0xff

back.release()
cv2.destroyAllWindows()
