import textwrap

# Константи для кольорів
COLOR_GREEN = '92'
COLOR_RED = '91'

# Константи для ширини рамки і рядка тексту
FRAME_WIDTH = 60
TEXT_WIDTH = 100

# Константи для повідомлень
SUCCESS_MESSAGE = "Test Passed!"
ERROR_MESSAGE = "Test Failed!"

def generate_border(color_code):
    return f'\033[{color_code}m+{"-" * (FRAME_WIDTH - 2)}+\033[0m\n'

def wrap_message(message, color_code):
    return f'\033[{color_code}m{message}\033[0m\n'

def format_message(message):
    wrapped_lines = textwrap.wrap(message, width=TEXT_WIDTH)
    return '\n'.join(wrapped_lines)

def colored_output_success(color_code, success_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            border = generate_border(color_code)
            return border + wrap_message(success_message, color_code) + border
        # Додаємо атрибут success_message до функції-обгортки для подальшого використання
        wrapper.success_message = success_message
        return wrapper
    return decorator

def colored_output_error(color_code, error_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            border = generate_border(color_code)
            error_descriptions = kwargs.get('error_descriptions', None)
            if error_descriptions:
                formatted_errors = '\n'.join([wrap_message(f"{i+1}) {format_message(error)}", color_code) for i, error in enumerate(error_descriptions)])
                return border + wrap_message(error_message, color_code) + border + formatted_errors + border
            else:
                return border + wrap_message(error_message, color_code) + border  # Змінено тут
        return wrapper
    return decorator

@colored_output_success(COLOR_GREEN, SUCCESS_MESSAGE)
def success():
    pass

@colored_output_error(COLOR_RED, ERROR_MESSAGE)
def error(error_descriptions=None):
    pass