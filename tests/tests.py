from lib.code_checker import DockerCodeChecker
from lib.code_parsers.docker_parser import get_code
from lib.messages.messages import success, error


solution_file = 'tests/solution/Dockerfile'
user_code_file = 'Dockerfile'


solution = get_code(solution_file)
user_code = get_code(user_code_file)

task = DockerCodeChecker(solution, user_code)

messages = task.is_different()

if messages:
    print(error(error_descriptions=messages))
else:
    print(success())
