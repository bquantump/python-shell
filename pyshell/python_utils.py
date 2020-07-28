import runpy

class pyRunner:

    def __init__(self):
        pass
    
    def run_py_script(self, path):
        out = runpy.run_path(file_path=path)

    def run_python(self, py_code):
        pass

    def get_var(self, var_name):
        pass
    