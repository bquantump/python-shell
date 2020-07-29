import os
import cmd
import sys
from . import consts, parser
from sultan.api import Sultan
from termcolor import colored

def display_welcome():
    print(' Welcome to pyshell!')
    print(' Useage:')
    print('     Echo python variable with character @')
    print("     Write single-line python code start with '>>>', if it is in multi-line start with '...'\n")


def get_prefix():
    prefix = os.getcwd()
    if 'VIRTUAL_ENV' in os.environ:
        prefix = '(' + os.environ.get('VIRTUAL_ENV').split('/')[-1] + ')' + prefix
    return prefix + ': '


def main():
    sell_parser = parser.shellParser()
    display_welcome()
    while(True):
        user_in = Sultan().stdin(colored(get_prefix(), 'cyan'))
        if user_in == consts.EXIT_PYSHELL_CMD:
            break
        if user_in.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):
            while(True):
                single_line_code = Sultan().stdin('')
                user_in += single_line_code
                if single_line_code == consts.PYTHON_MULTI_LINE_INPUT_DELIMETER:
                    break
        output = sell_parser.checkBashOrPython(user_in)
        if output != None:
            print(output)


multi_line = False
line_buffer = []
class CmdParse(cmd.Cmd):
    prompt = get_prefix()
    def do_exit(self, arg):
        sys.exit(0)
    def default(self, line):
        if multi_line:
            line_buffer.append(line)
        elif user_in.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):
            while(True):
                single_line_code = Sultan().stdin('')
                user_in += single_line_code
                if single_line_code == consts.PYTHON_MULTI_LINE_INPUT_DELIMETER:
                    break
            print(sell_parser.checkBashOrPython(user_in)) # pass the input to parser
    def do_py(self, arg):
        if multi_line:
            sell_parser.checkBashOrPython(line_buffer)
            multi_line = False
            self.prompt = get_prefix()
            return
        multi_line = True
        self.prompt = "python mode>>>"


if __name__ == "__main__":
    main()