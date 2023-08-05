
from commands.CommandExecutor import CommandExecutor
from models.Command import Command
from models.Slot    import Slot
from service.ParkingLotService import ParkingLotService
from OutputPrinter import OutputPrinter


class ColorToSlotNumberCommandExecutor(CommandExecutor):

    COMMAND_NAME = "slot_numbers_for_cars_with_colour"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command) -> bool:
        return len(command.getParams()) == 1

    def execute(self, command) -> None:
        slotsForColor = self.parking_lot_service.getSlotsForColor(command.getParams()[0])
        result = []
        if not slotsForColor:
            self.output_printer.not_found()
        else:
            for slot in slotsForColor:
                result.append(str(slot.slotNumber))

            self.output_printer.print_with_new_line(", ".join(result)) 




