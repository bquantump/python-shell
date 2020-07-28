from . import consts
from . import shell_utils
from . import python_utils

class shellParser():
    def __init__(self):
        self.pythonRunner = python_utils.pyRunner()
        self.shellRunner = shell_utils.shellRunner()

    def checkBashOrPython(self, user_in):
        user_in = user_in.lstrip()
        # Python var: '@'
        if user_in[0] == consts.PYTHON_VAR_DELIMETER:
            return 'Python var:\n' + user_in[1:] #call pyRunner(self.input[1:])
        # Python single line: '>>>'
        elif user_in.startswith(consts.PYTHON_SINGLE_LINE_INPUT_DELEMETER): 
            return 'Python single line:\n' + user_in[3:] #call pyRunner(self.input[2:])
        # Python multi line: '...'
        elif user_in.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):             
            user_in = user_in[len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):]
            user_in = user_in[:-len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER)]
            return 'Python multi line:\n' + user_in #call pyRunner(input)
        # check for Python or bash scripts
        elif user_in.startswith(consts.PYTHON_BASH_SCRIPT_DELIMETER):
            return 'Bash Python script:\n' + self.script_formatter(user_in) #call pyRunner.run_py_script(user_in)
        elif user_in.startswith(consts.SHELL_SCRIPT_START_DELIMETER):
            return 'Shell script:\n' + self.script_formatter(user_in) #call shellRunner.run_script(user_in)
        elif user_in.startswith(consts.SHELL_SCRIPT_SH_START_DELIMETER):
            return 'Shell script:\n' + self.script_formatter(user_in) #call shellRunner.run_script(user_in)
        elif user_in.startswith(consts.BASH_SCRIPT_START_DELIMETER):
            return 'Bash script:\n' + self.script_formatter(user_in) #call shellRunner.run_script(user_in)
        # all other commands must be bash/shell
        else:
            self.shellRunner.feed(user_in)
            return 'Bash command:\n' + user_in #call shellRunner(self.input) 

    def script_formatter(self, user_in):
        input_split = user_in.split(' ')
        user_output = ''
        for word in input_split:
            # check if we need to switch out variable
            if word[0] == '@':
                user_output += 'replaced pyvar' + ' ' #pyRunner.get_var(word[1:])
            elif word[0] == '$':
                user_output += 'replaced bashvar' + ' ' #shellRunner.get_var(word[1:])
            else: 
                user_output += word + ' '
        return user_output 
        