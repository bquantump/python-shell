import runpy

class pyRunner:

    def __init__(self):
        pass
    
    def run_py_script(self, path):
        out = runpy.run_path(file_path=path)