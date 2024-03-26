from lib.python_checkers.code_checker import CodeChecker


import io
import tokenize


class CodeBlockChecker(CodeChecker):
    def __init__(self, solution: str, user_code: str):
        super().__init__(solution, user_code)

    def len_test(self):
        if len(self.user_text) != len(self.solution_text):
            return ['Your code does not meet the task requirements.\n' \
                   f'Solution lines length: {len(self.solution_text)}\n' \
                   f'Your code lines length: {len(self.user_text)}']

    @staticmethod
    def split_code(codes):
        new_codes = []
        for code in codes:
            space = ''
            for element in code:
                if element == ' ':
                    space += element
                else:
                    break
            new_code = space + ''.join(code.split())
            new_codes.append(new_code)
        return new_codes



    def is_different(self):
        messages = []
        if not self.len_test():
            for i in range(len(self.user_text)):
                solution_codes = CodeBlockChecker.split_code(self.solution_text)
                user_codes = CodeBlockChecker.split_code(self.user_text)
                if '___' in self.user_text[i]:
                    messages.append(f"Fill in all '___' gaps in code. An error was found in the line '{self.solution_text[i]}'")

                elif user_codes[i] != solution_codes[i]:
                    messages.append(f"Expected '{self.solution_text[i]}', but got '{self.user_text[i]}'")

            if messages:
                return messages
        else:
            return self.len_test()


class ErrorChecker:
    def __init__(self, code):
        self.code = code

    def get_errors(self):
        try:
            compiled = compile(self.code, '<string>', 'exec')
            return
        except SyntaxError as e:
            error_message = f"Syntax Error: {e}"
            lines = self.code.split('\n')
            error_line_number = e.lineno
            if error_line_number <= len(lines):
                error_line = lines[error_line_number - 1]
                error_message += f"\nError in line: '{error_line}'"
            return [error_message]
        except Exception as e:
            return [f"Execution Error: {e}"]




