from abc import abstractmethod
from Core import Image

class PeopleCountingStrategy:
    @abstractmethod
    def CountPeople(self, image: Image) -> float: pass