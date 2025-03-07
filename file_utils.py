import os

# Get the base directory of the current file
base_dir = os.path.dirname(__file__)

def get_path(filename):
    """
    Get the full path of a file located in the base directory.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The full path to the file.
    """
    return os.path.join(base_dir, filename)

def file_exists(filename):
    """
    Check if a file exists in the base directory.

    Args:
        filename (str): The name of the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(get_path(filename))

def open_file(filename, mode):
    """
    Open a file located in the base directory.

    Args:
        filename (str): The name of the file.
        mode (str): The mode in which to open the file.

    Returns:
        file object: The opened file object.
    """
    return open(get_path(filename), mode)
