from sultan.api import Sultan
from collections import deque 
from . import consts


class shellRunner:
    def __init__(self):
        self.command_que_in = deque(maxlen=10)
        self.command_que_out = deque(maxlen=10)

    def feed(self, command): # string.split()
        
        self.command_que_in.append(command)

    def get_bash_var(self, var):
        return os.environ.get(var)

    def _process_command(self, command):
        to_split = command
        
        if command[0] == 'export':
            if len(command) < 2:
                print("exporting nothing is not allowed")
                return
            split_cmd = command[1].split('=')
            if len(split_cmd) > 1:
                 os.environ[split_cmd[0]] = split_cmd[1]
            cmd_string = 'result = s.export' + '(' + command[1] + ').run()'
        elif '=' in command[0]:
            split_cmd = command[0].split('=')
            if len(split_cmd) < 2:
                raise RuntimeError("cannot set = to nothing")
            os.environ[split_cmd[0]] = split_cmd[1]
        else:
            s = Sultan.load(sudo=True if command[0] == 'sudo' else False)
            bas_cmd = self.parse_base(command[1] if command[0] == 'sudo' else command[0])
            idx = 2 if command[0] == 'sudo' else 1
            options = ''
            while idx < len(command):
                options += command[idx]
                idx += 1

        cmd_string = 'result = s.' + bas_cmd + '(' + options + ')' + '.run()'
        exec(cmd_string)
        result.print_stdout()

def parse_base(self, cmd):
    pass
        
