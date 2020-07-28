from sultan.api import Sultan
import time
from collections import deque 
import os
from . import consts


class shellRunner:
    def __init__(self):
        pass

    def feed(self, command): # string.split()
        self._process_command(command)

    def get_bash_var(self, var):
        return os.environ.get(var)

    def run_script(self, script):
        pass

    def _process_command(self, command):
        command = command.split()
        streaming = False
        if command[0] == 'export':
            if len(command) < 2:
                print("exporting nothing is not allowed")
                return
            split_cmd = command[1].split('=')
            if len(split_cmd) > 1:
                 os.environ[split_cmd[0]] = split_cmd[1]
            idx = 1
        elif '=' in command[0]:
            split_cmd = command[0].split('=')
            if len(split_cmd) < 2:
                raise RuntimeError("cannot set = to nothing")
            os.environ[split_cmd[0]] = split_cmd[1]
            return
        elif 'cd' in command[0]:
            if len(command) < 2:
                print('cannot change dir to nothing')
                return
            os.chdir(command[1])
            return
        elif 'pip' in command[0]:
            if 'VIRTUAL_ENV' in os.environ:
                s = Sultan.load(src=os.path.join(os.environ['VIRTUAL_ENV'], 'bin', 'activate'),
                                executable='/bin/bash')
            else:
                s = Sultan.load()
            streaming = True
            bas_cmd = 'pip'
            idx = 1
        else:
            bas_cmd = command[1] if command[0] == 'sudo' else command[0]
            s = Sultan.load(sudo=True if command[0] == 'sudo' else False)
            idx = 2 if command[0] == 'sudo' else 1

        options = ''
        while idx < len(command):
            options += command[idx] + " "
            idx += 1
        if streaming:
            cmd_string = 'global result; result = s.' + bas_cmd + '(\'' + options + '\')' + '.run(streaming=True)'
            print("cmd str is: " + str(cmd_string))
            exec(cmd_string, globals(), locals())      
            complete = False
            while not complete:
                complete = result.is_complete
                for line in result.stdout:
                    print(line)
                for line in result.stderr:
                    print(line)
                time.sleep(.5)
        else:
            cmd_string = 'global result; result = s.' + bas_cmd + '(\'' + options + '\')' + '.run()'
            print("cmd str is: " + str(cmd_string))
            exec(cmd_string, globals(), locals())      
            result.print_stdout()
