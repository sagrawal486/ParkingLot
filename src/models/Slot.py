from pydantic import BaseModel, Field
from typing import Optional
from .Car import Car

class Slot(BaseModel):
    parkedCar: Optional[Car] = None
    slotNumber: int
    
    def __init__(self, slotNumber: int):
        super().__init__(slotNumber=slotNumber)

    def __str__(self):
        return f"Car[" + \
        "registrationNumber='" + self.registrationNumber + '\'' + \
        ", color='" + self.color + \
        '}'

    def getParkedCar(self) -> Car: 
        return self.parkedCar

    def isSlotFree(self) -> bool:
        return self.parkedCar == None

    def assignCar(self,car: Car) -> None:
        self.parkedCar = car

    def unassignCar(self) -> None:
        self.parkedCar = None 
