from commands.CommandExecutor import CommandExecutor
from OutputPrinter import OutputPrinter

class StatusCommandExecutor(CommandExecutor):


    COMMAND_NAME = "status"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command) -> bool:
        return len(command.getParams()) == 0

    def execute(self, command) -> None:
        occupiedSlots = self.parking_lot_service.getOccupiedSlots()
        if not occupiedSlots:
            self.output_printer.parking_lot_empty()
            return

        self.output_printer.status_header()
        for slot in occupiedSlots:
            parkedCar = slot.getParkedCar()
            slotNumber = slot.slotNumber

            self.output_printer.print_with_new_line(str(slotNumber) + "  " + parkedCar.registrationNumber + "  " + parkedCar.color)
