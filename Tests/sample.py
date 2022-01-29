import sys
import os

from Handlers.SqlDataRepository import SqlDataRepository
sys.path.append(os.getcwd())

import cv2
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


counter = RcnnPeopleCountingStrategy(True)


image = cv2.imread("Tests/Samples/person_near.jpg")
count = counter.CountPeople(image)

print(count)