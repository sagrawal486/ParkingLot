from commands.CommandExecutor import CommandExecutor
from validator.IntegerValidator import IntegerValidator
from service.ParkingLotService import ParkingLotService
from strategy.NaturalOrderingParkingStrategy import NaturalOrderingParkingStrategy

from models.ParkingLot import ParkingLot

class CreateParkingLotCommandExecutor(CommandExecutor):

    COMMAND_NAME = "create_parking_lot";

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command) -> bool:
        if len(command.getParams()) != 1:
            return False

        else:
            return IntegerValidator.isInteger(command.getParams()[0])

    def execute(self, command) -> None:
        parkingLotCapacity = int(command.getParams()[0])
        parkingLot = ParkingLot(parkingLotCapacity)
        self.parking_lot_service.createParkingLot(parkingLot, NaturalOrderingParkingStrategy())
        self.output_printer.print_with_new_line("Created a parking lot with " + str(parkingLot.getCapacity()) + " slots")

