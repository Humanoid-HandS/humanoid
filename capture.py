import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.start_preview()
    time.sleep(0.1)
    # Take a picture including the annotation
    camera.capture('foo.jpg')