import runpy

class pyRunner:

    def __init__(self):
        self.py_local_context = locals()
    
    def run_py_script(self, path):
        try:
            out = runpy.run_path(path)
        except Exception as e:
            print(e)
            print('command failed!')

    def run_python(self, py_code):
        try:
            exec(py_code, self.py_local_context)
        except Exception as e:
            print(e)
            print('command failed!')

    def get_var(self, var_name):
        return (self.py_local_context.get(var_name) or globals().get(var_name))