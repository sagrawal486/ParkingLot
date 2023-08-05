from commands.CommandExecutor import CommandExecutor

class ExitCommandExecutor(CommandExecutor):
    COMMAND_NAME = "exit"
    def __init__(self, parking_lot_service, output_printer):
        super().__init__(parking_lot_service, output_printer)

    def validate(self, command) -> bool:
        return len(command.getParams()) == 0

    def execute(self, command) -> None:
        return self.output_printer.end()

        
        