from . import consts

class Parser:
    def __init__ (self, input):
        self.input = input

    def checkBashOrPython(self):
        # Python var: '@'
        if self.input[0] == consts.PYTHON_VAR_DELIMETER:
            #print('Get Python var: ', self.input[1:])
            return 'Python var ' + self.input[1:] #call pyRunner(self.input[1:])
        # Python single line: '>>>'
        elif self.input[0:3] == consts.PYTHON_SINGLE_LINE_INPUT_DELEMETER: 
            #print('Get Python single line: ', self.input[3:])
            return 'Python single line ' + self.input[3:] #call pyRunner(self.input[2:])
        # Python multi line: '...'
        elif self.input[0:3] == consts.PYTHON_MULTI_LINE_INPUT_DELIMETER:             
            inputSplit = self.input[3:].replace(consts.PYTHON_MULTI_LINE_INPUT_DELIMETER,'\n\t') #get newlines in string instead of ...
            #print('Get Python multi line: (prints on newline to show tabs)\n', inputSplit)
            return 'Python multi line ' + inputSplit #call pyRunner(inputSplit)
        # all other commands must be bash/shell
        else:
            #print('Bash/shell command: ', self.input)
            return 'Bash command ' + self.input #call shellRunner(self.input)

# small tests
test0 = Parser("@m")
test0.checkBashOrPython()
test1 = Parser(">>>m = 3")
test1.checkBashOrPython()
test2 = Parser("...for i in range(3):...print(\"hello\")...print(i)")
test2.checkBashOrPython()
test3 = Parser("echo m")
test3.checkBashOrPython()