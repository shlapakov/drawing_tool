from drawing_tool.commands import Line, Canvas
from drawing_tool.constants import LINE_COMMAND, CANVAS_COMMAND, COMMANDS

from drawing_tool.error import ValidationError


class CommandReader:
    def __init__(self, file='input.txt', open_mode='r'):
        self.open_mode = open_mode
        self.file = file

    @property
    def commands(self) -> list:
        with open(self.file, self.open_mode) as f:
            return f.read().splitlines()


class Drawer:
    def __init__(self, commands: list, output_file='output.txt'):
        self.commands = commands
        self.output_file = output_file

    def check_errors(self):
        if not self.commands:
            raise ValidationError('Commands not found')

        if self.commands[0].split()[0].lower() != CANVAS_COMMAND:
            raise ValidationError('First command must create canvas')

        for command in self.commands:
            command_type = command[0].lower()
            if command_type not in COMMANDS:
                raise ValidationError(f'Not supported command: {command_type.upper()}')

    def draw(self):
        self.check_errors()
        with open(self.output_file, 'a') as f:
            template = []

            for command in self.commands:
                command = command.split()
                command_type = command[0].lower()
                command_params = [int(param) if param.isdigit() else param for param in command[1:]]

                if command_type == CANVAS_COMMAND:
                    template = Canvas(f).create(*command_params)

                if command_type == LINE_COMMAND:
                    template = Line(f, template).create(*command_params)

        return True


