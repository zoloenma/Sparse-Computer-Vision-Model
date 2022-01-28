
from Core import Image
from Core.ImageGrabber import ImageGrabber
import cv2

class FileImageGrabber(ImageGrabber):
    def __init__(self, image_path) -> None:
        super().__init__()
        self.image_path = image_path

    def GetImage(self) -> Image:
        return cv2.imread(self.image_path)