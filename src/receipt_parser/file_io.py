# file_io.py
import os
import base64

def encode_file(path):
    """
    Reads a file from disk and encodes its content into a base64 string.

    Args:
        path (str): The absolute or relative path to the image file.

    Returns:
        str: The base64 encoded string representing the file content.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """
    Iterates through a directory and yields the filename and full path of each file.

    Args:
        dirpath (str): The path to the directory containing receipt images.

    Yields:
        tuple: A tuple containing the filename (str) and the full path (str).
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path