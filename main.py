import time
from Handlers.CameraImageGrabber import CameraImageGrabber
from Handlers.MongoDataRepository import MongoDataRepository
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


def main():
    repository = MongoDataRepository()
    grabber = CameraImageGrabber(0)
    counter = RcnnPeopleCountingStrategy()

    while True:
        image = grabber.GetImage()
        peopleCount = counter.CountPeople(image)
        repository.SavePeopleCount(peopleCount)
        time.sleep(5*60)

    
main()