import json, re


class IpynbCode:
    def __init__(self, path: str):
        self.path = path
        self.code_blocks = self.__extract_code_from_ipynb()
        self.code = '\n'.join(self.__extract_code_from_ipynb())

    def __extract_code_from_ipynb(self):
        with open(self.path, "r") as file:
            content = json.load(file)

        code_blocks = []

        for cell in content['cells']:
            if cell['cell_type'] == 'code':
                source_code = ''.join(cell['source'])
                code_blocks.append(source_code)

        return code_blocks + ['\n']
