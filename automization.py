# External module imp
import RPi.GPIO as GPIO
import datetime
from time import sleep


def automization_open():
    
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    
    GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
    #GPIO initialize
    
    GPIO.output(24, GPIO.LOW)
    #sleep(inTime)  #
    #GPIO.output(24, GPIO.HIGH) #
    
    #print ("Finished!") #
    #GPIO.cleanup()
   
def automization_close():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.output(24, GPIO.HIGH)
    GPIO.cleanup()
    
'''
automization_open()
sleep(1)
automization_close()
'''


