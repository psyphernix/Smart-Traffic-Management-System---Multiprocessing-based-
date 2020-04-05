# importing all required libraries
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from picamera import PiCamera
from time import sleep

# defining camera module to take picture of a road
def camera():
    '''
    Input Parameter: None
    Return: None
    Purpose: to take image using raspberry camera and save to local disk
    '''
    
    camera = PiCamera() # powerup camera
    camera.start_preview() # start camera preview
    sleep(5) # stop program processing for 5 seconds to take better picture
    camera.capture('image.jpeg') #capture image and save as image.jpeg
    camera.stop_preview()  # stop camera preview
    return None # returning nothing
     
# defining object recognition and counting module
def vehicleCounting(sensorState, sid):
    '''
    Input Parameter: sensorState - master array from multiprocessing module
                     sid - sensor identification number
    Return: sensorState containg value number
    Purpose: to detect vehicle and count number
    '''
    
    camera() # taking image
    image = cv2.imread('image.jpeg') # converting image to numpy array using opencv library
    image = image[250:550, 0:1280] # cropping image
    bbox, label, conf = cv.detect_common_objects(image) # detecting common objects using yolov3 trained model and label them
    vehicleNumber = label.count('car')+label.count('truck')+label.count('bus')+label.count('motorcycle') # count common vehicles
    sensorState[sid-1] = int(vehicleNumber) # adding vehicle number to multiprocessing master array
    return sensorState # returning sensorState
    
