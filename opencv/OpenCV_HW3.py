import cv2
import numpy as np

c1 = cv2.VideoCapture("./src/homework3.mp4")

while c1.isOpened()==True:
    ret, m1 = c1.read()

    m2 = cv2.inRange(m1, (100, 30, 20), (200, 80, 55))

    m2 = cv2.dilate(m2, np.ones((45,45)))
    m2 = cv2.erode(m2, np.ones((25,25)))

    if ret:
        contours, hierarchy = cv2.findContours(m2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  
        #cv2.drawContours(m1,contours,-1,(0,0,255),3)  

        if 0 < len(contours):
            x, y, w, h = cv2.boundingRect(contours[0])
            cv2.rectangle(m1, (x,y), (x + w, y + h), (0, 0, 255), 4)

        cv2.imshow("output", m1)
        #cv2.imshow("Image 2", m2)
        if cv2.waitKey(33)!=-1:
           break
    else:
        break
cv2.destroyAllWindows()
