import re


class CodeChecker:
    def __init__(self, solution: str, user_code: str):
        self.solution = solution
        self.user_code = user_code
        self.solution_text = self.code_to_text(self.solution)
        self.user_text = self.code_to_text(self.user_code)

    def len_test(self):
        if len(self.user_text) != len(self.solution_text):
            return ['Your code does not meet the task requirements.\n' \
                   f'Solution lines length: {len(self.solution_text)}\n' \
                   f'Your code lines length: {len(self.user_text)}']

    @staticmethod
    def code_to_text(info):
        remove_comments = True
        info = info.split('\n')
        code = [line for line in info if line != ""]

        cleared_hints_list = []

        for line in code:
            hint = line.strip()
            if hint and (hint[0] != '#' or not remove_comments):
                if remove_comments:
                    hint = re.sub(r'\s*#.*$', '', hint)
                cleared_hints_list.append(hint)

        text_lines = []
        for line in cleared_hints_list:
            indent_match = re.match(r'^(\s+)', line)
            if indent_match:
                indent = indent_match.group(1)
            else:
                indent = ''
            stripped_line = re.sub(r'^\s+', '', line)
            text_lines.append(indent + stripped_line)
        return text_lines


class PyCodeChecker(CodeChecker):
    def __init__(self, solution: str, user_code: str):
        super().__init__(solution, user_code)

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
                solution_codes = PyCodeChecker.split_code(self.solution_text)
                user_codes = PyCodeChecker.split_code(self.user_text)
                if '___' in self.user_text[i]:
                    messages.append(f"Fill in all '___' gaps in code. An error was found in the line '{self.solution_text[i]}'")

                elif user_codes[i] != solution_codes[i]:
                    messages.append(f"Expected '{self.solution_text[i]}', but got '{self.user_text[i]}'")

            if messages:
                return messages
        else:
            return self.len_test()


class PyErrorChecker:
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


class DockerCodeChecker(CodeChecker):
    def __init__(self, solution: str, user_code: str):
        super().__init__(solution, user_code)

    @staticmethod
    def split_code(code: list):
        new_code = []
        for line in code:
            line = line.replace('  ', ' ')
            new_code.append(line)
        return new_code

    def is_different(self):
        messages = []
        if not self.len_test():
            started = False
            for i in range(len(self.user_text)):
                solution_codes = DockerCodeChecker.split_code(self.solution_text)
                user_codes = DockerCodeChecker.split_code(self.user_text)
                if '___' in self.user_text[i]:
                    if not started:
                        messages.append("Fill in all '___' gaps in code.")
                        started = True
                    else:
                        continue

                elif user_codes[i] != solution_codes[i]:
                    messages.append(f"Expected '{self.solution_text[i]}', but got '{self.user_text[i]}'")

            if messages:
                return messages
        else:
            return self.len_test()

    def info(self):
        print(self.solution_text)
        print(self.user_text)

