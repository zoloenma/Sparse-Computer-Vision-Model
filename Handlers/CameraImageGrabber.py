
from Core import Image
from Core.ImageGrabber import ImageGrabber
import cv2

class CameraImageGrabber(ImageGrabber):
    def __init__(self, device_id: int):
        self.device_id = device_id
        self.cam = cv2.VideoCapture(self.device_id)

    def GetImage(self) -> Image:
        _, frame = self.cam.read()
        return frame

    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()