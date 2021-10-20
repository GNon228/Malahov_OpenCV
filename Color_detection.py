import cv2
import numpy as np

img:np.ndarray = cv2.imread('robot.jpeg', cv2.IMREAD_COLOR)
shrink_koeff = 2
img_h, img_w, _ = img.shape
img = cv2.resize(img, (int(img_w//shrink_koeff),int(img_h/shrink_koeff)),cv2.INTER_NEAREST)

cv2.imshow("img",img)
cv2.waitKey()