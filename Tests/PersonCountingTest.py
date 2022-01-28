from unittest import TestCase

from Handlers import FileImageGrabber, RcnnPeopleCountingStrategy


class PersonCountingTest(TestCase):
    def setUp(self) -> None:
        self.model = RcnnPeopleCountingStrategy()

    def is_counting_persons_zero(self):
        file_name = "test/samples/persons_zero"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_persons_one(self):
        file_name = "test/samples/persons_one"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_persons_two(self):
        file_name = "test/samples/persons_two"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_persons_three(self):
        file_name = "test/samples/persons_three"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_persons_four(self):
        file_name = "test/samples/persons_four"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def is_counting_persons_five(self):
        file_name = "test/samples/persons_five"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)
