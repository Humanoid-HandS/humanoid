# -*- coding: utf-8 -*-

# import platform
# import numpy as np
# import argparse
import cv2
import serial
# import time
# import sys

#----------------------------------------------- 
# def clock():
#     return cv2.getTickCount() / cv2.getTickFrequency()
# #-----------------------------------------------
# def draw_str_height(dst, target, s, height):
#     x, y = target
#     cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, height, (0, 0, 0), thickness = 2, lineType=cv2.LINE_AA)
#     cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, height, (255, 255, 255), lineType=cv2.LINE_AA)
# #-----------------------------------------------
# def create_blank(width, height, rgb_color=(0, 0, 0)):

#     image = np.zeros((height, width, 3), np.uint8)
#     color = tuple(reversed(rgb_color))
#     image[:] = color

#     return image
#-----------------------------------------------
def TX_data(serial, one_byte):  # one_byte= 0~255
    try:
        serial.write(bytes(chr(int(one_byte)),'UTF-8'))
    except:
        print('tx error')
        pass
#-----------------------------------------------
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
#-----------------------------------------------        
# **************************************************
# **************************************************
# **************************************************
if __name__ == '__main__':

    #-------------------------------------
    # print ("-------------------------------------")
    # print ("(2018-6-15) Serial Test Program.    MINIROBOT Corp.")
    # print ("-------------------------------------")
    # print ("")
    # os_version = platform.platform()
    # print (" ---> OS " + os_version)
    # python_version = ".".join(map(str, sys.version_info[:3]))
    # print (" ---> Python " + python_version)
    # opencv_version = cv2.__version__
    # print (" ---> OpenCV  " + opencv_version)
    # print ("")
    
    # Setting_screen_w = 320
    # Setting_screen_h = 120
    # img = create_blank(Setting_screen_w, Setting_screen_h, rgb_color=(0, 100, 100))

    # Top_name = "Serial Test Program"
    # cv2.namedWindow(Top_name)
    # draw_str_height(img, (15, (Setting_screen_h/4)), 'MINIROBOT Corp.', 1.2)
    # draw_str_height(img, (15, int(Setting_screen_h/1.6)), 'key 1~9 Press', 2.0)

    # draw_str_height(img, (15, int(Setting_screen_h/1.1)), 'Exit:  ESC key ', 1.2)
    
    # cv2.imshow(Top_name, img)
    #---------------------------
    BPS =  4800  # 4800,9600,14400, 19200,28800, 57600, 115200
    
    serial_port = serial.Serial('/dev/ttyAMA0', BPS, timeout=0.001)
    serial_port.flush() # serial cls
    #---------------------------
       
    # -------- Main Loop Start --------
    Send_data = 0
    while True:        
        Send_data = input()
        Read_RX = RX_data(serial_port)
        if Read_RX != 0:
            print("  <= RX : " + str(Read_RX))
       
        # key = 0xFF & cv2.waitKey(1)  
        TX_data(serial_port,Send_data)
        print("TX => " + str(Send_data))

        # key = 0xFF & cv2.waitKey(0)
    # cleanup the camera and close any open windows
    serial_port.close()

    cv2.destroyAllWindows()






