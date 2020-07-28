from . import consts


def checkBashOrPython(input):
    # Python var: '@'
    if input[0] == consts.PYTHON_VAR_DELIMETER:
        #print('Get Python var: ', self.input[1:])
        return 'Python var:\n' + input[1:] #call pyRunner(self.input[1:])
    # Python single line: '>>>'
    elif input.startswith(consts.PYTHON_SINGLE_LINE_INPUT_DELEMETER): 
        #print('Get Python single line: ', self.input[3:])
        return 'Python single line:\n' + input[3:] #call pyRunner(self.input[2:])
    # Python multi line: '...'
    elif input.startswith(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):             
        input = input[len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER):]
        input = input[:-len(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER)]
        #print('Get Python multi line: (prints on newline to show tabs)\n', input)
        return 'Python multi line:\n' + input #call pyRunner(input)
    # all other commands must be bash/shell
    else:
        #print('Bash/shell command: ', self.input)
        return 'Bash command:\n' + input #call shellRunner(self.input)