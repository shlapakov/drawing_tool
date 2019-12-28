from drawing_tool.error import ValidationError
import io


class BaseCommand:
    def __init__(self, file: io.TextIOWrapper, template: list = None, char: str = ' '):
        self.file = file
        self.template = template if template else []
        self.char = char


class BaseError:
    @staticmethod
    def check_errors(file, template, x1, y1, x2, y2):
        if not hasattr(file, 'closed'):
            raise ValidationError(f'{file} is not file')
        if file.closed:
            raise ValidationError(f'File {file} is not open')

        if not template:
            raise ValidationError('Template is not found')

        x_length = len(template[0]) - 1
        y_length = len(template) - 1
        if x1 > x_length or x2 > x_length or x1 < 0 or x2 < 0 \
                or y1 > y_length or y2 > y_length or y1 < 0 or y2 < 0:
            raise ValidationError('Please, check coordinates. Its not correct')