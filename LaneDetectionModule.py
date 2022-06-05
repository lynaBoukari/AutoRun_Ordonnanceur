import cv2
import numpy as np
import Utils

width = 480
height = 380
curve = 0

def getLaneCurve(img):

    ###STEP1
    imgThres = Utils.thresholding(img)

    ###STEP2
    cx = Utils.getContours(imgThres,img)
    curve = cx - width//2

    ##NORMALIZATION
    curve = curve/100

    if curve>1: curve == 1
    if curve<-1: curve == -1

    cv2.imshow('thres', imgThres)
    cv2.imshow('vid', img)

    return curve

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img = cv2.resize(img,(width,height))
        curve = getLaneCurve(img)
        print(curve)
        cv2.waitKey(1)