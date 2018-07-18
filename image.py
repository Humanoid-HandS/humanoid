# -*- coding: utf-8 -*-

import cv2
import serial
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)

def TX_data(serial, one_byte):  # one_byte= 0~255
    try:
        serial.write(bytes(chr(int(one_byte)),'UTF-8'))
    except:
        print('tx error')
        pass
def RX_data(serial):
    try:
        if serial.inWaiting() > 0:
            result = serial.read(1)
            RX = ord(result)
            return RX
        else:
            print('rx error')
            return 0
    except:
        return 0
        pass

BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200

lower_y = np.array([59,123,0])
upper_y = np.array([255,225,80])    

serial_port = serial.Serial('/dev/ttyAMA0', BPS, timeout=0.001)
serial_port.flush() # serial cls
#---------------------------
       
    # -------- Main Loop Start --------
Send_data = 0 #right 6->9 vs left 4->7 straight 11
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = frame.array
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)        

    mask = cv2.inRange(hsv, lower_y, upper_y)
    ##################################################3



    ###################################################
    
    Read_RX = RX_data(serial_port)
    if Read_RX != 0:
        print("  <= RX : " + str(Read_RX))
    
    TX_data(serial_port,Send_data)
    
    rawCapture.truncate(0)
    print("TX => " + str(Send_data))
    
serial_port.close()