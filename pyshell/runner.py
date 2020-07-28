import os

from . import consts, parser
from sultan.api import Sultan


def display_welcome():
    print(' Welcome to pyshell')
    print(' Useage:')
    print('     Echo python variable with character @')
    print("     Write single-line python code start with '>>>', if it is in multi-line start with '...'\n")


def main():
    display_welcome()
    while(True):
        input = Sultan().stdin(os.getcwd() + ': ')
        if input == consts.EXIT_PYSHELL_CMD:
            break
        if input.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):
            while(True):
                single_line_code = Sultan().stdin('')
                # print('multi-line mode: '+input)
                input += single_line_code
                if single_line_code == consts.PYTHON_MULTI_LINE_INPUT_DELIMETER:
                    break
        print(parser.checkBashOrPython(input)) # pass the input to parser


if __name__ == "__main__":
    main()