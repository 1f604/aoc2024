import os 
import inspect

def get_input_lines() -> list[str]:
    """ Get lines from the file input.txt """
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    dir_path = os.path.dirname(os.path.realpath(filename))
    with open(dir_path+"/input.txt") as f:
        lines = f.readlines()
    return lines
