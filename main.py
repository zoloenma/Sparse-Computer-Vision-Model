from Handlers.CameraImageGrabber import CameraImageGrabber
from Handlers.MongoDataRepository import MongoDataRepository
from Handlers.YoloPeopleCountingStrategy import YoloPeopleCountingStrategy
from Infrastructure.MinuteScheduler import MinuteScheduler

repository = MongoDataRepository()
grabber = CameraImageGrabber()
counter = YoloPeopleCountingStrategy()


def main():
    scheduler = MinuteScheduler()
    scheduler.schedule(task, 5)
    
def task():
    image = grabber.GetImage()
    peopleCount = counter.CountPeople(image)
    repository.SavePeopleCount(peopleCount)