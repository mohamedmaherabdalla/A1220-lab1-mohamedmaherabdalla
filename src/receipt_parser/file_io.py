# file_io.py
import os
import base64

def encode_file(path):
    """
    Reads a file from the specified path and encodes its content into a base64 string.

    Args:
        path (str): The file system path to the image file to be encoded.

    Returns:
        str: A UTF-8 decoded base64 string representing the file's binary data.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """
    Scans a directory and yields the filename and full path for each file found.

    Args:
        dirpath (str): The directory path to search for files.

    Yields:
        tuple: A tuple containing the filename (str) and its absolute or relative path (str).
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path