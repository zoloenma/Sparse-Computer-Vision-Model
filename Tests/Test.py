import sys

from Handlers.SqlDataRepository import SqlDataRepository
sys.path.append("..")

import cv2
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


counter = RcnnPeopleCountingStrategy()


image = cv2.imread('Tests\Samples\people_in_library2.jpg')
count = counter.CountPeople(image)
repo = SqlDataRepository()
repo.SavePeopleCount(count)


print(count)