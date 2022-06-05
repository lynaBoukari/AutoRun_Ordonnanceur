from servoControl import Motor
from LaneDetectionModule import getLaneCurve
import CameraModule
from time import sleep
import cv2
import threading


curveVal=0
motor = Motor()
 
def getMeasurementInput():
    while True:
        global curveVal
        ## read image
        img = CameraModule.getImg()
        ## calculate translation required
        curveVal = getLaneCurve(img)
        maxVal = 0.8
        if curveVal>maxVal:curveVal = maxVal
        if curveVal<(-maxVal):curveVal = -maxVal
# normalement ici il doit y avoir le set_lane_curves de l'ordonnanceur et l'appel de la fonction ordonnancer
        cv2.waitKey(1)
        #print(curveVal)

###" cette fontion a été implementé dans l'ordonnanceur "
# def SetMeasurementOutput():
#     while True:
#         global curveVal

#         #sleep(2)
        
#         if curveVal < -0.3:
#             state = 1
#         elif curveVal > 0.3:
#             state = 2
#         else:
#             state = 0

#         if (state == 0):
#             # Move forward
#             motor.rotateMiddle()
#             motor.forward()
#             sleep(0.5)
#            # motor.move(0.0,0,0.2)
#             # for 2 seconds
#             #motor.stop()
#         elif (state == 1):
#             # Turn Left
#             motor.rotateLeft()
#             motor.forward()
#             sleep(0.5)
#             # for 1 seconds
#             #motor.stop()
#         elif (state == 2):
#             # Turm Right
#             motor.rotateRight();
#             motor.forward();
#             sleep(0.5)
#             # for 1 seconds
#             #motor.stop()
#       #  motor.stop(0.5)


t1 = threading.Thread(target=getMeasurementInput)
# t2 = threading.Thread(target=SetMeasurementOutput)


if __name__ == '__main__':
    t1.start()
    # t2.start()