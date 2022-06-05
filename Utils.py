import cv2
import numpy as np

def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([85, 2, 0])
    upperWhite = np.array([179, 120, 255])
    maskedWhite= cv2.inRange(hsv,lowerWhite,upperWhite)
    return maskedWhite


def getContours(imgThres, img):
    contours = cv2.findContours(imgThres, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    biggest = max(contours, key=cv2.contourArea)
    x,y,w,h = cv2.boundingRect(biggest)
    cx = x+w//2
    cy = y+h//2
    cv2.drawContours(img, biggest,-1, (255,0,255), 7)
    cv2.circle(img,(cx, cy), 10, (0,255,0),cv2.FILLED)
    return cx