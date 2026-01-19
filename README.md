# Receipt Parser Lab

This project is a command-line tool designed to automate the extraction of data from receipt images. It processes images in a directory, extracts key information using a language model (or a mock simulator), and outputs the results in a structured JSON format.

## Functionality
- **Image Processing**: Encodes receipt images (JPG, PNG, WebP) into base64 format.
- **Data Extraction**: Identifies the date, total amount, vendor, and category (Meals, Transport, Other).
- **Amount Cleaning**: Automatically removes currency symbols and converts string amounts into floating-point numbers for data consistency.
- **Documentation**: Automatically generated HTML documentation using `pdoc`.

## How to Run

### Prerequisites
- Python 3.12+
- A virtual environment configured with dependencies from `requirements.txt`.

### Execution
To run the parser and print the results to the terminal, use the following command from the root directory:

```bash
./.venv/bin/python -m src.receipt_parser.main app/receipts --print