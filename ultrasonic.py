# Importing required libraries
import RPi.GPIO as GPIO
import time

# defining distance function
def distance(GPIO_TRIGGER, GPIO_ECHO):
    '''
    Input Parameter: GPIO_TRIGGER - Trigger Pin Number
                     GPIO_ECHO - Echo Pin Number
    Return: True or False
    Purpose: To calculate distance of object from ultrasonic sensor in
             centimeter
    '''
    
    # generating pulse serring Trigger to True for 10 microseconds
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    # set start time when echo is low
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    # set stop time while echo is high
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    # time taken by sound to reach back to sensor
    TimeElapsed = StopTime - StartTime
    
    # calculating object distance (speed of sound in air - 340 m/s)
    distance = (TimeElapsed * 34000) / 2
    
    # returning distance
    return int(distance)

# definfing traffic check function    
def trafficCheck(Trigger, Echo, sensorState, sid):
    '''
    Input Parameter: Trigger - Trigger Pin Number
                     Echo - Echo Pin Number
                     sensorState - master array containg state from all sensors
                     sid: Sensor Identification Number
    Return: Stat - an array containing six value. Each value can be
            either True or False.
    Purpose: To check stopped traffic at the junction. If obstacle is
             dedected continuously for 30 distance calculation, there is considered
             to be a traffic jam.
    Note: Uses distance function
    '''
    
    # creating state list
    state = []
    
    # taking data from a sensor for 20 times
    for i in range(20):
            dist = distance(Trigger, Echo) # calling distance function
            value = 1 if dist <= 10 and dist >= 2 else 0 # if object is in between 2 cm and 10 cm, value is 1 else 0
            state.append(value) # append value to state
            time.sleep(1) # sleep for one second
    
    # if all value in list are 1 return 1 else return 0 and append it to master list from multiprocessing module
    sensorState[sid-1] = 1 if all(state) == True else 0
    
    # return traffic state
    return sensorState
