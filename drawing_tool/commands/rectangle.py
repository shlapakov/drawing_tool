from drawing_tool.constants import BACKGROUND_SYMBOL, RECTANGLE_SYMBOL
from .base_classes import BaseCommand, BaseError
from .line import Line

import io


class Rectangle(BaseCommand, BaseError):
    def __init__(self, file: io.TextIOWrapper, template: list):
        super().__init__(file, template)

    def clear_fill(self, x1, y1, x2, y2):
        for y_position, y in enumerate(self.template):
            for x_position, x in enumerate(self.template[y_position]):
                if y1 <= y_position <= y2 and x1 <= x_position <= x2:
                    self.template[y_position] = ''.join((
                        self.template[y_position][:x_position],
                        BACKGROUND_SYMBOL,
                        self.template[y_position][x_position + 1:]
                    ))

    def create(self, x1, y1, x2, y2):
        self.check_errors(self.file, self.template, x1, y1, x2, y2)
        self.clear_fill(x1, y1, x2, y2)

        Line(
            file=self.file,
            template=self.template,
        ).create(x1, y1, x2, y1, saving=False)

        Line(
            file=self.file,
            template=self.template
             ).create(x1, y2, x2, y2, saving=False)

        Line(
            file=self.file,
            template=self.template
        ).create(x1, y1, x1, y2, saving=False)

        Line(
            file=self.file,
            template=self.template
        ).create(x2, y1, x2, y2)

        return self.template


