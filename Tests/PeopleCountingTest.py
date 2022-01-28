from unittest import TestCase

from Handlers import FileImageGrabber, RcnnPeopleCountingStrategy


class PeopleCountingTest(TestCase):
    def setUp(self) -> None:
        self.model = RcnnPeopleCountingStrategy()

    def is_counting_people_zero(self):
        file_name = "test/samples/people_zero"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 0

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_people_one(self):
        file_name = "test/samples/people_one"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_people_two(self):
        file_name = "test/samples/people_two"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 2

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_people_three(self):
        file_name = "test/samples/people_three"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 3

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_people_four(self):
        file_name = "test/samples/people_four"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 4

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_people_five(self):
        file_name = "test/samples/people_five"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 5

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)
