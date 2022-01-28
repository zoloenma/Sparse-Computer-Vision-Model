from unittest import TestCase

from Handlers import RcnnPeopleCountingStrategy
from Handlers.FileImageGrabber import FileImageGrabber


class PersonDetectionTest(TestCase):
    def setUp(self) -> None:
        self.model = RcnnPeopleCountingStrategy()

    def is_detecting_person_near(self):
        file_name = "test/samples/person_near"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_medium_distance(self):
        file_name = "test/samples/person_medium_distance"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_far(self):
        file_name = "test/samples/person_far"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_very_far(self):
        file_name = "test/samples/person_very_far"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_back(self):
        file_name = "test/samples/person_back"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_side(self):
        file_name = "test/samples/person_back"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_female(self):
        file_name = "test/samples/person_female"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_male(self):
        file_name = "test/samples/person_male"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_partially_blocked(self):
        file_name = "test/samples/person_partially_blocked"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_full_body(self):
        file_name = "test/samples/person_full_body"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_upper_body(self):
        file_name = "test/samples/person_upper_body"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_detecting_person_head(self):
        file_name = "test/samples/person_head"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)
