from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.shortcuts import render
from maskapp.mask import mask
import cv2
import threading
import numpy as np 
import math
from . import mask

def index(request):
	return render(request, 'maskapp/home.html')

@gzip.gzip_page
def livefe(request):
    try:
        print("entered livefe")
        cam = VideoCamera()
        cam.video.read

        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
def mask_feed(request):
    print("entered maskfeed")
    return StreamingHttpResponse(gen(mask()),content_type='multipart/x-mixed-replace; boundary=frame')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0+cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
      while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

