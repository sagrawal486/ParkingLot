from commands.CommandExecutor import CommandExecutor
from models.ParkingLot import ParkingLot
from OutputPrinter import OutputPrinter
class SlotForRegNumberCommandExecutor(CommandExecutor):

    COMMAND_NAME = "slot_number_for_registration_number"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)


    def validate(self, command) -> bool:
        return len(command.getParams()) == 1

    def execute(self, command) -> None:
        allSlots = self.parking_lot_service.getOccupiedSlots()
        result = None
        for slot in allSlots:
            if slot.getParkedCar().registrationNumber == command.getParams()[0]:
                result = slot.slotNumber
                break
        if result:
            self.output_printer.print_with_new_line("Slot number is " + str(result))
        else:
            self.output_printer.not_found()



