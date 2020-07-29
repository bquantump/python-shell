from . import consts
from . import shell_utils
from . import python_utils

class shellParser():
    def __init__(self):
        self.pythonRunner = python_utils.pyRunner()
        self.shellRunner = shell_utils.shellRunner()


    def checkBashOrPython(self, user_in):
        user_in = user_in.lstrip()
        # echo
        if user_in.split()[0] == consts.ECHO_CMD:
            #TODO: validate split is greater than one
            cmd_split = user_in.split()
            if cmd_split[1][0] == consts.PYTHON_VAR_DELIMETER:
                return self.pythonRunner.get_var(cmd_split[1][1:])
            else:
                return self.shellRunner.get_bash_var(cmd_split[1][1:])
        # Python var: '@'
        elif user_in[0] == consts.PYTHON_VAR_DELIMETER:
            return self.pythonRunner.get_var(user_in[1:])
        # Python single line: '>>>'
        elif user_in.startswith(consts.PYTHON_SINGLE_LINE_INPUT_DELEMETER): 
            return self.pythonRunner.run_python(user_in[3:])
        # Python multi line: '...'
        elif user_in.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):             
            user_in = user_in[len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):]
            user_in = user_in[:-len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER)]
            return self.pythonRunner.run_python(user_in)
        # check for Python or bash scripts
        elif user_in.startswith(consts.PYTHON_BASH_SCRIPT_DELIMETER):   # python
            return self.pythonRunner.run_py_script(self.script_formatter(user_in))
        # COMBINE INTO ONE COND
        elif user_in.startswith(consts.SHELL_SCRIPT_DELIMETER): # ./script.sh -s "hello"
            # return 'Shell script:\n' + self.script_formatter(user_in) #call shellRunner.run_script(user_in)
            return self.shellRunner.run_script(self.script_formatter(user_in))
        elif user_in.startswith(consts.SHELL_SCRIPT_SH_DELIMETER): # sh script.sh -s "hello"
            return 'Shell script:\n' + self.script_formatter(user_in) #call shellRunner.run_script(user_in)
        elif user_in.startswith(consts.BASH_SCRIPT_DELIMETER): # bash script.sh -s "hello"
            return 'Bash script:\n' + self.script_formatter(user_in) #call shellRunner.run_script(user_in)
        # all other commands must be bash/shell
        else:
            return self.shellRunner.feed(user_in)

        
    def script_formatter(self, user_in):
        input_split = user_in.rstrip().split(' ') 
        user_output = ''
        for word in input_split:
            # check if we need to switch out variable
            if word != consts.PYTHON_BASH_SCRIPT_DELIMETER:
                if word.startswith(consts.PYTHON_VAR_DELIMETER):
                    user_output += this.pythonRunner.get_var(word[1:]) + ' '
                elif word.startswith(consts.BASH_VAR_DELIMETER):
                    user_output += this.shellRunner.get_bash_var(word[1:]) + ' '
                else: 
                    user_output += word + ' '
        return user_output
        