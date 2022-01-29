from unittest import TestCase

from Handlers.FileImageGrabber import FileImageGrabber
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


class PersonDetectionTest(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.model = RcnnPeopleCountingStrategy()

    def test_is_detecting_person_near(self):
        file_name = "Tests/Samples/person_near.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_medium_distance(self):
        file_name = "Tests/Samples/person_medium_distance.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_far(self):
        file_name = "Tests/Samples/person_far.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_very_far(self):
        file_name = "Tests/Samples/person_very_far.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_back(self):
        file_name = "Tests/Samples/person_back.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_side(self):
        file_name = "Tests/Samples/person_side.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_female(self):
        file_name = "Tests/Samples/person_female.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_male(self):
        file_name = "Tests/Samples/person_male.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_partially_blocked(self):
        file_name = "Tests/Samples/person_partially_blocked.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_full_body(self):
        file_name = "Tests/Samples/person_full_body.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_upper_body(self):
        file_name = "Tests/Samples/person_upper_body.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_detecting_person_head(self):
        file_name = "Tests/Samples/person_head.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)
