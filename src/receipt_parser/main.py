# main.py
import json
import argparse
from . import file_io as io_mod
from . import gpt_mock as gpt  # Change import to gpt_mock as gpt per professor's fix

def process_directory(dirpath):
    """
    Processes all receipt images in a directory and extracts their information.

    This function iterates through the files in the given directory, encodes them,
    calls the language model to extract data, and cleans the amount field. [cite: 44]

    Args:
        dirpath (str): The path to the directory containing receipt images. [cite: 46]

    Returns:
        dict: A dictionary mapping filenames to their extracted information. [cite: 46]
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
    Main entry point for the receipt parser application.

    Parses command-line arguments to get the directory path and execution options. [cite: 10]
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