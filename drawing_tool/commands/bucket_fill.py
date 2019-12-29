import io

from drawing_tool.constants import SYMBOLS
from drawing_tool.error import ValidationError
from .base_classes import BaseCommand


class BucketFill(BaseCommand):
    def __init__(self, file: io.TextIOWrapper, template: list):
        super().__init__(file, template)

    def check_errors(self, x, y, c):
        if not hasattr(self.file, 'closed'):
            raise ValidationError(f'{self.file} is not file file')
        if self.file.closed:
            raise ValidationError(f'File {self.file} is not open')
        if len(c) != 1:
            raise ValidationError('Fill element must include one symbol')
        if not self.is_empty_char(self.template[y][x]):
            raise ValidationError('You should give coordinates of the empty area')

    def is_empty_char(self, current_char: str):
        if current_char in SYMBOLS:
            return False
        return True

    def is_connected_char(self, current_char: str):
        if current_char == self.char:
            return True
        return False

    def is_empty_area(self, x: int, y: int):
        char = self.template[y][x]
        if self.is_empty_char(char) \
                and not self.is_connected_char(char):
            return True
        return False

    def draw(self, x, y):
        self.template[y] = ''.join((
            self.template[y][:x],
            self.char,
            self.template[y][x + 1:]
        ))

    def check_area(self, x, y):
        current_x_state = []
        for position, x_char in enumerate(self.template[y][1:-1]):
            if self.is_empty_char(x_char):
                current_x_state.append(position + 1)
            elif position + 1 < x:
                current_x_state.clear()
            elif position + 1 > x:
                break

        for x_position in current_x_state:
            self.draw(x_position, y)

        for x_position in current_x_state:
            if self.is_empty_area(x_position, y + 1):
                self.check_area(x_position, y + 1)
            if self.is_empty_area(x_position, y - 1):
                self.check_area(x_position, y - 1)

    def create(self, x, y, c: str):
        self.check_errors(x, y, c)
        self.char = c
        self.check_area(x, y)
        self.file.write('\n'.join(self.template) + '\n')

        return self.template
