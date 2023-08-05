class Command:

    SPACE = " "

    def __init__(self, input_line) -> None:
        tokens_list = [token.strip() for token in input_line.strip().split(Command.SPACE) if token.strip()]
        if len(tokens_list) == 0:
            raise Exception("Invalid Command")
        
        self.command_name = tokens_list[0].lower()
        self.params = tokens_list[1:]

    def get_command_name(self):
        return self.command_name
    
    def getParams(self):
        return self.params