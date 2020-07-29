import os
import cmd
import sys
from . import consts, parser
from sultan.api import Sultan
from termcolor import colored, cprint

def display_welcome():
    cprint(' Welcome to pyshell!\n Useage:', 'cyan', attrs=['bold'])
    cprint('     Echo python variable with character @', 'cyan', attrs=['bold'])
    cprint("     Write single-line python code start with '>>>', if it is in multi-line start with '...'\n", 'cyan',
        attrs=['bold'])


def get_prefix():
    prefix = os.getcwd()
    if 'VIRTUAL_ENV' in os.environ:
        prefix = '(' + os.environ.get('VIRTUAL_ENV').split('/')[-1] + ')' + prefix
    return prefix + ': '


def main():
    display_welcome()
    cmd = CmdParse(parser.shellParser())
    cmd.cmdloop()

class CmdParse(cmd.Cmd):
    def __init__(self, shell_parser):
        super().__init__(completekey='tab', stdin=None, stdout=None)
        self.shell_parser = shell_parser
        self.multi_line = False
        self.line_buffer = ''
    
    prompt = colored(get_prefix(), 'cyan')
    
    
    def do_exit(self, arg):
        if not self.multi_line:
            sys.exit(0)
    
    
    def default(self, line):
        if self.multi_line:
            self.line_buffer += line + "\n"
        else:
            output = self.shell_parser.checkBashOrPython(line)
            if output != None:
                print(output)
        self.prompt = colored(get_prefix(), 'cyan')
    
    
    def do_py(self, arg):
        if self.multi_line:
            print(self.line_buffer)
            self.line_buffer = '...' + self.line_buffer + '...'
            self.shell_parser.checkBashOrPython(self.line_buffer)
            self.multi_line = False
            self.prompt = colored(get_prefix(), 'cyan')
            self.line_buffer = ''
            return
        self.multi_line = True
        self.prompt = colored("python mode >>>", 'green', attrs=['bold'])

    def parseline(self, line):
        """Parse the line into a command name and a string containing
        the arguments.  Returns a tuple containing (command, args, line).
        'command' and 'args' may be None if the line couldn't be parsed.
        """
        if not line:
            return None, None, line
        elif line[0] == '?':
            line = 'help ' + line[1:]
        elif line[0] == '!':
            if hasattr(self, 'do_shell'):
                line = 'shell ' + line[1:]
            else:
                return None, None, line
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars: i = i+1
        cmd, arg = line[:i], line[i:].strip()
        return cmd, arg, line

if __name__ == "__main__":
    main()