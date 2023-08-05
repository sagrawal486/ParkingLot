
from OutputPrinter import OutputPrinter
from commands.CommandExecutorFactory import CommandExecutorFactory
from mode.FileMode import FileMode
from mode.InteractiveMode import InteractiveMode
from service.ParkingLotService import ParkingLotService
import sys

def main(args):
    output_printer = OutputPrinter()
    parking_lot_service = ParkingLotService()
    command_executor_factory = CommandExecutorFactory(parking_lot_service)

    if is_interactive_mode(args):
        InteractiveMode(command_executor_factory, output_printer).process()
    elif is_file_input_mode(args):
        FileMode(command_executor_factory, output_printer, args[0]).process()
    else:
        raise Exception("Invalid Mode Exception")

def is_file_input_mode(args):
    return len(args) == 1

def is_interactive_mode(args):
    return len(args) == 0

if __name__ == "__main__":
    main(sys.argv[1:])
