from .Mode import Mode
from models.Command import Command
from commands.ExitCommandExecutor import ExitCommandExecutor

class InteractiveMode(Mode):
    def __init__(self, command_executor_factory, output_printer):
        super().__init__(command_executor_factory, output_printer)

    def process(self):
        self.output_printer.welcome()
        try:
            while True:
                input_line = input()

                command = Command(input_line)
                self.process_command(command)
                if command.get_command_name() == ExitCommandExecutor.COMMAND_NAME:
                    break
        except EOFError:
            pass
