from abc import ABC, abstractmethod
from OutputPrinter import OutputPrinter
from models.Command import Command
from service.ParkingLotService import ParkingLotService

class CommandExecutor(ABC):
    def __init__(self, parking_lot_service, output_printer):
        self.parking_lot_service = parking_lot_service
        self.output_printer = output_printer

    @abstractmethod
    def validate(self, command) -> bool:
        pass

    @abstractmethod
    def execute(self, command) -> None:
        pass
