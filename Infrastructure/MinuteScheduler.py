import time

from threading import Thread


def schedule_task(task, minutes):
    print("task scheduled")
    while True:
        task()
        time.sleep(minutes*60)


class MinuteScheduler:

    def schedule(self, task, minutes):
        thread = Thread(target=schedule_task, args=(task, minutes))
        thread.start()
        thread.join()