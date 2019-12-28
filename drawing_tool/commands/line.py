from drawing_tool.constants import LINE_SYMBOL
from drawing_tool.error import ValidationError
from .base_classes import BaseCommand, BaseError
import io


class Line(BaseCommand, BaseError):
    def __init__(self, file: io.TextIOWrapper, template: list):
        super().__init__(file, template)
        self.char = LINE_SYMBOL

    def check_errors(self, x1, y1, x2, y2):
        super().check_errors(self.file, self.template, x1, y1, x2, y2)

        if x1 != x2 and y1 != y2:
            raise ValidationError('You can use only horizontal and vertical lines')

    def create(self, x1, y1, x2, y2, saving=True):
        
        self.check_errors(x1, y1, x2, y2)

        if y1 == y2:
            for place, x in enumerate(self.template[y1]):
                if x1 <= place <= x2:
                    self.template[y1] = ''.join((
                        self.template[y1][:place],
                        self.char,
                        self.template[y1][place + 1:]
                    ))

        if x1 == x2:
            for place, x in enumerate(self.template):
                if y1 <= place <= y2:
                    self.template[place] = ''.join((
                        self.template[place][:x1],
                        self.char,
                        self.template[place][x1 + 1:]
                    ))

        if saving:
            self.file.write('\n'.join(self.template) + '\n')
        return self.template
