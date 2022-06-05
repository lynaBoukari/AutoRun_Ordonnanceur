from servoControl import Motor 
from time import sleep
class SingletonMeta(type):
    

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Ordonnanceur(metaclass=SingletonMeta):
   
    ########################### GLOBAL VARIABLES ################################
    trafficSign = 0
    laneCurves = 0
    obstacleDetected = False
    currentSpeed = 0

     # getter method
    def get_traffic_sign(self):
        return self.trafficSign
      
    # setter method
    def set_traffic_sign(self, value):
        self.trafficSign = value


         # getter method         
    def get_lane_curves(self):
        return self.laneCurves
    
    # setter method
    def set_lane_curves(self, value):
        maxVal = 0.8
        if curveVal>maxVal:curveVal = maxVal
        if curveVal<(-maxVal):curveVal = -maxVal
        self.laneCurves = curveVal

      # getter method
    def get_obstacle_detected(self):
        return self.obstacleDetected 
      
    # setter method
    def set_obstacle_detected(self, value):
        self.obstacleDetected  = value
    
      # getter method
    def get_current_speed(self):
        return self.currentSpeed 
      
    # setter method
    def set_current_speed(self, value):
        self.currentSpeed  = value
    
    ## Motor functions 
    def laneMiddle(self):
        Motor.rotateMiddle()
        Motor.forward()
        sleep(0.5)
    
    def laneLeft(self):
        Motor.rotateLeft()
        Motor.forward()
        sleep(0.5)
        
    def laneRight(self):
        Motor.rotateRight()
        Motor.forward()
        sleep(0.5)
        
    def ordonnancer(self):
    
        print("ordonnanceur working")
        if (self.obstacleDetected) :
            Motor.stop()

        elif(self.laneCurves < -0.3) :
            self.laneLeft()

        elif (self.laneCurves > 0.3) :
            self.laneRight()
        
        elif( -0.3 <= self.laneCurves<= 0.3):
            self.laneMiddle()
            
        elif (self.trafficSign == 4 & self.currentSpeed <= 70) :
            Motor.forward()

        elif (self.trafficSign == 4 & self.currentSpeed > 70) :
            Motor.deccelerer(70)

        elif (self.trafficSign == 5 & self.currentSpeed <= 80) :
            Motor.forward()

        elif (self.trafficSign == 5 & self.currentSpeed > 80) :
            Motor.deccelerer(80)

        elif (self.trafficSign == 2 & self.currentSpeed <= 50) :
            Motor.forward()

        elif (self.trafficSign == 2 & self.currentSpeed > 50) :
            Motor.deccelerer(80)

        elif (self.trafficSign == 1) :
            Motor.forward()

        elif (self.trafficSign == 14 | self.trafficSign == 17 | self.trafficSign == 28) :
            Motor.stop()

        elif (self.trafficSign == 13 | self.trafficSign == 38):
            Motor.forward()
            sleep(3)

        elif (self.trafficSign == 40):
            Motor.rondPoint()
    
        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Ordonnanceur()
    s2 = Ordonnanceur()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")