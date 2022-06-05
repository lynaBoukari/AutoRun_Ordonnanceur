from typing_extensions import Self
from Ordonnanceur import Ordonnanceur 
from LaneDetectionModule import getLaneCurve
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as gpio


#from pynput import keyboard #for keyboard events

factory = PiGPIOFactory()
servo = Servo(21, pin_factory=factory)
class Motor():
    servo = Servo(20)

    SERVO_MIDDLE_VALUE = 0.0

    SERVO_RIGHT_VALUE = -0.8 

    SERVO_LEFT_VALUE = 0.5

    hasTurnedLeft = False
    hasTurnedRight = False
    currentSpeed = 0
    #enables
    gpio.setmode(gpio.BCM)
    gpio.setup(13, gpio.OUT) # right motor
    gpio.setup(12, gpio.OUT) #left motor

    rightMotor = gpio.PWM(13, 100)
    leftMotor= gpio.PWM(12, 100)

    leftMotor.start(0)
    rightMotor.start(0)

    def __init__(self):    
        gpio.setmode(gpio.BCM)
        gpio.setup(17, gpio.OUT)
        gpio.setup(22, gpio.OUT) # input 2 back
        gpio.setup(23, gpio.OUT)
        gpio.setup(24, gpio.OUT) # input 1 forward
        self.firstSpeed()
       
        
    def reverse(self):
        print("going reverse")
        gpio.output(17, gpio.LOW)
        gpio.output(22, gpio.HIGH)
        gpio.output(23, gpio.HIGH)
        gpio.output(24, gpio.LOW)
        
    def forward(self):
        print("going forward")
        gpio.output(17, gpio.HIGH)
        gpio.output(22, gpio.LOW)
        gpio.output(23, gpio.LOW)
        gpio.output(24, gpio.HIGH)

    def stop(self):
        print("STOP")
        self.rightMotor.ChangeDutyCycle(0)
        self.leftMotor.ChangeDutyCycle(0)
       
    def firstSpeed(self):
        print("First speed")
        self.rightMotor.ChangeDutyCycle(35)
        self.leftMotor.ChangeDutyCycle(35)
        self.currentSpeed =35

    def secondSpeed(self):
        print("Second speed")
        self.rightMotor.ChangeDutyCycle(50)
        self.leftMotor.ChangeDutyCycle(50)
        self.currentSpeed =50

    def thirdSpeed(self):
        print("Third speed")
        self.rightMotor.ChangeDutyCycle(75)
        self.leftMotor.ChangeDutyCycle(75)
        self.currentSpeed =75
    
    def fourthSpeed(self):
        print("Fourth speed")
        self.rightMotor.ChangeDutyCycle(100)
        self.leftMotor.ChangeDutyCycle(100)
        self.currentSpeed =100
        
    def demiTourInterdit(self):
        print("Demi Tour interdit")
        self.forward()

    def noStopping(self):
        print('No stopping ')
        self.forward()
        sleep(3)
        self.stop()
        sleep(5)
    
    def deccelerer(self,currenSpeed) :
        print("limited speed " , currenSpeed,"\n")
        if (self.currentSpeed > currenSpeed) :
            if (currenSpeed <= 35) :
                 self.firstSpeed()
            elif( currenSpeed <= 50 ) :
                self.secondSpeed()
            elif( currenSpeed <=75) :
                self.thirdSpeed()
            elif( currenSpeed <=100) :
                self.fourthSpeed()
        else : print("Decceleration vitesse acctuelle à :  " ,self.currentSpeed, "\n")
        
    def limitSpeed70(self):
        print("limited speed 70")
        self.thirdSpeed()
        
    def limitedSpeed80(self) :
        print("limited speed 80 hm/h")
        self.thirdSpeed()

    def limitedSpeed50(self) :
        print("limited speed 50 km/h")
        self.secondSpeed()
        
    def rotateLeft(self):
        if not self.hasTurnedLeft:
            print("Rotating Left")
            self.servo.value = self.SERVO_LEFT_VALUE
            self.hasTurnedLeft = True
        
    def rotateMiddle(self):
        print("Going to the middle")
        self.hasTurnedRight = False
        self.hasTurnedLeft = False
        self.servo.value = self.SERVO_MIDDLE_VALUE

    def rotateRight(self):
        print("Rotating Right")
        if not self.hasTurnedRight:
            self.servo.value = self.SERVO_RIGHT_VALUE
        self.hasTurnedRight = True
            

    def  rondPoint(self) :
        print ("Rond Point")
        sleep(3) # the necessary time to reach the rond point
        self.rotateLeft( ) 
        self.firstSpeed()
        self.sleep(5) # the necessary time to finish the rotation
        self.rotateMiddle()
        
    