# importing all required libraries
from ultrasonic import trafficCheck
import multiprocessing as mp
from camera import vehicleCounting

# defining multiprocessing function
def multi(us1t, us1e, us2t, us2e, us3t, us3e, us4t, us4e, us5t, us5e, us6t, us6e):
    '''
    Input Parameter: us1t - Ultrasonic Sensor 1 Trigger Pin Number
                     us1e - Ultrasonic Sensor 1 Echo Pin Number
                     us2t - Ultrasonic Sensor 2 Trigger Pin Number
                     us2e - Ultrasonic Sensor 2 Echo Pin Number
                     us3t - Ultrasonic Sensor 3 Trigger Pin Number
                     us3e - Ultrasonic Sensor 3 Echo Pin Number
                     us4t - Ultrasonic Sensor 4 Trigger Pin Number
                     us4e - Ultrasonic Sensor 4 Echo Pin Number
                     us5t - Ultrasonic Sensor 5 Trigger Pin Number
                     us5e - Ultrasonic Sensor 5 Echo Pin Number
                     us6t - Ultrasonic Sensor 6 Trigger Pin Number
                     us6e - Ultrasonic Sensor 6 Echo Pin Number
    Return: array containing traffic state.
    Purpose: to run all sensors and camera simultaneously.
    '''
    
    sensorState = mp.Array('i', 7) # creating multiprocessing array
    
    # creating process list
    p1 = mp.Process(target=trafficCheck, args=(us1t,us1e,sensorState,1))
    p2 = mp.Process(target=trafficCheck, args=(us2t,us2e,sensorState,2))
    p3 = mp.Process(target=trafficCheck, args=(us3t,us3e,sensorState,3))
    p4 = mp.Process(target=trafficCheck, args=(us4t,us4e,sensorState,4))
    p5 = mp.Process(target=trafficCheck, args=(us5t,us5e,sensorState,5))
    p6 = mp.Process(target=trafficCheck, args=(us6t,us6e,sensorState,6))
    p7 = mp.Process(target=vehicleCounting, args=(sensorState,7))
    
    # starting process
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    
    # joining process
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
        
    return sensorState[:] #returning traffic state