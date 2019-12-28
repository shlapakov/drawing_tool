from drawing_tool.error import ValidationError
import io


class BaseCommand:
    def __init__(self, file: io.TextIOWrapper, template: list = None, char: str = ' '):
        self.file = file
        self.template = template if template else []
        self.char = char
