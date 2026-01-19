# gpt_mock.py

values = [{
    "receipt_1_food.jpg": {
        "date": None,
        "amount": "70.74",
        "vendor": None,
        "category": "Meals"
    }},{
    "drive.webp": {
        "date": "Wed, Nov 06, 2019",
        "amount": "$43.83",
        "vendor": "Uber",
        "category": "Transport"
    }},{
    "walmart.png": {
         "date": "10/17/2020",
         "amount": "27.27",
         "vendor": "WALL-MART-SUPERSTORE",
         "category": "Other"
    }},{
    "recipe_2_food.png": {
         "date": "30/09/2025 20:15",
         "amount": "$51.30",
         "vendor": "DINEFINE RESTAURANT",
         "category": "Meals"
      }
    }]


def extract_receipt_info(img):
    """
    Simulates calling a language model to extract information from a receipt image. [cite: 46]

    Args:
        img (str): The base64 encoded string of the receipt image. [cite: 46]

    Returns:
        dict: A dictionary containing the date, amount, vendor, and category. [cite: 46]
    """
    name = list(values[0].keys())[0]
    return values.pop(0)[name]

def clean_amount(amount_str):
    """
    Processes the raw string from the model to remove currency symbols and convert to float. [cite: 63]

    Args:
        amount_str (str): The amount as a string (e.g., "$51.30"). [cite: 46]
        
    Returns:
        float: The numeric value (e.g., 51.3). Returns 0.0 if invalid. [cite: 46, 63]
    """
    if amount_str is None:
        return 0.0
    # Remove $ symbol and any commas 
    clean_str = str(amount_str).replace("$", "").replace(",", "").strip()
    try:
        return float(clean_str)
    except (ValueError, TypeError):
        return 0.0