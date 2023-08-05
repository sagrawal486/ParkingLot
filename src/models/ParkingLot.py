from pydantic import BaseModel, Field
from typing import Optional
from .Slot import Slot
from .Car import Car

class ParkingLot(BaseModel):
    MAX_CAPACITY: int = Field(default=100000) #not working could be defined in config
    capacity: int
    slots: dict = {}
    
    def __init__(self, capacity: int):
        if (capacity > 100000 or capacity <= 0):
            raise Exception("Invalid capacity given for parking lot.")
        super().__init__(capacity=capacity)


    def __str__(self):
        return f"ParkingLot" + \
        "capacity='" + self.capacity + '\'' + \
        ", slots='" + self.slots + \
        '}'

    def getCapacity(self) -> int:
        return self.capacity

    def getSlots(self) -> dict:
        return self.slots

    def getSlot(self, slotNumber: int) -> Slot: 
        if slotNumber > self.capacity or slotNumber <= 0:
            raise Exception("Invalid Slot")
        allSlots = self.getSlots()
        if not allSlots.get(slotNumber):
            allSlots[slotNumber] = Slot(slotNumber)
        return allSlots[slotNumber]

    def park(self, car: Car, slotNumber: int):
        slot = self.getSlot(slotNumber)
        if not slot.isSlotFree():
            raise Exception("Slot already occupied")
        slot.assignCar(car)
        return slot

    def makeSlotFree(self, slotNumber: int):
        slot = self.getSlot(slotNumber)
        if slot.isSlotFree():
            raise Exception("Slot is already free")
        slot.unassignCar()
        return slot