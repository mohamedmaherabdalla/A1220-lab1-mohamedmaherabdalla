# main.py
import json
import argparse
from . import file_io as io_mod
from . import gpt_mock as gpt

def process_directory(dirpath):
    """
    Orchestrates the processing of a directory containing receipt images.

    It iterates through the files, encodes them, extracts information using 
    the language model, and applies amount cleaning.

    Args:
        dirpath (str): The path to the directory containing receipt images.

    Returns:
        dict: A dictionary mapping filenames to their extracted and cleaned data.
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        
        # Apply the clean_amount function to the parsed data 
        data['amount'] = gpt.clean_amount(data.get('amount'))
        
        results[name] = data
    return results

def main():
    """
    Entry point for the command-line interface.

    Parses arguments, processes the directory, and prints the result as JSON.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()