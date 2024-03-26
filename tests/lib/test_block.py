# Імпортуємо необхідні модулі та функції з інших файлів
from lib.python_checkers.ipynb import IpynbCode
from lib.python_checkers.text_comparison import CodeChecker, CodeBlockChecker, ErrorChecker
from lib.messages import success, error


def test(solution_file_path: str, user_code_file_path: str, index: int, debug=False):
    solution_file = IpynbCode(solution_file_path)
    user_code_file = IpynbCode(user_code_file_path)

    solution = '\n'.join(solution_file.code_blocks[:index + 1])
    user_code = '\n'.join(solution_file.code_blocks[:index] + user_code_file.code_blocks[index:index + 1])

    code_errors = ErrorChecker(user_code).get_errors()

    if not code_errors:
        test = CodeBlockChecker(solution, user_code)
        if test.is_different():
            print(error(error_descriptions=test.is_different()))
        else:
            print(success())

    else:
        print(error(error_descriptions=code_errors))




