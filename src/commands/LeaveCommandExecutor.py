from commands.CommandExecutor import CommandExecutor
from validator.IntegerValidator import IntegerValidator
class LeaveCommandExecutor(CommandExecutor):

    COMMAND_NAME = "leave"

    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command) -> bool:
        if len(command.getParams()) != 1:
            return False

        else:
            return IntegerValidator.isInteger(command.getParams()[0])

    def execute(self, command) -> None:
        slotNum = int(command.getParams()[0])
        self.parking_lot_service.makeSlotFree(slotNum)
        self.output_printer.print_with_new_line("Slot number " + str(slotNum) + " is free")

