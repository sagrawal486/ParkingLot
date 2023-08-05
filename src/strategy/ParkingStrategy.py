from abc import ABC, abstractmethod

class ParkingStrategy (ABC):
    @abstractmethod
    def addSlot(self,slotNumber: int) -> None:
        pass

    @abstractmethod
    def removeSlot(self,slotNumber: int) -> None:
        pass

    @abstractmethod
    def getNextSlot(self) -> int:
        pass