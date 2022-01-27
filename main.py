import time
from Core import Model
from Handlers.CameraImageGrabber import CameraImageGrabber
from Handlers.SqlDataRepository import MongoDataRepository
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


def main():
    model = Model(
        grabber=CameraImageGrabber(0),
        counter=RcnnPeopleCountingStrategy(),
        repository=MongoDataRepository()
    )

    while True:
        model.Run()
        minute_interval = 1
        time.sleep(minute_interval * 60)


main()
