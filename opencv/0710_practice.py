import cv2
import numpy as np

lena = cv2.imread("lena.jpg", 1)
print(type(lena))
cv2.imshow("window_1", lena)
cv2.waitKey(5000)  # 10 sec
cv2.destroyAllWindows()
