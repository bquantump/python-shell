from shell import Shell
from collections import deque 
from . import consts


class shellRunner:
    def __init__(self):
        self.command_que_in = deque(maxlen=10)
        self.command_que_out = deque(maxlen=10)
    
    def feed(self, command):

        self.command_que_in.append(command)

    def _process_command(self, command):
        to_split = command

        if command[0] == 'export':
            pass
        elif '=' in command[0]:
            pass
        else:
            if command[0] in const.INPUT_CMDS_LUT:
                sh = Shell(has_input=True)
            else:
                sh = Shell()
                sh.run(''.join(command))
            