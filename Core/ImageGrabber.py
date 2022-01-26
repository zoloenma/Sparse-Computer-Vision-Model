from abc import abstractmethod


class ImageGrabber:
    @abstractmethod
    def GetImage(self): pass