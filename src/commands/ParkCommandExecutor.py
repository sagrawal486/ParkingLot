from commands.CommandExecutor import CommandExecutor
from models.Car import Car
from OutputPrinter import OutputPrinter
class ParkCommandExecutor(CommandExecutor):

    COMMAND_NAME = "park"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command) -> bool:
        return len(command.getParams()) == 2

    def execute(self, command) -> None:
        car = Car(command.getParams()[0],command.getParams()[1])
        try:
            slot = self.parking_lot_service.park(car)
            self.output_printer.print_with_new_line("Allocated slot number: " + str(slot))
        except Exception as E:
            self.output_printer.parking_lot_full()




