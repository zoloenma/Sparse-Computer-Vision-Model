import time
from Core.Model import Model
from Handlers.CameraImageGrabber import CameraImageGrabber
from Handlers.SqlDataRepository import SqlDataRepository
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


def main():
    model = Model(
        grabber =CameraImageGrabber(0),
        counter=RcnnPeopleCountingStrategy(debug_mode=True),
        repository=SqlDataRepository()
    )

    while True:
        model.Run()
        minute_interval = 1
        time.sleep(minute_interval * 60)

if __name__ == "__main__":
    main()
