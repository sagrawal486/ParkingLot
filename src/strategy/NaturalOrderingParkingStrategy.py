from .ParkingStrategy import ParkingStrategy
from typing import Set

class NaturalOrderingParkingStrategy(ParkingStrategy):

    def __init__(self) -> None:
        self.slot_set: Set[int] = set()


    def addSlot(self, slotNumber: int) -> None:
        self.slot_set.add(slotNumber)

    def removeSlot(self, slotNumber: int) -> None:
        self.slot_set.discard(slotNumber)


    def getNextSlot(self) -> int:
        if not self.slot_set:
            raise Exception('NoFreeSlotAvailableException')
        return min(self.slot_set)


        
