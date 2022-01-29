import sys
import os

from Handlers.SqlDataRepository import SqlDataRepository
sys.path.append(os.getcwd())

import cv2
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


counter = RcnnPeopleCountingStrategy()


image = cv2.imread('Tests\Samples\people_in_library2.jpg')
count = counter.CountPeople(image)

print(count)