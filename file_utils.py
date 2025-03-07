import os

base_dir = os.path.dirname(__file__)

def get_path(filename):
    return os.path.join(base_dir, filename)

def file_exists(filename):
    return os.path.exists(get_path(filename))

def open_file(filename, mode):
    return open(get_path(filename), mode)
