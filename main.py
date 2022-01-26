from Handlers.CameraImageGrabber import CameraImageGrabber
from Handlers.MongoDataRepository import MongoDataRepository
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy
from Infrastructure.MinuteScheduler import MinuteScheduler

repository = MongoDataRepository()
grabber = CameraImageGrabber()
counter = RcnnPeopleCountingStrategy()


def main():
    scheduler = MinuteScheduler()
    scheduler.schedule(task, 5)
    
def task():
    image = grabber.GetImage()
    peopleCount = counter.CountPeople(image)
    repository.SavePeopleCount(peopleCount)

main()