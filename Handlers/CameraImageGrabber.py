
from Core import Image
from Core.ImageGrabber import ImageGrabber
import cv2

class CameraImageGrabber(ImageGrabber):
    def __init__(self, device_id: int):
        self.device_id = device_id

    def GetImage(self) -> Image:
        cam = cv2.VideoCapture(self.device_id)
        ret, frame = cam.read()
        return frame