import os
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


if __name__ == "__main__":
    main()