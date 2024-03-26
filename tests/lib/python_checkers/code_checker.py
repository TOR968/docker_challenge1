import re


class CodeChecker:
    def __init__(self, solution: str, user_code: str):
        self.solution = solution
        self.user_code = user_code
        self.solution_text = self.code_to_text(self.solution)
        self.user_text = self.code_to_text(self.user_code)

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

