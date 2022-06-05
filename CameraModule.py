import cv2
import numpy as np


class Camera():
    
 cap = cv2.VideoCapture(0)

 def getImg(self, display=False, size=[480, 320]):
    
    _,Img = self.cap.read()
    if display:
        cv2.imshow('VID', Img)
    return self.cap

# if __name__ == '__main__':
#     Camera= Camera()
#     while True:
#         Img = Camera.getImg(True)
#         cv2.waitKey(1)