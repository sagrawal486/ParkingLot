
from models.Car import Car
from models.ParkingLot import ParkingLot
from models.Slot import Slot
from strategy.ParkingStrategy import ParkingStrategy

class ParkingLotService:

    def __init__(self) -> None:
        self.parkingLot = None
        self.parkingStrategy = None
    

    def createParkingLot(self, parkingLot: ParkingLot, parkingStrategy: ParkingStrategy):

        if self.parkingLot != None:
            raise Exception("Parking Lot Already Exists")

        self.parkingLot = parkingLot
        self.parkingStrategy = parkingStrategy

        for i in range(1, parkingLot.getCapacity()+1):
            parkingStrategy.addSlot(i)

    def validateParkingLotExists(self):
        if self.parkingLot is None:
            raise Exception("Parking lot does not exists to park.")

    def park(self, car: Car):
        self.validateParkingLotExists()
        nextFreeSlot = self.parkingStrategy.getNextSlot()
        self.parkingLot.park(car, nextFreeSlot)
        self.parkingStrategy.removeSlot(nextFreeSlot)
        return nextFreeSlot
        
    def makeSlotFree(self, slotNumber):
        self.validateParkingLotExists()
        self.parkingLot.makeSlotFree(slotNumber)
        self.parkingStrategy.addSlot(slotNumber)

    def getOccupiedSlots(self):
        self.validateParkingLotExists()
        occupiedSlotsList = []
        allSlots = self.parkingLot.getSlots()
        for i in range(1, self.parkingLot.getCapacity()+1):
            if allSlots.get(i):
                slot = allSlots.get(i)
                if not slot.isSlotFree():
                    occupiedSlotsList.append(slot)

        return occupiedSlotsList

    def getSlotsForColor(self,color: str):
        self.validateParkingLotExists()
        occupiedSlots = []
        allSlots = self.parkingLot.getSlots()
        for i in range(1, self.parkingLot.getCapacity()+1):
            if allSlots.get(i):
                slot = allSlots.get(i)
                if not slot.isSlotFree() and slot.getParkedCar().color.lower() == color.lower():
                    occupiedSlots.append(slot)

        return occupiedSlots

