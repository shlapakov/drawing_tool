from drawing_tool.constants import BACKGROUND_SYMBOL, HORIZONTAL_BORDER_SYMBOL, VERTICAL_BORDER_SYMBOL
from drawing_tool.error import ValidationError
from .base_classes import BaseCommand


class Canvas(BaseCommand):
    def check_errors(self, w, h):
        if w < 0 or h < 0:
            raise ValidationError('Value of w and h must be more than 0')
        if not hasattr(self.file, 'closed'):
            raise ValidationError(f'{self.file} is not file')
        if self.file.closed:
            raise ValidationError(f'File {self.file} is not open')

    def create(self, w, h):

        self.check_errors(w, h)
        template = [HORIZONTAL_BORDER_SYMBOL * (w + 2)]
        for pixel in range(h):
            template.append(VERTICAL_BORDER_SYMBOL + BACKGROUND_SYMBOL * w + VERTICAL_BORDER_SYMBOL)
        template.append(HORIZONTAL_BORDER_SYMBOL * (w + 2))
        self.file.write('\n'.join(template) + '\n')

        return template
