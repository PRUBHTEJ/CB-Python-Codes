import cv2

img = cv2.imread('profile.png')

gray = cv2.imread('profile.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('pf-pic',img)

cv2.imshow('pf-pic-gray',gray)


cv2.waitKey(0)

cv2.destroyAllWindows()