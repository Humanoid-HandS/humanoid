import cv2
import numpy as np
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time

def nothing(x):
    pass

# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 32
# rawCapture = PiRGBArray(camera, size=(640, 480))
# time.sleep(0.1)

frame = cv2.imread('foo.jpg')
# Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('h','image',0,255,nothing)
cv2.createTrackbar('s','image',0,255,nothing)
cv2.createTrackbar('v','image',0,255,nothing)
cv2.createTrackbar('H','image',0,255,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)

# create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)
# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
# frame = open('foo.jpg')
# frame = frame.array

bef_lower_y = []
bef_upper_y = []

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hh = cv2.getTrackbarPos('H','image')
    sh = cv2.getTrackbarPos('S','image')
    vh = cv2.getTrackbarPos('V','image')
    hl = cv2.getTrackbarPos('h','image')
    sl = cv2.getTrackbarPos('s','image')
    vl = cv2.getTrackbarPos('v','image')

    # define range of blue color in HSV
    
    lower_y = np.array([hl,sl,vl])
    upper_y = np.array([hh,sh,vh])

    if bef_upper_y != upper_y:
        if bef_lower_y != lower_y:
            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_y, upper_y)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame,frame, mask= mask)
            cv2.line(res ,(305,0), ( 305,700), (255,255,255), 3)
            cv2.imshow('image',frame)
            # cv2.imshow('mask',mask)
            cv2.imshow('res',res)
            # cv2.imshow('image',img)
            # rawCapture.truncate(0)
            # time.sleep(0.1)
            # if the `q` key was pressed, break from the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            time.sleep(0.1)

cv2.destroyAllWindows()