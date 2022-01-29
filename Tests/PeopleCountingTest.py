import unittest

from Handlers.FileImageGrabber import FileImageGrabber
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


class PeopleCountingTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.model = RcnnPeopleCountingStrategy(True)

    def test_is_counting_people_zero(self):
        file_name = "Tests/Samples/people_zero.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 0

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_counting_people_one(self):
        file_name = "Tests/Samples/people_one.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 1

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_counting_people_two(self):
        file_name = "Tests/Samples/people_two.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 2

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_counting_people_three(self):
        file_name = "Tests/Samples/people_three.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 3

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_counting_people_four(self):
        file_name = "Tests/Samples/people_four.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 4

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)

    def test_is_counting_people_five(self):
        file_name = "Tests/Samples/people_five.jpg"
        image = FileImageGrabber(file_name).GetImage()
        actual_count = 5

        calculated_count = self.model.CountPeople(image)

        self.assertEqual(calculated_count, actual_count)


if __name__ == "__main__":
    unittest.main()