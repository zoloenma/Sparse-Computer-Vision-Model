from abc import abstractmethod

from Core.DataRepository import DataRepository


class PeopleCountingStrategy:

    
    @abstractmethod
    def CountPeople(self, image) -> int: pass