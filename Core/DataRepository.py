from abc import abstractmethod


class DataRepository:
    @abstractmethod
    def SavePeopleCount(self, roomOccupancy: float): pass