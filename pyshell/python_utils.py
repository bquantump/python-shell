import runpy

class pyRunner:

    def __init__(self):
        self.py_local_context = locals()
    
    def run_py_script(self, path):
        out = runpy.run_path(file_path=path)

    def run_python(self, py_code):
        exec(py_code, globals(), self.py_local_context)

    def get_var(self, var_name):
        return self.py_local_context.get(var_name)