import cv2
import numpy as np

img = cv2.imread("homework2.png", 1)

for h in range(img.shape[0]):
    for w in range(img.shape[1]):
        if (img[h][w] == np.array([0, 0, 255])).all():
            img[h][w] = np.array([0, 0, 0])
        else:
            img[h][w] = np.array([255, 255, 255])

cv2.imshow("new image", img)
cv2.waitKey(6000)
cv2.destroyAllWindows()
