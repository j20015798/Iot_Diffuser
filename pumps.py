import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
relay_pins = [17, 22, 23]
#{Oil_1: 17, Oil_2: 22, Oil_3: 23}

 
# loop through pins and set mode and state to 'low'
for i in relay_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)


    
# time to sleep between operations in the main loop

SleepTime_1 = 5   #1 drip
SleepTime_2 = 10   #2 drips
SleepTime_3 = 15   #3 drips
SleepTime_4 = 20   #4 drips


def oil_1(ratio):
    if ratio == "1":
        
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_1)
        
    elif ratio == "2":
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_2)
        
    elif ratio == "3":
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_3)
        
    elif ratio == "4":
        GPIO.output(17, GPIO.LOW)
        sleep(SleepTime_4)
        
    print ("oil_1 has added")
    
def oil_2(ratio):
    if ratio == "1":
        GPIO.output(22, GPIO.LOW)
        sleep(SleepTime_1)

    
    elif ratio == "2":
        GPIO.output(22, GPIO.LOW)
        sleep(SleepTime_2)


    elif ratio == "3":
        GPIO.output(22, GPIO.LOW)
        sleep(SleepTime_3)
        
    elif ratio == "4":
        GPIO.output(22, GPIO.LOW)
        sleep(SleepTime_4)
    
    print ("oil_2 has added")
        
def oil_3(ratio):
    if ratio == "1":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_1)
    
    elif ratio == "2":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_2)


    elif ratio == "3":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_3)
        
    elif ratio == "4":
        GPIO.output(23, GPIO.LOW)
        sleep(SleepTime_4)
    
    print ("oil_3 has done")
    

def dripProcess(type,ratio):
    if type == "oil_1":
        oil_1(ratio)
    elif type == "oil_2":
        oil_2(ratio)
    elif type == "oil_3":
        oil_3(ratio)

    GPIO.cleanup()

'''    
#test    
try:
    dripProcess("oil_3","1")
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
'''
