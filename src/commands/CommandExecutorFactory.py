
from commands.ColorToRegNumberCommandExecutor import ColorToRegNumberCommandExecutor
from OutputPrinter import OutputPrinter
from commands.ColorToSlotNumberCommandExecutor import ColorToSlotNumberCommandExecutor
from commands.CreateParkingLotCommandExecutor import CreateParkingLotCommandExecutor
from commands.ExitCommandExecutor import ExitCommandExecutor
from commands.LeaveCommandExecutor import LeaveCommandExecutor
from commands.ParkCommandExecutor import ParkCommandExecutor
from commands.SlotForRegNumberCommandExecutor import SlotForRegNumberCommandExecutor
from commands.StatusCommandExecutor import StatusCommandExecutor

class CommandExecutorFactory:

    def __init__(self,parking_lot_service) -> None:
        self.commands = {}
        outputPrinter = OutputPrinter()

        self.commands[ColorToRegNumberCommandExecutor.COMMAND_NAME] = ColorToRegNumberCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[ColorToSlotNumberCommandExecutor.COMMAND_NAME] = ColorToSlotNumberCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[CreateParkingLotCommandExecutor.COMMAND_NAME] = CreateParkingLotCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[ExitCommandExecutor.COMMAND_NAME] = ExitCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[LeaveCommandExecutor.COMMAND_NAME] = LeaveCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[ParkCommandExecutor.COMMAND_NAME] = ParkCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[SlotForRegNumberCommandExecutor.COMMAND_NAME] = SlotForRegNumberCommandExecutor(parking_lot_service,outputPrinter)
        self.commands[StatusCommandExecutor.COMMAND_NAME] = StatusCommandExecutor(parking_lot_service,outputPrinter)


    def get_command_executor(self, command):
        command_executor = self.commands.get(command.get_command_name())
        if command_executor is None:
            raise Exception("Invalid Command Exception")
        return command_executor


