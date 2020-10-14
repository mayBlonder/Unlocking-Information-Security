import inspect

def quine():
    func_src_code = ""
    lines = inspect.getsourcelines(quine)
    for line in lines[0][1:]:
        func_src_code += line
    return func_src_code
