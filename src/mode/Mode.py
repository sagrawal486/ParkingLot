from abc import ABC, abstractmethod

class Mode(ABC):
    def __init__(self, command_executor_factory, output_printer):
        self.command_executor_factory = command_executor_factory
        self.output_printer = output_printer

    def process_command(self, command):
        command_executor = self.command_executor_factory.get_command_executor(command)
        if command_executor.validate(command):
            command_executor.execute(command)
        else:
            raise Exception("Invalid Command Exception")

    @abstractmethod
    def process(self):
        pass
