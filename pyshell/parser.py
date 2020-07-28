from . import consts
from . import shell_utils
from . import python_utils

class shellParser():
    def __init__(self):
        self.pythonRunner = python_utils.pyRunner()
        self.shellRunner = shell_utils.shellRunner()

    def checkBashOrPython(self, user_in):
        # Python var: '@'
        user_in = user_in.lstrip()
        if user_in[0] == consts.PYTHON_VAR_DELIMETER:
            #print('Get Python var: ', self.input[1:])
            return 'Python var:\n' + user_in[1:] #call pyRunner(self.input[1:])
        # Python single line: '>>>'
        elif user_in.startswith(consts.PYTHON_SINGLE_LINE_INPUT_DELEMETER): 
            #print('Get Python single line: ', self.input[3:])
            return 'Python single line:\n' + user_in[3:] #call pyRunner(self.input[2:])
        # Python multi line: '...'
        elif user_in.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):             
            user_in = user_in[len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):]
            user_in = user_in[:-len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER)]
            #print('Get Python multi line: (prints on newline to show tabs)\n', input)
            return 'Python multi line:\n' + user_in #call pyRunner(input)
        # all other commands must be bash/shell
        else:
            #print('Bash/shell command: ', self.input)
            self.shellRunner.feed(user_in)
            return 'Bash command:\n' + user_in #call shellRunner(self.input)