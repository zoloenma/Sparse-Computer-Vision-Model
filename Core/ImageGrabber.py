from abc import abstractmethod

from Core import Image

class ImageGrabber:
    @abstractmethod
    def GetImage(self) -> Image: pass